import pytest
from unittest.mock import patch, call # Import 'call' for more precise mock assertions
from src.dice_roller import roll_die, roll_multiple_dice

# No class structure for pytest tests

@patch('src.dice_roller.random.randint')
def test_roll_die_valid_input(mock_randint):
    """
    Test that roll_die returns a value within the expected range (1 to sides)
    for valid 'sides' input. The random.randint function is mocked to ensure
    deterministic test results.
    """
    # Test a standard D6 roll
    mock_randint.return_value = 3
    result = roll_die(6)
    assert result == 3
    mock_randint.assert_called_once_with(1, 6)
    mock_randint.reset_mock() # Reset for the next assertion context within this test

    # Test a D20 roll
    mock_randint.return_value = 15
    result = roll_die(20)
    assert result == 15
    mock_randint.assert_called_once_with(1, 20)
    mock_randint.reset_mock()

    # Test the minimum possible roll (1)
    mock_randint.return_value = 1
    result = roll_die(10)
    assert result == 1
    mock_randint.assert_called_once_with(1, 10)
    mock_randint.reset_mock()

    # Test the maximum possible roll (sides)
    mock_randint.return_value = 10
    result = roll_die(10)
    assert result == 10
    mock_randint.assert_called_once_with(1, 10)
    mock_randint.reset_mock()

def test_roll_die_invalid_sides():
    """
    Test that roll_die raises a ValueError when 'sides' is not a positive integer.
    This includes zero, negative numbers, floats, strings, and None.
    """
    # Use pytest.raises without asserting on the error message string
    with pytest.raises(ValueError):
        roll_die(0)  # Zero sides
    with pytest.raises(ValueError):
        roll_die(-1) # Negative sides
    with pytest.raises(ValueError):
        roll_die(1.5) # Float sides
    with pytest.raises(ValueError):
        roll_die("six") # String sides
    with pytest.raises(ValueError):
        roll_die(None) # None sides

@patch('src.dice_roller.random.randint')
def test_roll_multiple_dice_valid_input(mock_randint):
    """
    Test that roll_multiple_dice returns a list of rolls of the correct length
    and with expected values for valid inputs. The random.randint function
    is mocked to control the sequence of roll results.
    """
    # Test rolling 2 D6 dice
    mock_randint.side_effect = [1, 6] # Simulates rolling a 1 then a 6
    rolls = roll_multiple_dice(2, 6)
    assert rolls == [1, 6]
    assert len(rolls) == 2
    assert mock_randint.call_count == 2 # randint should be called twice
    mock_randint.assert_has_calls([call(1, 6), call(1, 6)]) # Verify the sequence of calls
    mock_randint.reset_mock() # Reset side_effect and call_count for the next scenario

    # Test rolling 3 D10 dice
    mock_randint.side_effect = [5, 1, 10]
    rolls = roll_multiple_dice(3, 10)
    assert rolls == [5, 1, 10]
    assert len(rolls) == 3
    assert mock_randint.call_count == 3
    mock_randint.assert_has_calls([call(1, 10), call(1, 10), call(1, 10)])
    mock_randint.reset_mock()

    # Test rolling a single die (equivalent to roll_die)
    mock_randint.return_value = 7
    rolls = roll_multiple_dice(1, 8)
    assert rolls == [7]
    assert len(rolls) == 1
    assert mock_randint.call_count == 1
    mock_randint.assert_called_once_with(1, 8)
    # No reset_mock needed as this is the last part of this test function

def test_roll_multiple_dice_invalid_num_dice():
    """
    Test that roll_multiple_dice raises a ValueError when 'num_dice'
    is not a positive integer.
    """
    # Use pytest.raises without asserting on the error message string
    with pytest.raises(ValueError):
        roll_multiple_dice(0, 6)  # Zero dice
    with pytest.raises(ValueError):
        roll_multiple_dice(-1, 6) # Negative dice
    with pytest.raises(ValueError):
        roll_multiple_dice(1.0, 6) # Float num_dice (not considered int by validation)
    with pytest.raises(ValueError):
        roll_multiple_dice("one", 6) # String num_dice
    with pytest.raises(ValueError):
        roll_multiple_dice(None, 6) # None num_dice

def test_roll_multiple_dice_invalid_sides():
    """
    Test that roll_multiple_dice raises a ValueError when 'sides'
    is not a positive integer.
    """
    # Use pytest.raises without asserting on the error message string
    with pytest.raises(ValueError):
        roll_multiple_dice(2, 0)  # Zero sides
    with pytest.raises(ValueError):
        roll_multiple_dice(2, -1) # Negative sides
    with pytest.raises(ValueError):
        roll_multiple_dice(2, 6.0) # Float sides (not considered int by validation)
    with pytest.raises(ValueError):
        roll_multiple_dice(2, "six") # String sides
    with pytest.raises(ValueError):
        roll_multiple_dice(2, None) # None sides

def test_roll_multiple_dice_invalid_both():
    """
    Test that roll_multiple_dice raises a ValueError when both 'num_dice'
    and 'sides' are invalid. It should prioritize the 'num_dice' error
    message as per the implementation's validation order.
    """
    # Use pytest.raises without asserting on the error message string
    with pytest.raises(ValueError):
        roll_multiple_dice(0, 0)  # Both invalid
    with pytest.raises(ValueError):
        roll_multiple_dice(-1, -1) # Both invalid