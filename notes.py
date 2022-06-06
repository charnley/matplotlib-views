
import numpy as np
import re

import matplotlib as mpl
import matplotlib.pyplot as plt

from matplotlib import ticker

def formatter_int(x, pos):
    return "%i" % x

def formatter_float(x, pos):
    return "%4.2f" % x

def formatter_off(x, pos):
    return ""

def formatter_notrail(x, pos):
    """
    remove trailing zeros
    """

    if x.is_integer():
        return formatter_int(x, pos)
    else:
        return '{0:g}'.format(x)

    return


def hex2color(s):
    """
    Function from MPL lib.

    Take a hex string *s* and return the corresponding rgb 3-tuple
    Example: #efefef -> (0.93725, 0.93725, 0.93725)
    """
    hexColorPattern = re.compile("\A#[a-fA-F0-9]{6}\Z")
    # if not isinstance(s, basestring):
    #     raise TypeError('hex2color requires a string argument')
    if hexColorPattern.match(s) is None:
        raise ValueError('invalid hex color string "%s"' % s)
    return tuple([int(n, 16)/255.0 for n in (s[1:3], s[3:5], s[5:7])])


def set_global_font(font="Fira Sans", fontsize=14):
    """
    """

    plt.rc('legend', fontsize=fontsize)
    mpl.rcParams['font.sans-serif'] = font
    mpl.rcParams['font.family'] = "sans-serif"
    mpl.rcParams['font.weight'] = "medium" # font.weight         : medium


    mpl.rcParams.update({'figure.autolayout': True})

    return


def set_custom_color():

    from cycler import cycler
    mpl.colors.ColorConverter.colors['r'] = hex2color('#e41a1c')
    mpl.colors.ColorConverter.colors['b'] = hex2color('#377eb8')
    mpl.colors.ColorConverter.colors['g'] = hex2color('#4daf4a')
    mpl.colors.ColorConverter.colors['p'] = hex2color('#984ea3')
    mpl.colors.ColorConverter.colors['y'] = hex2color('#ff7f00')

    return


def set_custom_lines():

    plt.rc('lines', antialiased=True) # render lines in antialised (no jaggies)
    plt.rc('xtick.major', size=6)      # major tick size in points
    plt.rc('xtick.minor', size=6)      # minor tick size in points
    plt.rc('xtick.major', pad=6)       # distance to major tick label in points
    plt.rc('xtick.minor', pad=6)       # distance to the minor tick label in points
    # plt.rc('xtick', color='111111')    # color of the tick labels
    # plt.rc('xtick', direction='out')    # direction: in or out
    #
    plt.rc('ytick.major', size=6)      # major tick size in points
    plt.rc('ytick.minor', size=6)      # minor tick size in points
    plt.rc('ytick.major', pad=6)       # distance to major tick label in points
    plt.rc('ytick.minor', pad=6)       # distance to the minor tick label in points
    # plt.rc('ytick', color='111111')    # color of the tick labels
    # plt.rc('ytick', direction='in')    # direction: in or out

    return


def plot_learning_curve(ax, xkeys, ykeys,
                        border=[True, False, True, False],
                        loglog=True,
                        show_legend=True):
    """

    """

    if loglog:
        ax.set_xscale('log')
        ax.set_yscale('log')

    if show_legend:
        leg = ax.legend(loc="best", borderaxespad=0., framealpha=1.0, fancybox=False, borderpad=1)
        leg.get_frame().set_linewidth(0.0)
        leg.get_frame().set_facecolor('#ffffff')

    ax.yaxis.grid(True, zorder=0)

    if border:
        # I like the css standard
        spines = ax.spines.items()
        for direction, spine in spines:
            if direction == "top": spine.set_visible(border[0])
            if direction == "right": spine.set_visible(border[1])
            if direction == "bottom": spine.set_visible(border[2])
            if direction == "left": spine.set_visible(border[3])


        # spines[0].set_visible(False) # left
        # spines[0].set_visible(border[3]) # left
        # spines[1].set_visible(border[1]) # right
        # spines[2].set_visible(border[2]) # bottom
        # spines[3].set_visible(border[0]) # top

    ax.set_xticks(xkeys)
    ax.set_xlim((min(xkeys)*(1-0.1), max(xkeys)*(1+0.1)))

    ax.set_yticks(ykeys)
    ax.set_ylim((min(ykeys), max(ykeys)))

    # ax.yaxis.set_major_formatter(ticker.FuncFormatter(yformatter))
    # ax.yaxis.set_minor_formatter(ticker.FuncFormatter(off_formatter))
    #
    # ax.xaxis.set_major_formatter(ticker.FuncFormatter(xformatter))
    # ax.xaxis.set_minor_formatter(ticker.FuncFormatter(off_formatter))

    return None


