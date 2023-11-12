import streamlit as st

# Function to create an HTML string for a blank 5x5 grid
def create_blank_grid(rows, cols):
    table = "<table>"
    for _ in range(rows):
        table += "<tr>"
        for _ in range(cols):
            table += "<td style='border:1px solid black; width: 50px; height: 50px;'></td>"
        table += "</tr>"
    table += "</table>"
    return table

# Create a 5x5 grid
grid_html = create_blank_grid(5, 5)

# Display the grid in Streamlit
st.markdown(grid_html, unsafe_allow_html=True)
