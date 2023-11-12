import streamlit as st

# Function to create an HTML string for a 5x5 grid with 'test' in the first cell
def create_grid_with_test(rows, cols):
    table = "<table>"
    for row in range(rows):
        table += "<tr>"
        for col in range(cols):
            if row == 0 and col == 0:  # First cell
                table += "<td style='border:1px solid black; width: 50px; height: 50px; color: black;'>Test</td>"
            else:
                table += "<td style='border:1px solid black; width: 50px; height: 50px;'></td>"
        table += "</tr>"
    table += "</table>"
    return table

# Create a 5x5 grid with 'test' in the first cell
grid_html = create_grid_with_test(5, 5)

# Display the grid in Streamlit
st.markdown(grid_html, unsafe_allow_html=True)
