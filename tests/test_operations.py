import unittest
import sys
import os

# Add the 'src' directory to the Python path to enable importing 'operations'
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

import operations

class TestOperations(unittest.TestCase):
    """
    Unit tests for the functions defined in 'src/operations.py'.
    Ensures the correctness of the 'add' function and
    provides a framework for future arithmetic operations.
    """

    def test_add_positive_integers(self):
        """
        Test 'add' with two positive integers.
        """
        self.assertEqual(operations.add(2, 3), 5)
        self.assertEqual(operations.add(100, 200), 300)
        self.assertEqual(operations.add(1, 0), 1)

    def test_add_negative_integers(self):
        """
        Test 'add' with two negative integers.
        """
        self.assertEqual(operations.add(-2, -3), -5)
        self.assertEqual(operations.add(-10, -5), -15)

    def test_add_mixed_integers(self):
        """
        Test 'add' with a positive and a negative integer.
        """
        self.assertEqual(operations.add(-2, 3), 1)
        self.assertEqual(operations.add(5, -10), -5)
        self.assertEqual(operations.add(-7, 7), 0)

    def test_add_zero(self):
        """
        Test 'add' involving zero.
        """
        self.assertEqual(operations.add(0, 5), 5)
        self.assertEqual(operations.add(5, 0), 5)
        self.assertEqual(operations.add(0, 0), 0)
        self.assertEqual(operations.add(-8, 0), -8)

    def test_add_floats(self):
        """
        Test 'add' with floating-point numbers.
        """
        self.assertEqual(operations.add(2.5, 3.5), 6.0)
        self.assertEqual(operations.add(-1.5, 2.5), 1.0)
        self.assertEqual(operations.add(0.0, 10.0), 10.0)

    def test_add_floats_precision(self):
        """
        Test 'add' with floating-point numbers requiring precision checks.
        """
        # Using assertAlmostEqual for floating-point comparisons
        self.assertAlmostEqual(operations.add(0.1, 0.2), 0.3)
        self.assertAlmostEqual(operations.add(1.0/3.0, 2.0/3.0), 1.0)
        self.assertAlmostEqual(operations.add(-0.0001, 0.0002), 0.0001)

    def test_add_large_numbers(self):
        """
        Test 'add' with very large integers.
        """
        self.assertEqual(operations.add(1_000_000_000, 2_000_000_000), 3_000_000_000)
        self.assertEqual(operations.add(999_999_999_999, 1), 1_000_000_000_000)

    def test_add_mixed_types_numeric(self):
        """
        Test 'add' with mixed numeric types (int and float).
        """
        self.assertEqual(operations.add(5, 2.5), 7.5)
        self.assertEqual(operations.add(2.5, 5), 7.5)
        self.assertEqual(operations.add(-10, 3.5), -6.5)

    def test_add_non_numeric_input(self):
        """
        Test 'add' with non-numeric inputs to ensure proper error handling.
        Assumes 'add' is intended for numeric types only.
        """
        with self.assertRaises(TypeError):
            operations.add("hello", "world")
        with self.assertRaises(TypeError):
            operations.add(1, "two")
        with self.assertRaises(TypeError):
            operations.add([1, 2], [3])
        with self.assertRaises(TypeError):
            operations.add(None, 5)
        with self.assertRaises(TypeError):
            operations.add(5, None)
        with self.assertRaises(TypeError):
            operations.add({"a": 1}, {"b": 2})


if __name__ == '__main__':
    unittest.main()