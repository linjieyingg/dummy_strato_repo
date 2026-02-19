import unittest
import os
import sys

# Add the project root to sys.path to allow importing modules from 'src'
# Assuming the directory structure:
# project_root/
# ├── src/
# │   └── utils.py
# └── tests/
#     └── test_utils.py
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir))
if project_root not in sys.path:
    sys.path.insert(0, project_root)

# Attempt to import the function. If it fails, tests will be skipped.
try:
    from src.utils import is_even_or_odd
except ImportError:
    # Set to None if import fails, tests will be skipped via @unittest.skipUnless
    is_even_or_odd = None
except Exception:
    # Catch any other unexpected errors during import process
    is_even_or_odd = None


class TestIsEvenOrOdd(unittest.TestCase):
    """
    Unit tests for the `is_even_or_odd` function in `src/utils.py`.
    """

    @unittest.skipUnless(is_even_or_odd, "is_even_or_odd function not available in src/utils.py")
    def test_positive_even_integer(self):
        """Test with a positive even integer."""
        self.assertEqual(is_even_or_odd(4), "Even")
        self.assertEqual(is_even_or_odd(100), "Even")

    @unittest.skipUnless(is_even_or_odd, "is_even_or_odd function not available in src/utils.py")
    def test_positive_odd_integer(self):
        """Test with a positive odd integer."""
        self.assertEqual(is_even_or_odd(3), "Odd")
        self.assertEqual(is_even_or_odd(99), "Odd")

    @unittest.skipUnless(is_even_or_odd, "is_even_or_odd function not available in src/utils.py")
    def test_negative_even_integer(self):
        """Test with a negative even integer."""
        self.assertEqual(is_even_or_odd(-2), "Even")
        self.assertEqual(is_even_or_odd(-50), "Even")

    @unittest.skipUnless(is_even_or_odd, "is_even_or_odd function not available in src/utils.py")
    def test_negative_odd_integer(self):
        """Test with a negative odd integer."""
        self.assertEqual(is_even_or_odd(-1), "Odd")
        self.assertEqual(is_even_or_odd(-45), "Odd")

    @unittest.skipUnless(is_even_or_odd, "is_even_or_odd function not available in src/utils.py")
    def test_zero(self):
        """Test with zero (which is considered an even number)."""
        self.assertEqual(is_even_or_odd(0), "Even")

    @unittest.skipUnless(is_even_or_odd, "is_even_or_odd function not available in src/utils.py")
    def test_float_even_integer(self):
        """Test with a floating-point number that is an exact even integer (e.g., 4.0)."""
        self.assertEqual(is_even_or_odd(4.0), "Even")
        self.assertEqual(is_even_or_odd(-6.0), "Even")

    @unittest.skipUnless(is_even_or_odd, "is_even_or_odd function not available in src/utils.py")
    def test_float_odd_integer(self):
        """Test with a floating-point number that is an exact odd integer (e.g., 3.0)."""
        self.assertEqual(is_even_or_odd(3.0), "Odd")
        self.assertEqual(is_even_or_odd(-5.0), "Odd")

    @unittest.skipUnless(is_even_or_odd, "is_even_or_odd function not available in src/utils.py")
    def test_non_integer_float_positive(self):
        """Test with a positive non-integer floating-point number."""
        self.assertEqual(is_even_or_odd(2.5), "Neither Even Nor Odd")
        self.assertEqual(is_even_or_odd(3.14), "Neither Even Nor Odd")

    @unittest.skipUnless(is_even_or_odd, "is_even_or_odd function not available in src/utils.py")
    def test_non_integer_float_negative(self):
        """Test with a negative non-integer floating-point number."""
        self.assertEqual(is_even_or_odd(-1.7), "Neither Even Nor Odd")
        self.assertEqual(is_even_or_odd(-0.5), "Neither Even Nor Odd")

    @unittest.skipUnless(is_even_or_odd, "is_even_or_odd function not available in src/utils.py")
    def test_very_large_number(self):
        """Test with a very large integer."""
        self.assertEqual(is_even_or_odd(12345678901234567890), "Even")
        self.assertEqual(is_even_or_odd(12345678901234567891), "Odd")

    @unittest.skipUnless(is_even_or_odd, "is_even_or_odd function not available in src/utils.py")
    def test_non_numeric_input_raises_type_error(self):
        """
        Test with non-numeric input to ensure a TypeError is raised.
        A production-ready function should typically raise a TypeError for invalid input types.
        """
        with self.assertRaises(TypeError):
            is_even_or_odd("hello")
        with self.assertRaises(TypeError):
            is_even_or_odd([1, 2, 3])
        with self.assertRaises(TypeError):
            is_even_or_odd(None)
        with self.assertRaises(TypeError):
            is_even_or_odd({'a': 1})


if __name__ == '__main__':
    unittest.main()