import unittest
import sys
import os

# Add the directory containing solution.py to the Python path
current_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(current_dir)

from solution import find_first_occurrence

class TestFindFirstOccurrence(unittest.TestCase):

    def test_example_case(self):
        self.assertEqual(find_first_occurrence([2, 4, 10, 10, 10, 18, 20], 10), 2)

    def test_not_found(self):
        self.assertEqual(find_first_occurrence([1, 2, 3, 4, 5], 6), -1)

    def test_single_element(self):
        self.assertEqual(find_first_occurrence([10], 10), 0)

    def test_multiple_occurrences(self):
        self.assertEqual(find_first_occurrence([1, 1, 1, 1], 1), 0)

if __name__ == '__main__':
    unittest.main(verbosity=2)
