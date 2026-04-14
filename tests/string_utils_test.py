import unittest
from src.string_utils import has_number

class TestHasNumber(unittest.TestCase):
    """
    Unit tests for the `has_number` function in `src/string_utils.py`.
    """

    def test_string_with_number(self):
        """
        Test case for strings containing at least one digit.
        Expected: True
        """
        self.assertTrue(has_number("hello1world"))
        self.assertTrue(has_number("abc-123-xyz"))
        self.assertTrue(has_number("version_2.0"))
        self.assertTrue(has_number("price: $10.99"))

    def test_string_with_only_numbers(self):
        """
        Test case for strings consisting entirely of digits.
        Expected: True
        """
        self.assertTrue(has_number("12345"))
        self.assertTrue(has_number("0"))
        self.assertTrue(has_number("9876543210"))

    def test_string_without_number(self):
        """
        Test case for strings containing no digits.
        Expected: False
        """
        self.assertFalse(has_number("helloworld"))
        self.assertFalse(has_number("no_numbers_here"))
        self.assertFalse(has_number("!@#$%^&*()_+-="))
        self.assertFalse(has_number("All alphabetic characters"))

    def test_empty_string(self):
        """
        Test case for an empty string.
        Expected: False
        """
        self.assertFalse(has_number(""))

    def test_string_with_whitespace_and_no_number(self):
        """
        Test case for a string containing only whitespace.
        Expected: False
        """
        self.assertFalse(has_number("   "))
        self.assertFalse(has_number("\t\n\r"))

    def test_string_with_number_at_start(self):
        """
        Test case for a string where a number appears at the very beginning.
        Expected: True
        """
        self.assertTrue(has_number("1start"))
        self.assertTrue(has_number("0.5alpha"))

    def test_string_with_number_at_end(self):
        """
        Test case for a string where a number appears at the very end.
        Expected: True
        """
        self.assertTrue(has_number("end1"))
        self.assertTrue(has_number("beta_1.0"))

    def test_string_with_unicode_digits(self):
        """
        Test case for strings containing unicode digits (e.g., full-width digits).
        Expected: True
        """
        # Test basic ASCII digits first for completeness, though already covered
        self.assertTrue(has_number("abc123def"))
        # Test some non-ASCII digits if the function is expected to handle them
        # Note: The `isdigit()` method generally handles Unicode digits.
        self.assertTrue(has_number("１２３ full-width digits")) # Full-width digits
        self.assertTrue(has_number("٠١٢٣٤٥٦٧٨٩ Arabic-Indic digits")) # Arabic-Indic digits

    def test_non_string_input(self):
        """
        Test cases for non-string inputs to ensure graceful handling or type errors.
        Note: The `has_number` function is expected to operate on strings.
        If it does not raise an error for non-string inputs, it might be
        designed to return False or handle it in another way.
        Assuming `has_number` expects a string and might raise TypeError
        or implicitly handle it (e.g., if it uses str.isdigit() directly,
        it would raise an AttributeError on non-string).

        A robust `has_number` function should either ensure input type or
        handle non-string inputs explicitly. If the function itself
        does not validate type, testing for expected `TypeError` is good.
        If it's assumed to only receive strings, this test might be removed
        or adapted based on `src/string_utils.py`'s actual implementation
        and contract.

        For this context, we will assume `has_number` expects a string
        and if a non-string is passed, it should raise a TypeError
        (or fail in a similar manner due to method calls on non-string objects).
        """
        with self.assertRaises(TypeError):
            has_number(None)
        with self.assertRaises(TypeError):
            has_number(123)
        with self.assertRaises(TypeError):
            has_number(['a', '1', 'b'])
        with self.assertRaises(TypeError):
            has_number({'key': 1})

if __name__ == '__main__':
    unittest.main()