from itertools import cycle

import matplotlib.patches as mpatches
import matplotlib.pyplot as plt
import numpy as np
from toolz.itertoolz import unique
from commons import COLORS, HATCHES
from lcplot import dataviz as dv

COLORS_IT = cycle(COLORS)

# Format: [(group_label, [(label, [xs])])]
def generate_props(ds):
    ret = {}
    labels = sorted(list(unique([y for _, x in ds for y, _ in x])))
    for i, l in enumerate(labels):
        style = i / len(COLORS)
        color = next(COLORS_IT)
        if style < 1:
            ret[l] = {"edgecolor": "k", "facecolor": color}
        elif style >= 1 and style < 2:
            ret[l] = {
                "edgecolor": color,
                "facecolor": "w",
                "hatch": HATCHES[i % len(HATCHES)],
            }
        else:
            ret[l] = {
                "edgecolor": "k",
                "facecolor": color,
                "hatch": HATCHES[i % len(HATCHES)],
            }

    return ret


def generate_positions(ds, width, interspacing=2, intraspacing=0.1):
    ret = {}
    max_item_length = max([len(xs) for xs in ds])
    for i, d in enumerate(ds):
        group, items = d
        # Center group
        offset = (
            0
            if max_item_length == len(items)
            else (max_item_length - len(items)) * width
        )
        ret[group] = [
            i * interspacing + j * width + j * intraspacing + offset
            for j in range(len(items))
        ]
    return ret


def get_box_width(ds, addition=0):
    return 1 / (max([len(xs) for xs in ds]) + addition)


# bp: boxplot object, ds: dataset, ps: style properties
def set_box_colors(bp, items, ps):
    for i, (label, _) in enumerate(items):
        c = next(COLORS_IT)
        plt.setp(bp["boxes"][i], **ps[label])
        plt.setp(bp["medians"][i], color="#fbe17b")


def generate_legend_handles(props):
    return [mpatches.Patch(label=label, **ps) for label, ps in props.items()]


def group_boxplot(ds, ax, showfliers=True, addition=0):
    props = generate_props(ds)
    width = get_box_width(ds, addition)
    pos = generate_positions(ds, width)

    for group, items in ds:
        items = sorted(items, key=lambda x: x[0])
        labels = [label for label, _ in items]
        bp = ax.boxplot(
            [xs for _, xs in items],
            positions=pos[group],
            widths=width,
            patch_artist=True,
            notch=False,
            showfliers=showfliers,
        )
        set_box_colors(bp, items, props)

    ax.set_xticks([p[0] + (p[-1] - p[0]) / 2 for _, p in pos.items()])
    ax.set_xticklabels([group for group, _ in ds])
    return ax, pos, props
