import unittest
import sys
import os

# Add the directory containing solution.py to the Python path
current_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(current_dir)

from solution import Person

class TestPerson(unittest.TestCase):

    def test_example_case(self):
        p = Person("Jane Doe", 32)
        self.assertEqual(p.display_info(), "Name: Jane Doe, Age: 32")

    def test_different_person(self):
        p = Person("John Smith", 25)
        self.assertEqual(p.display_info(), "Name: John Smith, Age: 25")

    def test_empty_name(self):
        p = Person("", 40)
        self.assertEqual(p.display_info(), "Name: , Age: 40")

if __name__ == '__main__':
    unittest.main(verbosity=2)
