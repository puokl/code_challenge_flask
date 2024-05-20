import unittest
import sys
import os

# Add the directory containing solution.py to the Python path
current_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(current_dir)

from solution import find_missing_number

class TestFindMissingNumber(unittest.TestCase):

    def test_example_case(self):
        self.assertEqual(find_missing_number([1, 2, 4, 5]), 3)

    def test_no_missing_number(self):
        self.assertEqual(find_missing_number([1, 2, 3, 4, 5]), None)

    def test_large_gap(self):
        self.assertEqual(find_missing_number([10, 11, 13]), 12)

    def test_multiple_gaps(self):
        self.assertEqual(find_missing_number([1, 2, 4, 6]), 3)

    def test_unsorted_input(self):
        self.assertEqual(find_missing_number([3, 7, 6, 5, 4, 1]), 2)

if __name__ == '__main__':
    unittest.main(verbosity=2)
