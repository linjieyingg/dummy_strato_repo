import unittest
from src.health import calculate_bmi

class TestHealth(unittest.TestCase):
    """
    A comprehensive test suite for the `calculate_bmi` function.

    This class tests the `calculate_bmi` function across various valid inputs,
    edge cases, and error conditions to ensure its correctness and robustness.
    """

    def test_valid_positive_integers(self):
        """
        Tests `calculate_bmi` with valid positive integer inputs for weight and height.
        """
        # BMI = weight / (height * height)
        # 70 kg / (1.75 m * 1.75 m) = 70 / 3.0625 = 22.85714...
        self.assertAlmostEqual(calculate_bmi(70, 1.75), 22.857142857142858, places=9)
        # 60 kg / (1.6 m * 1.6 m) = 60 / 2.56 = 23.4375
        self.assertAlmostEqual(calculate_bmi(60, 1.6), 23.4375, places=9)

    def test_valid_positive_floats(self):
        """
        Tests `calculate_bmi` with valid positive float inputs for weight and height.
        """
        # 75.5 kg / (1.82 m * 1.82 m) = 75.5 / 3.3124 = 22.7937...
        self.assertAlmostEqual(calculate_bmi(75.5, 1.82), 22.793744771766023, places=9)
        # 55.0 kg / (1.55 m * 1.55 m) = 55.0 / 2.4025 = 22.8928...
        self.assertAlmostEqual(calculate_bmi(55.0, 1.55), 22.89282000416233, places=9)

    def test_large_inputs(self):
        """
        Tests `calculate_bmi` with large numeric inputs (integers and floats)
        to check precision and scale.
        """
        # Very heavy, very tall person
        # 300 kg / (2.5 m * 2.5 m) = 300 / 6.25 = 48.0
        self.assertAlmostEqual(calculate_bmi(300, 2.5), 48.0, places=9)
        # Extremely heavy, extremely tall person (float)
        # 1000.5 kg / (3.0 m * 3.0 m) = 1000.5 / 9.0 = 111.1666...
        self.assertAlmostEqual(calculate_bmi(1000.5, 3.0), 111.16666666666667, places=9)

    def test_zero_weight(self):
        """
        Tests `calculate_bmi` when weight is zero.
        BMI should be 0 in this case, assuming height is valid.
        """
        self.assertAlmostEqual(calculate_bmi(0, 1.7), 0.0, places=9)

    def test_height_near_zero(self):
        """
        Tests `calculate_bmi` with height very close to zero.
        The result should be a very large number.
        """
        # 70 kg / (0.01 m * 0.01 m) = 70 / 0.0001 = 700000.0
        self.assertAlmostEqual(calculate_bmi(70, 0.01), 700000.0, places=9)
        # A tiny height, result should be a huge BMI
        self.assertAlmostEqual(calculate_bmi(1, 0.001), 1_000_000.0, places=9)


    def test_zero_height(self):
        """
        Verifies that a `ValueError` is raised when `height_m` is zero,
        as division by zero is undefined.
        """
        with self.assertRaisesRegex(ValueError, "Height cannot be zero."):
            calculate_bmi(70, 0)

    def test_negative_weight(self):
        """
        Verifies that a `ValueError` is raised when `weight_kg` is negative.
        """
        with self.assertRaisesRegex(ValueError, "Weight and height must be positive values."):
            calculate_bmi(-70, 1.75)

    def test_negative_height(self):
        """
        Verifies that a `ValueError` is raised when `height_m` is negative.
        """
        with self.assertRaisesRegex(ValueError, "Weight and height must be positive values."):
            calculate_bmi(70, -1.75)

    def test_both_negative(self):
        """
        Verifies that a `ValueError` is raised when both `weight_kg` and `height_m` are negative.
        """
        with self.assertRaisesRegex(ValueError, "Weight and height must be positive values."):
            calculate_bmi(-70, -1.75)

    def test_non_numeric_weight(self):
        """
        Verifies that a `TypeError` is raised when `weight_kg` is a non-numeric type.
        """
        with self.assertRaisesRegex(TypeError, "Weight and height must be numeric values."):
            calculate_bmi("70", 1.75)
        with self.assertRaisesRegex(TypeError, "Weight and height must be numeric values."):
            calculate_bmi([70], 1.75)

    def test_non_numeric_height(self):
        """
        Verifies that a `TypeError` is raised when `height_m` is a non-numeric type.
        """
        with self.assertRaisesRegex(TypeError, "Weight and height must be numeric values."):
            calculate_bmi(70, "1.75")
        with self.assertRaisesRegex(TypeError, "Weight and height must be numeric values."):
            calculate_bmi(70, None)

    def test_non_numeric_both(self):
        """
        Verifies that a `TypeError` is raised when both `weight_kg` and `height_m` are
        non-numeric types.
        """
        with self.assertRaisesRegex(TypeError, "Weight and height must be numeric values."):
            calculate_bmi("70", "1.75")
        with self.assertRaisesRegex(TypeError, "Weight and height must be numeric values."):
            calculate_bmi(None, [1.75])

if __name__ == '__main__':
    unittest.main()