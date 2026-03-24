import unittest
from src.math_utils import calculate_cube_volume

class TestCalculateCubeVolume(unittest.TestCase):

    def test_positive_integer_side(self):
        """
        Test calculate_cube_volume with a positive integer side.
        """
        self.assertAlmostEqual(calculate_cube_volume(3), 27.0)

    def test_positive_float_side(self):
        """
        Test calculate_cube_volume with a positive float side.
        """
        self.assertAlmostEqual(calculate_cube_volume(2.5), 15.625)

    def test_zero_side(self):
        """
        Test calculate_cube_volume with a side length of zero.
        """
        self.assertAlmostEqual(calculate_cube_volume(0), 0.0)

    def test_negative_side_raises_value_error(self):
        """
        Test that calculate_cube_volume raises ValueError for a negative side.
        """
        with self.assertRaisesRegex(ValueError, "Side length cannot be negative."):
            calculate_cube_volume(-5)

    def test_non_numeric_side_raises_type_error(self):
        """
        Test that calculate_cube_volume raises TypeError for a non-numeric side.
        """
        with self.assertRaisesRegex(TypeError, "Side length must be a number \\(int or float\\)."):
            calculate_cube_volume("abc")
        with self.assertRaisesRegex(TypeError, "Side length must be a number \\(int or float\\)."):
            calculate_cube_volume([1, 2])
        with self.assertRaisesRegex(TypeError, "Side length must be a number \\(int or float\\)."):
            calculate_cube_volume(None)

if __name__ == '__main__':
    unittest.main()