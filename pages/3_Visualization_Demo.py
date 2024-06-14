import streamlit as st
import pandas as pd
import numpy as np
import time

import folium
import branca.colormap as cm
from streamlit_folium import folium_static
import plotly.express as px

st.title('Demo: Visualizing')

st.markdown(
    """
    Di script ini, kita bakal nulis Python code yang akan:
    - Loading a dataset from our folder
    - Do visualizations about it
    """
)

df = pd.read_csv('dataset/Cleaned Apartment Data.csv')

@st.cache_data
def show_data():
    st.write(df)

@st.cache_data
def draw_map():
    # First, we need to know where is our map's center
    centerlat = (df['Latitude'].max() + df['Latitude'].min()) / 2
    centerlon = (df['Longitude'].max() + df['Longitude'].min()) / 2

    center_map = centerlat, centerlon

    # Then, we define how we'd like to set the color
    colormap = cm.LinearColormap(colors = ['lightgreen', 'green', 'darkgreen'], vmin = df['AnnualPrice'].min(), vmax = df['AnnualPrice'].max())
    m = folium.Map(location=center_map, zoom_start=10, tiles='OpenStreetMap')

    # For each 'row' in the dataframe, add it to the map, according to their longitude, latitude, and price value
    for lat, lon, ap in zip(df['Latitude'], df['Longitude'], df['AnnualPrice']):
        folium.Circle(
            location = [lat, lon],
            radius = 100,
            fill = True,
            color = colormap(ap),
            fill_opacity = 0.25,
            weight = 5
        ).add_to(m)

    # Display the map
    m.add_child(colormap)
    folium_static(m)


if st.checkbox('Show Data!'):
    show_data()

st.subheader('Map Visualization of Apartments for Rent in Jakarta')
draw_map()

st.subheader('Scatterplot of Price and Area')

unique_region_list = ['All']
unique_region_list.extend(df.Region.unique().tolist())

region_select = st.selectbox('Select region:', unique_region_list)

@st.cache_data
def visualize_scatterplot(region):
    if region == 'All':
        fig = px.scatter(df, x = 'Area', y = 'AnnualPrice', color = 'No_Rooms')
        st.plotly_chart(fig, theme = 'streamlit')
    else:
        df_select = df[df['Region'] == region]
        fig = px.scatter(df_select, x = 'Area', y = 'AnnualPrice', color = 'No_Rooms')
        st.plotly_chart(fig, theme = 'streamlit')        

visualize_scatterplot(region_select)

st.subheader('Price Boxplot for Apartments in Jakarta')

@st.cache_data
def visualize_boxplot():
    tab1, tab2 = st.tabs(['By Number of Bedrooms', 'By Region'])
    with tab1:
        fig = px.box(df, x = 'No_Rooms', y='AnnualPrice')
        st.plotly_chart(fig, theme = 'streamlit', use_container_width = True)
    with tab2:
        fig = px.box(df, x = 'Region', y = 'AnnualPrice')
        st.plotly_chart(fig, theme = 'streamlit', use_container_width = True)

visualize_boxplot()