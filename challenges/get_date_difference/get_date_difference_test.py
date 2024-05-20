import unittest
import sys
import os
import datetime

# Add the directory containing solution.py to the Python path
current_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(current_dir)

from solution import get_date_difference

class TestGetDateDifference(unittest.TestCase):

    def test_example_case(self):
        self.assertEqual(get_date_difference("2023-01-01", "2023-01-31"), 30)

    def test_same_date(self):
        self.assertEqual(get_date_difference("2023-01-01", "2023-01-01"), 0)

    def test_reverse_order(self):
        self.assertEqual(get_date_difference("2023-01-31", "2023-01-01"), 30)

    def test_leap_year(self):
        self.assertEqual(get_date_difference("2020-02-28", "2020-03-01"), 2)

if __name__ == '__main__':
    unittest.main(verbosity=2)
