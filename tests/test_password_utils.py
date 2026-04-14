import unittest
from src.utils.password_utils import has_number

class TestPasswordUtils(unittest.TestCase):
    """
    Unit tests for the password utility functions in src/utils/password_utils.py.
    """

    def test_has_number_with_number(self):
        """
        Test cases where the string contains at least one digit.
        """
        self.assertTrue(has_number("password123"))
        self.assertTrue(has_number("123password"))
        self.assertTrue(has_number("p@ssw0rd!"))
        self.assertTrue(has_number("0"))
        self.assertTrue(has_number("99"))
        self.assertTrue(has_number("hello world 7"))

    def test_has_number_without_number(self):
        """
        Test cases where the string does not contain any digits.
        """
        self.assertFalse(has_number("password"))
        self.assertFalse(has_number("PYTHON"))
        self.assertFalse(has_number("!@#$%^&*()"))
        self.assertFalse(has_number("abc-def_ghi"))
        self.assertFalse(has_number(""))
        self.assertFalse(has_number(" "))
        self.assertFalse(has_number("   "))

    def test_has_number_with_mixed_characters(self):
        """
        Test cases with a mix of letters, symbols, and numbers.
        """
        self.assertTrue(has_number("P@ssw0rd!"))
        self.assertTrue(has_number("User_1_Password"))
        self.assertFalse(has_number("!@#$abcD"))

    def test_has_number_with_non_string_inputs(self):
        """
        Test cases with non-string inputs to ensure robustness.
        Assuming has_number raises a TypeError for non-string inputs.
        """
        with self.assertRaises(TypeError):
            has_number(None)
        with self.assertRaises(TypeError):
            has_number(123)
        with self.assertRaises(TypeError):
            has_number(['1', '2', '3'])
        with self.assertRaises(TypeError):
            has_number({'key': 'value1'})


if __name__ == '__main__':
    unittest.main()