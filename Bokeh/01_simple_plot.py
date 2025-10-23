import numpy as np
from bokeh.plotting import curdoc, figure, show
from bokeh.palettes import all_palettes as ap
from bokeh.layouts import row


def main():
    x = np.arange(0,10,0.1)

    y1 = np.sin(x * 2) * 10
    y2 = np.cos(x * 3) * 10
    y3 = np.tan(x)

    curdoc().theme = "light_minimal"

    p1 = figure(title = "Sine Function",
                  x_axis_label = "X-Axis",
                  y_axis_label = "Y-Axis")
    
    p2 = figure(title = "Cosine Function",
                  x_axis_label = "X-Axis",
                  y_axis_label = "Y-Axis")
    
    p3 = figure(title = "Tangent Function",
                  x_axis_label = "X-Axis",
                  y_axis_label = "Y-Axis")
    
    p1.line(x, y1, legend_label = "Sin(x)", line_width = 2, color = "red")
    p2.line(x, y2, legend_label = "Cos(x)", line_width = 2, color = "green")
    p3.line(x, y3, legend_label = "Tan(x)", line_width = 2, color = "blue")

    show(row(children=[p1, p2, p3], sizing_mode = "scale_width"))
        
if __name__ == "__main__":
    main()