import requests
import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap

def iss_location():
    response = requests.get("http://api.open-notify.org/iss-now.json")
    if response.status_code == 200:
        data = response.json()
        iss_position = data["iss_position"]
        return iss_position
    else:
        return None


def iss_map(positions):
    lon = float(pos["longitude"])
    lat = float(pos["latitude"])
    geo_map = Basemap(projection="ortho", lat_0 = lat , lon_0 = lon)
    #geo_map.drawmapboundary(fill_color='#A6CAE0')
    #geo_map.fillcontinents(color='#69b2a2',lake_color='#A6CAE0')
    geo_map.drawcoastlines(color = "white", linewidth = 0.5)
    geo_map.bluemarble()
    x, y = geo_map(lon, lat)
    geo_map.plot(x, y, "ro", markersize = 5)
    plt.title("Current ISS position")
    plt.show()


if __name__ == "__main__":
    pos = iss_location()
    iss_map(pos)
