import unittest
import sys
import os

# Add the directory containing solution.py to the Python path
current_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(current_dir)

from solution import is_prime

class TestIsPrime(unittest.TestCase):

    def test_example_case(self):
        self.assertTrue(is_prime(7))

    def test_non_prime(self):
        self.assertFalse(is_prime(10))

    def test_edge_cases(self):
        self.assertFalse(is_prime(1))
        self.assertTrue(is_prime(2))
        self.assertTrue(is_prime(3))

    def test_large_prime(self):
        self.assertTrue(is_prime(97))

if __name__ == '__main__':
    unittest.main(verbosity=2)
