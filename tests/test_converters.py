import unittest
import sys
import os

# Add the src directory to the Python path to allow importing modules from it
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

# pylint: disable=C0413
import converters # noqa: E402


class TestConverters(unittest.TestCase):
    """
    Test suite for the converters module, specifically targeting the
    meters_to_centimeters function.
    """

    def test_positive_integer_meters(self):
        """
        Test meters_to_centimeters with a positive integer input.
        """
        self.assertEqual(converters.meters_to_centimeters(1), 100)
        self.assertEqual(converters.meters_to_centimeters(5), 500)

    def test_zero_meters(self):
        """
        Test meters_to_centimeters with zero input.
        """
        self.assertEqual(converters.meters_to_centimeters(0), 0)

    def test_negative_integer_meters(self):
        """
        Test meters_to_centimeters with a negative integer input.
        """
        self.assertEqual(converters.meters_to_centimeters(-1), -100)
        self.assertEqual(converters.meters_to_centimeters(-10), -1000)

    def test_positive_float_meters(self):
        """
        Test meters_to_centimeters with a positive float input.
        """
        self.assertEqual(converters.meters_to_centimeters(1.5), 150.0)
        self.assertAlmostEqual(converters.meters_to_centimeters(0.75), 75.0)

    def test_negative_float_meters(self):
        """
        Test meters_to_centimeters with a negative float input.
        """
        self.assertEqual(converters.meters_to_centimeters(-2.5), -250.0)
        self.assertAlmostEqual(converters.meters_to_centimeters(-0.33), -33.0)

    def test_large_number_meters(self):
        """
        Test meters_to_centimeters with a large number input.
        """
        self.assertEqual(converters.meters_to_centimeters(1000000), 100000000)
        self.assertEqual(converters.meters_to_centimeters(-1000000.5), -100000050.0)

    def test_string_input_raises_type_error(self):
        """
        Test meters_to_centimeters with a string input should raise TypeError.
        """
        with self.assertRaises(TypeError) as cm:
            converters.meters_to_centimeters("not_a_number")
        self.assertEqual(str(cm.exception), "Input must be an integer or a float.")

    def test_list_input_raises_type_error(self):
        """
        Test meters_to_centimeters with a list input should raise TypeError.
        """
        with self.assertRaises(TypeError) as cm:
            converters.meters_to_centimeters([1, 2, 3])
        self.assertEqual(str(cm.exception), "Input must be an integer or a float.")

    def test_none_input_raises_type_error(self):
        """
        Test meters_to_centimeters with None input should raise TypeError.
        """
        with self.assertRaises(TypeError) as cm:
            converters.meters_to_centimeters(None)
        self.assertEqual(str(cm.exception), "Input must be an integer or a float.")

    def test_boolean_input_raises_type_error(self):
        """
        Test meters_to_centimeters with boolean input should raise TypeError.
        Note: Python treats True/False as 1/0 in arithmetic, but for strict
        type checking, it should be caught.
        """
        with self.assertRaises(TypeError) as cm:
            converters.meters_to_centimeters(True)
        self.assertEqual(str(cm.exception), "Input must be an integer or a float.")
        with self.assertRaises(TypeError) as cm:
            converters.meters_to_centimeters(False)
        self.assertEqual(str(cm.exception), "Input must be an integer or a float.")


if __name__ == '__main__':
    unittest.main()