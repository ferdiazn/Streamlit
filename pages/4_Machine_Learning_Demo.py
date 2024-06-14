import streamlit as st
import pandas as pd
import numpy as np
import time

import pickle
import lightgbm
from lightgbm import LGBMRegressor

st.title('Demo: Machine Learning')

st.markdown(""" Prerequisite:
    - You have to save a usable model first
    - Your saved model is accessible from the directory of this project """)

@st.cache_data
def load_model():
    return pickle.load(open('model/regression_lgb.pkl', 'rb'))

@st.cache_data
def load_region_data():
    return pd.read_csv('dataset/Longitude Latitude.csv')

model = load_model()
region_data = load_region_data()

st.subheader("Fill in your apartment information below and we'll guess the price!")

no_rooms = st.radio('Number of Rooms: ', ['Studio', '1BR', '2BR', '3BR', '4+BR'])
if no_rooms == 'Studio':
    no_rooms = 0
elif no_rooms == '1BR':
    no_rooms = 1
elif no_rooms == '2BR':
    no_rooms = 2
elif no_rooms == '3BR':
    no_rooms = 3
else:
    no_rooms = 4

bathroom = st.radio('Number of Bathrooms: ', [1, 2, 3])

furnished = st.radio('Is your apartment fully furnished?', ['Yes', 'No'])
if furnished == 'Yes':
    furnished = 1
else:
    furnished = 0

water_heater = st.radio('Does it come with a water heater included?', ['Yes', 'No'])
if water_heater == 'Yes':
    water_heater = 1
else:
    water_heater = 0

area = st.slider('How large is your apartment? (Area)', 20, 200, 30)

region = st.selectbox("Where is your apartment located? (City)", region_data.Region.unique().tolist())
if region:
    locality = st.selectbox("Where is your apartment located? (Subdistrict)", region_data.query(f"Region == '{region}'")['Locality'].unique().tolist())

selected_region = region_data.query(f"Region == '{region}' & Locality == '{locality}'").reset_index(drop = True)

longitude = selected_region.Longitude.values[0]
latitude = selected_region.Latitude.values[0]

your_apartment = pd.DataFrame({
    'No_Rooms':[no_rooms],
    'Bathroom':[bathroom],
    'Longitude' :[longitude],
    'Latitude':[latitude],
    'Area':[area],
    'Furnished':[furnished],
    'Water_Heater':[water_heater],
    'InJakarta':[1 if 'Jakarta' in region else 0]

})

if st.button('Calculate Price!'):
    your_apartment_price = model.predict(your_apartment)
    your_apartment_price = your_apartment_price[0]
    your_apartment_price = np.round(your_apartment_price)
    st.write(f"### Your apartment's annual rent price is predicted at: IDR {your_apartment_price}")






