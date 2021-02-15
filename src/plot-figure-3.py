import matplotlib.pyplot as plt
import numpy as np
from funcy import group_by

from commons import COLORS
from continents import get_continent

with open("data/min-ping.csv", "r") as f:

    def parse_line(line):
        line = line.rstrip("\n").split(",")
        return (int(line[0]), line[3], float(line[2]))

    ds = [parse_line(x) for x in f.readlines()]

ds = group_by(lambda x: x[0], [(d[1], d[2]) for d in ds])
ds = {k: [v[1] for v in vs] for k, vs in ds.items()}
ds = sorted([(k, vs) for k, vs in ds.items()], key=lambda x: x[0])


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
ax.set_xlim([-5, 305])
ax.legend(
    labelspacing=0.06,
    columnspacing=0.5,
    handletextpad=0.3,
    ncol=2,
    fontsize="small",
    loc="best",
)
plt.subplots_adjust(top=0.98, bottom=0.24, left=0.15, right=0.99)
plt.savefig("figures/figure-3.pdf")
