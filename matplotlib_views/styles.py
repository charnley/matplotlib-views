
from cycler import cycler
import string

from matplotlib import rcParams, rcParamsDefault, get_backend, rcParamsOrig
from matplotlib import patheffects, ticker

from matplotlib_views import utils, formats

import numpy as np


outline = dict(
    path_effects = [patheffects.withStroke(linewidth=4, foreground="w")],
)


class ppt:

    pass


class teach:
    # This cannot be implemented in terms of rc_context() because this needs to
    # work as a non-contextmanager too.

    # marker_size = 100
    # label_size = 30

    def __init__(
        self,
        scale=1,
        length=100,
        randomness=2,
        font_size=30,
    ):

        self._orig = rcParams.copy()

        if rcParams['text.usetex']:
            raise RuntimeError("xkcd mode is not compatible with text.usetex = True")

        # Color blind colors
        colors = dict(
            b = utils.hex2color('#377eb8'),
            g = utils.hex2color('#4daf4a'),
            p = utils.hex2color('#984ea3'),
            r = utils.hex2color('#e41a1c'),
            y = utils.hex2color('#ff7f00'),
        )

        rcParams.update({
            'font.family': ['xkcd', 'xkcd Script', 'Humor Sans', 'Comic Neue', 'Comic Sans MS'],
            'font.size': font_size,
            'path.sketch': (scale, length, randomness),
            'path.effects': [],
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

            # scatter plot defaults
            'lines.markersize': 10,

            # Colors
            'axes.prop_cycle': cycler(color=colors.values())
        })

    def __enter__(self):
        return self

    def __exit__(self, *args):
        dict.update(rcParams, self._orig)


def use_teach(func, *args, **kwargs):
    """ Decorator to use teach style on plot functions """
    def wrapper(*args, **kwargs):
        with teach():
            return func(*args, **kwargs)
    return wrapper


def simple_axes(axs):

    for ax in axs:
        utils.fix_borders(ax)
        ax.yaxis.set_major_formatter(ticker.FuncFormatter(formats.formatter_off))
        ax.xaxis.set_major_formatter(ticker.FuncFormatter(formats.formatter_off))

    return

def simple_ticks(axis):
    mi = min(axis)
    ma = max(axis)
    ticks = [mi, np.mean([mi, ma]), ma]
    return ticks


def name_axes(axs, loc=None):

    x = 0.9
    y = 0.9

    if loc and "right" in loc:
        x = 0.1

    if loc and "bottom" in loc:
        y = 0.1


    alphabet = string.ascii_lowercase

    for i, ax in enumerate(axs):
        char = alphabet[i].upper()
        ax.text(x, y, f'{char})', horizontalalignment='center', verticalalignment='center', transform=ax.transAxes)