def learning_curve_error(ax, xkeys, ykeys,
                         x_range=None,
                         y_range=None,
                         border=[False, False, True, True],
                         loglog=True,
                         show_legend=True):
    """

    """

    if loglog:
        ax.set_xscale('log')
        ax.set_yscale('log')


    ax.set_xticks(xkeys)
    ax.set_yticks(ykeys)

    if x_range is None:
        ax.set_xlim((min(xkeys)*(1-0.1), max(xkeys)*(1+0.1)))
    else:
        ax.set_xlim(tuple(x_range))

    if y_range is None:
        ax.set_ylim((min(ykeys), max(ykeys)))
    else:
        ax.set_ylim(tuple(y_range))


    ax.yaxis.set_major_formatter(ticker.FuncFormatter(formatter_notrail))
    ax.yaxis.set_minor_formatter(ticker.FuncFormatter(formatter_off))

    ax.xaxis.set_major_formatter(ticker.FuncFormatter(formatter_int))
    ax.xaxis.set_minor_formatter(ticker.FuncFormatter(formatter_off))


    # ax.xaxis.set_tick_params(width=1.2)
    # ax.yaxis.set_tick_params(width=1.2)

    if border:
        # I like the css standard
        spines = ax.spines.items()
        for direction, spine in spines:

            # spine.set_linewidth(1.2)

            if direction == "top":
                spine.set_visible(border[0])

            if direction == "right":
                spine.set_visible(border[1])

            if direction == "bottom":
                spine.set_visible(border[2])
                spine.set_bounds(min(xkeys), max(xkeys))

            if direction == "left":
                spine.set_visible(border[3])
                spine.set_bounds(min(ykeys), max(ykeys))


    # Remove the small minor ticks in log-log plot
    ax.minorticks_off()



    return

def save(filename, fig=plt):

    fig.savefig(filename + ".png", bbox_inches="tight")
    fig.savefig(filename + ".pdf", bbox_inches="tight")

    return


def main():

    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('-f', '--filename', type=str, help='', metavar='file')
    args = parser.parse_args()


    # fig, axes = plt.subplots(N_plots, 1, figsize=(4, 4*N_plots))
    # ax.plot(learning_list, rmse_list, 'o-', label=name)

    return

if __name__ == '__main__':
    main()





# https://www.dataquest.io/blog/learning-curves-machine-learning/

import matplotlib.pyplot as plt
import matplotlib.patheffects as PathEffects
import numpy as np
import copy
import matplotlib_learningcurve as mpl_lc






def basic_idea():

    with plt.xkcd():
        fig, ax = plt.subplots()


    mu, sigma = 0, 0.5

    training_set_size = [2**x for x in range(1, 10)]
    training_set_size = np.linspace(1, 512, 50)

    training_set_size = np.array(training_set_size)
    N = len(training_set_size)

    error_training = training_set_size
    error_validation = 1/training_set_size

    s = np.random.normal(mu, sigma, N)
    scale = 6.0/np.arange(1, N+1)
    s *= scale
    error_training = 5*np.log(error_training) + s

    s = np.random.normal(mu, sigma, N)
    scale = 6.0/np.arange(1, N+1)
    s *= scale
    error_validation = 5*np.log(error_validation) + 64 + s

    ax.plot(training_set_size, error_training, "k--")
    ax.plot(training_set_size, error_validation, "k--")

    ax.set_ylabel("error")
    ax.set_xlabel("training set size")

    ykeys = [0, 30.0, 60]
    xkeys = [10, 150, 300, 500]

    mpl_lc.learning_curve_error(ax, xkeys, ykeys,
        x_range=(-20, 500),
        y_range=(-5, 60),
        loglog=False)

    plt.xticks([])
    plt.yticks([])

    font = {"family": "xkcd", "fontsize":15}


    txt_train = "Learning for training set".lower()
    txt_valid = "Learning for validation set".lower()
    ax.text(150, 50, txt_valid, **font)
    ax.text(150, 10, txt_train, **font)

    # ax.arrow(20, 10, 20, 0, head_width=2, head_length=4, head_starts_at_zero=True)

    mpl_lc.save("basic_learning")

    plt.clf()

    return



