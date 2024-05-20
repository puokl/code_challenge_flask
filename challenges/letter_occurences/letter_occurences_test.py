import unittest
import sys
import os

# Add the directory containing solution.py to the Python path
current_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(current_dir)

from solution import letter_occurrences

class TestLetterOccurrences(unittest.TestCase):

    def test_example_case(self):
        self.assertEqual(letter_occurrences('hello world'), {'h': 1, 'e': 1, 'l': 3, 'o': 2, 'w': 1, 'r': 1, 'd': 1})

    def test_case_insensitivity(self):
        self.assertEqual(letter_occurrences('HeLLo WoRLd'), {'h': 1, 'e': 1, 'l': 3, 'o': 2, 'w': 1, 'r': 1, 'd': 1})

    def test_non_letter_characters(self):
        self.assertEqual(letter_occurrences('123@#$'), {})

    def test_empty_string(self):
        self.assertEqual(letter_occurrences(''), {})

    def test_all_unique(self):
        self.assertEqual(letter_occurrences('abc'), {'a': 1, 'b': 1, 'c': 1})

if __name__ == '__main__':
    unittest.main(verbosity=2)
