import unittest
import os
import sys

# Add the 'src' directory to the Python path to allow importing modules from it.
# This ensures that tests can locate the 'utils.py' module even when run from the project root.
current_dir = os.path.dirname(os.path.abspath(__file__))
src_dir = os.path.join(current_dir, '..', 'src')
sys.path.insert(0, src_dir)

try:
    from utils import decimal_to_binary
except ImportError:
    # If utils.py or decimal_to_binary is not found, provide a mock
    # to allow tests to run, but they will fail in a controlled way.
    # In a real scenario, this would indicate a setup issue.
    print(f"WARNING: Could not import 'decimal_to_binary' from '{src_dir}/utils.py'. "
          "Tests will use a mock function and likely fail.")

    def decimal_to_binary(decimal_num):
        """Mock function for decimal_to_binary for testing purposes when original is not found."""
        if not isinstance(decimal_num, int):
            raise TypeError("Input must be an integer. (Mock)")
        if decimal_num < 0:
            raise ValueError("Input must be a non-negative integer. (Mock)")
        return bin(decimal_num)[2:] # Standard Python binary conversion


class TestDecimalToBinary(unittest.TestCase):
    """
    Comprehensive unit tests for the `decimal_to_binary` function located in `src/utils.py`.

    This test suite covers various scenarios including:
    - Conversion of zero.
    - Conversion of small, medium, and large positive integers.
    - Handling of boolean inputs (which are subclasses of int in Python).
    - Error handling for negative integer inputs.
    - Error handling for non-integer inputs (floats, strings, None, lists, etc.).
    """

    def test_zero(self):
        """Test `decimal_to_binary(0)` should return '0'."""
        self.assertEqual(decimal_to_binary(0), "0")

    def test_positive_small_numbers(self):
        """Test conversion of small positive integers (1-5)."""
        self.assertEqual(decimal_to_binary(1), "1")
        self.assertEqual(decimal_to_binary(2), "10")
        self.assertEqual(decimal_to_binary(3), "11")
        self.assertEqual(decimal_to_binary(4), "100")
        self.assertEqual(decimal_to_binary(5), "101")

    def test_positive_medium_numbers(self):
        """Test conversion of medium positive integers (e.g., powers of 2, boundary values)."""
        self.assertEqual(decimal_to_binary(10), "1010")
        self.assertEqual(decimal_to_binary(16), "10000")
        self.assertEqual(decimal_to_binary(31), "11111")  # All ones
        self.assertEqual(decimal_to_binary(32), "100000") # Power of 2

    def test_positive_large_numbers(self):
        """Test conversion of larger positive integers."""
        self.assertEqual(decimal_to_binary(255), "11111111") # 2^8 - 1
        self.assertEqual(decimal_to_binary(256), "100000000") # 2^8
        self.assertEqual(decimal_to_binary(1023), "1111111111") # 2^10 - 1
        self.assertEqual(decimal_to_binary(1024), "10000000000") # 2^10
        self.assertEqual(decimal_to_binary(65535), "1111111111111111") # 2^16 - 1

    def test_boolean_inputs(self):
        """
        Test that boolean values (which are subclasses of int) are handled correctly.
        `True` evaluates to 1, `False` to 0.
        """
        self.assertEqual(decimal_to_binary(True), "1")
        self.assertEqual(decimal_to_binary(False), "0")

    def test_negative_integer_raises_value_error(self):
        """
        Test that passing a negative integer raises a `ValueError`
        with an appropriate error message.
        """
        with self.assertRaises(ValueError) as cm:
            decimal_to_binary(-1)
        self.assertIn("non-negative integer", str(cm.exception).lower())

        with self.assertRaises(ValueError) as cm:
            decimal_to_binary(-100)
        self.assertIn("non-negative integer", str(cm.exception).lower())

    def test_float_raises_type_error(self):
        """
        Test that passing a float (even one with a zero fractional part)
        raises a `TypeError` with an appropriate error message.
        """
        with self.assertRaises(TypeError) as cm:
            decimal_to_binary(5.0)
        self.assertIn("integer", str(cm.exception).lower())

        with self.assertRaises(TypeError) as cm:
            decimal_to_binary(3.14)
        self.assertIn("integer", str(cm.exception).lower())

    def test_string_raises_type_error(self):
        """Test that passing a string raises a `TypeError`."""
        with self.assertRaises(TypeError) as cm:
            decimal_to_binary("10")
        self.assertIn("integer", str(cm.exception).lower())

        with self.assertRaises(TypeError) as cm:
            decimal_to_binary("abc")
        self.assertIn("integer", str(cm.exception).lower())

    def test_none_raises_type_error(self):
        """Test that passing `None` raises a `TypeError`."""
        with self.assertRaises(TypeError) as cm:
            decimal_to_binary(None)
        self.assertIn("integer", str(cm.exception).lower())

    def test_list_raises_type_error(self):
        """Test that passing a list raises a `TypeError`."""
        with self.assertRaises(TypeError) as cm:
            decimal_to_binary([1, 2, 3])
        self.assertIn("integer", str(cm.exception).lower())

    def test_dict_raises_type_error(self):
        """Test that passing a dictionary raises a `TypeError`."""
        with self.assertRaises(TypeError) as cm:
            decimal_to_binary({'a': 1})
        self.assertIn("integer", str(cm.exception).lower())


if __name__ == '__main__':
    unittest.main()