import unittest
import sys
import os

# Add the directory containing solution.py to the Python path
current_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(current_dir)

from solution import remove_duplicates

class TestRemoveDuplicates(unittest.TestCase):

    def test_example_case(self):
        self.assertEqual(remove_duplicates([1, 2, 2, 3, 4, 4, 4, 5]), [1, 2, 3, 4, 5])

    def test_no_duplicates(self):
        self.assertEqual(remove_duplicates([1, 2, 3]), [1, 2, 3])

    def test_all_duplicates(self):
        self.assertEqual(remove_duplicates([1, 1, 1, 1]), [1])

    def test_empty_list(self):
        self.assertEqual(remove_duplicates([]), [])

if __name__ == '__main__':
    unittest.main(verbosity=2)
