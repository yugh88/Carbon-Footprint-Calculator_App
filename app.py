import streamlit as st

# First command
st.set_page_config(layout="wide", page_title="Carbon Footprint Calculator", page_icon="./media/favicon.ico")

# Imports
import uuid
import pandas as pd
import numpy as np
from streamlit.components.v1 import html
from sklearn.preprocessing import StandardScaler
import pickle
import base64
from web3 import Web3
from blockchain_config import CONTRACT_ADDRESS, CARBON_FOOTPRINT_ABI, GANACHE_URL

# Import from your functions
from functions import input_preprocessing, sample, chart, hesapla, component

# Add Guest Mode Tracking
if 'guest_id' not in st.session_state:
    st.session_state['guest_id'] = str(uuid.uuid4())
    
# Add Login Mode Selection to Sidebar
login_mode = st.sidebar.radio("Select Login Mode", ["Guest", "Blockchain"])

# Blockchain and Guest Mode Recording Function
def record_footprint(carbon_footprint, tree_credits, user_identifier=None):
    """
    Record footprint either on blockchain or in guest mode
    
    Args:
        carbon_footprint (float): Calculated carbon footprint
        tree_credits (float): Tree credits calculated
        user_identifier (str, optional): Blockchain address or guest ID
    """
    if login_mode == "Blockchain" and user_identifier:
        try:
            tx = contract.functions.recordFootprint(carbon_footprint, tree_credits).build_transaction({
                'from': user_identifier,
                'gas': 3000000,
                'gasPrice': w3.toWei('20', 'gwei'),
                'nonce': w3.eth.getTransactionCount(user_identifier)
            })
            signed_tx = w3.eth.account.sign_transaction(tx, private_key="YOUR_PRIVATE_KEY")
            tx_hash = w3.eth.sendRawTransaction(signed_tx.rawTransaction)
            st.success(f"Recorded on blockchain successfully! Transaction Hash: {w3.toHex(tx_hash)}")
            return w3.toHex(tx_hash)
        except Exception as e:
            st.error(f"Blockchain recording error: {e}")
            return None
    elif login_mode == "Guest":
        # Guest mode: Store locally or in a simple database
        guest_data = {
            'guest_id': st.session_state['guest_id'],
            'carbon_footprint': carbon_footprint,
            'tree_credits': tree_credits,
            'timestamp': pd.Timestamp.now()
        }
        # Store data in a file (optional: save in a database or CSV file for persistence)
        with open("guest_data.csv", "a") as f:
            pd.DataFrame([guest_data]).to_csv(f, header=f.tell()==0, index=False)
        st.success("Recorded locally as a guest. You can check your data in the file.")
        return guest_data

# Blockchain Configuration
w3 = Web3(Web3.HTTPProvider(GANACHE_URL))
contract = w3.eth.contract(address=CONTRACT_ADDRESS, abi=CARBON_FOOTPRINT_ABI)

def get_base64(bin_file):
    with open(bin_file, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()

# Load Base64 Encoded Images
background = get_base64("./media/background_min.jpg")
icon2 = get_base64("./media/icon2.png")
icon3 = get_base64("./media/icon3.png")

# Apply Custom CSS
with open("./style/style.css", "r") as style:
    css = f"""<style>{style.read().format(background=background, icon2=icon2, icon3=icon3)}</style>"""
    st.markdown(css, unsafe_allow_html=True)

# Blockchain Interaction Functions
def record_footprint_on_blockchain(carbon_footprint, tree_credits, user_address):
    """Records the user's footprint on the blockchain."""
    try:
        tx = contract.functions.recordFootprint(carbon_footprint, tree_credits).build_transaction({
            'from': user_address,
            'gas': 3000000,
            'gasPrice': w3.toWei('20', 'gwei'),
            'nonce': w3.eth.getTransactionCount(user_address)
        })
        signed_tx = w3.eth.account.sign_transaction(tx, private_key="YOUR_PRIVATE_KEY")
        tx_hash = w3.eth.sendRawTransaction(signed_tx.rawTransaction)
        return w3.toHex(tx_hash)
    except Exception as e:
        st.error(f"Blockchain recording error: {e}")
        return None

def get_user_tree_credits_from_blockchain(user_address):
    """Fetches user's tree credits from the blockchain."""
    try:
        return contract.functions.getUserTreeCredits(user_address).call()
    except Exception as e:
        st.error(f"Blockchain data fetch error: {e}")
        return None

# Layout Setup
left, middle, right = st.columns([2, 3.5, 2])
main, comps, result = middle.tabs([" ", " ", " "])

# Main Page Content
with open("./style/main.md", "r", encoding="utf-8") as main_page:
    main.markdown(f"""{main_page.read()}""")

_, but, _ = main.columns([1, 2, 1])
if but.button("Calculate Your Carbon Footprint!", type="primary"):
    st.session_state['current_tab'] = 'tab-1'

# Tabs Configuration
tab1, tab2, tab3, tab4, tab5 = comps.tabs(["👴 Personal", "🚗 Travel", "🗑️ Waste", "⚡ Energy", "💸 Consumption"])
tab_result, _ = result.tabs([" ", " "])

# Main Calculation Flow
df = component()
data = input_preprocessing(df)  # Now imported from functions.py

# Create sample dataframe for model prediction
sample_df = pd.DataFrame(data=sample, index=[0])
sample_df[sample_df.columns] = 0
sample_df[data.columns] = data

# Load Prediction Model
ss = pickle.load(open("./models/scale.sav", "rb"))
model = pickle.load(open("./models/model.sav", "rb"))
prediction = round(np.exp(model.predict(ss.transform(sample_df))[0]))

# Create visualization
chart_image = chart(model, ss, sample_df, prediction)
st.image(chart_image)

# Blockchain Integration UI
_, resultbutton, _ = tab5.columns([1, 1, 1])
user_address = st.text_input("Enter Your Ethereum Address", placeholder="0x...")

if resultbutton.button("Submit to Blockchain"):
    if user_address:
        tx_hash = record_footprint_on_blockchain(prediction, round(prediction / 411.4), user_address)
        if tx_hash:
            st.success(f"Recorded on blockchain successfully! Transaction Hash: {tx_hash}")
    else:
        st.warning("Please enter a valid Ethereum address")

if st.button("Fetch My Blockchain Data"):
    if user_address:
        tree_credits = get_user_tree_credits_from_blockchain(user_address)
        if tree_credits is not None:
            st.info(f"Your total tree credits: {tree_credits}")
    else:
        st.warning("Please enter a valid Ethereum address")

# Final Carbon Footprint Display
tree_count = round(prediction / 411.4)
tab_result.markdown(f"""
You owe nature <b>{tree_count}</b> tree{'s' if tree_count > 1 else ''} monthly. 
{f"<a href='https://www.tema.org.tr/en/homepage' id='button-17' class='button-17' role='button'> 🌳 Proceed to offset 🌳</a>" if tree_count > 0 else ""}
""", unsafe_allow_html=True)
