import unittest
import sys
import os

# Add the directory containing solution.py to the Python path
current_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(current_dir)

from solution import is_power_of_two

class TestIsPowerOfTwo(unittest.TestCase):

    def test_example_case(self):
        self.assertTrue(is_power_of_two(8))

    def test_zero(self):
        self.assertFalse(is_power_of_two(0))

    def test_negative_number(self):
        self.assertFalse(is_power_of_two(-2))

    def test_not_power_of_two(self):
        self.assertFalse(is_power_of_two(10))

    def test_power_of_two(self):
        self.assertTrue(is_power_of_two(1024))

if __name__ == '__main__':
    unittest.main(verbosity=2)
