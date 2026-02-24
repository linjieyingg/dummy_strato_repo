import unittest
import sys
import os

# Add the src directory to the Python path to allow importing src.string_utils.
# This is a common pattern when running tests where the 'src' directory is a sibling
# to the 'tests' directory, and 'src' is not installed as a package.
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

try:
    # Import the functions to be tested from src.string_utils.
    # Added 'is_palindrome' based on the presence of 'update_readme_for_is_palindrome_function'
    # in the repository context, implying it's a function that needs testing.
    from src.string_utils import reverse_string, count_vowels, count_letters, is_palindrome
except ImportError as e:
    print(f"Error: Could not import functions from src/string_utils.py: {e}")
    print("Please ensure 'src/string_utils.py' exists and contains 'reverse_string', 'count_vowels', 'count_letters', and 'is_palindrome' functions.")
    sys.exit(1)


class TestStringUtils(unittest.TestCase):
    """
    Test suite for string utility functions: reverse_string, count_vowels, count_letters,
    and is_palindrome. Ensures that functions handle various inputs correctly, including
    edge cases and non-string types, as defined in src/string_utils.py.
    """

    # --- Tests for reverse_string ---
    def test_reverse_string_empty(self):
        """Test reverse_string with an empty string."""
        self.assertEqual(reverse_string(""), "")

    def test_reverse_string_single_character(self):
        """Test reverse_string with a single character string."""
        self.assertEqual(reverse_string("a"), "a")
        self.assertEqual(reverse_string("Z"), "Z")
        self.assertEqual(reverse_string("1"), "1")

    def test_reverse_string_normal_word(self):
        """Test reverse_string with a regular word."""
        self.assertEqual(reverse_string("hello"), "olleh")
        self.assertEqual(reverse_string("python"), "nohtyp")

    def test_reverse_string_palindrome(self):
        """Test reverse_string with a string that is a palindrome."""
        self.assertEqual(reverse_string("madam"), "madam")
        self.assertEqual(reverse_string("racecar"), "racecar")

    def test_reverse_string_with_spaces(self):
        """Test reverse_string with strings containing spaces."""
        self.assertEqual(reverse_string("hello world"), "dlrow olleh")
        self.assertEqual(reverse_string(" a b c "), " c b a ")

    def test_reverse_string_with_special_characters(self):
        """Test reverse_string with strings containing special characters."""
        self.assertEqual(reverse_string("!@#$"), "$#@!")
        self.assertEqual(reverse_string("test!123"), "321!tset")

    def test_reverse_string_mixed_case(self):
        """Test reverse_string with mixed case characters."""
        self.assertEqual(reverse_string("HeLlO"), "OlLeH")

    def test_reverse_string_non_string_input(self):
        """Test reverse_string with non-string inputs to ensure TypeError is raised."""
        with self.assertRaises(TypeError, msg="Should raise TypeError for integer input"):
            reverse_string(123)
        with self.assertRaises(TypeError, msg="Should raise TypeError for list input"):
            reverse_string(['a', 'b'])
        with self.assertRaises(TypeError, msg="Should raise TypeError for None input"):
            reverse_string(None)
        with self.assertRaises(TypeError, msg="Should raise TypeError for float input"):
            reverse_string(3.14)

    # --- Tests for count_vowels ---
    def test_count_vowels_empty_string(self):
        """Test count_vowels with an empty string."""
        self.assertEqual(count_vowels(""), 0)

    def test_count_vowels_no_vowels(self):
        """Test count_vowels with a string containing no vowels."""
        self.assertEqual(count_vowels("rhythm"), 0)
        self.assertEqual(count_vowels("sky"), 0)
        self.assertEqual(count_vowels("gypt"), 0)

    def test_count_vowels_all_lowercase_vowels(self):
        """Test count_vowels with a string containing only lowercase vowels."""
        self.assertEqual(count_vowels("aeiou"), 5)
        self.assertEqual(count_vowels("apple"), 2)  # a, e
        self.assertEqual(count_vowels("banana"), 3) # a, a, a

    def test_count_vowels_all_uppercase_vowels(self):
        """Test count_vowels with a string containing only uppercase vowels."""
        self.assertEqual(count_vowels("AEIOU"), 5)
        self.assertEqual(count_vowels("EXAMPLE"), 3) # E, A, E
        self.assertEqual(count_vowels("ORANGE"), 3) # O, A, E

    def test_count_vowels_mixed_case_vowels(self):
        """Test count_vowels with a string containing mixed case vowels."""
        self.assertEqual(count_vowels("AeIoU"), 5)
        self.assertEqual(count_vowels("PyThOn"), 1)  # O
        self.assertEqual(count_vowels("EDUCATION"), 5) # E, U, A, I, O

    def test_count_vowels_with_consonants_and_spaces(self):
        """Test count_vowels with a string containing consonants, vowels, and spaces."""
        self.assertEqual(count_vowels("hello world"), 3)  # e, o, o
        self.assertEqual(count_vowels("The quick brown fox"), 5) # e, u, i, o, o

    def test_count_vowels_with_special_characters_and_numbers(self):
        """Test count_vowels with special characters and numbers."""
        self.assertEqual(count_vowels("!@#$%^&*()12345"), 0)
        self.assertEqual(count_vowels("a1e2i3o4u5"), 5)
        self.assertEqual(count_vowels("Pyth0n Is AW3S0M3!"), 4) # I, A, e, O

    def test_count_vowels_non_string_input(self):
        """Test count_vowels with non-string inputs to ensure TypeError is raised."""
        with self.assertRaises(TypeError, msg="Should raise TypeError for integer input"):
            count_vowels(123)
        with self.assertRaises(TypeError, msg="Should raise TypeError for list input"):
            count_vowels(['a', 'e'])
        with self.assertRaises(TypeError, msg="Should raise TypeError for None input"):
            count_vowels(None)
        with self.assertRaises(TypeError, msg="Should raise TypeError for float input"):
            count_vowels(3.14)

    # --- Tests for count_letters ---
    def test_count_letters_empty_string(self):
        """Test count_letters with an empty string."""
        self.assertEqual(count_letters(""), 0)

    def test_count_letters_only_letters(self):
        """Test count_letters with a string containing only letters."""
        self.assertEqual(count_letters("hello"), 5)
        self.assertEqual(count_letters("PythonProgramming"), 17)
        self.assertEqual(count_letters("HelloWorld"), 10)

    def test_count_letters_with_spaces(self):
        """Test count_letters with a string containing spaces."""
        self.assertEqual(count_letters("hello world"), 10)
        self.assertEqual(count_letters("  Python  "), 6)

    def test_count_letters_with_numbers(self):
        """Test count_letters with a string containing numbers."""
        self.assertEqual(count_letters("abc123def"), 6)
        self.assertEqual(count_letters("12345"), 0)
        self.assertEqual(count_letters("Python3"), 6)

    def test_count_letters_with_special_characters(self):
        """Test count_letters with a string containing special characters."""
        self.assertEqual(count_letters("!@#$%^&*()"), 0)
        self.assertEqual(count_letters("test!@#string"), 10)
        self.assertEqual(count_letters("ab-cd_ef"), 6)

    def test_count_letters_mixed_content(self):
        """Test count_letters with a string containing mixed letters, numbers, spaces, and special characters."""
        self.assertEqual(count_letters("Hello World! 123"), 10) # "Hello" (5) + "World" (5)
        self.assertEqual(count_letters("Python is fun! 🚀"), 10) # '🚀' is not considered a letter by `isalpha()`

    def test_count_letters_non_string_input(self):
        """Test count_letters with non-string inputs to ensure TypeError is raised."""
        with self.assertRaises(TypeError, msg="Should raise TypeError for integer input"):
            count_letters(123)
        with self.assertRaises(TypeError, msg="Should raise TypeError for list input"):
            count_letters(['a', 'b'])
        with self.assertRaises(TypeError, msg="Should raise TypeError for None input"):
            count_letters(None)
        with self.assertRaises(TypeError, msg="Should raise TypeError for float input"):
            count_letters(3.14)
            
    # --- Tests for is_palindrome ---
    def test_is_palindrome_empty_string(self):
        """Test is_palindrome with an empty string."""
        self.assertTrue(is_palindrome(""))

    def test_is_palindrome_single_character(self):
        """Test is_palindrome with a single character string."""
        self.assertTrue(is_palindrome("a"))
        self.assertTrue(is_palindrome("Z"))
        self.assertTrue(is_palindrome("1"))

    def test_is_palindrome_simple_palindromes(self):
        """Test is_palindrome with simple palindromic words."""
        self.assertTrue(is_palindrome("madam"))
        self.assertTrue(is_palindrome("racecar"))
        self.assertTrue(is_palindrome("level"))

    def test_is_palindrome_simple_non_palindromes(self):
        """Test is_palindrome with simple non-palindromic words."""
        self.assertFalse(is_palindrome("hello"))
        self.assertFalse(is_palindrome("python"))
        self.assertFalse(is_palindrome("world"))

    def test_is_palindrome_with_mixed_case(self):
        """Test is_palindrome with mixed case strings (should ignore case)."""
        self.assertTrue(is_palindrome("Madam"))
        self.assertTrue(is_palindrome("Racecar"))
        self.assertFalse(is_palindrome("Python")) # still not a palindrome

    def test_is_palindrome_with_spaces_and_punctuation(self):
        """Test is_palindrome with spaces and punctuation (should ignore them)."""
        self.assertTrue(is_palindrome("A man, a plan, a canal: Panama"))
        self.assertTrue(is_palindrome("No lemon, no melon"))
        self.assertTrue(is_palindrome("Was it a car or a cat I saw?"))
        self.assertFalse(is_palindrome("Hello world!"))

    def test_is_palindrome_with_numbers(self):
        """Test is_palindrome with numbers in the string."""
        self.assertTrue(is_palindrome("12321"))
        # This example combines letters, spaces, and punctuation as well, similar to 'A man...'
        self.assertTrue(is_palindrome("Able was I ere I saw Elba")) 
        self.assertFalse(is_palindrome("12345"))
        self.assertTrue(is_palindrome("Aibohphobia")) # Fear of palindromes itself

    def test_is_palindrome_non_string_input(self):
        """Test is_palindrome with non-string inputs to ensure TypeError is raised."""
        with self.assertRaises(TypeError, msg="Should raise TypeError for integer input"):
            is_palindrome(123)
        with self.assertRaises(TypeError, msg="Should raise TypeError for list input"):
            is_palindrome(['a', 'b'])
        with self.assertRaises(TypeError, msg="Should raise TypeError for None input"):
            is_palindrome(None)
        with self.assertRaises(TypeError, msg="Should raise TypeError for float input"):
            is_palindrome(3.14)


# This block allows running tests directly from the script
if __name__ == '__main__':
    # Using a modified main() call to prevent sys.exit() and avoid issues with some environments
    # that might pass unexpected arguments or require different exit behavior.
    unittest.main(argv=['first-arg-is-ignored'], exit=False)