def vapnik_learning_curve():

    np.random.seed(999)

    plt.rc('path', effects=[PathEffects.withStroke(linewidth=4, foreground="w")])

    def get_error(N,a,b):
        error = a/N**b
        return error

    def get_error_bad(N, a, b, offset, noise=0.2):
        error = a/N**b * (1-np.random.normal(0, noise, 1)) + offset
        return error

    with plt.xkcd():
        fig, ax = plt.subplots()

    mu, sigma = 0, 0.5

    training_set_size = [10**x for x in range(1, 8)]
    training_set_size = np.array(training_set_size)
    N = len(training_set_size)

    # error_training = 5/training_set_size
    #
    # s = np.random.normal(mu, sigma, N)
    # scale = 6.0/np.arange(1, N+1)
    # s *= scale
    # error_training += 64 + s

    offset = 10

    error_training = [get_error_bad(x,600,0.3,100) for x in training_set_size]
    error_training = np.array(error_training)
    error_a = np.array([get_error_bad(x,10_000,0.7, 5.0) for x in training_set_size])
    error_b = np.array([get_error_bad(x,10_000,0.7,1.0) for x in training_set_size])

    ax.plot(training_set_size, error_training)
    ax.plot(training_set_size, error_a+1.0)
    ax.plot(training_set_size, error_b)

    # Models End
    model_names = ["A", "B", "C"]
    end_points = []
    end_points.append(error_training[-1])
    end_points.append(error_a[-1])
    end_points.append(error_b[-1])

    for name, point in zip(model_names, end_points):

        font = {
            "family": "xkcd",
            "fontsize":15,
            "horizontalalignment": 'right',
            "verticalalignment": 'center',
        }
        txtobj = ax.text(10**7, point, name, **font)
        txtobj.set_path_effects([PathEffects.withStroke(linewidth=5, foreground='w')])

    # lines

    line_data = [10]*N
    line_data = np.array(line_data) + np.random.normal(0,0.5,N)
    lineobj = ax.plot(training_set_size, line_data, "k--")

    yticks = [0.1, 1.0, 10, 100, 10**3, 10**4]
    line_data_y = np.array(yticks)
    line_data_x = np.array([10**4]*line_data_y.shape[0]) * (1- np.random.normal(0,0.05,line_data_y.shape[0]))
    lineobj = ax.plot(line_data_x, line_data_y, "k", linestyle="dotted")

    yticks = [0.1, 1.0, 10, 100, 10**3, 10**4]
    line_data_y = np.array(yticks)
    line_data_x = np.array([10**5]*line_data_y.shape[0]) * (1- np.random.normal(0,0.05,line_data_y.shape[0]))
    lineobj = ax.plot(line_data_x, line_data_y, "k", linestyle="dotted")


    lineobj[0].set_path_effects([PathEffects.withStroke(linewidth=5, foreground='w')])

    # text

    font = {
        "family": "xkcd",
        "fontsize":15,
        "horizontalalignment": 'center',
        "verticalalignment": 'center',
    }

    txt_valid = "target error".lower()
    txtobj = ax.text(10**2, 10**1, txt_valid, **font)
    txtobj.set_path_effects([PathEffects.withStroke(linewidth=5, foreground='w')])

    txt_valid = "data avail.".lower()
    txtobj = ax.text(10**4, 10**3, txt_valid, **font)
    txtobj.set_path_effects([PathEffects.withStroke(linewidth=5, foreground='w')])

    txt_valid = "data need.".lower()
    txtobj = ax.text(10**5, 10**3.5, txt_valid, **font)
    txtobj.set_path_effects([PathEffects.withStroke(linewidth=5, foreground='w')])


    # labels
    ax.set_ylabel("error")
    ax.set_xlabel("experience")

    # ticks
    yticks = [10**x for x in range(1, 8)]
    plt.yticks(yticks)



    ykeys = [1, 10.0, 100, 1000, 10**4]
    xkeys = [10**x for x in range(1,8)]
    # mpl_lc.learning_curve_error(ax, xkeys, ykeys)

    # plt.xticks([])
    # plt.yticks([])

    font = {"family": "xkcd", "fontsize":15}


    # txt_train = "Learning for training set".lower()
    # txt_valid = "Learning for validation set".lower()
    # ax.text(150, 50, txt_valid, **font)
    # ax.text(150, 10, txt_train, **font)

    # ax.arrow(20, 10, 20, 0, head_width=2, head_length=4, head_starts_at_zero=True)


    ax.set_xscale('log')
    ax.set_yscale('log')
    ax.minorticks_off()

    ax.set_xlim((5, max(xkeys)*(1+0.1)))
    ax.set_ylim((5*10**-1, max(ykeys)))

    border = [False, False, True, True]
    spines = ax.spines.items()
    for direction, spine in spines:
        if direction == "top":
            spine.set_visible(border[0])

        if direction == "right":
            spine.set_visible(border[1])

        if direction == "bottom":
            spine.set_visible(border[2])
            spine.set_bounds(min(xkeys), max(xkeys))

        if direction == "left":
            spine.set_visible(border[3])
            spine.set_bounds(min(ykeys), max(ykeys))


    mpl_lc.save("basic_learning_vapnik")

    plt.clf()



    return



