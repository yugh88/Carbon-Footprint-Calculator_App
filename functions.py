import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image, ImageDraw, ImageFont
import matplotlib.pyplot as plt
import io

def component():
    """
    Creates an input form for carbon footprint calculation
    
    Returns:
        pd.DataFrame: User input data for carbon footprint calculation
    """
    # Personal Information
    body_type = st.selectbox("Body Type", ['underweight', 'normal', 'overweight', 'obese'])
    sex = st.selectbox("Sex", ['female', 'male'])
    
    # Shower and Social Activity
    shower_frequency = st.selectbox("How Often Do You Shower", ['less frequently', 'daily', "twice a day", "more frequently"])
    social_activity = st.selectbox("Social Activity", ['never', 'sometimes', "often"])
    
    # Travel
    air_travel_freq = st.selectbox("Frequency of Traveling by Air", ['never', 'rarely', "frequently", "very frequently"])
    monthly_vehicle_distance = st.number_input("Monthly Vehicle Distance (km)", min_value=0, value=0)
    
    # Waste
    waste_bag_size = st.selectbox("Waste Bag Size", ['small', 'medium', "large", "extra large"])
    waste_bag_count = st.number_input("Waste Bag Weekly Count", min_value=0, value=0)
    
    # Energy and Electronics
    tv_daily_hours = st.number_input("Daily TV/PC Hours", min_value=0.0, value=0.0, step=0.5)
    internet_daily_hours = st.number_input("Daily Internet Hours", min_value=0.0, value=0.0, step=0.5)
    
    # Clothing and Consumption
    new_clothes_monthly = st.number_input("New Clothes per Month", min_value=0, value=0)
    monthly_grocery_bill = st.number_input("Monthly Grocery Bill ($)", min_value=0.0, value=0.0)
    
    # Diet
    diet = st.selectbox("Diet", ['omnivore', 'pescatarian', 'vegan', 'vegetarian'])
    
    # Energy Efficiency and Recycling
    energy_efficiency = st.selectbox("Energy Efficiency", ['No', 'Sometimes', "Yes"])
    recycling = st.multiselect("What Do You Recycle?", ['Paper', 'Plastic', 'Glass', 'Metal'])
    
    # Cooking Methods
    cooking_methods = st.multiselect("Cooking Methods", ['stove', 'oven', 'microwave', 'grill', 'airfryer'])
    
    # Transportation
    transport_mode = st.selectbox("Primary Transport Mode", ['private', 'public', 'walk/bicycle'])
    vehicle_type = st.selectbox("Vehicle Type", ['None', 'diesel', 'electric', 'hybrid', 'lpg', 'petrol'])
    
    # Heating Energy Source
    heating_source = st.selectbox("Heating Energy Source", ['coal', 'electricity', 'natural gas', 'wood'])
    
    # Prepare data for model
    data = {
        'Body Type': body_type,
        'Sex': sex,
        'How Often Shower': shower_frequency,
        'Social Activity': social_activity,
        'Monthly Grocery Bill': monthly_grocery_bill,
        'Frequency of Traveling by Air': air_travel_freq,
        'Vehicle Monthly Distance Km': monthly_vehicle_distance,
        'Waste Bag Size': waste_bag_size,
        'Waste Bag Weekly Count': waste_bag_count,
        'How Long TV PC Daily Hour': tv_daily_hours,
        'How Many New Clothes Monthly': new_clothes_monthly,
        'How Long Internet Daily Hour': internet_daily_hours,
        'Energy efficiency': energy_efficiency,
        'Diet': diet,
        'Heating Energy Source': heating_source,
        'Transport': transport_mode,
        'Vehicle Type': vehicle_type
    }
    
    # Add recycling columns
    for recycle_type in ['Paper', 'Plastic', 'Glass', 'Metal']:
        data[f'Do You Recyle_{recycle_type}'] = 1 if recycle_type in recycling else 0
    
    # Add cooking method columns
    for method in ['stove', 'oven', 'microwave', 'grill', 'airfryer']:
        data[f'Cooking_with_{method}'] = 1 if method in cooking_methods else 0
    
    # Submit button
    if st.button("Calculate Carbon Footprint"):
        return pd.DataFrame([data])
    
    return pd.DataFrame([sample])  # Return sample data if not submitted

# Rest of your existing functions remain the same (input_preprocessing, hesapla, chart, etc.)
# Import necessary libraries and other code

def click_element(element):
    open_script = f"<script type = 'text/javascript'>window.parent.document.querySelector('[id^=tabs-bui][id$=-{element}]').click();</script>"
    html(open_script, width=0, height=0)

