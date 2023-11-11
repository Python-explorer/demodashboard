import streamlit as st
from bokeh.plotting import figure  # Make sure this import is included
from charts import generate_chart_1  # Import the modular chart function from charts.py
from bokeh.layouts import gridplot

# Function to create empty placeholder charts
def create_placeholder_chart():
    p = figure(height=250, width=250, title="Placeholder Chart")
    p.outline_line_color = None
    return p

# Set the page config to wide mode
st.set_page_config(layout="wide", page_title="Demo Assurance Dashboard")

# Create the sidebar with radio buttons
st.sidebar.title('Demo Assurance Dashboard')
options = ['Headline Charts', 'Planned care', 'Urgent care', 'Mental health', 'General practice', 'Primary and community', 'Inequality', 'Risk', 'Insight']
selection = st.sidebar.radio("Choose a category", options)

# Main page content
if selection == 'Headline Charts':
    st.markdown("<h1 style='color: black;'>Headline Charts</h1>", unsafe_allow_html=True)

    # Use the imported function to create the first chart
    first_chart = generate_chart_1()

    # Generate placeholder charts for the rest of the grid
    placeholder_charts = [create_placeholder_chart() for _ in range(5)]
    
    # Combine the first chart with the placeholders into a single list
    all_charts = [first_chart] + placeholder_charts

    # Arrange the charts in two columns and three rows
    grid = gridplot(all_charts, ncols=2, sizing_mode='scale_width')
    st.bokeh_chart(grid)
else:
    # For other selections, you can add appropriate content here
    st.write(f"You selected: {selection}")
