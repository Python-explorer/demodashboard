import streamlit as st
import pandas as pd

# Write the word 'test' to the Streamlit app
st.markdown("<span style='color: black;'>test</span>", unsafe_allow_html=True)
st.write('test')

# Raw URL of the CSV file in the GitHub repository
csv_url = 'https://raw.githubusercontent.com/Python-explorer/demodashboard/main/risk/Risk.csv'

# Load the CSV file into a DataFrame
df = pd.read_csv(csv_url)

st.write(df.head(2))

# Display the DataFrame as a table in Streamlit
st.table(df)



