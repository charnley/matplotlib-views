import string

import numpy as np
from cycler import cycler
from matplotlib import patheffects, rcParams, ticker

from matplotlib_views import formats, utils

# matplotlib.font_manager._rebuild()
# shutil.rmtree(matplotlib.get_cachedir())
# Path(matplotlib.get_cachedir()).rmdir()

# import matplotlib.font_manager as font_manager
# # Add every font at the specified location
# font_dir = ['/Users/darioradecic/Downloads/Merriweather']
# for font in font_manager.findSystemFonts(font_dir):
#     font_manager.fontManager.addfont(font)

default_effects = [patheffects.withStroke(linewidth=4, foreground="w")]

outline = dict(path_effects=default_effects)

from matplotlib.colors import get_named_colors_mapping

from matplotlib_views import formats, utils


class outline:
    def __init__(
        self,
    ):

        self._orig = rcParams.copy()

        rcParams.update(
            {
                "path.effects": [patheffects.withStroke(linewidth=5, foreground="w")],
                "lines.linewidth": 3.0,
                # scatter plot defaults
                "lines.markersize": 10,
            }
        )

    def __enter__(self):
        return self

    def __exit__(self, *args):
        dict.update(rcParams, self._orig)


class ppt:
    def __init__(
        self,
        font="Arial Black",
        font_size=20,
        colors=None,
    ):
        # valid rc parameter (see rcParams.keys() for a list of valid parameters

        # TODO Assert that the font exist

        self._orig = rcParams.copy()
        self._colors = get_named_colors_mapping().copy()

        # Color blind colors
        if colors is None:
            colors = dict()

        colors = {
            **dict(
                b="#377eb8",
                g="#4daf4a",
                p="#984ea3",
                r="#e41a1c",
                y="#ff7f00",
            ),
            **colors,
        }

        # Translate hex
        colors = {key: utils.hex2color(colors[key]) for key in colors.keys()}

        # TODO Set default colors. This does not work for plot(x, y, 'bo')
        get_named_colors_mapping().update(colors)

        rcParams.update(
            {
                "font.family": [font],
                "font.size": font_size,
                "path.effects": [],
                "axes.linewidth": 3,
                "lines.linewidth": 3.0,
                "figure.facecolor": "white",
                "grid.linewidth": 0.0,
                "axes.grid": False,
                "axes.unicode_minus": False,
                "axes.edgecolor": "black",
                "xtick.major.size": 6,
                "xtick.major.width": 3,
                "ytick.major.size": 5,
                "ytick.major.width": 3,
                # scatter plot defaults
                "lines.markersize": 10,
                # Colors
                "axes.prop_cycle": cycler(color=colors.values()),
                # Legend
                "legend.loc": "best",
                "legend.frameon": False,  # if True, draw the legend on a background patch
                "legend.framealpha": 0.0,  # legend patch transparency
                "legend.facecolor": "inherit",  # inherit from axes.facecolor; or color spec
                # 'legend.edgecolor':     0.8,      # background patch boundary color
                "legend.fancybox": False,  # if True, use a rounded box for the
                "legend.shadow": False,  # if True, give background a shadow effect
                "legend.numpoints": 1,  # the number of marker points in the legend line
                "legend.scatterpoints": 1,  # number of scatter points
                "legend.markerscale": 1.5,  # the relative size of legend markers vs. original
                "legend.fontsize": "medium",
                "legend.labelcolor": None,
                "legend.title_fontsize": None,  # None sets to the same as the default axes.
            }
        )

    def __enter__(self):
        return self

    def __exit__(self, *args):
        dict.update(rcParams, self._orig)
        dict.update(get_named_colors_mapping(), self._colors)


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

        if rcParams["text.usetex"]:
            raise RuntimeError("xkcd mode is not compatible with text.usetex = True")

        # Color blind colors
        colors = dict(
            b=utils.hex2color("#377eb8"),
            g=utils.hex2color("#4daf4a"),
            p=utils.hex2color("#984ea3"),
            r=utils.hex2color("#e41a1c"),
            y=utils.hex2color("#ff7f00"),
        )

        rcParams.update(
            {
                "font.family": [
                    "xkcd",
                    "xkcd Script",
                    "Humor Sans",
                    "Comic Neue",
                    "Comic Sans MS",
                ],
                "font.size": font_size,
                "path.sketch": (scale, length, randomness),
                "path.effects": [],
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
                # scatter plot defaults
                "lines.markersize": 10,
                # Colors
                "axes.prop_cycle": cycler(color=colors.values()),
            }
        )

    def __enter__(self):
        return self

    def __exit__(self, *args):
        dict.update(rcParams, self._orig)


def use_teach(func, *args, **kwargs):
    """Decorator to use teach style on plot functions"""

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
        ax.text(
            x,
            y,
            f"{char})",
            horizontalalignment="center",
            verticalalignment="center",
            transform=ax.transAxes,
        )
