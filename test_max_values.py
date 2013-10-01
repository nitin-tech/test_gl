#!/usr/bin/env python

"""Tests for the max share value program"""

import unittest
import max_values


class TestMaxValues(unittest.TestCase):
    def test_get_max_values_small(self):
        ans = [('Intel', 2001, 1, 979),
               ('Google', 2001, 9, 918),
               ('Yahoo', 2000, 7, 996)]
        res = max_values.get_max_values('data_small.csv')
        self.assertEqual(ans, res)

    def test_get_max_values_large(self):
        ans = [('Intel', 1912, 11, 1000),
               ('Google', 2009, 10, 999),
               ('Yahoo', 1919, 10, 1000)]
        res = max_values.get_max_values('data_large.csv')
        self.assertEqual(ans, res)

if __name__ == '__main__':
    unittest.main()
