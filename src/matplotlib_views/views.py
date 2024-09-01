#!/usr/bin/env python

import matplotlib as mpl
import matplotlib.pyplot as plt

FONTNAME = "Fira Sans"
FONTWEIGHT = "bold"
DEFAULT_FONT = {"fontweight": FONTWEIGHT, "fontname": FONTNAME}


COLOR_STANDARD = "#d81b6a"
COLOR_HIGHLIGHT = "#800031"

# Text
# import numpy as np
# import matplotlib.pyplot as plt
# import matplotlib.patheffects as PathEffects
# plt.imshow(np.zeros((5,5), cmap=plt.gray())
# txt = plt.text(2,2,'This is a test', size=11, color='black')
# txt.set_path_effects([PathEffects.withStroke(linewidth=5, foreground='w')])
# plt.draw()


def save(filename, fig=plt, clf=False):
    fig.savefig(filename, bbox_inches="tight")
    fig.savefig(filename + ".pdf", bbox_inches="tight")
    fig.savefig(filename + ".svg", bbox_inches="tight")

    if clf:
        fig.clf()


def get_spines(ax):
    """

    return the spines in the order of Cascading-style sheets for the ax

    - Top
    - Right
    - Bottom
    - Left

    """

    spines = ax.spines.items()
    rtn_spines = [0, 1, 2, 3]

    for direction, spine in spines:

        if direction == "top":
            rtn_spines[0] = spine

        if direction == "right":
            rtn_spines[1] = spine

        if direction == "bottom":
            rtn_spines[2] = spine

        if direction == "left":
            rtn_spines[3] = spine

    return rtn_spines


def border(ax, visibles=[False, False, True, True], bounds=[None, None, None, None]):
    """

    quick wrapper to change the borders

    # spines = ax.spines.items()
    # spine.set_bounds(min(xkeys), max(xkeys))

    """

    spines = get_spines(ax)

    for spine, visible, bound in zip(spines, visibles, bounds):
        spine.set_visible(visible)

        if bound is not None:
            spine.set_bounds(min(bound), max(bound))

    return


def set_font():

    plt.rc("text", usetex=True)
    plt.rc("font", family="serif")
    plt.rc("font", size=18)
    plt.rc("font", size=14)
    fontname = "Fira Sans"
    fontweight = "bold"
    plt.rc("legend", fontsize=15)
    mpl.rcParams["font.sans-serif"] = fontname
    mpl.rcParams["font.family"] = "sans-serif"
    mpl.rcParams["font.weight"] = fontweight

    return
