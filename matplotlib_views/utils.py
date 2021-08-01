import matplotlib
from matplotlib import patheffects
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt


def get_plot(n_ax=1, sharey=True, sharex=True):
    """ Get a jupyter-sized plot """
    size=12
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
    matplotlib.rcParams['axes.linewidth'] = 2
    matplotlib.rcParams['xtick.major.width'] = 2
    matplotlib.rcParams['ytick.major.width'] = 2

    return


def teach_style(font_size=18):

    scale = 1
    length = 100
    randomness = 2

    rcParams.update({
        'font.family': ['xkcd', 'xkcd Script', 'Humor Sans', 'Comic Neue', 'Comic Sans MS'],
        'font.size': 14.0,
        'path.sketch': (scale, length, randomness),
        'path.effects': [patheffects.withStroke(linewidth=4, foreground="w")],
        'axes.linewidth': 1.5,
        'lines.linewidth': 2.0,
        'figure.facecolor': 'white',
        'grid.linewidth': 0.0,
        'axes.grid': False,
        'axes.unicode_minus': False,
        'axes.edgecolor': 'black',
        'xtick.major.size': 8,
        'xtick.major.width': 3,
        'ytick.major.size': 8,
        'ytick.major.width': 3,
    })



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

    min_x = np.min(xticks)
    max_x = np.max(xticks)

    min_y = np.min(yticks)
    max_y = np.max(yticks)

    # TODO Better ax.set_xlim()

    for direction, visible in zip(directions, visibles):

        spine = spines[direction]
        spine.set_visible(visible)

        if not visible:
            continue

        if not fix_bounds:
            continue

        if direction == "left" or direction == "right":
            spine.set_bounds(min_y, max_y)

        else:
            spine.set_bounds(min_x, max_x)

