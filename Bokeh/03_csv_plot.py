import pandas as pd
from bokeh.plotting import curdoc, figure, show
from bokeh.palettes import all_palettes as ap
from bokeh.layouts import row


def main():
    file = "./data/01_climate_data.csv"
    climate_data = pd.read_csv(file)  
    print(climate_data)
    
    curdoc().theme = "caliber"
    palette = ap['Category20'][20]

    TOOLTIPS = [
        ("Latitude", "$name"),
        ("Year:", "$x{int}"),
        ("Deviation:", "$y{1.1} °C")
    ]

    plot = figure(title = "Climate Data",
                    x_axis_label = "Year",
                    y_axis_label = "Deviation",
                    width = 800,
                    height = 600,
                    tooltips = TOOLTIPS)
    
    plot.grid.minor_grid_line_color = '#eeeeee'

    plot_global = figure(title = "Climate Data Global Average",
                    x_axis_label = "Year",
                    y_axis_label = "Deviation",
                    width = 800,
                    height = 600,
                    tooltips = TOOLTIPS)
    
    plot_global.grid.minor_grid_line_color = '#eeeeee'
    
    for index, column in enumerate(climate_data.columns):
        if column == "Year":
            continue
        plot.circle(x = "Year", 
                    y = column, 
                    legend_label = column,
                    name = column,
                    source = climate_data, 
                    radius = 0.5, 
                    fill_color = palette[index], 
                    fill_alpha = 0.75, 
                    line_alpha = 0.0)
        
        if column != "Glob":
            continue
        plot_global.line(x = "Year", 
                         y = column, 
                         name = column,
                         source = climate_data, 
                         line_width= 1.0,
                         line_color = palette[6])

    plot.legend.location = "top_left"
    plot.legend.title = "Temperature deviation"
    plot.legend.ncols = 4
    show(row(children=[plot_global, plot], sizing_mode = "scale_width"))


if __name__ == "__main__":
    main()