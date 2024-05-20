import unittest
import sys
import os

# Add the directory containing solution.py to the Python path
current_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(current_dir)

from solution import first_non_repeated_character

class TestFirstNonRepeatedCharacter(unittest.TestCase):

    def test_example_case(self):
        self.assertEqual(first_non_repeated_character('abacddbec'), 'e')

    def test_no_non_repeated_characters(self):
        self.assertEqual(first_non_repeated_character('aabbcc'), None)

    def test_first_char_non_repeated(self):
        self.assertEqual(first_non_repeated_character('abacddbe'), 'a')

    def test_all_unique(self):
        self.assertEqual(first_non_repeated_character('abcdef'), 'a')

    def test_single_character(self):
        self.assertEqual(first_non_repeated_character('z'), 'z')

if __name__ == '__main__':
    unittest.main(verbosity=2)
