from collections import defaultdict

import cartopy
import cartopy.crs as ccrs
import cartopy.io.shapereader as shpreader
import matplotlib.font_manager as font_manager
import matplotlib.patches as mpatches
import matplotlib.pyplot as plt
from cartopy.feature import ShapelyFeature
from shapely.geometry import MultiPolygon, Polygon

from commons import COLORS_MAP, WIDTH_IN
from continents import get_continent


def load_worldmap_csv(filename: str) -> dict:
    with open(filename) as f:
        return {
            l.split(",")[0]: float(l.rstrip("\n").split(",")[1]) for l in f.readlines()
        }


def four_bins_color(x: float, xmin: float = 0.0, xmax: float = 1.0) -> str:
    # cs = ["#E85E4C", "#E8AC4C", "#F7F074", "#59D163"]
    cs = COLORS_MAP[:4]
    # Avoid exceeding array bounds
    bin = (xmax - xmin + 0.001) / 4
    return cs[int(x // bin)]


def map_threshold(ds, threshold):
    projection = ccrs.PlateCarree()
    plt.figure(figsize=(3.5, 1.5))
    ax = plt.axes(projection=projection)
    ax.add_feature(cartopy.feature.OCEAN, facecolor="#ffffff")
    ax.add_feature(cartopy.feature.BORDERS, linewidth=0.2)
    #    ax.outline_patch.set_edgecolor("k")
    ax.set_extent([-180, 180, -60, 90], ccrs.PlateCarree())

    shpfilename = shpreader.natural_earth(
        resolution="110m", category="cultural", name="admin_0_countries"
    )
    reader = shpreader.Reader(shpfilename)
    countries = reader.records()

    for country in countries:
        if country.attributes["NAME_EN"] == "France":
            country.attributes["ISO_A2"] = "FR"

        if country.attributes["NAME_EN"] == "Norway":
            country.attributes["ISO_A2"] = "NO"

        iso_code = country.attributes["ISO_A2"]
        color = "#DDDDDD"
        if iso_code in ds and ds.get(iso_code) != None:
            color = four_bins_color(ds[iso_code])
        else:
            color = "#ffffff"

        # BUG: cartopy v0.18
        geom = (
            country.geometry
            if isinstance(country.geometry, MultiPolygon)
            else MultiPolygon([country.geometry])
        )

        ax.add_geometries(
            geom,
            crs=ccrs.PlateCarree(),
            facecolor=(color),
            label=country.attributes["ISO_A3"],
            edgecolor="#647275",
            linewidth=0.15,
        )

    handles = [mpatches.Rectangle((0, 0), 1, 1, facecolor=c) for c in COLORS_MAP]
    txt = ["0-25%", "25-50%", "50-75%", "75-100%"]
    plt.legend(
        handles,
        txt,
        handlelength=1,
        labelspacing=0.06,
        columnspacing=0.5,
        handletextpad=0.3,
        loc="lower left",
        fancybox=False,
        edgecolor="k",
        fontsize="x-small",
    )
    plt.subplots_adjust(top=1, bottom=0.01, left=0.01, right=0.99)
    plt.savefig(t)


dss = [
    ("./data/countries-under-20.csv", "figures/figure-6c.pdf"),
    ("./data/countries-under-100.csv", "figures/figure-6b.pdf"),
    ("./data/countries-under-250.csv", "figures/figure-6a.pdf"),
]

for f, t in dss:
    map_threshold(load_worldmap_csv(f), t)
