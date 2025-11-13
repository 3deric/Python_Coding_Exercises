import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt
from pypalettes import load_cmap
from drawarrow import fig_arrow
from pyfonts import load_google_font
from highlight_text import fig_text, ax_text

def plot_choropleth_map():
    #colormap
    cmap = load_cmap("BrwnYl", cmap_type="continuous")
    background_color = "white"
    text_color = "black"

    # load the fonts
    font = load_google_font("Bebas Neue")
    other_font = load_google_font("Fira Sans", weight="light")
    other_bold_font = load_google_font("Fira Sans", weight="medium")

    
    # arrow properties
    arrow_props = dict(width=0.5, head_width=4, head_length=8, color="black")

    #load geojson of europe
    url = "./data/europe.geojson"
    world = gpd.read_file(url)
    world.head()

    #load csv data
    url = "./data/co2PerCapita.csv"
    df = pd.read_csv(url)

    #merge csv data by name with the world data
    #merges datasets based on name for first and country for second
    data = world.merge(df, how="left", left_on="name", right_on="Country")

    #filter the dataset, by europe, removes russia and iceland and sets year to 2021
    data = data[data["continent"] == "Europe"]
    data = data[~data["name"].isin(["Russia", "Iceland"])]
    data = data[data["Year"] == 2021]
    data = data[["name", "Total", "geometry"]]
    #remove not available data
    data = data.dropna()
    data.head()
    
    #debug print merged data
    print(data)

    #create a figure
    fig, ax = plt.subplots(figsize=(10, 10), dpi = 72)
    fig.set_facecolor(background_color)
    ax.set_facecolor(background_color)

    #plot the data
    data.plot(ax=ax, column = "Total", cmap = cmap, edgecolor = "black", linewidth = 0.5)

    #limit the axis and disable axis display
    ax.set_xlim(-11, 41)
    ax.set_ylim(32, 73)
    ax.set_axis_off()

    #calculate the center of each country
    data_projected = data.to_crs(epsg = 3035)
    data_projected["centroid"] = data_projected.geometry.centroid
    data["centroid"] = data_projected["centroid"].to_crs(data.crs)

    countries_to_annotate = [
                "France",
                "Italy",
                "Romania",
                "Poland",
                "Finland",
                "Ukraine",
                "Spain",
                "Germany",
                "Sweden",
                "United Kingdom",
                "Belarus",
                "Norway",
                ]
    
    adjustments = {
                "France": (10, 3),
                "Italy": (-2.4, 2.5),
                "Finland": (0, -2),
                "Belarus": (0, -0.4),
                "Ireland": (0, -1),
                "Germany": (-0.2, 0),
                "Poland": (0, 0.2),
                "Sweden": (-1.2, -2.8),
                "United Kingdom": (1, -1.5),
                "Norway": (-4, -5.5),
                }
    
    #create annotations for each country
    for country in countries_to_annotate:
        centroid = data.loc[data["name"] == country, "centroid"].values[0]
        x, y = centroid.coords[0]
        try:
            x += adjustments[country][0]
            y += adjustments[country][1]
        except KeyError:
            pass
        rate = data.loc[data["name"] == country, "Total"].values[0]
        if country == "United Kingdom":
            country = "UK"
        if rate > 7:
            color_text = "white"
        else:
            color_text = text_color
        ax_text(
            x = x,
            y = y,
            s=f"<{country.upper()}>: {rate:.2f}",
            fontsize = 10,
            color = color_text,
            ha = "center",
            va = "center",
            ax = ax,
            highlight_textprops=[{"font": other_bold_font}],
        )

    # title
    fig_text(
        s="CO2 emissions per capita in Europe (2021)",
        x=0.5,
        y=0.14,
        color=text_color,
        fontsize=25,
        font=font,
        ha="center",
        va="top",
        ax=ax,
    )

    # subtitle
    fig_text(
        s="<Unit>: metric tons | <Data>: zenodo.org | <Viz>: barbierjoseph.com",
        x=0.5,
        y=0.1,
        color=text_color,
        fontsize=14,
        font=other_font,
        ha="center",
        va="top",
        ax=ax,
        highlight_textprops=[
            {"font": other_bold_font},
            {"font": other_bold_font},
            {"font": other_bold_font},
        ],
    )

    # arrows for the Luxembourg
    luxembourg_values = data.loc[data["name"] == "Luxembourg", "Total"].values[0]
    fig_arrow(
        tail_position=(0.32, 0.7), head_position=(0.375, 0.45), radius=0.3, **arrow_props
    )
    fig_text(
        s=f"<LUXEMBOURG>: {luxembourg_values:.2f}",
        x=0.32,
        y=0.71,
        highlight_textprops=[{"font": other_bold_font}],
        color=text_color,
        fontsize=9,
        font=other_font,
        ha="center",
        va="center",
        fig=fig,
    )
    #show the plot
    plt.show()
    


if __name__ == "__main__":
    plot_choropleth_map()