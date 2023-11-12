import streamlit as st
import pandas as pd

def show_risk():
    url = 'https://raw.githubusercontent.com/Python-explorer/demodashboard/main/risk/Risk.csv'
    df = pd.read_csv(url)
    st.write(df)


# This call should be at the top-level indentation, not inside any function or conditional block
show_risk()
