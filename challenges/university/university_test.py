import unittest
import sys
import os

# Add the directory containing solution.py to the Python path
current_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(current_dir)

from solution import University

class TestUniversity(unittest.TestCase):

    def test_add_department(self):
        uni = University()
        uni.add_department("Computer Science")
        self.assertIn("Computer Science", uni.get_departments())

    def test_remove_department(self):
        uni = University()
        uni.add_department("Mathematics")
        uni.remove_department("Mathematics")
        self.assertNotIn("Mathematics", uni.get_departments())

    def test_no_duplicates(self):
        uni = University()
        uni.add_department("Physics")
        uni.add_department("Physics")
        departments = uni.get_departments()
        self.assertEqual(len(departments), 1)
        self.assertIn("Physics", departments)

if __name__ == '__main__':
    unittest.main(verbosity=2)
