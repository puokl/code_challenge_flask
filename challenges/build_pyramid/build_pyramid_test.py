import unittest
import sys
import os

# Add the directory containing solution.py to the Python path
current_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(current_dir)

from solution import build_pyramid

class TestBuildPyramid(unittest.TestCase):

    def test_example_case(self):
        expected = [
            "    *    ",
            "   ***   ",
            "  *****  ",
            " ******* ",
            "*********"
        ]
        self.assertEqual(build_pyramid(5), expected)

    def test_single_floor(self):
        self.assertEqual(build_pyramid(1), ["*"])

    def test_two_floors(self):
        self.assertEqual(build_pyramid(2), [" * ", "***"])

    def test_invalid_input(self):
        with self.assertRaises(ValueError):
            build_pyramid(-1)

if __name__ == '__main__':
    unittest.main(verbosity=2)
