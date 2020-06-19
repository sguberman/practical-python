# pcost.py
#
# Exercise 1.27

import csv
import sys


def portfolio_cost(filename):
    total = 0

    with open(filename, 'rt') as f:
        portfolio = csv.reader(f)
        headers = next(portfolio)
        for row in portfolio:
            try:
                symbol, shares, price = row
                total += int(shares) * float(price)
            except ValueError:
                print(f'Error parsing row: {row} ... Skipping...')

    return total


if len(sys.argv) == 2:
    filename = sys.argv[1]
else:
    filename = 'Data/portfolio.csv'

cost = portfolio_cost(filename)
print(f'Total cost: ${cost:>7.2f}')
