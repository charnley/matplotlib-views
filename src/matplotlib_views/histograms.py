import numpy as np
from scipy.stats import gaussian_kde

from matplotlib_views import views


def two_dimensional_hexbin(
    ax, xvalues, yvalues, density=25, mincount=1, colormap="PuRd", bins="log"
):
    """Wrapper for MPL hexbin func with sane defaults"""

    # Settings
    lineswidth = 0.0  # white lines
    lineswidth = 0.2  # perfect fit
    lineswidth = 0.3  # fit for pngs
    lineswidth = 0.4  # fit for pngs

    hexbinpar = {
        "gridsize": density,
        "cmap": colormap,
        "linewidths": lineswidth,
        "mincnt": mincount,
        "bins": bins,
    }

    im = ax.hexbin(xvalues, yvalues, **hexbinpar)
    return im


def histogram_1d(ax, xvalues, use_kde=False, include_points=False, fix_border=True):
    """
    :param use_kde: Kernel density estimation
    """

    # mu = 0.0
    # std = stats.truncnorm.fit(data, 3.0, 200.0, floc=0, scale=1.0)
    # std = std[-1]
    # std = np.sqrt(std)/np.sqrt(2)

    min_val = np.min(xvalues)
    max_val = np.max(xvalues)

    # hist, bins = np.histogram(xvalues, density=True, bins=30)

    if use_kde:

        bins = np.linspace(min_val, max_val, 200)
        gaussian_kernel = gaussian_kde(xvalues)
        values = gaussian_kernel(bins)
        ax.plot(bins, values, "k", linewidth=1.0)

        xticks = ax.get_xticks()
        yticks = ax.get_yticks()

        views.border(
            ax,
            bounds=[
                None,
                None,
                (min(xticks[1:-1]), max(xticks[1:-1])),
                (min(yticks[1:-1]), max(yticks[1:-1])),
            ],
        )

    else:

        n, bins, patches = ax.hist(
            xvalues, bins=20, histtype="stepfilled", color="k", density=False
        )

    # xticks = ax.get_xticks()
    # yticks = ax.get_yticks()
    #
    # tick_width = xticks[1] - xticks[0]
    # idx_max, = np.where(xticks < max_val+tick_width)
    # xticks = xticks[idx_max]
    #
    # border(ax,bounds=[None,None,(min(xticks)*1.05, max(xticks)), None])
    views.border(ax)
    #
    # ax.set_xticks(xticks)
    # ax.set_yticks(yticks)

    return
