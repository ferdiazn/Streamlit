import streamlit as st
import pandas as pd
import numpy as np
import time

st.title('Demo: Loading Uber Pickup Data in NYC with Caching')

st.markdown(
    """
    Di script ini, kita bakal nulis Python code yang akan:
    - Nge-download dataset dari internet
    - Mengubah kolom tanggal menjadi format datetime
    - Setelah dataset tersebut ter-download, kita bisa tampilkan dataset tersebut as a Pandas Dataframe

    But now, we do it with caching!
    """
)

DATE_COLUMN = 'Date/Time'
DATA_URL = ('https://s3-us-west-2.amazonaws.com/'
            'streamlit-demo-data/uber-raw-data-sep14.csv.gz')

@st.cache_data
def load_data(nrow):
    ### Simulating Loading a Large Dataset
    data = pd.read_csv(DATA_URL, nrows=nrow)

    chunk_1 = data[0:200]
    chunk_2 = data[200:400]
    chunk_3 = data[400:600]
    chunk_4 = data[600:800]
    chunk_5 = data[800:]

    all_chunk = [chunk_1, chunk_2, chunk_3, chunk_4, chunk_5]

    new_data = pd.DataFrame()
    counter_text = st.text('Processing...')
    for i, chunk in enumerate(all_chunk):
        counter_text.text(f"Processing Part {i+1}/{len(all_chunk)}")
        time.sleep(0.6)
        new_data = new_data.append(chunk).reset_index(drop = True)
    del counter_text
    
    data[DATE_COLUMN] = pd.to_datetime(data[DATE_COLUMN])
    return data

data_load_state = st.text('Loading data...')
data = load_data(1000)
data_load_state.text('Done!')

if st.checkbox('Show raw data'):
    st.subheader('Raw data')
    st.write(data)

st.markdown(
    """
    Nah, sekarang coba refresh the app. Seharusnya, dia nggak akan nge-download ulang dataset tersebut.

    Caching memungkinkan kita agar, jika app kita di refresh, tapi tidak ada perubahan ke suatu 'function', maka..
    ..'hasil' running dari function ini tetap disimpan sama Streamlit, sehingga function ini tidak akan di re-run tiap kali kita refresh the app.
    """
)