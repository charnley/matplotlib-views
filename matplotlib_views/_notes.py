import matplotlib

font_size = 20

font = {"weight": "bold", "size": font_size}

matplotlib.rc("font", **font)
matplotlib.rc("axes", labelweight="bold")


def get_plot(n_ax=1):
    """ Get a jupyter-sized plot """
    fig, axs = plt.subplots(1, n_ax, sharey=True, sharex=True, figsize=(12, n_ax * 12))
    return fig, axs


def view_cluster(ax, values, cluster_indices, outliers=None, markersize=6):
    """ View clusters of points """

    n_clusters = len(cluster_indices)
    colors = [plt.cm.Spectral(each) for each in np.linspace(0, 1, n_clusters)]
    # colors = [plt.cm.rainbow(each) for each in np.linspace(0, 1, n_clusters)]

    for idxs, color in zip(cluster_indices, colors):

        marker_options = {
            "markerfacecolor": tuple(color),
            "markeredgecolor": "k",
            "markersize": markersize,
        }

        x = values[0, idxs]
        y = values[1, idxs]
        ax.plot(x, y, "o", **marker_options)

    if outliers is not None:

        outlier_color = [1, 1, 1, 1]
        marker_options = {
            "markerfacecolor": tuple(outlier_color),
            "markeredgecolor": "k",
            "markersize": markersize,
        }

        x = values[0, outliers]
        y = values[1, outliers]
        ax.plot(x, y, "o", **marker_options)


def hexbin(ax, xvalues, yvalues, density=25, mincount=2, colormap="PuRd", bins="log"):  # 'Greys'
    """ Wrapper for MPL hexbin func with sane defaults """

    # Settings
    lineswidth = 0.0  # white lines
    lineswidth = 0.2  # perfect fit
    lineswidth = 0.3  # fit for pngs
    lineswidth = 0.4  # fit for pngs

    hexbinpar = {
        "gridsize": density,
        "cmap": colormap,
        "linewidths": lineswidth,
        "mincnt": 1,
        "bins": bins,
    }

    _ = ax.hexbin(xvalues, yvalues, **hexbinpar)

    return


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
    (x_idxs,) = np.where((xticks > min_x) & (xticks < max_x))
    (y_idxs,) = np.where((yticks > min_y) & (yticks < max_y))
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



# fig, axs = get_plot(n_ax=1)
# axs.plot(*desc_omega, "k.")
# axs.set_xlabel("SASA")
# axs.set_ylabel("Dipole")
# axs.set_title("Shapes of Omega conformers")
# fix_borders(axs)



# fig, ax = get_plot(n_ax=1)
# hexbin(ax, *desc_omega)
# ax.scatter(*desc_omega[:, selection], edgecolors="w", c="black", s=70)
# # ax.scatter(*shapes_pipe, edgecolors="w", c="black", s=70, alpha=1.0)
# ax.set_xlabel("SASA")
# ax.set_ylabel("Dipole")
# fix_borders(ax)

#
# import matplotlib.patheffects as PathEffects
# import numpy as np
# import pandas as pd
# from matplotlib import pyplot as plt
# from rdkit import Chem
