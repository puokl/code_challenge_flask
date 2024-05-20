import unittest
import sys
import os

# Add the directory containing solution.py to the Python path
current_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(current_dir)

from solution import factorial

class TestFactorial(unittest.TestCase):

    def test_example_case(self):
        self.assertEqual(factorial(5), 120)

    def test_zero(self):
        self.assertEqual(factorial(0), 1)

    def test_one(self):
        self.assertEqual(factorial(1), 1)

    def test_large_number(self):
        self.assertEqual(factorial(10), 3628800)

if __name__ == '__main__':
    unittest.main(verbosity=2)
