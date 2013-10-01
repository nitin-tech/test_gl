#!/usr/bin/env python

"""Program to find maximum share value of data in a given csv file"""

import sys
import csv

MONTH_NUM = dict(Jan=1, Feb=2, Mar=3, Apr=4, May=5, Jun=6,
                 Jul=7, Aug=8, Sep=9, Oct=10, Nov=11, Dec=12)
NUM_MONTH = {v: k for k, v in MONTH_NUM.iteritems()}


def get_max_values(csv_file):
    """Return dict of max values, year, month of shares in given csv file."""
    data = []
    result = []
    with open(csv_file) as fcsv:
        reader = csv.reader(fcsv)
        header = reader.next()
        for line in reader:
            entry = [int(x.strip()) if i != 1 else MONTH_NUM[x.strip()]
                        for i, x in enumerate(line)]
            data.append(entry)
    for i in range(2, len(header)):
        data.sort(key=lambda x: x[i], reverse=True)
        result.append((header[i].strip(), data[0][0], data[0][1], data[0][i]))
    return result


def print_result(result):
    """Print company name, year, month and max value as per given data."""
    print "Name, Year, Month, Max_value"
    for name, year, month, value in result:
        print "%s, %d, %s, %d" % (name, year, NUM_MONTH[month], value)

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print "Usage: max_values.py csvfile"
    else:
        print_result(get_max_values(sys.argv[1]))
