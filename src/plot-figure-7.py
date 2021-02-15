from collections import defaultdict

import matplotlib.pyplot as plt

from boxes import generate_legend_handles, group_boxplot
from commons import WIDTH_IN

with open("data/hops.csv") as f:
    ret = defaultdict(list)
    for l in f.readlines()[1:]:
        split = l.rstrip("\n").split(",")
        # is datacenter?
        if split[-1] == "1":
            continue
        # Hops, ASes
        ret[split[0]].append((int(split[5]), int(split[6])))

grp = [
    (continent, [("Hops", [x[0] for x in xs]), ("ASes", [x[1] for x in xs])])
    for continent, xs in ret.items()
]


fig, ax = plt.subplots(figsize=(WIDTH_IN, 1.2))
ax, positions, props = group_boxplot(grp, ax, showfliers=False)
ax.set_yticks(range(0, 26, 5))
ax.set_ylabel("Path length")
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
plt.subplots_adjust(top=0.99, bottom=0.17, left=0.14, right=0.99)
plt.savefig("figures/figure-7.pdf")
