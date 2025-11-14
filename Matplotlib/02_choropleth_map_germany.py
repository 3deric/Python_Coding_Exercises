import pandas as pd
import geopandas as gpd
import json
import numpy as np
import matplotlib.pyplot as plt
from pypalettes import load_cmap
from pyfonts import load_google_font


def plot_choropleth_map():
    #colormap
    cmap = load_cmap("BrwnYl", cmap_type="continuous")
    background_color = "white"
    text_color = "black"

    # load the fonts
    font = load_google_font("Bebas Neue")
    other_font = load_google_font("Fira Sans", weight="light")
    other_bold_font = load_google_font("Fira Sans", weight="medium")

    #load geojson of germany
    url = "./data/landkreise_simplify200.geojson"
    gdf = gpd.read_file(url)

    #transform string into json dictionary for destatis column
    #split dictionary in columns and delete original column
    gdf["destatis"] = gdf["destatis"].apply(json.loads)
    gdf = gdf.join(gdf["destatis"].apply(pd.Series))
    
    gdf["m_or_w"] = np.where(gdf["population_m"] >= gdf["population_w"], True, False)

    print(gdf.columns)
    #print(gdf.head(5))
    
    #create a figure
    fig, ax = plt.subplots(figsize=(10, 10), dpi = 150)
    #fig.set_facecolor(background_color)
    #ax.set_facecolor(background_color)

    #plot the data
    gdf.plot(ax=ax, column = "m_or_w" ,cmap = cmap, edgecolor = "black", linewidth = 0.5)

    #limit the axis and disable axis display
    ax.set_xlim(5.5, 15.5)
    ax.set_ylim(47, 55.5)
    ax.set_axis_off()

    #calculate the center of each country
    data_projected = gdf.to_crs(epsg = 3035)
    data_projected["centroid"] = data_projected.geometry.centroid
    gdf["centroid"] = data_projected["centroid"].to_crs(gdf.crs)

    #show the plot
    plt.show()
    

if __name__ == "__main__":
    plot_choropleth_map()