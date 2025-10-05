import streamlit as st
import pickle
import pandas as pd
import numpy as np
import os

st.set_page_config(page_title="Main Page",
                   layout = 'wide')  #set browser tab title

#importing model and dataset
MAIN_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATASET_PATH = os.path.join(MAIN_DIR,'1_Datasets','5.3_dataset_final.pkl')
MODEL_PATH = os.path.join(MAIN_DIR,'3_models','3.1_pipeline.pkl')
with open(DATASET_PATH, 'rb') as file:
    df = pickle.load(file)


# Create use input boxes

#'sector', 'super_area', 'bedrooms', 'bathroom', 'balcony','age_possession', 'servant_room', 'luxury_category', 'parking','building_type']

#sector input

sector = st.selectbox(label = "Sector", options=df['sector'].str.capitalize().sort_values().unique()).lower()

#super_area
super_area = float(st.number_input(label = 'Super Built-up Area',placeholder='Enter Super Built-up Area'))

#bedroom
bedroom = int(st.selectbox(label = "Bedrooms", options=sorted(df['bedrooms'].unique())))

#bathroom
bathroom = int(st.selectbox(label='Bathroom', options= sorted(df['bathroom'].unique())))

#balcony
balcony = st.selectbox(label = "Balcony", options=sorted(df['balcony'].unique())).lower()

#age_possession
age_possession = st.selectbox(label = "Age", options=sorted(df['age_possession'].unique())).lower()

#servant room
servant_room = st.selectbox(label='Servant Room', options = ['Yes','No'])
servant_room = 1 if servant_room =='Yes' else 0

#luxury_category
luxury_category = st.selectbox(label = "Luxury Category", options=df['luxury_category'].str.capitalize().sort_values().unique()).lower()

#parking
parking = int(st.selectbox(label = 'Parking', options = sorted(df['parking'].unique())))

#building type
building_type = st.selectbox(label = 'Building type', options=df['building_type'].str.capitalize().sort_values().unique()).lower()


#do prediction
if st.button('Predict'):
    #1. Create dataframe
    inputs = [[sector, super_area, bedroom, bathroom, balcony,age_possession, servant_room, luxury_category, parking ,building_type]]
    print(inputs)

    input_df = pd.DataFrame(data = inputs , columns= df.columns)
    print(input_df.columns.shape)
    #2.Predict
    with open(MODEL_PATH,'rb') as file:
        piepline = pickle.load(file)
        print(piepline['preprocessor'].get_feature_names_out().shape)
        prediction = np.expm1(piepline.predict(input_df))[0]
    
    #display
    st.dataframe(input_df)
    upper_limit = round(prediction + 0.28,2)
    lower_limit = round(prediction - 0.28,2)
    st.text(f'The predicted house price is between {lower_limit}Cr and {upper_limit}Cr')