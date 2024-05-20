import unittest
import sys
import os

# Add the directory containing solution.py to the Python path
current_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(current_dir)

from solution import roman_to_int

class TestRomanToInt(unittest.TestCase):

    def test_example_case(self):
        self.assertEqual(roman_to_int("XIV"), 14)

    def test_large_roman(self):
        self.assertEqual(roman_to_int("MMXVIII"), 2018)

    def test_invalid_roman(self):
        self.assertEqual(roman_to_int("IIII"), 0)

    def test_empty_string(self):
        self.assertEqual(roman_to_int(""), 0)

if __name__ == '__main__':
    unittest.main(verbosity=2)
