import unittest
import sys
import os

# Add the 'src' directory to the Python path to allow importing number_utils
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

try:
    from number_utils import is_even_or_odd
except ImportError:
    # This block handles the case where src/number_utils.py or is_even_or_odd is not found.
    # For a production setup, this would typically mean a missing dependency or incorrect path.
    # For testing purposes, we'll create a mock function or raise an error to indicate the issue.
    print("Warning: Could not import 'is_even_or_odd' from 'src/number_utils.py'.")
    print("Please ensure 'src/number_utils.py' exists and contains the 'is_even_or_odd' function.")

    # Define a placeholder or raise an error to prevent test execution errors
    def is_even_or_odd(number):
        """
        A placeholder function for testing purposes if the actual module is not found.
        This allows tests to run and potentially fail in a controlled manner,
        highlighting the missing dependency.
        """
        raise NotImplementedError("is_even_or_odd function not found in src/number_utils.py")


class TestNumberUtils(unittest.TestCase):
    """
    Unit tests for the number_utils.py module, specifically focusing on the
    is_even_or_odd function.
    """

    def test_even_numbers(self):
        """
        Test cases for various even integer inputs.
        """
        self.assertEqual(is_even_or_odd(2), "Even", "Should return 'Even' for 2")
        self.assertEqual(is_even_or_odd(0), "Even", "Should return 'Even' for 0")
        self.assertEqual(is_even_or_odd(100), "Even", "Should return 'Even' for 100")
        self.assertEqual(is_even_or_odd(-4), "Even", "Should return 'Even' for -4")

    def test_odd_numbers(self):
        """
        Test cases for various odd integer inputs.
        """
        self.assertEqual(is_even_or_odd(1), "Odd", "Should return 'Odd' for 1")
        self.assertEqual(is_even_or_odd(7), "Odd", "Should return 'Odd' for 7")
        self.assertEqual(is_even_or_odd(-3), "Odd", "Should return 'Odd' for -3")
        self.assertEqual(is_even_or_odd(99), "Odd", "Should return 'Odd' for 99")

    def test_non_integer_inputs(self):
        """
        Test cases for non-integer inputs, expecting a TypeError.
        Assumes is_even_or_odd raises TypeError for non-integer inputs.
        """
        with self.assertRaises(TypeError, msg="Should raise TypeError for float input"):
            is_even_or_odd(2.5)
        with self.assertRaises(TypeError, msg="Should raise TypeError for string input"):
            is_even_or_odd("hello")
        with self.assertRaises(TypeError, msg="Should raise TypeError for list input"):
            is_even_or_odd([1, 2])
        with self.assertRaises(TypeError, msg="Should raise TypeError for None input"):
            is_even_or_odd(None)

    def test_large_numbers(self):
        """
        Test cases for large integer inputs.
        """
        self.assertEqual(is_even_or_odd(1234567890), "Even", "Should return 'Even' for large even number")
        self.assertEqual(is_even_or_odd(987654321), "Odd", "Should return 'Odd' for large odd number")
        self.assertEqual(is_even_or_odd(-111222333444555666), "Even", "Should return 'Even' for large negative even number")
        self.assertEqual(is_even_or_odd(-777888999000111223), "Odd", "Should return 'Odd' for large negative odd number")


if __name__ == '__main__':
    unittest.main()