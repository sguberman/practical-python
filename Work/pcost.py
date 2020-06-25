#!/usr/bin/env python3
# pcost.py
#
# Exercise 1.27

import sys

import report


def portfolio_cost(filename):
    portfolio = report.read_portfolio(filename)
    return report.portfolio_cost(portfolio)


def main(argv):
    if len(argv) != 2:
        raise SystemExit(f'Usage: {sys.argv[0]} ' 'portfile')

    _, portfile = argv
    cost = portfolio_cost(portfile)
    print(f'Total cost: ${cost:>7.2f}')

    sys.exit()


if __name__ == '__main__':
    main(sys.argv)
