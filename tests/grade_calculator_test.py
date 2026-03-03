import unittest
import sys
import os

# Dynamically add the project root to sys.path to enable module imports
current_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.abspath(os.path.join(current_dir, os.pardir))
sys.path.insert(0, project_root)

# Conditional import for the function under test
try:
    from src.grade_calculator import calculate_letter_grade
    _GRADE_CALCULATOR_AVAILABLE = True
except ImportError:
    _GRADE_CALCULATOR_AVAILABLE = False
    print("WARNING: Could not import 'calculate_letter_grade' from 'src/grade_calculator.py'. Skipping tests.", file=sys.stderr)

@unittest.skipUnless(_GRADE_CALCULATOR_AVAILABLE,
                     "src/grade_calculator.py or calculate_letter_grade function not found.")
class TestGradeCalculator(unittest.TestCase):
    """
    Test suite for the calculate_letter_grade function in src/grade_calculator.py.

    This class provides comprehensive unit tests to ensure that the
    calculate_letter_grade function correctly assigns letter grades based on scores,
    handles boundary conditions, and raises appropriate errors for invalid inputs.
    """

    def test_grade_a(self):
        """
        Tests scores that should result in an 'A' grade (90-100).
        """
        self.assertEqual(calculate_letter_grade(95), 'A')
        self.assertEqual(calculate_letter_grade(90), 'A')  # Lower boundary
        self.assertEqual(calculate_letter_grade(100), 'A') # Upper boundary

    def test_grade_b(self):
        """
        Tests scores that should result in a 'B' grade (80-89).
        """
        self.assertEqual(calculate_letter_grade(85), 'B')
        self.assertEqual(calculate_letter_grade(80), 'B')  # Lower boundary
        self.assertEqual(calculate_letter_grade(89.9), 'B') # Upper boundary just below A

    def test_grade_c(self):
        """
        Tests scores that should result in a 'C' grade (70-79).
        """
        self.assertEqual(calculate_letter_grade(75), 'C')
        self.assertEqual(calculate_letter_grade(70), 'C')  # Lower boundary
        self.assertEqual(calculate_letter_grade(79.9), 'C') # Upper boundary just below B

    def test_grade_d(self):
        """
        Tests scores that should result in a 'D' grade (60-69).
        """
        self.assertEqual(calculate_letter_grade(65), 'D')
        self.assertEqual(calculate_letter_grade(60), 'D')  # Lower boundary
        self.assertEqual(calculate_letter_grade(69.9), 'D') # Upper boundary just below C

    def test_grade_f(self):
        """
        Tests scores that should result in an 'F' grade (0-59).
        """
        self.assertEqual(calculate_letter_grade(55), 'F')
        self.assertEqual(calculate_letter_grade(0), 'F')   # Lower boundary
        self.assertEqual(calculate_letter_grade(59.9), 'F') # Upper boundary just below D
        self.assertEqual(calculate_letter_grade(30), 'F')

    def test_floating_point_scores(self):
        """
        Tests various floating-point scores, including those near boundaries.
        """
        self.assertEqual(calculate_letter_grade(89.99), 'B')
        self.assertEqual(calculate_letter_grade(90.01), 'A')
        self.assertEqual(calculate_letter_grade(79.99), 'C')
        self.assertEqual(calculate_letter_grade(70.01), 'C')
        self.assertEqual(calculate_letter_grade(59.99), 'F')
        self.assertEqual(calculate_letter_grade(60.01), 'D')

    def test_invalid_input_type(self):
        """
        Tests that a TypeError is raised for non-numeric input types.
        """
        with self.assertRaises(TypeError):
            calculate_letter_grade("ninety")
        with self.assertRaises(TypeError):
            calculate_letter_grade([90])
        with self.assertRaises(TypeError):
            calculate_letter_grade(None)
        with self.assertRaises(TypeError):
            calculate_letter_grade(True) # Booleans are ints, but might be treated as invalid

    def test_score_out_of_lower_range(self):
        """
        Tests that a ValueError is raised for scores below 0.
        """
        with self.assertRaises(ValueError):
            calculate_letter_grade(-1)
        with self.assertRaises(ValueError):
            calculate_letter_grade(-0.01)
        with self.assertRaises(ValueError):
            calculate_letter_grade(-100)

    def test_score_out_of_upper_range(self):
        """
        Tests that a ValueError is raised for scores above 100.
        """
        with self.assertRaises(ValueError):
            calculate_letter_grade(101)
        with self.assertRaises(ValueError):
            calculate_letter_grade(100.01)
        with self.assertRaises(ValueError):
            calculate_letter_grade(200)

if __name__ == '__main__':
    unittest.main()