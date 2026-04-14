import unittest
from src.math_utils import is_perfect_square

class TestIsPerfectSquare(unittest.TestCase):
    """
    Unit tests for the `is_perfect_square` function in `src.math_utils.py`.
    """

    def test_positive_perfect_squares(self):
        """
        Test cases for positive integers that are perfect squares.
        """
        self.assertTrue(is_perfect_square(4))
        self.assertTrue(is_perfect_square(9))
        self.assertTrue(is_perfect_square(16))
        self.assertTrue(is_perfect_square(100))
        self.assertTrue(is_perfect_square(144))
        self.assertTrue(is_perfect_square(1)) # 1 is a perfect square (1*1)

    def test_positive_non_perfect_squares(self):
        """
        Test cases for positive integers that are not perfect squares.
        """
        self.assertFalse(is_perfect_square(2))
        self.assertFalse(is_perfect_square(3))
        self.assertFalse(is_perfect_square(5))
        self.assertFalse(is_perfect_square(10))
        self.assertFalse(is_perfect_square(99))
        self.assertFalse(is_perfect_square(143))

    def test_zero(self):
        """
        Test case for zero, which is a perfect square (0*0).
        """
        self.assertTrue(is_perfect_square(0))

    def test_negative_numbers(self):
        """
        Test cases for negative integers, which cannot be perfect squares.
        """
        self.assertFalse(is_perfect_square(-1))
        self.assertFalse(is_perfect_square(-4))
        self.assertFalse(is_perfect_square(-99))

    def test_type_error_non_integer(self):
        """
        Test cases to ensure a TypeError is raised for non-integer inputs.
        """
        with self.assertRaises(TypeError):
            is_perfect_square(4.0)
        with self.assertRaises(TypeError):
            is_perfect_square("4")
        with self.assertRaises(TypeError):
            is_perfect_square(None)
        with self.assertRaises(TypeError):
            is_perfect_square([4])
        with self.assertRaises(TypeError):
            is_perfect_square(True) # Booleans are technically ints in Python, but better to test explicitly if behavior changes

    def test_large_numbers(self):
        """
        Test cases for large integers, both perfect and non-perfect squares.
        Relies on `math.isqrt` correctly handling large numbers.
        """
        # A large perfect square (e.g., 2^30)^2 = 2^60
        large_perfect_square = 1073741824 * 1073741824 # (2^30)^2
        self.assertTrue(is_perfect_square(large_perfect_square))

        # A number just above a large perfect square
        self.assertFalse(is_perfect_square(large_perfect_square + 1))

        # A number just below a large perfect square
        self.assertFalse(is_perfect_square(large_perfect_square - 1))

        # Another large perfect square
        another_large_perfect_square = 987654321 * 987654321
        self.assertTrue(is_perfect_square(another_large_perfect_square))


if __name__ == '__main__':
    unittest.main()