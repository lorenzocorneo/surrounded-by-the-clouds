from collections import defaultdict

import matplotlib.pyplot as plt
import numpy as np

from commons import COLORS, LINES

ds = defaultdict(list)
with open("data/merged-ds-pings.csv") as f:
    for l in f.readlines():
        line = l.rstrip("\n").split(",")
        if len(line) == 1:
            continue
        if line[1] == None or line[1] == "\\N":
            continue
        if line[0] not in ["KR", "JP", "CN", "IR", "SG", "IN", "PK"]:
            continue
        ds[line[0]].append(float(line[1]))
ds = {k: [v for v in vs if v < 400] for k, vs in ds.items()}


fig, ax = plt.subplots(figsize=(3.37, 1.7))
[
    ax.plot(
        sorted(d[1]),
        np.array(np.arange(len(d[1])) / float(len(d[1]))),
        label=d[0],
        color=COLORS[i],
    )
    for i, d in enumerate(ds.items())
]

ax.set_xlabel("RTT [ms]")
ax.set_ylabel("CDF")
ax.legend(
    #    handlelength=1,
    labelspacing=0.06,
    columnspacing=0.5,
    handletextpad=0.3,
    ncol=2,
    fontsize="small",
    loc="best",
)

plt.subplots_adjust(top=0.98, bottom=0.24, left=0.15, right=0.99)
plt.savefig("figures/figure-11.pdf")
