import unittest
import sys
import os

# Add the directory containing solution.py to the Python path
current_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(current_dir)

from solution import find_leap_years

class TestFindLeapYears(unittest.TestCase):

    def test_example_case(self):
        self.assertEqual(find_leap_years(1990, 2000), [1992, 1996, 2000])

    def test_no_leap_years(self):
        self.assertEqual(find_leap_years(2018, 2019), [])

    def test_all_leap_years(self):
        self.assertEqual(find_leap_years(2000, 2000), [2000])

    def test_large_range(self):
        self.assertEqual(find_leap_years(1900, 2000), [1904, 1908, 1912, 1916, 1920, 1924, 1928, 1932, 1936, 1940, 1944, 1948, 1952, 1956, 1960, 1964, 1968, 1972, 1976, 1980, 1984, 1988, 1992, 1996, 2000])

if __name__ == '__main__':
    unittest.main(verbosity=2)
