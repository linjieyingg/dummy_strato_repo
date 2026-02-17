import unittest
import sys
import os

# Add the src directory to the Python path to allow importing math_utils
# This assumes a directory structure like:
# project_root/
# ├── src/
# │   └── utils/
# │       └── math_utils.py
# └── tests/
#     └── test_math_utils.py
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src', 'utils')))
from math_utils import round_number_to_place


class TestRoundNumberToPlace(unittest.TestCase):
    """
    Comprehensive unit tests for the round_number_to_place function in src/utils/math_utils.py.
    Covers various positive/negative numbers, different rounding places (integer and decimal),
    edge cases like values ending in .5 (to verify Python's round-half-to-even behavior),
    and proper error handling for invalid place inputs.
    """

    def test_positive_numbers(self):
        """Test rounding positive numbers to various decimal places."""
        self.assertEqual(round_number_to_place(3.14159, 2), 3.14)
        self.assertEqual(round_number_to_place(123.456, 1), 123.5)
        self.assertEqual(round_number_to_place(100.0001, 3), 100.000)
        self.assertEqual(round_number_to_place(0.00000001, 5), 0.00000)
        self.assertEqual(round_number_to_place(123.0, 0), 123)
        self.assertEqual(round_number_to_place(123, 0), 123)

    def test_negative_numbers(self):
        """Test rounding negative numbers to various decimal places."""
        self.assertEqual(round_number_to_place(-3.14159, 2), -3.14)
        self.assertEqual(round_number_to_place(-123.456, 1), -123.5)
        self.assertEqual(round_number_to_place(-100.0001, 3), -100.000)
        self.assertEqual(round_number_to_place(-0.00000001, 5), -0.00000)
        self.assertEqual(round_number_to_place(-123.0, 0), -123)
        self.assertEqual(round_number_to_place(-123, 0), -123)

    def test_round_half_to_even_behavior(self):
        """
        Test cases specifically for Python's round-half-to-even behavior
        for values ending exactly in .5 (or equivalent in higher decimal places).
        """
        # Rounding to 0 decimal places
        self.assertEqual(round_number_to_place(2.5, 0), 2)  # 2 is even
        self.assertEqual(round_number_to_place(3.5, 0), 4)  # 4 is even
        self.assertEqual(round_number_to_place(-2.5, 0), -2) # -2 is even
        self.assertEqual(round_number_to_place(-3.5, 0), -4) # -4 is even

        # Rounding to 1 decimal place
        self.assertEqual(round_number_to_place(2.15, 1), 2.2) # 2.1_ (1 is odd) -> 2.2
        self.assertEqual(round_number_to_place(2.25, 1), 2.2) # 2.2_ (2 is even) -> 2.2
        self.assertEqual(round_number_to_place(2.35, 1), 2.4) # 2.3_ (3 is odd) -> 2.4
        self.assertEqual(round_number_to_place(2.45, 1), 2.4) # 2.4_ (4 is even) -> 2.4
        self.assertEqual(round_number_to_place(-2.15, 1), -2.2)
        self.assertEqual(round_number_to_place(-2.25, 1), -2.2)

    def test_zero_and_no_rounding_needed(self):
        """Test rounding zero and numbers where no decimal adjustment is required."""
        self.assertEqual(round_number_to_place(0.0, 2), 0.0)
        self.assertEqual(round_number_to_place(0, 0), 0)
        self.assertEqual(round_number_to_place(100.0, 2), 100.0)
        self.assertEqual(round_number_to_place(100, 2), 100.0)
        self.assertEqual(round_number_to_place(1.23, 5), 1.23) # More places than available decimals

    def test_different_positive_places(self):
        """Test with various positive integer rounding places."""
        self.assertEqual(round_number_to_place(123.456789, 0), 123)
        self.assertEqual(round_number_to_place(123.456789, 1), 123.5)
        self.assertEqual(round_number_to_place(123.456789, 3), 123.457)
        self.assertEqual(round_number_to_place(123.456789, 5), 123.45679)
        self.assertEqual(round_number_to_place(9.99999, 2), 10.00) # Check carrying over

    def test_negative_place_values(self):
        """
        Test rounding to tens, hundreds, etc., using negative 'place' values.
        This behavior mimics Python's built-in round() function.
        """
        self.assertEqual(round_number_to_place(1234.56, -1), 1230.0)
        self.assertEqual(round_number_to_place(1256.78, -2), 1300.0)
        self.assertEqual(round_number_to_place(1250.0, -2), 1200.0) # 1250 is halfway between 1200 (even) and 1300 (odd)
        self.assertEqual(round_number_to_place(1150.0, -2), 1200.0) # 1150 is halfway between 1100 (odd) and 1200 (even)
        self.assertEqual(round_number_to_place(789.0, -2), 800.0)
        self.assertEqual(round_number_to_place(-1234.56, -1), -1230.0)
        self.assertEqual(round_number_to_place(-1250.0, -2), -1200.0)
        self.assertEqual(round_number_to_place(55.0, -1), 60.0) # 55 is halfway between 50 (odd) and 60 (even)

    def test_invalid_number_input_type(self):
        """Test error handling for non-numeric 'number' input."""
        with self.assertRaises(TypeError, msg="Should raise TypeError for string 'number'"):
            round_number_to_place("abc", 2)
        with self.assertRaises(TypeError, msg="Should raise TypeError for list 'number'"):
            round_number_to_place([1, 2], 2)
        with self.assertRaises(TypeError, msg="Should raise TypeError for None 'number'"):
            round_number_to_place(None, 2)

    def test_invalid_place_input_type(self):
        """Test error handling for non-integer 'place' input."""
        with self.assertRaises(TypeError, msg="Should raise TypeError for float 'place'"):
            round_number_to_place(3.14, 1.5)
        with self.assertRaises(TypeError, msg="Should raise TypeError for string 'place'"):
            round_number_to_place(3.14, "two")
        with self.assertRaises(TypeError, msg="Should raise TypeError for None 'place'"):
            round_number_to_place(3.14, None)


if __name__ == '__main__':
    unittest.main()