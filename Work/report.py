# report.py
#
# Exercise 2.4

import csv


def read_portfolio(filename):
    portfolio = []

    with open(filename, 'rt') as f:
        rows = csv.reader(f)
        headers = next(rows)
        for i, row in enumerate(rows, start=1):
            record = dict(zip(headers, row))
            try:
                record['shares'] = int(record['shares'])
                record['price'] = float(record['price'])
                portfolio.append(record)
            except ValueError:
                print(f'Error parsing row {i}: {row}... Skipping.')

    return portfolio


def read_prices(filename):
    prices = {}

    with open(filename, 'rt') as f:
        rows = csv.reader(f)
        for i, row in enumerate(rows, start=1):
            try:
                name, price = row
                prices[name] = float(price)
            except ValueError:
                print('Row {i}: Error parsing: {row}')

    return prices


def portfolio_cost(portfolio):
    return sum(holding['shares'] * holding['price'] for holding in portfolio)


def portfolio_value(portfolio, prices):
    return sum(holding['shares'] * prices[holding['name']] for holding in portfolio)


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


portfolio = read_portfolio('Data/portfolio.csv')
prices = read_prices('Data/prices.csv')
value = portfolio_value(portfolio, prices)
gain = portfolio_gain(portfolio, prices)
print(f'Current portfolio value is: ${value:10.2f}')
print(f'Total gain/loss is: ${gain:10.2f}')

report = make_report(portfolio, prices)
print_report(report)
