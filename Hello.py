import streamlit as st
import pandas as pd

df=pd.read_csv("dataset/Retail_Transaction_Dataset.csv")

st.set_page_config(
    page_title="Hello",
)

st.markdown("# Hi, My name is Ferdian 👋")

st.markdown(
    """
    Welcome to your first streamlit app!

    ** Here is** some of my project such as my final project as Data Scientist
    Bootcamp at dibimbing.id

"""
)

st.dataframe(df)
