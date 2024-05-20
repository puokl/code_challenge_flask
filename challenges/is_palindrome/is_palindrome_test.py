import unittest
import sys
import os

# Add the directory containing solution.py to the Python path
current_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(current_dir)

from solution import is_palindrome

class TestIsPalindrome(unittest.TestCase):

    def test_example_case(self):
        self.assertTrue(is_palindrome("racecar"))

    def test_non_palindrome(self):
        self.assertFalse(is_palindrome("hello"))

    def test_mixed_case_palindrome(self):
        self.assertTrue(is_palindrome("A man a plan a canal Panama"))

    def test_empty_string(self):
        self.assertTrue(is_palindrome(""))

if __name__ == '__main__':
    unittest.main(verbosity=2)
