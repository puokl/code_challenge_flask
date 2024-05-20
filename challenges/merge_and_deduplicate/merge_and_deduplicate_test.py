import unittest
import sys
import os

# Add the directory containing solution.py to the Python path
current_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(current_dir)

from solution import merge_and_deduplicate

class TestMergeAndDeduplicate(unittest.TestCase):

    def test_example_case(self):
        self.assertEqual(merge_and_deduplicate([1, 3, 5], [2, 3, 6]), [1, 3, 5, 2, 6])

    def test_no_duplicates(self):
        self.assertEqual(merge_and_deduplicate([1, 2], [3, 4]), [1, 2, 3, 4])

    def test_all_duplicates(self):
        self.assertEqual(merge_and_deduplicate([1, 1, 1], [1, 1, 1]), [1])

    def test_empty_lists(self):
        self.assertEqual(merge_and_deduplicate([], []), [])

if __name__ == '__main__':
    unittest.main(verbosity=2)
