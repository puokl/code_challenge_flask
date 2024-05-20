import unittest
import sys
import os
import datetime

# Add the directory containing solution.py to the Python path
current_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(current_dir)

from solution import is_weekend

class TestIsWeekend(unittest.TestCase):

    def test_example_case(self):
        self.assertTrue(is_weekend(datetime.date(2023, 5, 20)))  # Saturday

    def test_not_weekend(self):
        self.assertFalse(is_weekend(datetime.date(2023, 5, 18)))  # Thursday

    def test_sunday(self):
        self.assertTrue(is_weekend(datetime.date(2023, 5, 21)))  # Sunday

    def test_monday(self):
        self.assertFalse(is_weekend(datetime.date(2023, 5, 22)))  # Monday

if __name__ == '__main__':
    unittest.main(verbosity=2)
