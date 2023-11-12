import streamlit as st
import pandas as pd

def show_risk():
    url = 'https://raw.githubusercontent.com/Python-explorer/demodashboard/main/risk/Risk.csv'
    try:
        # Read the CSV into a DataFrame
        df = pd.read_csv(url)
        # Display the DataFrame as a table in Streamlit
        st.write(df)
# Correct indentation: This call should be outside and after the function definition
show_risk()
