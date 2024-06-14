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

    **👈 Select any pages from the sidebar** to see some examples
    of what we can achieve in Streamlit!

    ### Want to learn more?
    - Check out [streamlit.io](https://streamlit.io)
    - Jump into our [documentation](https://docs.streamlit.io)
    - Ask a question in our [community
        forums](https://discuss.streamlit.io)
        
    ### See more complex demos
    - Use a neural net to [analyze the Udacity Self-driving Car Image
        Dataset](https://github.com/streamlit/demo-self-driving)
    - Explore a [New York City rideshare dataset](https://github.com/streamlit/demo-uber-nyc-pickups)
"""
)

st.button("Reset", type="primary")
if st.button("Say hello"):
    st.write("Why hello there")
else:
    st.write("Goodbye")

st.dataframe(df)
