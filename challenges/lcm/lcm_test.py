import unittest
import sys
import os

# Add the directory containing solution.py to the Python path
current_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(current_dir)

from solution import lcm

class TestLCM(unittest.TestCase):

    def test_example_case(self):
        self.assertEqual(lcm(4, 5), 20)

    def test_lcm_of_same_numbers(self):
        self.assertEqual(lcm(7, 7), 7)

    def test_lcm_with_zero(self):
        self.assertEqual(lcm(0, 5), 0)
        self.assertEqual(lcm(7, 0), 0)

    def test_lcm_of_primes(self):
        self.assertEqual(lcm(3, 5), 15)

if __name__ == '__main__':
    unittest.main(verbosity=2)
