
import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="My Streamlit App",
    layout="wide",
    initial_sidebar_state="expanded",
    theme={
        "base": "light",
        "textColor": "#000000",
        "primaryColor": "#f63366",
        "backgroundColor": "#ffffff",
        "secondaryBackgroundColor": "#f0f2f6",
    }
)


# Raw URL of the CSV file in the GitHub repository
csv_url = 'https://raw.githubusercontent.com/Python-explorer/demodashboard/main/risk/Risk.csv'

# Load the CSV file into a DataFrame and ensure proper data types, if necessary
df = pd.read_csv(csv_url, dtype={"text_column1": str, "text_column2": str, "num_column1": float, "num_column2": float, "num_column3": float})

# Display the DataFrame as a table in Streamlit to debug
st.write("Displaying the first two rows of the DataFrame:")
st.write(df.head(2))

# Display the DataFrame as a table in Streamlit
st.write("Displaying the full DataFrame:")
st.table(df)



