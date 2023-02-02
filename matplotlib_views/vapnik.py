from matplotlib import ticker

from matplotlib_views import formats


def learning_curve_error(
    ax,
    xkeys,
    ykeys,
    x_range=None,
    y_range=None,
    border=[False, False, True, True],
    loglog=True,
    show_legend=True,
):
    """ """

    if loglog:
        ax.set_xscale("log")
        ax.set_yscale("log")

    ax.set_xticks(xkeys)
    ax.set_yticks(ykeys)

    if x_range is None:
        ax.set_xlim((min(xkeys) * (1 - 0.1), max(xkeys) * (1 + 0.1)))
    else:
        ax.set_xlim(tuple(x_range))

    if y_range is None:
        ax.set_ylim((min(ykeys), max(ykeys)))
    else:
        ax.set_ylim(tuple(y_range))

    ax.yaxis.set_major_formatter(ticker.FuncFormatter(formats.formatter_notrail))
    ax.yaxis.set_minor_formatter(ticker.FuncFormatter(formats.formatter_off))

    ax.xaxis.set_major_formatter(ticker.FuncFormatter(formats.formatter_int))
    ax.xaxis.set_minor_formatter(ticker.FuncFormatter(formats.formatter_off))

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
