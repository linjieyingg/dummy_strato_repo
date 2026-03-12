import unittest
import sys
import os

# Adjust the path to import from the src directory
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../../src')))

from utils.math import absolute_value

class TestAbsoluteValue(unittest.TestCase):

    # Test cases for happy path with integers
    def test_positive_integer(self):
        self.assertEqual(absolute_value(5), 5)

    def test_negative_integer(self):
        self.assertEqual(absolute_value(-10), 10)

    def test_zero_integer(self):
        self.assertEqual(absolute_value(0), 0)

    # Test cases for happy path with floats
    def test_positive_float(self):
        self.assertAlmostEqual(absolute_value(3.14), 3.14)

    def test_negative_float(self):
        self.assertAlmostEqual(absolute_value(-0.5), 0.5)

    def test_zero_float(self):
        self.assertAlmostEqual(absolute_value(0.0), 0.0)

    # Test cases for TypeError as explicitly raised
    def test_type_error_with_string(self):
        with self.assertRaises(TypeError) as cm:
            absolute_value("hello")
        self.assertEqual(str(cm.exception), "Input 'num' must be an integer or a float.")

    def test_type_error_with_list(self):
        with self.assertRaises(TypeError) as cm:
            absolute_value([1, 2])
        self.assertEqual(str(cm.exception), "Input 'num' must be an integer or a float.")

    def test_type_error_with_none(self):
        with self.assertRaises(TypeError) as cm:
            absolute_value(None)
        self.assertEqual(str(cm.exception), "Input 'num' must be an integer or a float.")
            
    def test_type_error_with_boolean_true(self):
        # Booleans are explicitly checked and rejected if not a direct number.
        # This aligns with the `isinstance(num, bool)` check.
        with self.assertRaises(TypeError) as cm:
            absolute_value(True)
        self.assertEqual(str(cm.exception), "Input 'num' must be an integer or a float.")

    def test_type_error_with_boolean_false(self):
        with self.assertRaises(TypeError) as cm:
            absolute_value(False)
        self.assertEqual(str(cm.exception), "Input 'num' must be an integer or a float.")

if __name__ == '__main__':
    unittest.main()