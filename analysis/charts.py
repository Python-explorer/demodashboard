import numpy as np
from bokeh.plotting import figure
from bokeh.models import ColumnDataSource, Legend
import pandas as pd
from bokeh.layouts import column

def generate_chart_1():
    # Load the UHS65.csv file into a DataFrame
    url = 'https://raw.githubusercontent.com/Python-explorer/demodashboard/main/analysis/UHS65.csv'
    df = pd.read_csv(url)

    # Extract treatment function names (excluding 'Total')
    treatment_functions = df['Treatment Function'].loc[df['Treatment Function'] != 'Total']

    # Extract data for plotting (excluding 'Total' row)
    data = df.loc[df['Treatment Function'] != 'Total', :].iloc[:, 1:]

    # Create a Bokeh figure
    p = figure(x_range=list(df.columns[1:]), plot_height=400, title="UHSx 65ww by Treatment Function Time Series", x_axis_label="Month", y_axis_label="Number of Patients")

    # Prepare the data for plotting
    source = ColumnDataSource(data)

    # Generate a unique color for each treatment function
    num_colors = len(treatment_functions)
    color_palette = ["#%06x" % np.random.randint(0, 0xFFFFFF) for _ in range(num_colors)]

    # Plot a line for each treatment function
    for i, treatment_function in enumerate(treatment_functions):
        line = p.line(df.columns[1:], data.iloc[i, :], line_color=color_palette[i], line_width=2)
        legend = Legend(items=[(treatment_function, [line])], title="Treatment Function")
        p.add_layout(legend, 'below')

    return p
    # Test
