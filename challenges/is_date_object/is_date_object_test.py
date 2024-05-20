import unittest
import sys
import os
import datetime

# Add the directory containing solution.py to the Python path
current_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(current_dir)

from solution import is_date_object

class TestIsDateObject(unittest.TestCase):

    def test_example_case(self):
        self.assertTrue(is_date_object(datetime.date.today()))

    def test_string_date(self):
        self.assertFalse(is_date_object("2021-10-15"))

    def test_datetime_object(self):
        self.assertFalse(is_date_object(datetime.datetime.now()))

    def test_none(self):
        self.assertFalse(is_date_object(None))

if __name__ == '__main__':
    unittest.main(verbosity=2)
