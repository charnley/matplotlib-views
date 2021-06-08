#!/usr/bin/env python

import numpy as np
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.rc as rc


FONTNAME = "Fira Sans"
FONTWEIGHT = "bold"
DEFAULT_FONT = {
    "fontweight": fontweight,
    "fontname": fontname
}


def save(filename, fig=plt):
    fig.savefig(filename, bbox_inches="tight")
    fig.savefig(filename + ".pdf", bbox_inches="tight")
    fig.clf()
    return


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


def hexbin(ax,
    density=25,
    mincount=2,
    bins='log'):
    """

    wrapper for hexbin with sane defaults

    """

    # Settings
    lineswidth=0.0 # white lines
    lineswidth=0.2 # perfect fit
    lineswidth=0.3 # fit for pngs
    lineswidth=0.4 # fit for pngs

    colormap = 'Greys'
    colormap = 'PuRd'

    # move to parameter
    hex_density = 25

    hexbinpar = {
        'gridsize': hex_density,
        'cmap': colormap,
        'linewidths': lineswidth,
        'mincnt': 2,
        'bins': 'log',
    }

    return



## ACTUAL VIEWS


def histogram_2d_with_kde(
	xvalues, yvalues,
	xlabel=None,
	ylabel=None,
	debug=False,
    fontargs=DEFAULT_FONT):
	"""
    """

    color_std = "#d81b6a"
    color_hl = "#800031"

    # TODO Move font to somewhere else
    # plt.rc('text', usetex=True)
    # plt.rc('font', family='serif')
    # plt.rc('font', size=18)
    # plt.rc('font', size=14)
    # fontname = "Fira Sans"
    # fontweight = "bold"
    # plt.rc('legend', fontsize=15)
    # mpl.rcParams['font.sans-serif'] = fontname
    # mpl.rcParams['font.family'] = "sans-serif"
    # mpl.rcParams['font.weight'] = fontweight


    nullfmt = NullFormatter()

    left, width = 0.1, 0.65
    bottom, height = 0.1, 0.65
    bottom_h = left_h = left + width + 0.02

    rect_scatter = [left, bottom, width, height]
    rect_histx = [left, bottom_h, width, 0.1]
    rect_histy = [left_h, bottom, 0.1, height]

    plt.figure(1, figsize=(8, 8))

    ax_scatter = plt.axes(rect_scatter)
    ax_histx = plt.axes(rect_histx)
    ax_histy = plt.axes(rect_histy)


    # scatter plot
    # ax_scatter.scatter(xvalues, yvalues, color="k", alpha=0.4)

    # TODO move hexbin ax function somewhere else
    # Hack to make MPL hide the overlap of hexacons
    lineswidth=0.0 # white lines
    lineswidth=0.2 # perfect fit
    lineswidth=0.3 # fit for pngs
    lineswidth=0.4 # fit for pngs

    colormap = 'Greys'
    colormap = 'PuRd'

    hex_density = 25

    hexbinpar = {
        'gridsize': hex_density,
        'cmap': colormap,
        'linewidths': lineswidth,
        'mincnt': 2,
        'bins': 'log',
    }

    hb = ax_scatter.hexbin(xvalues, yvalues, **hexbinpar)

    # define binwidth
    x_max = np.max(xvalues)
    x_min = np.min(xvalues)
    x_binwidth = (abs(x_min) + x_max) / 30.0
    x_binwidth = int(x_binwidth)
    x_binwidth = 1.0
    x_bins = np.arange(x_min, x_max+x_binwidth, x_binwidth)

    y_max = np.max(yvalues)
    y_min = np.min(yvalues)
    y_binwidth = (abs(y_min) + y_max) / 50.0
    y_binwidth = int(y_binwidth)
    y_bins = np.arange(y_min, y_max+y_binwidth, y_binwidth)


    # scatter keys
    xkeys = np.arange(10, x_max+x_binwidth*2, 10)
    xkeys = [1] + list(xkeys)
    ykeys = np.arange(0, y_max+y_binwidth, 100)

    # filter ykeys
    n_keys = len(ykeys)
    if n_keys > 12:
        ykeys = np.arange(0, y_max+y_binwidth, 150)

    # Set limits and ticks of scatter
    # TODO More space to x-axis
    xkeys_min = min(xkeys)
    xkeys_max = max(xkeys)
    diff = xkeys[2]-xkeys[1]
    xlim = (xkeys_min-0.8*diff, xkeys_max+0.8*diff)
    ylim = (0-y_binwidth*5, y_max+y_binwidth*2)
    ax_scatter.set_xlim(xlim)
    ax_scatter.set_ylim(ylim)


    # Histogram

    if True:
        bins = np.linspace(min(xkeys), max(xkeys), 300)
        gaussian_kernel = gaussian_kde(xvalues)
        values = gaussian_kernel(bins)
        ax_histx.plot(bins, values, "k", linewidth=1.0)

        bins = np.linspace(min(ykeys), max(ykeys), 300)
        gaussian_kernel = gaussian_kde(yvalues)
        values = gaussian_kernel(bins)
        ax_histy.plot(values, bins, "k", linewidth=1.0)

    else:
        ax_histx.hist(xvalues, bins=x_bins, histtype='step', color="k")
        ax_histy.hist(yvalues, bins=y_bins, orientation='horizontal', histtype='step', color="k")

    ax_histx.set_xlim(ax_scatter.get_xlim())
    ax_histy.set_ylim(ax_scatter.get_ylim())

    # pretty
    if not debug:
        ax_histx.xaxis.set_major_formatter(nullfmt)
        ax_histy.yaxis.set_major_formatter(nullfmt)

        set_border(ax_scatter, xkeys, ykeys)
        set_border(ax_histx, [], [], border=[False, False, False, False])
        set_border(ax_histy, [], [], border=[False, False, False, False])

        ax_histx.set_xticks([], [])
        ax_histy.set_yticks([], [])


    ax_scatter.set_xlabel(xlabel, **fontargs)
    ax_scatter.set_ylabel(ylabel, **fontargs)

    plt.savefig(filename, bbox_inches="tight")
    plt.savefig(filename + ".pdf", bbox_inches="tight")

    plt.clf()

    return
