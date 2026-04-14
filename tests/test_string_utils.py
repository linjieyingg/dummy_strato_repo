import unittest
from src.utils.string_utils import is_palindrome

class TestIsPalindrome(unittest.TestCase):
    """
    Unit tests for the `is_palindrome` function found in
    `src.utils.string_utils`.
    """

    def test_simple_palindromes(self):
        """
        Tests `is_palindrome` with basic palindrome strings.
        """
        self.assertTrue(is_palindrome("madam"))
        self.assertTrue(is_palindrome("racecar"))
        self.assertTrue(is_palindrome("level"))

    def test_palindromes_with_mixed_case_and_punctuation(self):
        """
        Tests `is_palindrome` with strings that include mixed casing,
        spaces, and punctuation, which should be ignored.
        """
        self.assertTrue(is_palindrome("A man, a plan, a canal: Panama"))
        self.assertTrue(is_palindrome("No lemon, no melon."))
        self.assertTrue(is_palindrome("Was it a car or a cat I saw?"))
        self.assertTrue(is_palindrome("Racecar!")) # Punctuation at end

    def test_non_palindromes(self):
        """
        Tests `is_palindrome` with strings that are not palindromes.
        """
        self.assertFalse(is_palindrome("hello"))
        self.assertFalse(is_palindrome("world"))
        self.assertFalse(is_palindrome("python"))
        self.assertFalse(is_palindrome("not a palindrome"))

    def test_edge_cases(self):
        """
        Tests `is_palindrome` with edge case strings like empty,
        single character, or strings with only non-alphanumeric characters.
        """
        self.assertTrue(is_palindrome(""))         # Empty string is a palindrome
        self.assertTrue(is_palindrome("a"))        # Single character is a palindrome
        self.assertTrue(is_palindrome("B"))        # Single character, different case
        self.assertTrue(is_palindrome(" "))        # Only space, becomes empty string
        self.assertTrue(is_palindrome("!@#$%"))    # Only non-alphanumeric, becomes empty string
        self.assertTrue(is_palindrome("!a!"))      # Single alphanumeric with punctuation

    def test_numbers_as_string(self):
        """
        Tests `is_palindrome` with strings containing only numbers.
        """
        self.assertTrue(is_palindrome("12321"))
        self.assertFalse(is_palindrome("12345"))
        self.assertTrue(is_palindrome("1"))

    def test_type_error_for_non_string_input(self):
        """
        Tests that `is_palindrome` raises a TypeError when input is not a string.
        """
        with self.assertRaises(TypeError) as cm:
            is_palindrome(123)
        self.assertEqual(str(cm.exception), "Input must be a string.")

        with self.assertRaises(TypeError) as cm:
            is_palindrome(["list"])
        self.assertEqual(str(cm.exception), "Input must be a string.")

        with self.assertRaises(TypeError) as cm:
            is_palindrome(None)
        self.assertEqual(str(cm.exception), "Input must be a string.")


if __name__ == '__main__':
    unittest.main()