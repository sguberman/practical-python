# ticker.py

from .follow import follow
from .report import read_portfolio
from .tableformat import create_formatter

import csv


def select_columns(rows, indices):
    for row in rows:
        yield [row[idx] for idx in indices]


def convert_types(rows, types):
    for row in rows:
        yield [fn(val) for fn, val in zip(types, row)]


def make_dicts(rows, headers):
    for row in rows:
        yield dict(zip(headers, row))


def filter_symbols(rows, names):
    for row in rows:
        if row['name'] in names:
            yield row


def parse_stock_data(lines):
    rows = csv.reader(lines)
    rows = select_columns(rows, [0, 1, 4])
    rows = convert_types(rows, [str, float, float])
    rows = make_dicts(rows, ['name', 'price', 'change'])
    return rows


def ticker(portfile, logfile, fmt):
    portfolio = read_portfolio(portfile)
    rows = parse_stock_data(follow(logfile))
    rows = (row for row in rows if row['name'] in portfolio)
    fmtr = create_formatter(fmt)
    fmtr.headings(['name', 'price', 'change'])
    for row in rows:
        name = row['name']
        price = row['price']
        change = row['change']
        fmtr.row([name, f"{price:0.2f}", f"{change:0.2f}"])


if __name__ == '__main__':
    ticker('Data/portfolio.csv', 'Data/stocklog.csv', 'txt')
