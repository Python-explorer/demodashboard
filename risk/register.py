import streamlit as st
import pandas as pd

def show_risk():
    url = 'https://raw.githubusercontent.com/Python-explorer/demodashboard/main/risk/Risk.csv'
    try:
        # Read the CSV into a DataFrame
        df = pd.read_csv(url)
        # Display the DataFrame as a table in Streamlit
        st.write(df)
    except Exception as e:
        st.error(f"An error occurred while reading the file: {e}")

# This call should be at the top-level indentation, not inside any function or conditional block
show_risk()
