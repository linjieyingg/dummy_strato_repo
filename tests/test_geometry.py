import unittest
from src.geometry import calculate_pyramid_volume, calculate_cube_volume

class TestGeometry(unittest.TestCase):
    """
    Comprehensive suite of unit tests for the calculate_pyramid_volume function,
    ensuring its correctness across various valid inputs, edge cases, and error conditions.
    """

    def test_valid_positive_integers(self):
        """
        Tests calculate_pyramid_volume with valid positive integer inputs for base area and height.
        """
        self.assertAlmostEqual(calculate_pyramid_volume(10, 3), 10.0)
        self.assertAlmostEqual(calculate_pyramid_volume(15, 6), 30.0)
        self.assertAlmostEqual(calculate_pyramid_volume(9, 9), 27.0)

    def test_valid_positive_floats(self):
        """
        Tests calculate_pyramid_volume with valid positive float inputs for base area and height.
        """
        self.assertAlmostEqual(calculate_pyramid_volume(7.5, 2.0), 5.0)
        self.assertAlmostEqual(calculate_pyramid_volume(10.5, 3.3), 11.55)
        self.assertAlmostEqual(calculate_pyramid_volume(0.3, 0.6), 0.06)

    def test_zero_base_area(self):
        """
        Tests the function's behavior when base_area is zero.
        The volume should be zero.
        """
        self.assertAlmostEqual(calculate_pyramid_volume(0, 5), 0.0)
        self.assertAlmostEqual(calculate_pyramid_volume(0.0, 10.5), 0.0)

    def test_zero_height(self):
        """
        Tests the function's behavior when height is zero.
        The volume should be zero.
        """
        self.assertAlmostEqual(calculate_pyramid_volume(10, 0), 0.0)
        self.assertAlmostEqual(calculate_pyramid_volume(15.5, 0.0), 0.0)

    def test_both_zero(self):
        """
        Tests when both base_area and height are zero.
        The volume should be zero.
        """
        self.assertAlmostEqual(calculate_pyramid_volume(0, 0), 0.0)

    def test_large_inputs(self):
        """
        Tests with large numeric inputs (integers and floats) to check precision and scale.
        """
        self.assertAlmostEqual(calculate_pyramid_volume(1_000_000, 3_000_000), 1_000_000_000_000.0)
        self.assertAlmostEqual(calculate_pyramid_volume(1e9, 3e9), 1e18)
        self.assertAlmostEqual(calculate_pyramid_volume(1234567.89, 9876543.21), 4064115162235.632)

    def test_negative_base_area(self):
        """
        Verifies that a ValueError is raised when base_area is negative.
        """
        with self.assertRaisesRegex(ValueError, "Base area and height must be non-negative."):
            calculate_pyramid_volume(-10, 5)
        with self.assertRaisesRegex(ValueError, "Base area and height must be non-negative."):
            calculate_pyramid_volume(-0.1, 5)

    def test_negative_height(self):
        """
        Verifies that a ValueError is raised when height is negative.
        """
        with self.assertRaisesRegex(ValueError, "Base area and height must be non-negative."):
            calculate_pyramid_volume(10, -5)
        with self.assertRaisesRegex(ValueError, "Base area and height must be non-negative."):
            calculate_pyramid_volume(10, -0.1)

    def test_both_negative(self):
        """
        Verifies that a ValueError is raised when both base_area and height are negative.
        """
        with self.assertRaisesRegex(ValueError, "Base area and height must be non-negative."):
            calculate_pyramid_volume(-10, -5)

    def test_non_numeric_base_area(self):
        """
        Verifies that a TypeError is raised when base_area is a non-numeric type.
        """
        with self.assertRaisesRegex(TypeError, "Base area and height must be numbers."):
            calculate_pyramid_volume("abc", 5)
        with self.assertRaisesRegex(TypeError, "Base area and height must be numbers."):
            calculate_pyramid_volume(None, 5)
        with self.assertRaisesRegex(TypeError, "Base area and height must be numbers."):
            calculate_pyramid_volume([10], 5)

    def test_non_numeric_height(self):
        """
        Verifies that a TypeError is raised when height is a non-numeric type.
        """
        with self.assertRaisesRegex(TypeError, "Base area and height must be numbers."):
            calculate_pyramid_volume(10, "abc")
        with self.assertRaisesRegex(TypeError, "Base area and height must be numbers."):
            calculate_pyramid_volume(10, None)
        with self.assertRaisesRegex(TypeError, "Base area and height must be numbers."):
            calculate_pyramid_volume(10, [5])

    def test_non_numeric_both(self):
        """
        Verifies that a TypeError is raised when both base_area and height are non-numeric types.
        """
        with self.assertRaisesRegex(TypeError, "Base area and height must be numbers."):
            calculate_pyramid_volume("abc", "def")
        with self.assertRaisesRegex(TypeError, "Base area and height must be numbers."):
            calculate_pyramid_volume(None, None)


class TestCubeGeometry(unittest.TestCase):
    """
    Comprehensive suite of unit tests for the calculate_cube_volume function.
    """

    def test_valid_positive_integers(self):
        """
        Tests calculate_cube_volume with valid positive integer inputs for side length.
        """
        self.assertAlmostEqual(calculate_cube_volume(2), 8.0)
        self.assertAlmostEqual(calculate_cube_volume(5), 125.0)

    def test_valid_positive_floats(self):
        """
        Tests calculate_cube_volume with valid positive float inputs for side length.
        """
        self.assertAlmostEqual(calculate_cube_volume(1.5), 3.375)
        self.assertAlmostEqual(calculate_cube_volume(0.1), 0.001)

    def test_zero_side_length(self):
        """
        Tests the function's behavior when side_length is zero.
        The volume should be zero.
        """
        self.assertAlmostEqual(calculate_cube_volume(0), 0.0)

    def test_large_inputs(self):
        """
        Tests calculate_cube_volume with large numeric inputs (integers and floats).
        """
        self.assertAlmostEqual(calculate_cube_volume(100), 1000000.0)
        self.assertAlmostEqual(calculate_cube_volume(100.0), 1000000.0)
        self.assertAlmostEqual(calculate_cube_volume(1000.0), 1000000000.0)

    def test_negative_side_length(self):
        """
        Verifies that a ValueError is raised when side_length is negative.
        """
        with self.assertRaisesRegex(ValueError, "Side length cannot be negative."):
            calculate_cube_volume(-5)
        with self.assertRaisesRegex(ValueError, "Side length cannot be negative."):
            calculate_cube_volume(-0.1)

    def test_non_numeric_side_length(self):
        """
        Verifies that a TypeError is raised when side_length is a non-numeric type.
        """
        with self.assertRaisesRegex(TypeError, "Side length must be a number."):
            calculate_cube_volume("abc")
        with self.assertRaisesRegex(TypeError, "Side length must be a number."):
            calculate_cube_volume(None)
        with self.assertRaisesRegex(TypeError, "Side length must be a number."):
            calculate_cube_volume([1])

if __name__ == '__main__':
    unittest.main()