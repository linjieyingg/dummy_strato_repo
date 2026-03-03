import unittest
import sys
import os

# Add the src directory to the Python path for module import
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

try:
    from bmi_calculator import calculate_bmi
except ImportError:
    # If bmi_calculator or calculate_bmi is not found, define a placeholder
    # to allow tests to be skipped, or raise an error if it's critical.
    # For a test file, it's better to skip if the dependency is missing.
    print("WARNING: Could not import 'calculate_bmi' from 'src/bmi_calculator.py'. Tests will be skipped.", file=sys.stderr)
    calculate_bmi = None


@unittest.skipUnless(calculate_bmi, "BMI calculator function not found, skipping tests.")
class TestBMICalculator(unittest.TestCase):
    """
    Test suite for the calculate_bmi function in src/bmi_calculator.py.

    This class contains unit tests to verify:
    - Correct BMI calculation for various valid inputs (integers, floats).
    - Proper handling of edge cases.
    - Appropriate error handling for invalid input types (TypeError).
    - Appropriate error handling for non-positive input values (ValueError).
    """

    def test_positive_integer_inputs(self):
        """Test BMI calculation with positive integer weight and height."""
        # weight (kg), height (m) -> expected BMI
        # BMI = weight / (height * height)
        # 70 kg, 1.75 m -> 70 / (1.75 * 1.75) = 70 / 3.0625 = 22.857...
        self.assertAlmostEqual(calculate_bmi(70, 1.75), 22.857142857142858)
        self.assertAlmostEqual(calculate_bmi(80, 1.80), 24.691358024691358)
        self.assertAlmostEqual(calculate_bmi(60, 1.60), 23.4375)

    def test_positive_float_inputs(self):
        """Test BMI calculation with positive float weight and height."""
        self.assertAlmostEqual(calculate_bmi(75.5, 1.82), 22.79379663737156)
        self.assertAlmostEqual(calculate_bmi(55.0, 1.55), 22.89282006231014)

    def test_edge_case_inputs(self):
        """Test BMI calculation with edge case values like very small or large valid numbers."""
        # Very small valid height
        self.assertAlmostEqual(calculate_bmi(1, 0.1), 100.0)
        # Larger numbers
        self.assertAlmostEqual(calculate_bmi(150, 2.0), 37.5)

    def test_type_error_for_non_numeric_weight(self):
        """Test that TypeError is raised for non-numeric weight input."""
        with self.assertRaises(TypeError):
            calculate_bmi("70", 1.75)
        with self.assertRaises(TypeError):
            calculate_bmi([70], 1.75)
        with self.assertRaises(TypeError):
            calculate_bmi(None, 1.75)

    def test_type_error_for_non_numeric_height(self):
        """Test that TypeError is raised for non-numeric height input."""
        with self.assertRaises(TypeError):
            calculate_bmi(70, "1.75")
        with self.assertRaises(TypeError):
            calculate_bmi(70, [1.75])
        with self.assertRaises(TypeError):
            calculate_bmi(70, None)

    def test_value_error_for_zero_weight(self):
        """Test that ValueError is raised for zero weight input."""
        with self.assertRaises(ValueError):
            calculate_bmi(0, 1.75)

    def test_value_error_for_negative_weight(self):
        """Test that ValueError is raised for negative weight input."""
        with self.assertRaises(ValueError):
            calculate_bmi(-70, 1.75)

    def test_value_error_for_zero_height(self):
        """Test that ValueError is raised for zero height input."""
        with self.assertRaises(ValueError):
            calculate_bmi(70, 0)

    def test_value_error_for_negative_height(self):
        """Test that ValueError is raised for negative height input."""
        with self.assertRaises(ValueError):
            calculate_bmi(70, -1.75)

    def test_value_error_for_both_invalid(self):
        """Test that ValueError is raised if both weight and height are invalid (e.g., zero)."""
        with self.assertRaises(ValueError):
            calculate_bmi(0, 0)
        with self.assertRaises(ValueError):
            calculate_bmi(-10, -1.0)


if __name__ == '__main__':
    unittest.main()