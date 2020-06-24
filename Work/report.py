#!/usr/bin/env python3
# report.py
#
# Exercise 2.4

import sys

from fileparse import parse_csv


def read_portfolio(filename):
    with open(filename, 'rt') as lines:
        return parse_csv(lines, select=['name', 'shares', 'price'],
                         types=[str, int, float])


def read_prices(filename):
    with open(filename, 'rt') as lines:
        return dict(parse_csv(lines, has_headers=False, types=[str, float]))


def portfolio_cost(portfolio):
    return sum(h['shares'] * h['price'] for h in portfolio)


def portfolio_value(portfolio, prices):
    return sum(h['shares'] * prices[h['name']] for h in portfolio)


def portfolio_gain(portfolio, prices):
    return portfolio_value(portfolio, prices) - portfolio_cost(portfolio)


def make_report(portfolio, prices):
    report = []

    for holding in portfolio:
        name = holding['name']
        shares = holding['shares']
        price = prices[holding['name']]
        change = price - holding['price']
        report.append((name, shares, price, change))

    return report


def print_report(report):
    headers = ('Name', 'Shares', 'Price', 'Change')
    print('{:>10s} {:>10s} {:>10s} {:>10s}'.format(*headers))
    print(10*'-', 10*'-', 10*'-', 10*'-')
    for name, shares, price, change in report:
        price = f'${price:.2f}'
        print(f'{name:>10s} {shares:>10d} {price:>10s} {change:>10.2f}')


def portfolio_report(portfolio_filename, prices_filename):
    portfolio = read_portfolio(portfolio_filename)
    prices = read_prices(prices_filename)

    report = make_report(portfolio, prices)
    print_report(report)

    value = portfolio_value(portfolio, prices)
    gain = portfolio_gain(portfolio, prices)
    print(f'\nCurrent portfolio value is: ${value:10.2f}')
    print(f'Total gain/loss is: ${gain:10.2f}')


def main(argv):
    if len(argv) != 3:
        raise SystemExit(f'Usage: {sys.argv[0]} ' 'portfile pricefile')

    _, portfile, pricefile = argv
    portfolio_report(portfile, pricefile)

    sys.exit()


if __name__ == '__main__':
    main(sys.argv)
