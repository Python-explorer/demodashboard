import streamlit as st
import pandas as pd

def display_csv_as_table():
    # URL or path to your CSV file
    csv_url = 'https://raw.githubusercontent.com/Python-explorer/demodashboard/main/risk/Risk.csv'

    try:
        # Read the CSV file
        df = pd.read_csv(csv_url)

        # Display the DataFrame as a table in Streamlit
        st.write("## Data from CSV File")
        st.table(df)

    except Exception as e:
        st.error(f"An error occurred while reading the file: {e}")

def main():
    st.title("CSV Viewer App")
    display_csv_as_table()

if __name__ == "__main__":
    main()
