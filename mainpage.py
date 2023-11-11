import streamlit as st
import numpy as np
from bokeh.plotting import figure
from bokeh.models import ColumnDataSource
from bokeh.layouts import gridplot

# Function to create a Bokeh bar chart with random data
def create_bar_chart():
    categories = ['A', 'B', 'C', 'D', 'E']
    data = np.random.randint(1, 100, size=5)
    source = ColumnDataSource(data=dict(categories=categories, data=data))
    p = figure(x_range=categories, height=250, title="Sample Bar Chart",
               toolbar_location=None, tools="")
    p.vbar(x='categories', top='data', width=0.9, source=source)
    p.xgrid.grid_line_color = None
    p.y_range.start = 0
    return p

# Set the page config to wide mode
st.set_page_config(layout="wide", page_title="Demo Assurance Dashboard")

# Create the sidebar with radio buttons
st.sidebar.title('Demo Assurance Dashboard')
options = ['Headline Charts', 'Planned care', 'Urgent care', 'Mental health', 'General practice', 'Primary and community', 'Inequality', 'Risk', 'Insight']
selection = st.sidebar.radio("Choose a category", options)

# Show the main page with Bokeh bar charts if 'Headline Charts' is selected
if selection == 'Headline Charts':
    st.header('Headline Charts')
    charts = [create_bar_chart() for _ in range(6)]
    # Arrange the charts in two columns and three rows
    grid = gridplot(charts, ncols=2, sizing_mode='scale_width')
    st.bokeh_chart(grid)
