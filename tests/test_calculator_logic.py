import unittest
from src.calculator_logic import add, subtract

class TestCalculatorLogic(unittest.TestCase):
    """
    Comprehensive test suite for the functions defined in `src/calculator_logic.py`.
    This includes testing valid positive/negative integers and floats, large numbers,
    and non-numeric input types for both `add` and `subtract` functions.
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