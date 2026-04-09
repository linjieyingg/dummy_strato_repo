import unittest
import math
from src.geometry import calculate_cone_volume

class TestConeVolume(unittest.TestCase):
    """
    Test suite for the calculate_cone_volume function in src/geometry.py.
    """

    def test_valid_positive_integers(self):
        """
        Tests calculate_cone_volume with valid positive integer inputs.
        """
        # Test case 1: radius=3, height=7
        expected_volume = (1/3) * math.pi * (3**2) * 7
        self.assertAlmostEqual(calculate_cone_volume(3, 7), expected_volume, places=7)

        # Test case 2: radius=10, height=1
        expected_volume = (1/3) * math.pi * (10**2) * 1
        self.assertAlmostEqual(calculate_cone_volume(10, 1), expected_volume, places=7)

    def test_valid_positive_floats(self):
        """
        Tests calculate_cone_volume with valid positive float inputs.
        """
        # Test case 1: radius=2.5, height=6.0
        expected_volume = (1/3) * math.pi * (2.5**2) * 6.0
        self.assertAlmostEqual(calculate_cone_volume(2.5, 6.0), expected_volume, places=7)

        # Test case 2: radius=1.0, height=0.5
        expected_volume = (1/3) * math.pi * (1.0**2) * 0.5
        self.assertAlmostEqual(calculate_cone_volume(1.0, 0.5), expected_volume, places=7)

    def test_zero_radius(self):
        """
        Tests calculate_cone_volume when the radius is zero.
        The volume should be zero.
        """
        self.assertAlmostEqual(calculate_cone_volume(0, 10), 0.0, places=7)

    def test_zero_height(self):
        """
        Tests calculate_cone_volume when the height is zero.
        The volume should be zero.
        """
        self.assertAlmostEqual(calculate_cone_volume(5, 0), 0.0, places=7)

    def test_both_zero(self):
        """
        Tests calculate_cone_volume when both radius and height are zero.
        The volume should be zero.
        """
        self.assertAlmostEqual(calculate_cone_volume(0, 0), 0.0, places=7)

    def test_large_inputs(self):
        """
        Tests calculate_cone_volume with large numeric inputs to check scalability and precision.
        """
        # Large integer inputs
        expected_volume = (1/3) * math.pi * (1000**2) * 2000
        self.assertAlmostEqual(calculate_cone_volume(1000, 2000), expected_volume, places=7)

        # Large float inputs
        expected_volume = (1/3) * math.pi * (999.99**2) * 1999.99
        self.assertAlmostEqual(calculate_cone_volume(999.99, 1999.99), expected_volume, places=7)

    def test_negative_radius(self):
        """
        Verifies that a ValueError is raised when the radius is negative.
        """
        with self.assertRaisesRegex(ValueError, "Radius and height must be non-negative numbers."):
            calculate_cone_volume(-5, 10)

    def test_negative_height(self):
        """
        Verifies that a ValueError is raised when the height is negative.
        """
        with self.assertRaisesRegex(ValueError, "Radius and height must be non-negative numbers."):
            calculate_cone_volume(5, -10)

    def test_both_negative(self):
        """
        Verifies that a ValueError is raised when both radius and height are negative.
        """
        with self.assertRaisesRegex(ValueError, "Radius and height must be non-negative numbers."):
            calculate_cone_volume(-5, -10)

    def test_non_numeric_radius(self):
        """
        Verifies that a TypeError is raised when the radius is non-numeric.
        """
        with self.assertRaisesRegex(TypeError, "Radius and height must be numeric types."):
            calculate_cone_volume("abc", 10)
        with self.assertRaisesRegex(TypeError, "Radius and height must be numeric types."):
            calculate_cone_volume([1], 10)
        with self.assertRaisesRegex(TypeError, "Radius and height must be numeric types."):
            calculate_cone_volume(None, 10)

    def test_non_numeric_height(self):
        """
        Verifies that a TypeError is raised when the height is non-numeric.
        """
        with self.assertRaisesRegex(TypeError, "Radius and height must be numeric types."):
            calculate_cone_volume(5, "abc")
        with self.assertRaisesRegex(TypeError, "Radius and height must be numeric types."):
            calculate_cone_volume(5, (1,))
        with self.assertRaisesRegex(TypeError, "Radius and height must be numeric types."):
            calculate_cone_volume(5, None)

    def test_non_numeric_both(self):
        """
        Verifies that a TypeError is raised when both radius and height are non-numeric.
        """
        with self.assertRaisesRegex(TypeError, "Radius and height must be numeric types."):
            calculate_cone_volume("abc", "xyz")
        with self.assertRaisesRegex(TypeError, "Radius and height must be numeric types."):
            calculate_cone_volume([1], {2})


if __name__ == "__main__":
    unittest.main()