import unittest
from math_operations import subtract

class TestSubtractFunction(unittest.TestCase):
    """
    Unit tests for the 'subtract' function in math_operations.py.
    """

    def test_positive_numbers(self):
        """
        Test subtraction with two positive integers.
        """
        self.assertEqual(subtract(5, 3), 2)
        self.assertEqual(subtract(10, 7), 3)
        self.assertEqual(subtract(3, 5), -2) # Result is negative

    def test_negative_numbers(self):
        """
        Test subtraction with two negative integers.
        """
        self.assertEqual(subtract(-5, -3), -2)
        self.assertEqual(subtract(-3, -5), 2)
        self.assertEqual(subtract(-10, -15), 5)

    def test_mixed_positive_negative(self):
        """
        Test subtraction with a mix of positive and negative integers.
        """
        self.assertEqual(subtract(5, -3), 8)
        self.assertEqual(subtract(-5, 3), -8)
        self.assertEqual(subtract(0, -7), 7)

    def test_zero_values(self):
        """
        Test subtraction involving zero.
        """
        self.assertEqual(subtract(5, 0), 5)
        self.assertEqual(subtract(0, 5), -5)
        self.assertEqual(subtract(0, 0), 0)
        self.assertEqual(subtract(-5, 0), -5)

    def test_floating_point_numbers(self):
        """
        Test subtraction with floating-point numbers.
        Uses assertAlmostEqual for precision.
        """
        self.assertAlmostEqual(subtract(5.5, 3.2), 2.3)
        self.assertAlmostEqual(subtract(10.0, 3.5), 6.5)
        self.assertAlmostEqual(subtract(-2.1, 1.9), -4.0)
        self.assertAlmostEqual(subtract(0.1, 0.2), -0.1)

    def test_large_numbers(self):
        """
        Test subtraction with large integers to ensure no overflow issues
        (Python integers handle arbitrary precision, but good to test).
        """
        self.assertEqual(subtract(1_000_000_000, 500_000_000), 500_000_000)
        self.assertEqual(subtract(-1_000_000_000, -2_000_000_000), 1_000_000_000)

    def test_invalid_input_types(self):
        """
        Test that TypeError is raised for non-numeric input.
        """
        with self.assertRaises(TypeError, msg="Expected TypeError for string input"):
            subtract("abc", 5)
        with self.assertRaises(TypeError, msg="Expected TypeError for list input"):
            subtract(5, [1, 2])
        with self.assertRaises(TypeError, msg="Expected TypeError for None input"):
            subtract(None, 10)
        with self.assertRaises(TypeError, msg="Expected TypeError for mixed invalid input"):
            subtract("10", "5")

    def test_mixed_numeric_types(self):
        """
        Test subtraction with mixed integer and float types.
        """
        self.assertEqual(subtract(10, 3.5), 6.5)
        self.assertAlmostEqual(subtract(7.5, 2), 5.5)
        self.assertEqual(subtract(-4, 2.5), -6.5)

if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)