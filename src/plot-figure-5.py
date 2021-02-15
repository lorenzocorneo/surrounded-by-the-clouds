from collections import defaultdict

import matplotlib.pyplot as plt

from boxes import generate_legend_handles, group_boxplot
from commons import PROVIDERS, short_cloud
from continents import get_continent

ds = {}
for p in PROVIDERS:
    ds[p] = defaultdict(list)
with open("data/pings-closest-dcs.csv") as f:
    for l in f.readlines():
        line = l.rstrip("\n").split(",")
        if len(line) == 1:
            continue
        if line[3] == None or line[3] == "\\N":
            continue
        continent = get_continent(line[1])
        cloud = short_cloud(line[2])
        if not continent or continent and continent == "AN":
            continue
        if float(line[3]) > 400:
            continue
        ds[cloud][continent].append(float(line[3]))

# Not enough samples here
del ds["LIN"]["AF"]


ds = [(group, [(label, xs) for label, xs in ys.items()]) for group, ys in ds.items()]
fig, ax = plt.subplots(figsize=(7, 1.7))
ax, positions, props = group_boxplot(ds, ax, showfliers=False, addition=3)
xspan = 2
[
    ax.axvspan(i * xspan + 0.9, i * xspan + xspan + 0.9, facecolor="k", alpha=0.2)
    for i in range(len(ds) - 1)
    if i % 2 == 0
]
ax.set_ylabel("RTT [ms]")
ax.set_ylim([0, 500])
ax.legend(
    handles=generate_legend_handles(props),
    handlelength=1,
    labelspacing=0.06,
    columnspacing=0.5,
    handletextpad=0.3,
    ncol=6,
    fontsize="small",
    loc="best",
)

plt.grid(axis="y")
plt.subplots_adjust(top=0.98, bottom=0.12, left=0.1, right=0.99)
plt.savefig("figures/figure-5.pdf")
