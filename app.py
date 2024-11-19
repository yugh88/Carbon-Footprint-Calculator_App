import streamlit as st
import pandas as pd
import numpy as np
from streamlit.components.v1 import html
from sklearn.neural_network import MLPRegressor
from sklearn.preprocessing import StandardScaler
import pickle
import io
import matplotlib.pyplot as plt
from PIL import Image, ImageDraw, ImageFont
import base64
from functions import *
from web3 import Web3
from blockchain_config import CONTRACT_ADDRESS, CARBON_FOOTPRINT_ABI, GANACHE_URL

# Connect to Ganache
w3 = Web3(Web3.HTTPProvider(GANACHE_URL))
contract = w3.eth.contract(address=CONTRACT_ADDRESS, abi=CARBON_FOOTPRINT_ABI)

st.set_page_config(layout="wide", page_title="Carbon Footprint Calculator", page_icon="./media/favicon.ico")

def get_base64(bin_file):
    with open(bin_file, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()

background = get_base64("./media/background_min.jpg")
icon2 = get_base64("./media/icon2.png")
icon3 = get_base64("./media/icon3.png")

with open("./style/style.css", "r") as style:
    css = f"""<style>{style.read().format(background=background, icon2=icon2, icon3=icon3)}</style>"""
    st.markdown(css, unsafe_allow_html=True)

def script():
    with open("./style/scripts.js", "r", encoding="utf-8") as scripts:
        open_script = f"""<script>{scripts.read()}</script> """
        html(open_script, width=0, height=0)


left, middle, right = st.columns([2, 3.5, 2])
main, comps, result = middle.tabs([" ", " ", " "])

with open("./style/main.md", "r", encoding="utf-8") as main_page:
    main.markdown(f"""{main_page.read()}""")

_, but, _ = main.columns([1, 2, 1])
if but.button("Calculate Your Carbon Footprint!", type="primary"):
    click_element('tab-1')

tab1, tab2, tab3, tab4, tab5 = comps.tabs(["👴 Personal", "🚗 Travel", "🗑️ Waste", "⚡ Energy", "💸 Consumption"])
tab_result, _ = result.tabs([" ", " "])


# Blockchain interaction functions
def record_footprint_on_blockchain(carbon_footprint, tree_credits, user_address):
    """Records the user's footprint on the blockchain."""
    tx = contract.functions.recordFootprint(carbon_footprint, tree_credits).build_transaction({
        'from': user_address,
        'gas': 3000000,
        'gasPrice': w3.toWei('20', 'gwei'),
        'nonce': w3.eth.getTransactionCount(user_address)
    })
    signed_tx = w3.eth.account.sign_transaction(tx, private_key="YOUR_PRIVATE_KEY")
    tx_hash = w3.eth.sendRawTransaction(signed_tx.rawTransaction)
    return w3.toHex(tx_hash)


def get_user_tree_credits_from_blockchain(user_address):
    """Fetches user's tree credits from the blockchain."""
    return contract.functions.getUserTreeCredits(user_address).call()


# User Input Section
def component():
    tab1col1, tab1col2 = tab1.columns(2)
    height = tab1col1.number_input("Height", 0, 251, value=None, placeholder="160", help="in cm")
    weight = tab1col2.number_input("Weight", 0, 250, value=None, placeholder="75", help="in kg")
    if (weight is None) or (weight == 0): weight = 1
    if (height is None) or (height == 0): height = 1
    calculation = weight / (height/100)**2
    body_type = "underweight" if (calculation < 18.5) else \
                 "normal" if ((calculation >= 18.5) and (calculation < 25)) else \
                 "overweight" if ((calculation >= 25) and (calculation < 30)) else "obese"
    sex = tab1.selectbox('Gender', ["female", "male"])
    diet = tab1.selectbox('Diet', ['omnivore', 'pescatarian', 'vegetarian', 'vegan'])
    social = tab1.selectbox('Social Activity', ['never', 'often', 'sometimes'])

    transport = tab2.selectbox('Transportation', ['public', 'private', 'walk/bicycle'])
    if transport == "private":
        vehicle_type = tab2.selectbox('Vehicle Type', ['petrol', 'diesel', 'hybrid', 'lpg', 'electric'])
    else:
        vehicle_type = "None"

    if transport == "walk/bicycle":
        vehicle_km = 0
    else:
        vehicle_km = tab2.slider('Monthly distance traveled by vehicle (km)', 0, 5000, 0)

    air_travel = tab2.selectbox('How often did you fly last month?', ['never', 'rarely', 'frequently', 'very frequently'])

    waste_bag = tab3.selectbox('Waste bag size', ['small', 'medium', 'large', 'extra large'])
    waste_count = tab3.slider('Weekly waste bags', 0, 10, 0)
    recycle = tab3.multiselect('Recycle materials', ['Plastic', 'Paper', 'Metal', 'Glass'])

    heating_energy = tab4.selectbox('Heating source', ['natural gas', 'electricity', 'wood', 'coal'])
    cooking_methods = tab4.multiselect('Cooking systems', ['microwave', 'oven', 'grill', 'airfryer', 'stove'])
    energy_efficiency = tab4.selectbox('Energy efficiency', ['No', 'Yes', 'Sometimes'])
    daily_tv_pc = tab4.slider('Daily hours on PC/TV', 0, 24, 0)
    internet_daily = tab4.slider('Daily internet usage (hours)', 0, 24, 0)

    shower = tab5.selectbox('How often do you shower?', ['daily', 'twice a day', 'more frequently', 'less frequently'])
    grocery_bill = tab5.slider('Monthly grocery bill ($)', 0, 500, 0)
    clothes_monthly = tab5.slider('Monthly clothes purchase', 0, 30, 0)

    data = {'Body Type': body_type,
            "Sex": sex,
            'Diet': diet,
            "How Often Shower": shower,
            "Heating Energy Source": heating_energy,
            "Transport": transport,
            "Social Activity": social,
            'Monthly Grocery Bill': grocery_bill,
            "Frequency of Traveling by Air": air_travel,
            "Vehicle Monthly Distance Km": vehicle_km,
            "Waste Bag Size": waste_bag,
            "Waste Bag Weekly Count": waste_count,
            "How Long TV PC Daily Hour": daily_tv_pc,
            "Vehicle Type": vehicle_type,
            "How Many New Clothes Monthly": clothes_monthly,
            "How Long Internet Daily Hour": internet_daily,
            "Energy efficiency": energy_efficiency}
    data.update({f"Cooking_with_{x}": y for x, y in dict(zip(cooking_methods, np.ones(len(cooking_methods)))).items()})
    data.update({f"Do You Recycle_{x}": y for x, y in dict(zip(recycle, np.ones(len(recycle)))).items()})
    return pd.DataFrame(data, index=[0])


df = component()
data = input_preprocessing(df)

sample_df = pd.DataFrame(data=sample, index=[0])
sample_df[sample_df.columns] = 0
sample_df[data.columns] = data

# Prediction Model
ss = pickle.load(open("./models/scale.sav", "rb"))
model = pickle.load(open("./models/model.sav", "rb"))
prediction = round(np.exp(model.predict(ss.transform(sample_df))[0]))

# UI for Blockchain Integration
_, resultbutton, _ = tab5.columns([1, 1, 1])
user_address = "0xB6777d133613a719080DA54e71531214769d2552" # Replace with the actual Ethereum address
if resultbutton.button("Submit to Blockchain"):
    tx_hash = record_footprint_on_blockchain(prediction, round(prediction / 411.4), user_address)
    st.success(f"Recorded on blockchain successfully! Transaction Hash: {tx_hash}")

if st.button("Fetch My Blockchain Data"):
    tree_credits = get_user_tree_credits_from_blockchain(user_address)
    st.info(f"Your total tree credits: {tree_credits}")
