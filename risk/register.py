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
        # Read the CSV with specific data types for 'Risk' and 'Mitigation' columns
        df = pd.read_csv(url, on_bad_lines='skip', dtype={'Risk': str, 'Mitigation': str})

        # Display the DataFrame as a table in Streamlit
        st.write(df)
    except Exception as e:
        st.error(f"An error occurred while reading the file: {e}")

show_risk()


 
