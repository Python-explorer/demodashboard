import streamlit as st
import pandas as pd 
import os

def show_risk():
    st.markdown("<h1 style='color: black;'>Risk</h1>", unsafe_allow_html=True)
    st.write("Debug: Entered show_risk_content function")
    st.write("Risk-related content displayed here.")

    url = 'https://raw.githubusercontent.com/Python-explorer/demodashboard/main/risk/Risk.csv'
    try:
        # Attempt to read the CSV with some common debugging parameters
        df = pd.read_csv(url, error_bad_lines=False, quotechar='"', escapechar='\\')
        st.write(df)
    except Exception as e:
        st.error(f"An error occurred while reading the file: {e}")

 
