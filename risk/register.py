import streamlit as st
import pandas as pd

def display_csv_as_table():
    csv_url = 'path_or_url_to_your_csv_file.csv'  # Ensure this is correct

    try:
        df = pd.read_csv(csv_url)

        if df.empty:
            st.write("The DataFrame is empty. Check your CSV file.")
        else:
            st.write("## Data from CSV File")
            st.table(df)
    except Exception as e:
        st.error(f"An error occurred while reading the file: {e}")

def main():
    st.title("CSV Viewer App")
    display_csv_as_table()

if __name__ == "__main__":
    main()
