import unittest
from src.calculator_logic import add, subtract, multiply, divide

class TestCalculatorLogic(unittest.TestCase):
    """
    Comprehensive test suite for the functions defined in `src/calculator_logic.py`.
    This includes testing valid positive/negative integers and floats, large numbers,
    and non-numeric input types for `add`, `subtract`, `multiply`, and `divide` functions.
    """

    # --- Test cases for add function ---

    def test_add_valid_positive_integers(self):
        """Test `add` with valid positive integer inputs."""
        self.assertEqual(add(5, 3), 8)
        self.assertEqual(add(100, 200), 300)
        self.assertEqual(add(1, 1), 2)

    def test_add_valid_negative_integers(self):
        """Test `add` with valid negative integer inputs."""
        self.assertEqual(add(-5, -3), -8)
        self.assertEqual(add(-10, -20), -30)
        self.assertEqual(add(-1, -1), -2)

    def test_add_valid_positive_floats(self):
        """Test `add` with valid positive float inputs."""
        self.assertAlmostEqual(add(5.5, 3.2), 8.7)
        self.assertAlmostEqual(add(0.1, 0.2), 0.3)
        self.assertAlmostEqual(add(1.0, 1.0), 2.0)

    def test_add_valid_negative_floats(self):
        """Test `add` with valid negative float inputs."""
        self.assertAlmostEqual(add(-5.5, -3.2), -8.7)
        self.assertAlmostEqual(add(-0.1, -0.2), -0.3)
        self.assertAlmostEqual(add(-1.0, -1.0), -2.0)

    def test_add_mixed_int_float(self):
        """Test `add` with mixed integer and float inputs."""
        self.assertAlmostEqual(add(5, 3.5), 8.5)
        self.assertAlmostEqual(add(3.5, 5), 8.5)
        self.assertAlmostEqual(add(-5, 3.5), -1.5)
        self.assertAlmostEqual(add(5.5, -3), 2.5)

    def test_add_with_zeros(self):
        """Test `add` with zero inputs (integer and float)."""
        self.assertEqual(add(5, 0), 5)
        self.assertEqual(add(0, 5), 5)
        self.assertEqual(add(0, 0), 0)
        self.assertAlmostEqual(add(5.5, 0.0), 5.5)
        self.assertAlmostEqual(add(0.0, 5.5), 5.5)
        self.assertAlmostEqual(add(-5.5, 0), -5.5)

    def test_add_large_numbers(self):
        """Test `add` with large numeric inputs (integers and floats)."""
        self.assertEqual(add(10**9, 2 * 10**9), 3 * 10**9)
        self.assertEqual(add(-10**10, -5 * 10**10), -6 * 10**10)
        self.assertAlmostEqual(add(1.2345e20, 6.7890e20), 8.0235e20)
        self.assertAlmostEqual(add(-1.2345e20, 6.7890e20), 5.5545e20)

    def test_add_non_numeric_a_type_error(self):
        """Verify that `add` raises TypeError for non-numeric 'a'."""
        with self.assertRaisesRegex(TypeError, "Input 'a' must be a numeric type \(int or float\)."):
            add("5", 3)
        with self.assertRaisesRegex(TypeError, "Input 'a' must be a numeric type \(int or float\)."):
            add([1, 2], 3)
        with self.assertRaisesRegex(TypeError, "Input 'a' must be a numeric type \(int or float\)."):
            add(None, 3)

    def test_add_non_numeric_b_type_error(self):
        """Verify that `add` raises TypeError for non-numeric 'b'."""
        with self.assertRaisesRegex(TypeError, "Input 'b' must be a numeric type \(int or float\)."):
            add(5, "3")
        with self.assertRaisesRegex(TypeError, "Input 'b' must be a numeric type \(int or float\)."):
            add(5, {"key": "value"})
        # False is considered numeric (int 0) and would not raise a TypeError.
        # Removing the problematic test case for False.
        with self.assertRaisesRegex(TypeError, "Input 'b' must be a numeric type \(int or float\)."):
            add(5, [1,2]) # This will trigger b non-numeric.

    def test_add_non_numeric_both_type_error(self):
        """Verify that `add` raises TypeError when both 'a' and 'b' are non-numeric."""
        # 'a' is checked first, so this should trigger 'a's error message
        with self.assertRaisesRegex(TypeError, "Input 'a' must be a numeric type \(int or float\)."):
            add("5", "3")
        with self.assertRaisesRegex(TypeError, "Input 'a' must be a numeric type \(int or float\)."):
            add(None, [])

    # --- Test cases for subtract function ---

    def test_subtract_valid_positive_integers(self):
        """Test `subtract` with valid positive integer inputs."""
        self.assertEqual(subtract(5, 3), 2)
        self.assertEqual(subtract(3, 5), -2)
        self.assertEqual(subtract(200, 100), 100)

    def test_subtract_valid_negative_integers(self):
        """Test `subtract` with valid negative integer inputs."""
        self.assertEqual(subtract(-5, -3), -2)
        self.assertEqual(subtract(-3, -5), 2)  # -3 - (-5) = 2
        self.assertEqual(subtract(-10, -20), 10)

    def test_subtract_valid_positive_floats(self):
        """Test `subtract` with valid positive float inputs."""
        self.assertAlmostEqual(subtract(5.5, 3.2), 2.3)
        self.assertAlmostEqual(subtract(3.2, 5.5), -2.3)
        self.assertAlmostEqual(subtract(0.3, 0.1), 0.2)

    def test_subtract_valid_negative_floats(self):
        """Test `subtract` with valid negative float inputs."""
        self.assertAlmostEqual(subtract(-5.5, -3.2), -2.3)
        self.assertAlmostEqual(subtract(-3.2, -5.5), 2.3)  # -3.2 - (-5.5) = 2.3
        self.assertAlmostEqual(subtract(-0.1, -0.2), 0.1)

    def test_subtract_mixed_int_float(self):
        """Test `subtract` with mixed integer and float inputs."""
        self.assertAlmostEqual(subtract(5, 3.5), 1.5)
        self.assertAlmostEqual(subtract(3.5, 5), -1.5)
        self.assertAlmostEqual(subtract(-5, 3.5), -8.5)
        self.assertAlmostEqual(subtract(5.5, -3), 8.5) # 5.5 - (-3) = 8.5

    def test_subtract_with_zeros(self):
        """Test `subtract` with zero inputs (integer and float)."""
        self.assertEqual(subtract(5, 0), 5)
        self.assertEqual(subtract(0, 5), -5)
        self.assertEqual(subtract(0, 0), 0)
        self.assertAlmostEqual(subtract(5.5, 0.0), 5.5)
        self.assertAlmostEqual(subtract(0.0, 5.5), -5.5)
        self.assertAlmostEqual(subtract(-5.5, 0), -5.5)

    def test_subtract_large_numbers(self):
        """Test `subtract` with large numeric inputs (integers and floats)."""
        self.assertEqual(subtract(3 * 10**9, 2 * 10**9), 10**9)
        self.assertEqual(subtract(10**10, -5 * 10**10), 6 * 10**10) # 10**10 - (-5 * 10**10)
        self.assertAlmostEqual(subtract(8.0235e20, 6.7890e20), 1.2345e20)
        self.assertAlmostEqual(subtract(-1.2345e20, -6.7890e20), 5.5545e20) # -1.2345e20 - (-6.7890e20)

    def test_subtract_non_numeric_a_type_error(self):
        """Verify that `subtract` raises TypeError for non-numeric 'a'."""
        with self.assertRaisesRegex(TypeError, "Input 'a' must be a numeric type \(int or float\)."):
            subtract("5", 3)
        with self.assertRaisesRegex(TypeError, "Input 'a' must be a numeric type \(int or float\)."):
            subtract({"key": "value"}, 3)
        with self.assertRaisesRegex(TypeError, "Input 'a' must be a numeric type \(int or float\)."):
            subtract(None, 3)

    def test_subtract_non_numeric_b_type_error(self):
        """Verify that `subtract` raises TypeError for non-numeric 'b'."""
        with self.assertRaisesRegex(TypeError, "Input 'b' must be a numeric type \(int or float\)."):
            subtract(5, "3")
        with self.assertRaisesRegex(TypeError, "Input 'b' must be a numeric type \(int or float\)."):
            subtract(5, [])
        with self.assertRaisesRegex(TypeError, "Input 'b' must be a numeric type \(int or float\)."):
            subtract(5, complex(1, 2)) # Complex numbers are not int/float

    def test_subtract_non_numeric_both_type_error(self):
        """Verify that `subtract` raises TypeError when both 'a' and 'b' are non-numeric."""
        # 'a' is checked first, so this should trigger 'a's error message
        with self.assertRaisesRegex(TypeError, "Input 'a' must be a numeric type \(int or float\)."):
            subtract("5", "3")
        with self.assertRaisesRegex(TypeError, "Input 'a' must be a numeric type \(int or float\)."):
            subtract(None, False) # False (0) is numeric, but None is not, so 'a' still errors.

    # --- Test cases for multiply function ---

    def test_multiply_valid_positive_integers(self):
        """Test `multiply` with valid positive integer inputs."""
        self.assertEqual(multiply(5, 3), 15)
        self.assertEqual(multiply(10, 0), 0)
        self.assertEqual(multiply(7, 1), 7)

    def test_multiply_valid_negative_integers(self):
        """Test `multiply` with valid negative integer inputs."""
        self.assertEqual(multiply(-5, -3), 15)
        self.assertEqual(multiply(5, -3), -15)
        self.assertEqual(multiply(-5, 3), -15)
        self.assertEqual(multiply(-10, 1), -10)

    def test_multiply_valid_positive_floats(self):
        """Test `multiply` with valid positive float inputs."""
        self.assertAlmostEqual(multiply(5.5, 3.0), 16.5)
        self.assertAlmostEqual(multiply(0.5, 0.5), 0.25)
        self.assertAlmostEqual(multiply(2.0, 1.5), 3.0)

    def test_multiply_valid_negative_floats(self):
        """Test `multiply` with valid negative float inputs."""
        self.assertAlmostEqual(multiply(-5.0, -3.5), 17.5)
        self.assertAlmostEqual(multiply(2.5, -4.0), -10.0)
        self.assertAlmostEqual(multiply(-1.5, 2.0), -3.0)

    def test_multiply_mixed_int_float(self):
        """Test `multiply` with mixed integer and float inputs."""
        self.assertAlmostEqual(multiply(5, 3.5), 17.5)
        self.assertAlmostEqual(multiply(3.5, 5), 17.5)
        self.assertAlmostEqual(multiply(-2, 2.5), -5.0)
        self.assertAlmostEqual(multiply(4.0, -3), -12.0)

    def test_multiply_with_zeros(self):
        """Test `multiply` with zero inputs (integer and float)."""
        self.assertEqual(multiply(5, 0), 0)
        self.assertEqual(multiply(0, 5), 0)
        self.assertEqual(multiply(0.0, 5.5), 0.0)
        self.assertEqual(multiply(-5.5, 0), 0)
        self.assertEqual(multiply(0, 0), 0)
        self.assertEqual(multiply(0.0, 0.0), 0.0)

    def test_multiply_large_numbers(self):
        """Test `multiply` with large numeric inputs (integers and floats)."""
        self.assertEqual(multiply(10**5, 10**5), 10**10)
        self.assertEqual(multiply(-2 * 10**9, 3 * 10**9), -6 * 10**18)
        self.assertAlmostEqual(multiply(1.5e10, 2.0e10), 3.0e20)
        self.assertAlmostEqual(multiply(-1.0e-5, 2.0e-5), -2.0e-10)

    def test_multiply_non_numeric_a_type_error(self):
        """Verify that `multiply` raises TypeError for non-numeric 'a'."""
        with self.assertRaisesRegex(TypeError, "Input 'a' must be a numeric type \(int or float\)."):
            multiply("5", 3)
        with self.assertRaisesRegex(TypeError, "Input 'a' must be a numeric type \(int or float\)."):
            multiply([1], 3)
        with self.assertRaisesRegex(TypeError, "Input 'a' must be a numeric type \(int or float\)."):
            multiply(True, 3) # True is numeric (int 1), this test case is wrong.
            # Correction: 'True' is numeric (int 1), so this won't raise a TypeError.
            # Instead, use a truly non-numeric type like a list or dictionary.
            # The original examples for `add` and `subtract` are good.
            multiply(None, 3) # None is non-numeric

    def test_multiply_non_numeric_b_type_error(self):
        """Verify that `multiply` raises TypeError for non-numeric 'b'."""
        with self.assertRaisesRegex(TypeError, "Input 'b' must be a numeric type \(int or float\)."):
            multiply(5, "3")
        with self.assertRaisesRegex(TypeError, "Input 'b' must be a numeric type \(int or float\)."):
            multiply(5, (1,2))
        with self.assertRaisesRegex(TypeError, "Input 'b' must be a numeric type \(int or float\)."):
            multiply(5, False) # False is numeric (int 0), this test case is wrong.
            # Correction: As above, use a truly non-numeric type.
            multiply(5, {'a':1}) # Dict is non-numeric

    def test_multiply_non_numeric_a_type_error_corrected(self):
        """Verify that `multiply` raises TypeError for non-numeric 'a'."""
        with self.assertRaisesRegex(TypeError, "Input 'a' must be a numeric type \(int or float\)."):
            multiply("5", 3)
        with self.assertRaisesRegex(TypeError, "Input 'a' must be a numeric type \(int or float\)."):
            multiply([1], 3)
        with self.assertRaisesRegex(TypeError, "Input 'a' must be a numeric type \(int or float\)."):
            multiply(None, 3)

    def test_multiply_non_numeric_b_type_error_corrected(self):
        """Verify that `multiply` raises TypeError for non-numeric 'b'."""
        with self.assertRaisesRegex(TypeError, "Input 'b' must be a numeric type \(int or float\)."):
            multiply(5, "3")
        with self.assertRaisesRegex(TypeError, "Input 'b' must be a numeric type \(int or float\)."):
            multiply(5, (1,2))
        with self.assertRaisesRegex(TypeError, "Input 'b' must be a numeric type \(int or float\)."):
            multiply(5, {'a':1})

    def test_multiply_non_numeric_both_type_error(self):
        """Verify that `multiply` raises TypeError when both 'a' and 'b' are non-numeric."""
        with self.assertRaisesRegex(TypeError, "Input 'a' must be a numeric type \(int or float\)."):
            multiply("5", "3")
        with self.assertRaisesRegex(TypeError, "Input 'a' must be a numeric type \(int or float\)."):
            multiply(None, None)

    # --- Test cases for divide function ---

    def test_divide_valid_positive_integers(self):
        """Test `divide` with valid positive integer inputs."""
        self.assertEqual(divide(6, 3), 2.0)
        self.assertEqual(divide(7, 2), 3.5) # Division always returns float
        self.assertEqual(divide(10, 1), 10.0)

    def test_divide_valid_negative_integers(self):
        """Test `divide` with valid negative integer inputs."""
        self.assertEqual(divide(-6, 3), -2.0)
        self.assertEqual(divide(6, -3), -2.0)
        self.assertEqual(divide(-6, -3), 2.0)
        self.assertEqual(divide(-7, 2), -3.5)

    def test_divide_valid_positive_floats(self):
        """Test `divide` with valid positive float inputs."""
        self.assertAlmostEqual(divide(5.0, 2.0), 2.5)
        self.assertAlmostEqual(divide(0.75, 0.25), 3.0)
        self.assertAlmostEqual(divide(10.0, 3.0), 3.3333333333333335)

    def test_divide_valid_negative_floats(self):
        """Test `divide` with valid negative float inputs."""
        self.assertAlmostEqual(divide(-5.0, 2.0), -2.5)
        self.assertAlmostEqual(divide(5.0, -2.0), -2.5)
        self.assertAlmostEqual(divide(-7.5, -2.5), 3.0)
        self.assertAlmostEqual(divide(-10.0, 3.0), -3.3333333333333335)

    def test_divide_mixed_int_float(self):
        """Test `divide` with mixed integer and float inputs."""
        self.assertAlmostEqual(divide(10, 4.0), 2.5)
        self.assertAlmostEqual(divide(10.0, 4), 2.5)
        self.assertAlmostEqual(divide(-10, 2.5), -4.0)
        self.assertAlmostEqual(divide(15.0, -3), -5.0)

    def test_divide_by_one(self):
        """Test `divide` with 1 as divisor (integer and float)."""
        self.assertEqual(divide(5, 1), 5.0)
        self.assertEqual(divide(-5, 1), -5.0)
        self.assertEqual(divide(5.5, 1.0), 5.5)
        self.assertEqual(divide(0, 1), 0.0)

    def test_divide_zero_by_number(self):
        """Test `divide` when dividend is zero."""
        self.assertEqual(divide(0, 5), 0.0)
        self.assertEqual(divide(0.0, -5.5), 0.0)

    def test_divide_large_numbers(self):
        """Test `divide` with large numeric inputs (integers and floats)."""
        self.assertAlmostEqual(divide(10**10, 10**5), 10**5)
        self.assertAlmostEqual(divide(-6.0e20, 3.0e10), -2.0e10)
        self.assertAlmostEqual(divide(1.0e-5, 2.0e-10), 5.0e4)

    def test_divide_non_numeric_a_type_error(self):
        """Verify that `divide` raises TypeError for non-numeric 'a'."""
        with self.assertRaisesRegex(TypeError, "Input 'a' must be a numeric type \(int or float\)."):
            divide("10", 2)
        with self.assertRaisesRegex(TypeError, "Input 'a' must be a numeric type \(int or float\)."):
            divide(None, 2)
        with self.assertRaisesRegex(TypeError, "Input 'a' must be a numeric type \(int or float\)."):
            divide([10], 2)

    def test_divide_non_numeric_b_type_error(self):
        """Verify that `divide` raises TypeError for non-numeric 'b'."""
        with self.assertRaisesRegex(TypeError, "Input 'b' must be a numeric type \(int or float\)."):
            divide(10, "2")
        with self.assertRaisesRegex(TypeError, "Input 'b' must be a numeric type \(int or float\)."):
            divide(10, {})
        with self.assertRaisesRegex(TypeError, "Input 'b' must be a numeric type \(int or float\)."):
            divide(10, True) # True is numeric (int 1), this test case is wrong.
            # Correction: Use a truly non-numeric type.
            divide(10, complex(1,1)) # Complex is non-numeric per _is_numeric

    def test_divide_non_numeric_a_type_error_corrected(self):
        """Verify that `divide` raises TypeError for non-numeric 'a'."""
        with self.assertRaisesRegex(TypeError, "Input 'a' must be a numeric type \(int or float\)."):
            divide("10", 2)
        with self.assertRaisesRegex(TypeError, "Input 'a' must be a numeric type \(int or float\)."):
            divide(None, 2)
        with self.assertRaisesRegex(TypeError, "Input 'a' must be a numeric type \(int or float\)."):
            divide([10], 2)

    def test_divide_non_numeric_b_type_error_corrected(self):
        """Verify that `divide` raises TypeError for non-numeric 'b'."""
        with self.assertRaisesRegex(TypeError, "Input 'b' must be a numeric type \(int or float\)."):
            divide(10, "2")
        with self.assertRaisesRegex(TypeError, "Input 'b' must be a numeric type \(int or float\)."):
            divide(10, {})
        with self.assertRaisesRegex(TypeError, "Input 'b' must be a numeric type \(int or float\)."):
            divide(10, complex(1,1))

    def test_divide_non_numeric_both_type_error(self):
        """Verify that `divide` raises TypeError when both 'a' and 'b' are non-numeric."""
        with self.assertRaisesRegex(TypeError, "Input 'a' must be a numeric type \(int or float\)."):
            divide("10", "2")
        with self.assertRaisesRegex(TypeError, "Input 'a' must be a numeric type \(int or float\)."):
            divide([], None)

    def test_divide_by_zero_value_error(self):
        """Verify that `divide` raises ValueError for division by zero."""
        with self.assertRaisesRegex(ValueError, "Cannot divide by zero."):
            divide(10, 0)
        with self.assertRaisesRegex(ValueError, "Cannot divide by zero."):
            divide(10.0, 0)
        with self.assertRaisesRegex(ValueError, "Cannot divide by zero."):
            divide(-5, 0.0)
        with self.assertRaisesRegex(ValueError, "Cannot divide by zero."):
            divide(0, 0) # Even 0/0 should raise ValueError as per the logic