###################################



def quantum_machine_learning():

    with plt.xkcd():
        fig, ax = plt.subplots()

    np.random.seed(999)

    plt.rc('path', effects=[PathEffects.withStroke(linewidth=4, foreground="w")])


    ykeys = list(range(5))
    xkeys = list(range(5))


    # line
    jitter_line_x = np.array(xkeys) * (1-np.random.normal(0,0.05,len(xkeys)))
    jitter_line_y = np.array(list(reversed(ykeys)))
    ax.plot(jitter_line_x, jitter_line_y, "k-")

    # methods
    method_opt = {
        "family": "xkcd",
        "fontsize":15,
        "horizontalalignment": 'left',
        "verticalalignment": 'center',
    }
    method_names = ["force-fields", "semi-empirical", "hartree-fock", "coupled-cluster", "full-ci"]
    for i, name in enumerate(method_names):
        txtobj = ax.text(jitter_line_x[i]+0.1, jitter_line_y[i], name, **method_opt)
        ax.plot(jitter_line_x[i], jitter_line_y[i], "k.")

    ax.text(2.1, 1.4, "density functional theory", **method_opt)
    ax.plot([2.0], [1.4], "k.")


    method_opt_prime = copy.deepcopy(method_opt)
    method_opt_prime["fontsize"] = 20

    ax.arrow(0.5, 2.5, 0.0, -1.5, head_width=0.1, head_length=0.1, color="k")
    ax.text(0.6, 0.5, r'$\left ( \vec R, \vec Z \right ) \frac{{ML}}{{\rightarrow}} P$', **method_opt)
    ax.plot([0.5], [0.5], "k.")

    ax.text(3.0, 3.5, r'$\hat H \left ( \vec R, \vec Z \right ) \frac{{\Psi}}{{\rightarrow}} P$', **method_opt_prime)


    # labels
    ax.set_ylabel("error")
    ax.set_xlabel("computational cost")

    # ticks
    # yticks = [10**x for x in range(1, 8)]
    # plt.yticks(yticks)


    plt.xticks([])
    plt.yticks([])
    ax.minorticks_off()

    # ax.set_xlim((5, max(xkeys)*(1+0.1)))
    # ax.set_ylim((5*10**-1, max(ykeys)))

    border = [False, False, True, True]
    spines = ax.spines.items()
    for direction, spine in spines:
        if direction == "top":
            spine.set_visible(border[0])

        if direction == "right":
            spine.set_visible(border[1])

        if direction == "bottom":
            spine.set_visible(border[2])
            spine.set_bounds(min(xkeys), max(xkeys))

        if direction == "left":
            spine.set_visible(border[3])
            spine.set_bounds(min(ykeys), max(ykeys))


    mpl_lc.save("quantum_machine_learning")

    plt.clf()

    return


