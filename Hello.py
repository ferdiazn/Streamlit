import streamlit as st
import pandas as pd

df=pd.read_csv("dataset/Retail_Transaction_Dataset.csv")

st.set_page_config(
    page_title="Hello",
)

st.markdown("# Hi, My name is Ferdian 👋")

st.markdown(
    """
    Highly motivated Management Retail graduate from the University of Pelita Harapan with strong communication skills and a proven work ethic. 
    Recently completed 4 months internship at Indonesia Eximbank, demonstrating proficiency in business operations. 
    Currently pursuing a data science course on dibimbing.id to expand my technical skill set. 
    Seeking a challenging position that leverages my business acumen and allows me to develop both soft and technical skills within a dynamic company.

    **Here is** some of my project such as my final project as Data Scientist
    Bootcamp at dibimbing.id

"""
)

st.dataframe(df)
