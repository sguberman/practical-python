# fileparse.py
#
# Exercise 3.3

import csv


def parse_csv(lines, has_headers=True, select=None, types=None,
              delimiter=',', silence_errors=False):
    '''
    Parse an iterable into a list of records.
    '''
    if isinstance(lines, str):
        raise RuntimeError('lines argument must be a file-like iterable')
    elif select and not has_headers:
        raise RuntimeError('select argument requires column headers')

    rows = csv.reader(lines, delimiter=delimiter)

    if has_headers:
        headers = next(rows)  # grab the headers from the first row

    records = []
    for i, row in enumerate(rows, start=1):
        try:
            if not row:  # skip blank lines
                continue
            if has_headers:  # create a dict for data with headers
                record = dict(zip(headers, row))
                if select:
                    record = {field: val for field, val in record.items()
                              if field in select}
                if types:
                    record = {field: fn(val) for fn, (field, val) in
                              zip(types, record.items())}
            else:  # create a tuple for data without headers
                if types:
                    record = tuple(fn(val) for fn, val in zip(types, row))
                else:
                    record = row
            records.append(record)
        except ValueError as e:
            if not silence_errors:
                print(f"Row {i}: Couldn't convert {row}...")
                print(f'...Reason: {e}')
                print('...Skipping.')

    return records