####


def krr_query():


    with plt.xkcd():
        fig, ax = plt.subplots()

    np.random.seed(999)

    plt.rc('path', effects=[PathEffects.withStroke(linewidth=4, foreground="w")])


    def plot_func(x):

        y = np.cos(x/5)*x + x

        return y

    xvalues = np.linspace(1, 100, 100)
    yvalues = plot_func(xvalues)

    ax.plot(xvalues, yvalues, 'k')

    random_points = list(range(50, 55, 2)) + list(range(58, 63, 2)) + [65]
    random_points = np.array(random_points)
    plt.plot(xvalues[random_points], yvalues[random_points], 'ko')

    high_light = 56
    ax.plot(xvalues[high_light], yvalues[high_light], 'kx', ms=10)

    ax.set_xlabel('representation / feature', fontweight='medium', fontsize=15)
    ax.set_ylabel('property', fontweight='medium', fontsize=15)

    border = [False, False, True, True]

    spines = ax.spines.items()
    for direction, spine in spines:
        if direction == "top": spine.set_visible(border[0])
        if direction == "right": spine.set_visible(border[1])
        if direction == "bottom":
            spine.set_visible(border[2])
            spine.set_bounds(min(xvalues), max(xvalues))
        if direction == "left":
            spine.set_visible(border[3])
            spine.set_bounds(min(yvalues), max(yvalues))

    ax.set_xticks([])
    ax.set_yticks([])

    ax.set_xlim((-8, max(xvalues)*(1+0.1)))
    ax.set_ylim((-20, max(yvalues)*(1+0.1)))

    mpl_lc.save("krr_query")
    plt.clf()

    return




def main():

    basic_idea()
    vapnik_learning_curve()
    quantum_machine_learning()
    krr_query()


    return



if __name__ == "__main__":
    main()

###

fig, ax = viewlib.get_plot()

# Overlap with KDE

# Set histogram
ax.hist(no_conformers, bins=10, edgecolor='#ffffff')#, color="#2D82B5")

# Set KDE
ax2 = ax.twinx()
kde = stats.gaussian_kde(no_conformers)
kde_xaxis = np.linspace(min(no_conformers), max(no_conformers), 500)
kde_yaxis = kde(kde_xaxis)
ax2.plot(kde_xaxis, kde_yaxis, "k-",
    path_effects = [matplotlib.patheffects.withStroke(linewidth=8, foreground="w"),
    matplotlib.patheffects.Stroke(linewidth=3, foreground='k')]
)

ax.set_ylabel("Count")
ax.set_xlabel("Conformers per SMILES")


ax.set_ylim(-30, None)  # Set offset
viewlib.fix_borders(ax)
viewlib.fix_borders(ax2, visibles=[False]*4)

##

fig, axs = viewlib.get_plot(n_ax=3, sharex=False)

cmap="Blues"

viewlib.histograms.two_dimensional_hex(axs[0], res_atoms, res_time, colormap=cmap)
viewlib.histograms.two_dimensional_hex(axs[1], res_graph, res_time, colormap=cmap)
viewlib.histograms.two_dimensional_hex(axs[2], res_conformers, res_time, colormap=cmap)

axs[0].set_ylabel("computational time")
axs[0].set_xlabel("No. Atoms per compound")
axs[1].set_xlabel("No. Graphs per compound")
axs[2].set_xlabel("No. Conformers per compound")

viewlib.formats.set_axis_format(axs[0].yaxis, viewlib.formats.formatter_time)
viewlib.fix_borders(axs[0])
viewlib.fix_borders(axs[1], visibles=[False, False, True, False])
viewlib.fix_borders(axs[2], visibles=[False, False, True, False])

fig.tight_layout()

### 
