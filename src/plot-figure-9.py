from collections import defaultdict

import matplotlib.pyplot as plt

from boxes import generate_legend_handles, group_boxplot
from commons import PROVIDERS, short_cloud

ds = {}
for c in PROVIDERS:
    ds[c] = defaultdict(list)

with open("data/hops.csv") as f:
    for l in f.readlines()[1:]:
        split = l.rstrip("\n").split(",")
        if split[7] == "0":
            continue
        ds[short_cloud(split[2])][split[0]].append(int(split[7]) / int(split[5]) * 100)

ds = [
    (group, sorted([(label, xs) for label, xs in ys.items()], key=lambda x: x[0]))
    for group, ys in ds.items()
]


fig, ax = plt.subplots(figsize=(7, 1.7))
ax, positions, props = group_boxplot(ds, ax, showfliers=False, addition=3)
ax.set_ylabel("Pervasiveness [%]")
ax.set_ylim([0, 125])
ax.set_yticks(range(0, 101, 20))
ax.set_yticklabels([str(x) for x in range(0, 101, 20)])
xspan = 2
[
    ax.axvspan(i * xspan + 1.1, i * xspan + xspan + 0.9, facecolor="k", alpha=0.2)
    for i in range(len(ds) - 1)
    if i % 2 == 0
]

ax.legend(
    handles=generate_legend_handles(props),
    handlelength=1,
    labelspacing=0.06,
    columnspacing=0.5,
    handletextpad=0.3,
    ncol=6,
    fontsize="small",
    loc="upper right",
    fancybox=False,
    edgecolor="k",
)

plt.grid(axis="y")
plt.subplots_adjust(top=0.98, bottom=0.12, left=0.1, right=0.99)
plt.savefig("figures/figure-9.pdf")
