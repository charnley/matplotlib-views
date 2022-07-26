import re

import matplotlib
import matplotlib as mpl
import numpy as np
from matplotlib import patheffects
from matplotlib import pyplot as plt


def get_plot(n_ax=1, sharey=True, sharex=True, size=12):
    """ Get a jupyter-sized plot """
    fig, axs = plt.subplots(1, n_ax, sharey=sharey, sharex=sharex, figsize=(n_ax * size, size))
    return fig, axs


def set_global_style(font_size=18):
    """

    font_size : 20 powerpoint presentation

    """

    font = {"weight": "bold", "size": font_size}

    matplotlib.rc("font", **font)
    matplotlib.rc("axes", labelweight="bold")

    # Thicker spines
    matplotlib.rcParams["axes.linewidth"] = 2
    matplotlib.rcParams["xtick.major.width"] = 2
    matplotlib.rcParams["ytick.major.width"] = 2

    return


def set_global_style_tex(font_size=15):
    """

    font_size : 20 powerpoint presentation

    """

    font = {"weight": "bold", "size": font_size}

    matplotlib.rc("font", **font)
    matplotlib.rc("axes", labelweight="bold")

    # Thicker spines
    matplotlib.rcParams["axes.linewidth"] = 2
    matplotlib.rcParams["xtick.major.width"] = 2
    matplotlib.rcParams["ytick.major.width"] = 2

    return


def set_colorblind_colors():

    mpl.colors.ColorConverter.colors["r"] = hex2color("#e41a1c")
    mpl.colors.ColorConverter.colors["b"] = hex2color("#377eb8")
    mpl.colors.ColorConverter.colors["g"] = hex2color("#4daf4a")
    mpl.colors.ColorConverter.colors["p"] = hex2color("#984ea3")
    mpl.colors.ColorConverter.colors["y"] = hex2color("#ff7f00")


def hex2color(s):
    """
    Function from MPL lib.

    Take a hex string *s* and return the corresponding rgb 3-tuple
    Example: #efefef -> (0.93725, 0.93725, 0.93725)
    """
    hexColorPattern = re.compile(r"\A#[a-fA-F0-9]{6}\Z")
    # if not isinstance(s, basestring):
    #     raise TypeError('hex2color requires a string argument')
    if hexColorPattern.match(s) is None:
        raise ValueError('invalid hex color string "%s"' % s)
    return tuple([int(n, 16) / 255.0 for n in (s[1:3], s[3:5], s[5:7])])


def teach_style(font_size=14):

    # matplotlib.rc_context(rc=None, fname=None)
    # Return a context manager for temporarily changing rcParams

    scale = 1
    length = 100
    randomness = 2

    matplotlib.rcParams.update(
        {
            "font.family": ["xkcd", "xkcd Script", "Humor Sans", "Comic Neue", "Comic Sans MS"],
            "font.size": font_size,
            "path.sketch": (scale, length, randomness),
            "path.effects": [patheffects.withStroke(linewidth=4, foreground="w")],
            "axes.linewidth": 1.5,
            "lines.linewidth": 2.0,
            "figure.facecolor": "white",
            "grid.linewidth": 0.0,
            "axes.grid": False,
            "axes.unicode_minus": False,
            "axes.edgecolor": "black",
            "xtick.major.size": 8,
            "xtick.major.width": 3,
            "ytick.major.size": 8,
            "ytick.major.width": 3,
        }
    )


def get_tick_limits(ax):

    xticks = ax.get_xticks()
    yticks = ax.get_yticks()
    min_x, max_x = ax.get_xlim()
    min_y, max_y = ax.get_ylim()

    # Correct to the actual ticks
    (x_idxs,) = np.where((xticks > min_x) & (xticks < max_x))
    (y_idxs,) = np.where((yticks > min_y) & (yticks < max_y))
    xticks = xticks[x_idxs]
    yticks = yticks[y_idxs]

    min_x = np.min(xticks)
    max_x = np.max(xticks)

    min_y = np.min(yticks)
    max_y = np.max(yticks)

    return min_x, max_x, min_y, max_y


def fix_borders(ax, visibles=[False, False, True, True], fix_bounds=True):
    """ Make border pretty """

    directions = ["top", "right", "bottom", "left"]

    spines = ax.spines.items()
    spines = dict(spines)

    xticks = ax.get_xticks()
    yticks = ax.get_yticks()
    min_x, max_x = ax.get_xlim()
    min_y, max_y = ax.get_ylim()

    # Correct to the actual ticks
    (x_idxs,) = np.where((xticks >= min_x) & (xticks <= max_x))
    (y_idxs,) = np.where((yticks >= min_y) & (yticks <= max_y))
    xticks = xticks[x_idxs]
    yticks = yticks[y_idxs]

    xticks = list(xticks)
    yticks = list(yticks)

    if xticks:
        min_x = np.min(xticks)
        max_x = np.max(xticks)

    if yticks:
        min_y = np.min(yticks)
        max_y = np.max(yticks)

    # TODO Better ax.set_xlim()

    for direction, visible in zip(directions, visibles):

        spine = spines[direction]
        spine.set_visible(visible)

        if not visible and direction == "left":
            ax.yaxis.set_visible(False)

        if not visible:
            continue

        if not fix_bounds:
            continue

        if direction == "left" or direction == "right":
            if yticks:
                spine.set_bounds(min_y, max_y)

        else:
            if xticks:
                spine.set_bounds(min_x, max_x)
