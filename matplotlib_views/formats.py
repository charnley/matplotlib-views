
from matplotlib.ticker import NullFormatter

suffixes = {
    1e-9: 'n',
    1e-6: 'u',
    1e-3: 'm',
    1: '',
    1e3: 'k',
    1e6: 'M',
    1e9: 'G',
    1e12: 'T',
    1e15: 'Y',
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
