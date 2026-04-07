import unittest
from src.geometry import calculate_pyramid_volume

class TestGeometry(unittest.TestCase):
    """
    Unit tests for the geometry functions, specifically focusing on
    calculate_pyramid_volume.
    """

    def test_valid_positive_integers(self):
        """
        Test calculate_pyramid_volume with valid positive integer inputs
        for base_area and height.
        """
        # Test case: base_area = 9, height = 5
        # Expected volume = (1/3) * 9 * 5 = 15
        self.assertAlmostEqual(calculate_pyramid_volume(9, 5), 15.0)

        # Test case: base_area = 12, height = 7
        # Expected volume = (1/3) * 12 * 7 = 4 * 7 = 28
        self.assertAlmostEqual(calculate_pyramid_volume(12, 7), 28.0)

        # Test case: base_area = 3, height = 3
        # Expected volume = (1/3) * 3 * 3 = 3
        self.assertAlmostEqual(calculate_pyramid_volume(3, 3), 3.0)

    def test_valid_positive_floats(self):
        """
        Test calculate_pyramid_volume with valid positive float inputs
        for base_area and height.
        """
        # Test case: base_area = 7.5, height = 4.2
        # Expected volume = (1/3) * 7.5 * 4.2 = 2.5 * 4.2 = 10.5
        self.assertAlmostEqual(calculate_pyramid_volume(7.5, 4.2), 10.5)

        # Test case: base_area = 10.0, height = 3.0
        # Expected volume = (1/3) * 10.0 * 3.0 = 10.0
        self.assertAlmostEqual(calculate_pyramid_volume(10.0, 3.0), 10.0)

        # Test case: base_area = 0.3, height = 1.0
        # Expected volume = (1/3) * 0.3 * 1.0 = 0.1
        self.assertAlmostEqual(calculate_pyramid_volume(0.3, 1.0), 0.1)

    def test_zero_base_area(self):
        """
        Test calculate_pyramid_volume when base_area is zero.
        The volume should be zero.
        """
        self.assertAlmostEqual(calculate_pyramid_volume(0, 10), 0.0)
        self.assertAlmostEqual(calculate_pyramid_volume(0.0, 5.5), 0.0)

    def test_zero_height(self):
        """
        Test calculate_pyramid_volume when height is zero.
        The volume should be zero.
        """
        self.assertAlmostEqual(calculate_pyramid_volume(20, 0), 0.0)
        self.assertAlmostEqual(calculate_pyramid_volume(15.0, 0.0), 0.0)

    def test_both_zero(self):
        """
        Test calculate_pyramid_volume when both base_area and height are zero.
        The volume should be zero.
        """
        self.assertAlmostEqual(calculate_pyramid_volume(0, 0), 0.0)
        self.assertAlmostEqual(calculate_pyramid_volume(0.0, 0.0), 0.0)

    def test_large_inputs(self):
        """
        Test calculate_pyramid_volume with large numeric inputs
        to ensure precision and handling of large numbers.
        """
        base_area = 1_000_000_000
        height = 3_000_000_000
        # Expected volume = (1/3) * 10^9 * 3 * 10^9 = 10^9 * 10^9 = 10^18
        self.assertAlmostEqual(calculate_pyramid_volume(base_area, height), 1e18)

        base_area_float = 1.23e10
        height_float = 4.56e10
        expected_volume = (1/3) * base_area_float * height_float
        self.assertAlmostEqual(calculate_pyramid_volume(base_area_float, height_float), expected_volume)

    def test_negative_base_area(self):
        """
        Test that calculate_pyramid_volume raises a ValueError
        when base_area is negative.
        """
        with self.assertRaisesRegex(ValueError, "Base area and height must be non-negative."):
            calculate_pyramid_volume(-5, 10)
        with self.assertRaisesRegex(ValueError, "Base area and height must be non-negative."):
            calculate_pyramid_volume(-0.1, 10)

    def test_negative_height(self):
        """
        Test that calculate_pyramid_volume raises a ValueError
        when height is negative.
        """
        with self.assertRaisesRegex(ValueError, "Base area and height must be non-negative."):
            calculate_pyramid_volume(10, -5)
        with self.assertRaisesRegex(ValueError, "Base area and height must be non-negative."):
            calculate_pyramid_volume(10, -0.1)

    def test_both_negative(self):
        """
        Test that calculate_pyramid_volume raises a ValueError
        when both base_area and height are negative.
        """
        with self.assertRaisesRegex(ValueError, "Base area and height must be non-negative."):
            calculate_pyramid_volume(-5, -5)

    def test_non_numeric_base_area(self):
        """
        Test that calculate_pyramid_volume raises a TypeError
        when base_area is not a number.
        """
        with self.assertRaisesRegex(TypeError, "Base area and height must be numeric."):
            calculate_pyramid_volume("abc", 10)
        with self.assertRaisesRegex(TypeError, "Base area and height must be numeric."):
            calculate_pyramid_volume([1, 2], 10)
        with self.assertRaisesRegex(TypeError, "Base area and height must be numeric."):
            calculate_pyramid_volume(None, 10)

    def test_non_numeric_height(self):
        """
        Test that calculate_pyramid_volume raises a TypeError
        when height is not a number.
        """
        with self.assertRaisesRegex(TypeError, "Base area and height must be numeric."):
            calculate_pyramid_volume(10, "abc")
        with self.assertRaisesRegex(TypeError, "Base area and height must be numeric."):
            calculate_pyramid_volume(10, {"key": "value"})
        with self.assertRaisesRegex(TypeError, "Base area and height must be numeric."):
            calculate_pyramid_volume(10, None)

    def test_non_numeric_both(self):
        """
        Test that calculate_pyramid_volume raises a TypeError
        when both base_area and height are not numbers.
        """
        with self.assertRaisesRegex(TypeError, "Base area and height must be numeric."):
            calculate_pyramid_volume("abc", "def")
        with self.assertRaisesRegex(TypeError, "Base area and height must be numeric."):
            calculate_pyramid_volume(None, None)


if __name__ == '__main__':
    unittest.main()