import unittest
import math
from src.geometry import calculate_sphere_volume

class TestCalculateSphereVolume(unittest.TestCase):

    def test_zero_radius(self):
        """
        Test with a radius of zero.
        """
        self.assertAlmostEqual(calculate_sphere_volume(0), 0.0, places=9)

    def test_positive_integer_radius(self):
        """
        Test with a positive integer radius.
        """
        expected_volume = (4/3) * math.pi * (1**3)
        self.assertAlmostEqual(calculate_sphere_volume(1), expected_volume, places=9)

    def test_positive_float_radius(self):
        """
        Test with a positive float radius.
        """
        expected_volume = (4/3) * math.pi * (2.5**3)
        self.assertAlmostEqual(calculate_sphere_volume(2.5), expected_volume, places=9)

    def test_large_radius(self):
        """
        Test with a larger radius.
        """
        expected_volume = (4/3) * math.pi * (10**3)
        self.assertAlmostEqual(calculate_sphere_volume(10), expected_volume, places=9)

    def test_value_error_negative_radius(self):
        """
        Test that ValueError is raised for a negative radius.
        """
        with self.assertRaisesRegex(ValueError, "Radius cannot be negative."):
            calculate_sphere_volume(-1.0)
        with self.assertRaisesRegex(ValueError, "Radius cannot be negative."):
            calculate_sphere_volume(-5)

    def test_type_error_non_numeric_string(self):
        """
        Test that TypeError is raised for a string radius.
        """
        with self.assertRaisesRegex(TypeError, "Radius must be a number \\(int or float\\)."):
            calculate_sphere_volume("abc")

    def test_type_error_non_numeric_list(self):
        """
        Test that TypeError is raised for a list radius.
        """
        with self.assertRaisesRegex(TypeError, "Radius must be a number \\(int or float\\)."):
            calculate_sphere_volume([1])

    def test_type_error_non_numeric_none(self):
        """
        Test that TypeError is raised for a None radius.
        """
        with self.assertRaisesRegex(TypeError, "Radius must be a number \\(int or float\\)."):
            calculate_sphere_volume(None)

if __name__ == '__main__':
    unittest.main()