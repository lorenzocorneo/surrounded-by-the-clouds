import matplotlib.pyplot as plt
import numpy as np
from funcy import flatten

from commons import COLORS

LINES = ["-", "--", "-."]

stat_areas = []
with open("data/us-psa.csv", "r") as f:

    def parse_line(line):
        line = line.rstrip("\n").split(";")
        return (line[0], int(line[1]), [float(x) for x in line[2].split(",")])

    psas = [parse_line(x) for x in f.readlines()]

ds = {}
ds["US-PSA-MIN"] = list(flatten([[min(l)] * (p // 1000) for _, p, l in psas]))
ds["US-PSA-MEDIAN"] = list(flatten([[np.median(l)] * (p // 1000) for _, p, l in psas]))
ds["US-PSA-95"] = list(
    flatten([[np.percentile(l, 95)] * (p // 1000) for _, p, l in psas])
)


fig, ax = plt.subplots(figsize=(3.37, 1.7))
[
    ax.plot(
        sorted(d),
        np.array(np.arange(len(d)) / float(len(d))),
        color=COLORS[i],
        label=l,
        linestyle=LINES[i],
    )
    for i, (l, d) in enumerate(
        [
            ("US-PSA-Min", ds["US-PSA-MIN"]),
            ("US-PSA-Median", ds["US-PSA-MEDIAN"]),
            ("US-PSA-95th", ds["US-PSA-95"]),
        ]
    )
]

ax.set_xlabel("RTT [ms]")
ax.set_ylabel("CDF")
ax.set_xticks(range(0, 251, 25))
ax.legend(
    labelspacing=0.06,
    columnspacing=0.5,
    handletextpad=0.3,
    ncol=1,
    fontsize="small",
    loc="best",
)
plt.subplots_adjust(top=0.98, bottom=0.24, left=0.15, right=0.99)
plt.savefig("figures/figure-10.pdf")
