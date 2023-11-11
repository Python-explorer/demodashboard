# File: charts.py
import numpy as np
from bokeh.plotting import figure
from bokeh.models import ColumnDataSource

def generate_chart_1():
    categories = ['A', 'B', 'C', 'D', 'E']
    data = np.random.randint(1, 100, size=5)
    source = ColumnDataSource(data=dict(categories=categories, data=data))
    p = figure(x_range=categories, height=250, title="Modular Chart",
               toolbar_location=None, tools="")
    p.vbar(x='categories', top='data', width=0.9, source=source)
    p.xgrid.grid_line_color = None
    p.y_range.start = 0
    return p
