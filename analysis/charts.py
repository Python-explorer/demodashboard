import pandas as pd
import numpy as np
from bokeh.plotting import figure, show, output_file
from bokeh.models import ColumnDataSource

def generate_chart_1():
    url = 'https://raw.githubusercontent.com/Python-explorer/demodashboard/main/analysis/UHS65.csv'
    df = pd.read_csv(url)
    treatment_functions = df['Treatment Function'].loc[df['Treatment Function'] != 'Total']
    data = df.loc[df['Treatment Function'] != 'Total', :].iloc[:, 1:]
    p = figure(x_range=list(df.columns[1:]), plot_height=400, title="Number of Patients Over Time by Treatment Function", x_axis_label="Month", y_axis_label="Number of Patients")
    source = ColumnDataSource(data)
    num_colors = len(treatment_functions)
    color_palette = ["#%06x" % np.random.randint(0, 0xFFFFFF) for _ in range(num_colors)]
    for i, treatment_function in enumerate(treatment_functions):
        p.line(df.columns[1:], data.iloc[i, :], line_color=color_palette[i], legend_label=treatment_function, line_width=2)
    p.legend.title = "Treatment Function"
    p.legend.label_text_font_size = "10pt"
    p.legend.location = "top_left"
    p.legend.click_policy = "hide"
    show(p)
    return p
