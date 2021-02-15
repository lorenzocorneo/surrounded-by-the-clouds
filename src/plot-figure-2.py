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

with open("./data/merged-ds-pings.csv", "r") as f:
    ds = defaultdict(list)
    for l in f.readlines():
        line = l.rstrip("\n").split(",")
        if line[1] == "\\N" or float(line[1]) == 0:
            continue
        ds[line[0]].append(float(line[1]))
ds = {k: min(vs) for k, vs in ds.items()}


projection = ccrs.PlateCarree()
plt.figure(figsize=(4.66, 2))
ax = plt.axes(projection=projection)
ax.add_feature(cartopy.feature.OCEAN, facecolor="#ffffff")
ax.outline_patch.set_edgecolor("k")
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
        if ds[iso_code] < 10:
            color = COLORS_MAP[0]
        elif ds[iso_code] >= 10 and ds[iso_code] < 20:
            color = COLORS_MAP[1]
        elif ds[iso_code] >= 20 and ds[iso_code] < 40:
            color = COLORS_MAP[3]
        elif ds[iso_code] >= 40 and ds[iso_code] < 100:
            color = COLORS_MAP[3]
        elif ds[iso_code] >= 100 and ds[iso_code] < 250:
            color = COLORS_MAP[4]
        else:
            color = COLORS_MAP[5]
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
        linewidth=0.25,
    )

handles = [mpatches.Rectangle((0, 0), 1, 1, facecolor=c) for c in COLORS_MAP]
txt = ["<10ms", "10-20ms", "20-40ms", "40-100ms", "100-250ms", ">250ms"]
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
plt.savefig("figures/figure-2.pdf")
