#!/usr/bin/env python3
# pcost.py
#
# Exercise 1.27

import sys

from report import read_portfolio


def portfolio_cost(filename):
    portfolio = read_portfolio(filename)
    return sum(h['shares'] * h['price'] for h in portfolio)


def main(argv):
    if len(argv) != 2:
        raise SystemExit(f'Usage: {sys.argv[0]} ' 'portfile')

    _, portfile = argv
    cost = portfolio_cost(portfile)
    print(f'Total cost: ${cost:>7.2f}')

    sys.exit()


if __name__ == '__main__':
    main(sys.argv)
