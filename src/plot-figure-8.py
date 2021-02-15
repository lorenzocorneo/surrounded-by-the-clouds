from collections import defaultdict

import matplotlib.pyplot as plt

from boxes import generate_legend_handles, group_boxplot
from commons import WIDTH_IN, COLORS

with open("data/hops.csv") as f:
    ds = defaultdict(list)
    for l in f.readlines()[1:]:
        split = l.rstrip("\n").split(",")
        # is datacenter?
        if split[-1] == "1":
            continue
        if int(split[7]) == 0:
            continue
        ds[split[0]].append(int(split[7]) / int(split[5]) * 100)


fig, ax = plt.subplots(figsize=(WIDTH_IN, 1.2))
ds = sorted([(k, vs) for k, vs in ds.items()], key=lambda x: x[0])
bp = ax.boxplot(
    [d[1] for d in ds],
    positions=range(len(ds)),
    patch_artist=True,
    showfliers=False,
)
for i in range(len(ds)):
    plt.setp(bp["boxes"][i], color="k", facecolor=COLORS[0])
    plt.setp(bp["medians"][i], color="#fbe17b")

ax.set_xticklabels([l for l, _ in ds])
ax.set_ylabel("Pervasiveness [%]")
ax.set_yticks(range(0, 101, 25))
plt.grid(axis="y")
plt.subplots_adjust(top=0.99, bottom=0.17, left=0.17, right=0.99)
plt.savefig("figures/figure-8.pdf")
