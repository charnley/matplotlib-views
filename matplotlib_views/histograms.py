
from matplotlib_views import utils



def two_dimensional_hex(
    ax,
    xvalues,
    yvalues,
    density=25, mincount=2, 
        colormap="PuRd", bins="log"

):
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

