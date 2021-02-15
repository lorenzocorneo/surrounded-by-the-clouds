from collections import defaultdict

import matplotlib.pyplot as plt
import numpy as np

from commons import COLORS
from continents import get_continent

ds = defaultdict(list)
with open("data/pings.csv") as f:
    for l in f.readlines():
        line = l.rstrip("\n").split(",")
        if len(line) == 1:
            continue
        if line[1] == None or line[1] == "\\N":
            continue
        continent = get_continent(line[0])
        if not continent or continent and continent == "AN":
            continue
        value = float(line[1])
        if value > 400:
            continue
        ds[continent].append(value)

ds = sorted(ds.items(), key=lambda x: x[0])

fig, ax = plt.subplots(figsize=(3.37, 1.7))
[
    ax.plot(
        sorted(d[1]),
        np.array(np.arange(len(d[1])) / float(len(d[1]))),
        label=d[0],
        color=COLORS[i],
    )
    for i, d in enumerate(ds)
]

ax.set_xlabel("RTT [ms]")
ax.set_ylabel("CDF")
ax.set_xticks(range(0, 401, 50))
ax.legend(
    labelspacing=0.06,
    columnspacing=0.5,
    handletextpad=0.3,
    ncol=2,
    fontsize="small",
    loc="best",
)
plt.subplots_adjust(top=0.98, bottom=0.24, left=0.15, right=0.99)
plt.savefig("figures/figure-4.pdf")