def record_footprint(carbon_footprint, tree_credits, user_address):
    # Record user's footprint on the blockchain
    tx = contract.functions.recordFootprint(carbon_footprint, tree_credits).build_transaction({
        'from': user_address,
        'gas': 3000000,
        'gasPrice': w3.toWei('20', 'gwei'),
        'nonce': w3.eth.getTransactionCount(user_address)
    })
    # Sign and send the transaction
    signed_tx = w3.eth.account.sign_transaction(tx, private_key="0x0b0fb349a30a1ac3e6e6a1258181195cfc62c89f14bbc8bfe1f993cef68c2252")

    tx_hash = w3.eth.sendRawTransaction(signed_tx.rawTransaction)
    return w3.toHex(tx_hash)

def get_user_tree_credits(user_address):
    # Fetch user-specific tree credits
    return contract.functions.getUserTreeCredits(user_address).call()

sample = {'Body Type': 2,
 'Sex': 0,
 'How Often Shower': 1,
 'Social Activity': 2,
 'Monthly Grocery Bill': 230,
 'Frequency of Traveling by Air': 2,
 'Vehicle Monthly Distance Km': 210,
 'Waste Bag Size': 2,
 'Waste Bag Weekly Count': 4,
 'How Long TV PC Daily Hour': 7,
 'How Many New Clothes Monthly': 26,
 'How Long Internet Daily Hour': 1,
 'Energy efficiency': 0,
 'Do You Recyle_Paper': 0,
 'Do You Recyle_Plastic': 0,
 'Do You Recyle_Glass': 0,
 'Do You Recyle_Metal': 1,
 'Cooking_with_stove': 1,
 'Cooking_with_oven': 1,
 'Cooking_with_microwave': 0,
 'Cooking_with_grill': 0,
 'Cooking_with_airfryer': 1,
 'Diet_omnivore': 0,
 'Diet_pescatarian': 1,
 'Diet_vegan': 0,
 'Diet_vegetarian': 0,
 'Heating Energy Source_coal': 1,
 'Heating Energy Source_electricity': 0,
 'Heating Energy Source_natural gas': 0,
 'Heating Energy Source_wood': 0,
 'Transport_private': 0,
 'Transport_public': 1,
 'Transport_walk/bicycle': 0,
 'Vehicle Type_None': 1,
 'Vehicle Type_diesel': 0,
 'Vehicle Type_electric': 0,
 'Vehicle Type_hybrid': 0,
 'Vehicle Type_lpg': 0,
 'Vehicle Type_petrol': 0}

def input_preprocessing(data):
    # Create a copy of the input data to avoid modifying the original
    processed_data = data.copy()
    
    # Map specific columns first
    processed_data["Body Type"] = processed_data["Body Type"].map({'underweight':0, 'normal':1, 'overweight':2, 'obese':3})
    processed_data["Sex"] = processed_data["Sex"].map({'female':0, 'male':1})
    
    # One-hot encode categorical variables
    categorical_columns = {
        'Diet': ['omnivore', 'pescatarian', 'vegan', 'vegetarian'],
        'Heating Energy Source': ['coal', 'electricity', 'natural gas', 'wood'],
        'Transport': ['private', 'public', 'walk/bicycle'],
        'Vehicle Type': ['None', 'diesel', 'electric', 'hybrid', 'lpg', 'petrol']
    }
    
    for col, categories in categorical_columns.items():
        # Drop existing one-hot columns if they exist
        col_names_to_drop = [f"{col}_{cat}" for cat in categories]
        processed_data = processed_data.drop(columns=[c for c in col_names_to_drop if c in processed_data.columns], errors='ignore')
        
        # Create one-hot encoded columns
        for cat in categories:
            processed_data[f"{col}_{cat}"] = (processed_data[col] == cat).astype(int)
        
        # Drop the original categorical column
        processed_data = processed_data.drop(columns=[col])
    
    # Additional mappings
    processed_data["How Often Shower"] = processed_data["How Often Shower"].map({'less frequently':0, 'daily':1, "twice a day":2, "more frequently":3})
    processed_data["Social Activity"] = processed_data["Social Activity"].map({'never':0, 'sometimes':1, "often":2})
    processed_data["Frequency of Traveling by Air"] = processed_data["Frequency of Traveling by Air"].map({'never':0, 'rarely':1, "frequently":2, "very frequently":3})
    processed_data["Waste Bag Size"] = processed_data["Waste Bag Size"].map({'small':0, 'medium':1, "large":2,  "extra large":3})
    processed_data["Energy efficiency"] = processed_data["Energy efficiency"].map({'No':0, 'Sometimes':1, "Yes":2})
    
    return processed_data
