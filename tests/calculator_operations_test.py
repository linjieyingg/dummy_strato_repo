import unittest
import math
from src.calculator.operations import add, subtract, multiply, divide, _validate_numeric_input

class TestCalculatorOperations(unittest.TestCase):
    """
    Unit tests for the arithmetic operations defined in src/calculator/operations.py.

    This test suite covers various scenarios including:
    - Valid positive and negative integer/float inputs.
    - Operations involving zero.
    - Large number inputs.
    - Error conditions like division by zero.
    - Type errors for non-numeric inputs.
    """

    # --- Test cases for _validate_numeric_input helper (internal but good to test) ---
    def test_validate_numeric_input_valid(self):
        """Test _validate_numeric_input with valid numeric types."""
        try:
            _validate_numeric_input(10, 'a')
            _validate_numeric_input(10.5, 'b')
            _validate_numeric_input(-5, 'c')
            _validate_numeric_input(0.0, 'd')
        except TypeError:
            self.fail("_validate_numeric_input raised TypeError unexpectedly.")

    def test_validate_numeric_input_invalid(self):
        """Test _validate_numeric_input with invalid non-numeric types."""
        invalid_inputs = [
            ("hello", 'a'),
            ([1, 2], 'b'),
            ({'key': 'value'}, 'c'),
            (None, 'd'),
            (True, 'e') # Booleans are technically ints but often not desired for general numeric ops
        ]

        for value, param_name in invalid_inputs:
            with self.assertRaisesRegex(TypeError, f"'{param_name}' must be a numeric value \\(int or float\\)."):
                _validate_numeric_input(value, param_name)

    # --- Test cases for add function ---
    def test_add_positive_integers(self):
        """Test add with two positive integers."""
        self.assertEqual(add(5, 3), 8)
        self.assertEqual(add(100, 200), 300)

    def test_add_positive_floats(self):
        """Test add with two positive floats."""
        self.assertAlmostEqual(add(0.1, 0.2), 0.3)
        self.assertAlmostEqual(add(1.5, 2.7), 4.2)

    def test_add_mixed_integers_floats(self):
        """Test add with mixed integer and float inputs."""
        self.assertAlmostEqual(add(5, 3.5), 8.5)
        self.assertAlmostEqual(add(0.5, 10), 10.5)

    def test_add_negative_numbers(self):
        """Test add with negative integers and floats."""
        self.assertEqual(add(-5, -3), -8)
        self.assertAlmostEqual(add(-1.5, -2.5), -4.0)
        self.assertEqual(add(10, -3), 7)
        self.assertAlmostEqual(add(-7.5, 2.5), -5.0)

    def test_add_with_zero(self):
        """Test add when one or both inputs are zero."""
        self.assertEqual(add(5, 0), 5)
        self.assertEqual(add(0, 3.5), 3.5)
        self.assertEqual(add(0, 0), 0)
        self.assertEqual(add(-10, 0), -10)

    def test_add_large_numbers(self):
        """Test add with large numeric inputs."""
        self.assertEqual(add(10**9, 2*10**9), 3*10**9)
        self.assertAlmostEqual(add(1.23e20, 4.56e20), 5.79e20)

    def test_add_non_numeric_input_a(self):
        """Test add raises TypeError for non-numeric 'a'."""
        with self.assertRaisesRegex(TypeError, "'a' must be a numeric value \\(int or float\\)."):
            add("hello", 5)
        with self.assertRaisesRegex(TypeError, "'a' must be a numeric value \\(int or float\\)."):
            add([1], 5)

    def test_add_non_numeric_input_b(self):
        """Test add raises TypeError for non-numeric 'b'."""
        with self.assertRaisesRegex(TypeError, "'b' must be a numeric value \\(int or float\\)."):
            add(5, "world")
        with self.assertRaisesRegex(TypeError, "'b' must be a numeric value \\(int or float\\)."):
            add(5, None)

    # --- Test cases for subtract function ---
    def test_subtract_positive_integers(self):
        """Test subtract with two positive integers."""
        self.assertEqual(subtract(10, 3), 7)
        self.assertEqual(subtract(3, 10), -7)

    def test_subtract_positive_floats(self):
        """Test subtract with two positive floats."""
        self.assertAlmostEqual(subtract(5.5, 2.3), 3.2)
        self.assertAlmostEqual(subtract(2.3, 5.5), -3.2)

    def test_subtract_mixed_integers_floats(self):
        """Test subtract with mixed integer and float inputs."""
        self.assertAlmostEqual(subtract(10, 3.5), 6.5)
        self.assertAlmostEqual(subtract(3.5, 10), -6.5)

    def test_subtract_negative_numbers(self):
        """Test subtract with negative integers and floats."""
        self.assertEqual(subtract(-5, -3), -2)
        self.assertAlmostEqual(subtract(-1.5, -2.5), 1.0)
        self.assertEqual(subtract(10, -3), 13)
        self.assertAlmostEqual(subtract(-7.5, 2.5), -10.0)

    def test_subtract_with_zero(self):
        """Test subtract when one or both inputs are zero."""
        self.assertEqual(subtract(5, 0), 5)
        self.assertEqual(subtract(0, 3.5), -3.5)
        self.assertEqual(subtract(0, 0), 0)
        self.assertEqual(subtract(-10, 0), -10)

    def test_subtract_large_numbers(self):
        """Test subtract with large numeric inputs."""
        self.assertEqual(subtract(3*10**9, 10**9), 2*10**9)
        self.assertAlmostEqual(subtract(4.56e20, 1.23e20), 3.33e20)

    def test_subtract_non_numeric_input_a(self):
        """Test subtract raises TypeError for non-numeric 'a'."""
        with self.assertRaisesRegex(TypeError, "'a' must be a numeric value \\(int or float\\)."):
            subtract("test", 10)

    def test_subtract_non_numeric_input_b(self):
        """Test subtract raises TypeError for non-numeric 'b'."""
        with self.assertRaisesRegex(TypeError, "'b' must be a numeric value \\(int or float\\)."):
            subtract(10, "test")

    # --- Test cases for multiply function ---
    def test_multiply_positive_integers(self):
        """Test multiply with two positive integers."""
        self.assertEqual(multiply(5, 3), 15)
        self.assertEqual(multiply(10, 0), 0)

    def test_multiply_positive_floats(self):
        """Test multiply with two positive floats."""
        self.assertAlmostEqual(multiply(2.5, 2.0), 5.0)
        self.assertAlmostEqual(multiply(0.1, 0.2), 0.02)

    def test_multiply_mixed_integers_floats(self):
        """Test multiply with mixed integer and float inputs."""
        self.assertAlmostEqual(multiply(5, 2.5), 12.5)
        self.assertAlmostEqual(multiply(1.5, 4), 6.0)

    def test_multiply_negative_numbers(self):
        """Test multiply with negative numbers."""
        self.assertEqual(multiply(-5, 3), -15)
        self.assertEqual(multiply(5, -3), -15)
        self.assertEqual(multiply(-5, -3), 15)
        self.assertAlmostEqual(multiply(-2.5, 2.0), -5.0)
        self.assertAlmostEqual(multiply(-2.5, -2.0), 5.0)

    def test_multiply_by_zero(self):
        """Test multiply when one or both inputs are zero."""
        self.assertEqual(multiply(10, 0), 0)
        self.assertEqual(multiply(0, 7.5), 0)
        self.assertEqual(multiply(0, 0), 0)
        self.assertEqual(multiply(-10, 0), 0)

    def test_multiply_large_numbers(self):
        """Test multiply with large numeric inputs."""
        self.assertEqual(multiply(10**9, 2), 2*10**9)
        self.assertAlmostEqual(multiply(1.2e10, 2.0e10), 2.4e20)

    def test_multiply_non_numeric_input_a(self):
        """Test multiply raises TypeError for non-numeric 'a'."""
        with self.assertRaisesRegex(TypeError, "'a' must be a numeric value \\(int or float\\)."):
            multiply("factor", 5)

    def test_multiply_non_numeric_input_b(self):
        """Test multiply raises TypeError for non-numeric 'b'."""
        with self.assertRaisesRegex(TypeError, "'b' must be a numeric value \\(int or float\\)."):
            multiply(5, "factor")

    # --- Test cases for divide function ---
    def test_divide_positive_integers(self):
        """Test divide with two positive integers."""
        self.assertEqual(divide(10, 2), 5.0)
        self.assertAlmostEqual(divide(7, 2), 3.5)

    def test_divide_positive_floats(self):
        """Test divide with two positive floats."""
        self.assertAlmostEqual(divide(5.0, 2.0), 2.5)
        self.assertAlmostEqual(divide(0.3, 0.1), 3.0)

    def test_divide_mixed_integers_floats(self):
        """Test divide with mixed integer and float inputs."""
        self.assertAlmostEqual(divide(10, 2.5), 4.0)
        self.assertAlmostEqual(divide(7.0, 2), 3.5)

    def test_divide_negative_numbers(self):
        """Test divide with negative numbers."""
        self.assertEqual(divide(-10, 2), -5.0)
        self.assertEqual(divide(10, -2), -5.0)
        self.assertEqual(divide(-10, -2), 5.0)
        self.assertAlmostEqual(divide(-7.5, 2.5), -3.0)

    def test_divide_by_one(self):
        """Test divide by one."""
        self.assertEqual(divide(5, 1), 5.0)
        self.assertAlmostEqual(divide(3.14, 1), 3.14)

    def test_divide_zero_by_number(self):
        """Test divide with dividend as zero."""
        self.assertEqual(divide(0, 5), 0.0)
        self.assertEqual(divide(0, -5.5), 0.0)

    def test_divide_by_zero_error(self):
        """Test divide raises ZeroDivisionError when divisor is zero."""
        with self.assertRaisesRegex(ZeroDivisionError, "Cannot divide by zero."):
            divide(10, 0)
        with self.assertRaisesRegex(ZeroDivisionError, "Cannot divide by zero."):
            divide(-5, 0)
        with self.assertRaisesRegex(ZeroDivisionError, "Cannot divide by zero."):
            divide(0, 0) # This is usually undefined, but Python's division raises ZeroDivisionError

    def test_divide_large_numbers(self):
        """Test divide with large numeric inputs."""
        self.assertEqual(divide(10**9, 1000), 10**6)
        self.assertAlmostEqual(divide(1.2e20, 2.0e10), 6.0e9)

    def test_divide_non_numeric_input_a(self):
        """Test divide raises TypeError for non-numeric 'a'."""
        with self.assertRaisesRegex(TypeError, "'a' must be a numeric value \\(int or float\\)."):
            divide("dividend", 2)

    def test_divide_non_numeric_input_b(self):
        """Test divide raises TypeError for non-numeric 'b'."""
        with self.assertRaisesRegex(TypeError, "'b' must be a numeric value \\(int or float\\)."):
            divide(10, "divisor")


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)