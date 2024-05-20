import unittest
import sys
import os

# Add the directory containing solution.py to the Python path
current_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(current_dir)

from solution import calculate_cube_volume

class TestCalculateCubeVolume(unittest.TestCase):

    def test_example_case(self):
        self.assertEqual(calculate_cube_volume(3), 27)

    def test_zero_edge_length(self):
        self.assertEqual(calculate_cube_volume(0), 0)

    def test_negative_edge_length(self):
        self.assertEqual(calculate_cube_volume(-3), -27)

    def test_large_edge_length(self):
        self.assertEqual(calculate_cube_volume(10), 1000)

if __name__ == '__main__':
    unittest.main(verbosity=2)
