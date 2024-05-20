import unittest
import sys
import os
import math

# Add the directory containing solution.py to the Python path
current_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(current_dir)

from solution import calculate_sphere_volume

class TestCalculateSphereVolume(unittest.TestCase):

    def test_example_case(self):
        self.assertAlmostEqual(calculate_sphere_volume(3), 113.1, places=1)

    def test_zero_radius(self):
        self.assertAlmostEqual(calculate_sphere_volume(0), 0.0, places=1)

    def test_large_radius(self):
        self.assertAlmostEqual(calculate_sphere_volume(10), 4188.79, places=2)

if __name__ == '__main__':
    unittest.main(verbosity=2)
