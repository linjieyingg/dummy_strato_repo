import unittest
import sys
import os

# Add the 'src' directory to the Python path for importing modules.
# This ensures that imports like 'from src.number_utils import ...' work correctly
# when running tests, especially if the current working directory is not the project root.
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Import the function to be tested from src.number_utils
# This assumes that 'check_number_sign' function will be implemented within this module.
from src.number_utils import check_number_sign


class TestCheckNumberSign(unittest.TestCase):
    """
    Test suite for the `check_number_sign` function in `src.number_utils`.

    This class provides comprehensive unit tests to ensure that `check_number_sign`
    correctly identifies the sign of various numeric inputs (positive, negative, zero)
    and robustly handles invalid input types by raising a TypeError.
    """

    def test_positive_number(self):
        """
        Tests that `check_number_sign` correctly identifies positive integers and floats.
        """
        self.assertEqual(check_number_sign(5), "positive")
        self.assertEqual(check_number_sign(5.0), "positive")
        self.assertEqual(check_number_sign(123456789), "positive")
        self.assertEqual(check_number_sign(0.0001), "positive")
        self.assertEqual(check_number_sign(1e100), "positive")  # Large float
        self.assertEqual(check_number_sign(sys.maxsize), "positive") # Max integer


    def test_negative_number(self):
        """
        Tests that `check_number_sign` correctly identifies negative integers and floats.
        """
        self.assertEqual(check_number_sign(-5), "negative")
        self.assertEqual(check_number_sign(-5.0), "negative")
        self.assertEqual(check_number_sign(-987654321), "negative")
        self.assertEqual(check_number_sign(-0.0001), "negative")
        self.assertEqual(check_number_sign(-1e-50), "negative")  # Small negative float
        self.assertEqual(check_number_sign(-sys.maxsize - 1), "negative") # Min integer


    def test_zero(self):
        """
        Tests that `check_number_sign` correctly identifies zero for both integer and float inputs.
        """
        self.assertEqual(check_number_sign(0), "zero")
        self.assertEqual(check_number_sign(0.0), "zero")
        self.assertEqual(check_number_sign(-0.0), "zero") # Negative zero should also be "zero"


    def test_invalid_input_type(self):
        """
        Tests that `check_number_sign` raises a `TypeError` for non-numeric inputs.

        Based on the existing `is_even_or_odd` function's summary in `src/number_utils.py`
        (which indicates strict type validation for `int` or `float`),
        we expect `check_number_sign` to follow a similar pattern and reject
        types like strings, lists, dictionaries, None, and booleans as valid numbers for sign checking.
        """
        with self.assertRaises(TypeError, msg="Should raise TypeError for string input"):
            check_number_sign("hello")
        with self.assertRaises(TypeError, msg="Should raise TypeError for list input"):
            check_number_sign([1, 2, 3])
        with self.assertRaises(TypeError, msg="Should raise TypeError for dict input"):
            check_number_sign({'key': 'value'})
        with self.assertRaises(TypeError, msg="Should raise TypeError for None input"):
            check_number_sign(None)
        with self.assertRaises(TypeError, msg="Should raise TypeError for True (boolean) input"):
            check_number_sign(True)  # Booleans are subclasses of int, but often treated as distinct for strict validation
        with self.assertRaises(TypeError, msg="Should raise TypeError for False (boolean) input"):
            check_number_sign(False)


if __name__ == '__main__':
    unittest.main()