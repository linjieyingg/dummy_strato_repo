import unittest
import math
from src.utils import calculate_cylinder_volume

class TestUtils(unittest.TestCase):
    """
    Unit tests for the utility functions in src/utils.py.
    """

    def test_calculate_cylinder_volume_positive_values(self):
        """
        Test calculate_cylinder_volume with positive radius and height.
        """
        # Test case 1: radius=1, height=1
        # Volume = pi * 1^2 * 1 = pi
        self.assertAlmostEqual(calculate_cylinder_volume(1, 1), math.pi, places=7)

        # Test case 2: radius=2, height=3
        # Volume = pi * 2^2 * 3 = 12 * pi
        self.assertAlmostEqual(calculate_cylinder_volume(2, 3), 12 * math.pi, places=7)

        # Test case 3: radius=0.5, height=10
        # Volume = pi * 0.5^2 * 10 = pi * 0.25 * 10 = 2.5 * pi
        self.assertAlmostEqual(calculate_cylinder_volume(0.5, 10), 2.5 * math.pi, places=7)

    def test_calculate_cylinder_volume_zero_radius(self):
        """
        Test calculate_cylinder_volume with zero radius.
        Expected volume should be 0.
        """
        self.assertAlmostEqual(calculate_cylinder_volume(0, 5), 0.0, places=7)
        self.assertAlmostEqual(calculate_cylinder_volume(0, 0.1), 0.0, places=7)

    def test_calculate_cylinder_volume_zero_height(self):
        """
        Test calculate_cylinder_volume with zero height.
        Expected volume should be 0.
        """
        self.assertAlmostEqual(calculate_cylinder_volume(5, 0), 0.0, places=7)
        self.assertAlmostEqual(calculate_cylinder_volume(0.1, 0), 0.0, places=7)

    def test_calculate_cylinder_volume_zero_radius_and_height(self):
        """
        Test calculate_cylinder_volume with both radius and height as zero.
        Expected volume should be 0.
        """
        self.assertAlmostEqual(calculate_cylinder_volume(0, 0), 0.0, places=7)

    def test_calculate_cylinder_volume_negative_radius(self):
        """
        Test calculate_cylinder_volume with a negative radius.
        Expected to raise a ValueError.
        """
        with self.assertRaises(ValueError) as cm:
            calculate_cylinder_volume(-1, 5)
        self.assertEqual(str(cm.exception), "Radius and height must be non-negative.")

        with self.assertRaises(ValueError) as cm:
            calculate_cylinder_volume(-0.1, 10)
        self.assertEqual(str(cm.exception), "Radius and height must be non-negative.")

    def test_calculate_cylinder_volume_negative_height(self):
        """
        Test calculate_cylinder_volume with a negative height.
        Expected to raise a ValueError.
        """
        with self.assertRaises(ValueError) as cm:
            calculate_cylinder_volume(5, -1)
        self.assertEqual(str(cm.exception), "Radius and height must be non-negative.")

        with self.assertRaises(ValueError) as cm:
            calculate_cylinder_volume(10, -0.1)
        self.assertEqual(str(cm.exception), "Radius and height must be non-negative.")

    def test_calculate_cylinder_volume_negative_both(self):
        """
        Test calculate_cylinder_volume with both negative radius and height.
        Expected to raise a ValueError.
        """
        with self.assertRaises(ValueError) as cm:
            calculate_cylinder_volume(-1, -1)
        self.assertEqual(str(cm.exception), "Radius and height must be non-negative.")

    def test_calculate_cylinder_volume_invalid_type_radius(self):
        """
        Test calculate_cylinder_volume with non-numeric radius.
        Expected to raise a TypeError.
        """
        with self.assertRaises(TypeError) as cm:
            calculate_cylinder_volume("1", 5)
        self.assertEqual(str(cm.exception), "Radius and height must be numeric.")

        with self.assertRaises(TypeError) as cm:
            calculate_cylinder_volume([1], 5)
        self.assertEqual(str(cm.exception), "Radius and height must be numeric.")

    def test_calculate_cylinder_volume_invalid_type_height(self):
        """
        Test calculate_cylinder_volume with non-numeric height.
        Expected to raise a TypeError.
        """
        with self.assertRaises(TypeError) as cm:
            calculate_cylinder_volume(5, "1")
        self.assertEqual(str(cm.exception), "Radius and height must be numeric.")

        with self.assertRaises(TypeError) as cm:
            calculate_cylinder_volume(5, None)
        self.assertEqual(str(cm.exception), "Radius and height must be numeric.")

    def test_calculate_cylinder_volume_invalid_type_both(self):
        """
        Test calculate_cylinder_volume with non-numeric radius and height.
        Expected to raise a TypeError.
        """
        with self.assertRaises(TypeError) as cm:
            calculate_cylinder_volume("a", "b")
        self.assertEqual(str(cm.exception), "Radius and height must be numeric.")

    def test_calculate_cylinder_volume_large_values(self):
        """
        Test calculate_cylinder_volume with large radius and height.
        """
        # Test case for large numbers
        radius = 1e6  # 1,000,000
        height = 1e3  # 1,000
        expected_volume = math.pi * (radius ** 2) * height
        self.assertAlmostEqual(calculate_cylinder_volume(radius, height), expected_volume, places=7)

if __name__ == '__main__':
    unittest.main()