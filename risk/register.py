import streamlit as st
import pandas as pd 
import os

def show_risk():
    st.markdown("<h1 style='color: black;'>Risk</h1>", unsafe_allow_html=True)
    st.write("Debug: Entered show_risk_content function")
    # Your code to display the risk content goes here
    st.write("Risk-related content displayed here.")
    # More Streamlit commands to display data, charts, etc.
    url = 'https://raw.githubusercontent.com/Python-explorer/demodashboard/main/risk/Risk.csv'
    try:
        df = pd.read_csv(url)
        # Display the DataFrame as a table in Streamlit
        st.write(df)

 
