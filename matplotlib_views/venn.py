#!/usr/bin/env python

import numpy as np
import pandas as pd
import scipy
import sklearn


def main(args=None):

    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('-v', '--version', action='version', version="1.0")
    parser.add_argument('--debug', action='store_true', help='')
    parser.add_argument('--format', action='store', help='', metavar='FMT')

    if args is None:
        args = parser.parse_args()
    else:
        args = parser.parse_args(args)

    

    return


if __name__ == '__main__':
    main()
