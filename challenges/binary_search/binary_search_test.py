import unittest
import sys
import os

# Add the directory containing solution.py to the Python path
current_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(current_dir)

from solution import binary_search

class TestBinarySearch(unittest.TestCase):

    def test_example_case(self):
        self.assertEqual(binary_search([1, 3, 5, 7, 9], 5), 2)

    def test_not_found(self):
        self.assertEqual(binary_search([1, 3, 5, 7, 9], 2), -1)

    def test_single_element_found(self):
        self.assertEqual(binary_search([5], 5), 0)

    def test_single_element_not_found(self):
        self.assertEqual(binary_search([5], 3), -1)

    def test_large_array(self):
        arr = list(range(1, 100001))
        self.assertEqual(binary_search(arr, 56789), 56788)

if __name__ == '__main__':
    unittest.main(verbosity=2)
