import streamlit as st
import pickle
import pandas as pd
import numpy as np
import requests

API_URL = 'http://127.0.0.1:8000/predict'

st.set_page_config(page_title="Main Page",
                   layout = 'wide')  #set browser tab title

#importing model and dataset

with open('../1_Datasets/5.3_dataset_final.pkl', 'rb') as file:
    df = pickle.load(file)


#Create user input boxes

#sector input
sector = st.selectbox(label = "Sector", options=df['sector'].str.capitalize().sort_values().unique()).lower()

#super_area
super_area = float(st.number_input(label = 'Super Built-up Area',placeholder='Enter Super Built-up Area'))

#bedroom
bedrooms = int(st.selectbox(label = "Bedrooms", options=sorted(df['bedrooms'].unique())))

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
    #1. Create input data

    input_data = {
        'sector':sector,
        'super_area' : super_area,
        'bedrooms' : bedrooms,
        'bathroom' : bathroom,
        'balcony' : balcony,
        'age_possession' : age_possession,
        'servant_room' : servant_room,
        'luxury_category' : luxury_category,
        'parking' : parking,
        'building_type' : building_type
    }
    #display the inputs as dataframe
    st.dataframe(input_data)

    #perform api call
    try: 
        response = requests.post(API_URL,json=input_data)
        result = response.json()

        if response.status_code == 200 and "response" in result:

            prediction = result('response')
            upper_limit = round(prediction + 0.28,2)
            lower_limit = round(prediction - 0.28,2)
            st.text(f'The predicted house price is between {lower_limit}Cr and {upper_limit}Cr')
        
        else:
            st.error(body= f'API Error {response.status_code}')
            st.write(response.json())
    
    except requests.exceptions.ConnectionError:
        st.error("❌ Could not connect to the FastAPI server. Make sure it's running.")


    