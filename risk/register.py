import streamlit as st
import pandas as pd 
import os

def show_risk():
    url = 'https://raw.githubusercontent.com/Python-explorer/demodashboard/main/risk/Risk.csv'
    try:
        # Read the CSV into a DataFrame, specifying the line terminator if necessary
        df = pd.read_csv(url)
        st.write(df)
show_risk()
