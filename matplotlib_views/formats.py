"""
Collection of custom tick formatters

for example

ax.xaxis.set_major_formatter(formatter_suffix)

"""

import datetime

import matplotlib
import numpy as np

suffixes = {
    1e-9: "n",
    1e-6: "u",
    1e-3: "m",
    1: "",
    1e3: "k",
    1e6: "M",
    1e9: "G",
    1e12: "T",
    1e15: "Y",
}


def formatter_suffix(x, pos):

    fmt = ""

    if x > 1e3:
        fmt = "{:d}k"
        x /= 1e3
        x = np.round(x, decimals=0)
        x = int(x)
    else:
        fmt = "{:d}"

    point = fmt.format(x)

    return point


def formatter_time_float(seconds, pos):
    """ Automatically format time in seconds to nearest sec, mins, hours, days, years """

    delta = datetime.timedelta(seconds=seconds)

    days = delta.days
    seconds = delta.seconds
    hours = seconds // 3600
    minutes = (seconds // 60) % 60

    if days > 0:
        return f"{days}d"

    if hours > 0:
        return f"{hours}h"

    if minutes > 0:
        return f"{minutes}m"

    return f"{seconds}s"


def formatter_time(seconds, pos):
    """ Automatically format time in seconds to nearest sec, mins, hours, days, years """

    delta = datetime.timedelta(seconds=seconds)

    days = delta.days
    seconds = delta.seconds
    hours = seconds // 3600
    minutes = (seconds // 60) % 60

    if days > 0:
        return f"{days}d"

    if hours > 0:
        return f"{hours}h {minutes}m"

    if minutes > 0:
        return f"{minutes}m"

    return f"{seconds}s"


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
    return "{0:g}".format(x)


# usage


def set_axis_format(axis, format_func):
    """
    set ax.xaxis format
    """
    # ax.xaxis.set_major_formatter(matplotlib.ticker.FuncFormatter(formatter_sci))
    axis.set_major_formatter(matplotlib.ticker.FuncFormatter(format_func))
