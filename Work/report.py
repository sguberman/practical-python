#!/usr/bin/env python3
# report.py
#
# Exercise 2.4

import sys

from fileparse import parse_csv
from stock import Stock
from tableformat import create_formatter


def read_portfolio(filename):
    with open(filename, 'rt') as lines:
        portdicts = parse_csv(lines,
                              select=['name', 'shares', 'price'],
                              types=[str, int, float])

    return [Stock(d['name'], d['shares'], d['price']) for d in portdicts]


def read_prices(filename):
    with open(filename, 'rt') as lines:
        return dict(parse_csv(lines, has_headers=False, types=[str, float]))


def portfolio_cost(portfolio):
    return sum(s.cost() for s in portfolio)


def portfolio_value(portfolio, prices):
    return sum(s.shares * prices[s.name] for s in portfolio)


def portfolio_gain(portfolio, prices):
    return portfolio_value(portfolio, prices) - portfolio_cost(portfolio)


def make_report(portfolio, prices):
    report = []
    for holding in portfolio:
        name = holding.name
        shares = holding.shares
        price = prices[holding.name]
        change = price - holding.price
        report.append((name, shares, price, change))

    return report


def print_report(report, formatter):
    '''
    Print a nicely formatted table from a list of (name, shares, price, change)
    tuples.
    '''
    formatter.headings(['Name', 'Shares', 'Price', 'Change'])
    for name, shares, price, change in report:
        rowdata = [name, f'{shares:d}', f'{price:.2f}', f'{change:.2f}']
        formatter.row(rowdata)


def portfolio_report(portfolio_filename, prices_filename, fmt='txt'):
    '''
    Make a stock report given portfolio and price data files.
    '''
    # Read data files
    portfolio = read_portfolio(portfolio_filename)
    prices = read_prices(prices_filename)

    # Make report data
    report = make_report(portfolio, prices)

    # Print it out
    formatter = create_formatter(fmt)
    print_report(report, formatter)

#    value = portfolio_value(portfolio, prices)
#    gain = portfolio_gain(portfolio, prices)
#    print(f'\nCurrent portfolio value is: ${value:10.2f}')
#    print(f'Total gain/loss is: ${gain:10.2f}')


def main(argv):
    if len(argv) == 3:
        _, portfile, pricefile = argv
        portfolio_report(portfile, pricefile)
    elif len(argv) == 4:
        _, portfile, pricefile, fmt = argv
        portfolio_report(portfile, pricefile, fmt)
    else:
        raise SystemExit(f'Usage: {sys.argv[0]} ' 'portfile pricefile [fmt]')

    sys.exit()


if __name__ == '__main__':
    main(sys.argv)