def hesapla(model,ss, sample_df):
    copy_df = sample_df.copy()
    travels = copy_df[["Frequency of Traveling by Air",
                         "Vehicle Monthly Distance Km",
                         'Transport_private',
                          'Transport_public',
                          'Transport_walk/bicycle',
                          'Vehicle Type_None',
                          'Vehicle Type_diesel',
                          'Vehicle Type_electric',
                          'Vehicle Type_hybrid',
                          'Vehicle Type_lpg',
                          'Vehicle Type_petrol']]
    copy_df[list(set(copy_df.columns) - set(travels.columns))] = 0
    travel = np.exp(model.predict(ss.transform(copy_df)))

    copy_df = sample_df.copy()
    energys = copy_df[[ 'Heating Energy Source_coal','How Often Shower', 'How Long TV PC Daily Hour',
                         'Heating Energy Source_electricity','How Long Internet Daily Hour',
                         'Heating Energy Source_natural gas',
                         'Cooking_with_stove',
                          'Cooking_with_oven',
                          'Cooking_with_microwave',
                          'Cooking_with_grill',
                          'Cooking_with_airfryer',
                         'Heating Energy Source_wood','Energy efficiency']]
    copy_df[list(set(copy_df.columns) - set(energys.columns))] = 0
    energy = np.exp(model.predict(ss.transform(copy_df)))

    copy_df = sample_df.copy()
    wastes = copy_df[[  'Do You Recyle_Paper','How Many New Clothes Monthly',
                         'Waste Bag Size',
                         'Waste Bag Weekly Count',
                         'Do You Recyle_Plastic',
                         'Do You Recyle_Glass',
                         'Do You Recyle_Metal',
                         'Social Activity',]]
    copy_df[list(set(copy_df.columns) - set(wastes.columns))] = 0
    waste = np.exp(model.predict(ss.transform(copy_df)))

    copy_df = sample_df.copy()
    diets = copy_df[[ 'Diet_omnivore',
                     'Diet_pescatarian',
                     'Diet_vegan',
                     'Diet_vegetarian', 'Monthly Grocery Bill','Transport_private',
                     'Transport_public',
                     'Transport_walk/bicycle',
                      'Heating Energy Source_coal',
                      'Heating Energy Source_electricity',
                      'Heating Energy Source_natural gas',
                      'Heating Energy Source_wood',
                      ]]
    copy_df[list(set(copy_df.columns) - set(diets.columns))] = 0
    diet = np.exp(model.predict(ss.transform(copy_df)))
    hesap = {"Travel": travel[0], "Energy": energy[0], "Waste": waste[0], "Diet": diet[0]}

    return hesap


def chart(model, scaler,sample_df, prediction):
    p = hesapla(model, scaler,sample_df)
    bbox_props = dict(boxstyle="round", facecolor="white", edgecolor="white", alpha=0.7)

    plt.figure(figsize=(10, 10))
    patches, texts = plt.pie(x=p.values(),
                             labels=p.keys(),
                             explode=[0.03] * 4,
                             labeldistance=0.75,
                             colors=["#29ad9f", "#1dc8b8", "#99d9d9", "#b4e3dd" ], shadow=True,
                             textprops={'fontsize': 20, 'weight': 'bold', "color": "#000000ad"})
    for text in texts:
        text.set_horizontalalignment('center')

    data = io.BytesIO()
    plt.savefig(data, transparent=True)

    background = Image.open("./media/default.png")
    draw = ImageDraw.Draw(background)
    font1 = ImageFont.truetype(font="./style/ArchivoBlack-Regular.ttf", size=50)
    font = ImageFont.truetype(font="./style/arialuni.ttf", size=50)
    draw.text(xy=(320, 50), text=f"  How big is your\nCarbon Footprint?", font=font1, fill="#039e8e", stroke_width=1, stroke_fill="#039e8e")
    draw.text(xy=(370, 250), text=f"Monthly Emission \n\n   {prediction:.0f} kgCO₂e", font=font, fill="#039e8e", stroke_width=1, stroke_fill="#039e8e")
    data_back = io.BytesIO()
    background.save(data_back, "PNG")
    background = Image.open(data_back).convert('RGBA')
    piechart = Image.open(data)
    ayak = Image.open("./media/ayak.png").resize((370, 370))
    bg_width, bg_height = piechart.size
    ov_width, ov_height = ayak.size
    x = (bg_width - ov_width) // 2
    y = (bg_height - ov_height) // 2
    piechart.paste(ayak, (x, y), ayak.convert('RGBA'))
    background.paste(piechart, (40, 200), piechart.convert('RGBA'))
    data2 = io.BytesIO()
    background.save(data2, format="PNG")
    background = Image.open(data2).resize((700, 700))
    data3 = io.BytesIO()
    background.save(data3, "PNG")
    return data3
