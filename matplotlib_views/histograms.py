
from matplotlib_views import utils



def two_dimensional_hex(
    ax,
    xvalues,
    yvalues,
    density=25, mincount=2, 
        colormap="PuRd", bins="log"

):
    """ Wrapper for MPL hexbin func with sane defaults 


    add colorbar:
    https://stackoverflow.com/questions/40833295/matplotlib-hexbin-add-colour-bar-for-dummies
    """

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

    im = ax.hexbin(xvalues, yvalues, **hexbinpar)
    return im

