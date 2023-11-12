import streamlit as st
import pandas as pd 
import os

def show_risk():
    st.markdown("<h1 style='color: black;'>Risk</h1>", unsafe_allow_html=True)
    url = 'https://raw.githubusercontent.com/Python-explorer/demodashboard/main/risk/Risk.csv'
    try:
        # Read the CSV into a DataFrame, specifying the line terminator if necessary
        df = pd.read_csv(url, lineterminator='\n')
        st.write(df)

    except Exception as e:
        st.error(f"An error occurred while reading the file: {e}")

show_risk()
