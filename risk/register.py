import streamlit as st
import pandas as pd 
import os
import streamlit as st
import pandas as pd

def show_risk():
    st.markdown("<h1 style='color: black;'>Risk</h1>", unsafe_allow_html=True)
    st.write("Debug: Entered show_risk_content function")
    st.write("Risk-related content displayed here.")

    url = 'https://raw.githubusercontent.com/Python-explorer/demodashboard/main/risk/Risk.csv'
    try:
        # Display the DataFrame as a table in Streamlit
        st.write(df)

 
