import unittest
from unittest.mock import patch
from src.dice_roller import roll_die, roll_multiple_dice

class TestDiceRoller(unittest.TestCase):
    """
    Unit tests for the dice rolling functions implemented in src/dice_roller.py.
    These tests verify correct behavior for valid inputs, proper range of rolls,
    and graceful handling of invalid inputs.
    """

    @patch('src.dice_roller.random.randint')
    def test_roll_die_valid_input(self, mock_randint):
        """
        Test that roll_die returns a value within the expected range (1 to sides)
        for valid 'sides' input. The random.randint function is mocked to ensure
        deterministic test results.
        """
        # Test a standard D6 roll
        mock_randint.return_value = 3
        result = roll_die(6)
        self.assertEqual(result, 3)
        mock_randint.assert_called_once_with(1, 6)
        mock_randint.reset_mock() # Reset mock for subsequent assertions

        # Test a D20 roll
        mock_randint.return_value = 15
        result = roll_die(20)
        self.assertEqual(result, 15)
        mock_randint.assert_called_once_with(1, 20)
        mock_randint.reset_mock()

        # Test the minimum possible roll (1)
        mock_randint.return_value = 1
        result = roll_die(10)
        self.assertEqual(result, 1)
        mock_randint.assert_called_once_with(1, 10)
        mock_randint.reset_mock()

        # Test the maximum possible roll (sides)
        mock_randint.return_value = 10
        result = roll_die(10)
        self.assertEqual(result, 10)
        mock_randint.assert_called_once_with(1, 10)
        mock_randint.reset_mock()

    def test_roll_die_invalid_sides(self):
        """
        Test that roll_die raises a ValueError when 'sides' is not a positive integer.
        This includes zero, negative numbers, floats, strings, and None.
        """
        expected_error_message = r"Number of sides for the die must be a positive integer."

        with self.assertRaisesRegex(ValueError, expected_error_message):
            roll_die(0)  # Zero sides
        with self.assertRaisesRegex(ValueError, expected_error_message):
            roll_die(-1) # Negative sides
        with self.assertRaisesRegex(ValueError, expected_error_message):
            roll_die(1.5) # Float sides
        with self.assertRaisesRegex(ValueError, expected_error_message):
            roll_die("six") # String sides
        with self.assertRaisesRegex(ValueError, expected_error_message):
            roll_die(None) # None sides

    @patch('src.dice_roller.random.randint')
    def test_roll_multiple_dice_valid_input(self, mock_randint):
        """
        Test that roll_multiple_dice returns a list of rolls of the correct length
        and with expected values for valid inputs. The random.randint function
        is mocked to control the sequence of roll results.
        """
        # Test rolling 2 D6 dice
        mock_randint.side_effect = [1, 6] # Simulates rolling a 1 then a 6
        rolls = roll_multiple_dice(2, 6)
        self.assertEqual(rolls, [1, 6])
        self.assertEqual(len(rolls), 2)
        self.assertEqual(mock_randint.call_count, 2) # randint should be called twice
        mock_randint.assert_any_call(1, 6) # Both calls should be for a D6
        mock_randint.reset_mock()

        # Test rolling 3 D10 dice
        mock_randint.side_effect = [5, 1, 10]
        rolls = roll_multiple_dice(3, 10)
        self.assertEqual(rolls, [5, 1, 10])
        self.assertEqual(len(rolls), 3)
        self.assertEqual(mock_randint.call_count, 3)
        mock_randint.assert_any_call(1, 10)
        mock_randint.reset_mock()

        # Test rolling a single die (equivalent to roll_die)
        mock_randint.return_value = 7
        rolls = roll_multiple_dice(1, 8)
        self.assertEqual(rolls, [7])
        self.assertEqual(len(rolls), 1)
        self.assertEqual(mock_randint.call_count, 1)
        mock_randint.assert_called_once_with(1, 8)
        mock_randint.reset_mock()

    def test_roll_multiple_dice_invalid_num_dice(self):
        """
        Test that roll_multiple_dice raises a ValueError when 'num_dice'
        is not a positive integer.
        """
        expected_error_message = r"Number of dice to roll must be a positive integer."

        with self.assertRaisesRegex(ValueError, expected_error_message):
            roll_multiple_dice(0, 6)  # Zero dice
        with self.assertRaisesRegex(ValueError, expected_error_message):
            roll_multiple_dice(-1, 6) # Negative dice
        with self.assertRaisesRegex(ValueError, expected_error_message):
            roll_multiple_dice(1.0, 6) # Float num_dice (not considered int by validation)
        with self.assertRaisesRegex(ValueError, expected_error_message):
            roll_multiple_dice("one", 6) # String num_dice
        with self.assertRaisesRegex(ValueError, expected_error_message):
            roll_multiple_dice(None, 6) # None num_dice

    def test_roll_multiple_dice_invalid_sides(self):
        """
        Test that roll_multiple_dice raises a ValueError when 'sides'
        is not a positive integer.
        """
        expected_error_message = r"Number of sides for each die must be a positive integer."

        with self.assertRaisesRegex(ValueError, expected_error_message):
            roll_multiple_dice(2, 0)  # Zero sides
        with self.assertRaisesRegex(ValueError, expected_error_message):
            roll_multiple_dice(2, -1) # Negative sides
        with self.assertRaisesRegex(ValueError, expected_error_message):
            roll_multiple_dice(2, 6.0) # Float sides (not considered int by validation)
        with self.assertRaisesRegex(ValueError, expected_error_message):
            roll_multiple_dice(2, "six") # String sides
        with self.assertRaisesRegex(ValueError, expected_error_message):
            roll_multiple_dice(2, None) # None sides

    def test_roll_multiple_dice_invalid_both(self):
        """
        Test that roll_multiple_dice raises a ValueError when both 'num_dice'
        and 'sides' are invalid. It should prioritize the 'num_dice' error
        message as per the implementation's validation order.
        """
        expected_num_dice_error = r"Number of dice to roll must be a positive integer."

        with self.assertRaisesRegex(ValueError, expected_num_dice_error):
            roll_multiple_dice(0, 0)  # Both invalid
        with self.assertRaisesRegex(ValueError, expected_num_dice_error):
            roll_multiple_dice(-1, -1) # Both invalid


if __name__ == '__main__':
    unittest.main()