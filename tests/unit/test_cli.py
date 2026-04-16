import pytest
import sys
from unittest.mock import patch # Only patch is needed

from src.cli import main
# Removed 'from src import dice_roller' as we are now patching `src.cli.roll_multiple_dice`

# ============================================================================
# Fixtures
# ============================================================================


# ============================================================================
# Tests for main()
# ============================================================================

# Redundant imports are removed from here as they are already at the top of the file

def test_main_default_arguments_happy_path(capsys):
    """
    Tests main with default arguments (1 D6) and a successful dice roll.
    Verifies correct output to stdout.
    """
    # Simulate command: python src/cli.py
    test_args = ['cli.py']
    with patch.object(sys, 'argv', test_args):
        # CRITICAL FIX: Patch 'src.cli.roll_multiple_dice' as it's the reference used in cli.py
        with patch('src.cli.roll_multiple_dice', return_value=[3]):
            main()
            captured = capsys.readouterr()
            assert "Rolling 1 D6 dice..." in captured.out
            assert "Individual rolls: [3]" in captured.out
            assert "Total sum: 3" in captured.out
            assert captured.err == ""

def test_main_custom_arguments_happy_path(capsys):
    """
    Tests main with custom arguments (2 D10) and a successful dice roll.
    Verifies correct output to stdout.
    """
    # Simulate command: python src/cli.py -n 2 -s 10
    test_args = ['cli.py', '-n', '2', '--sides', '10']
    with patch.object(sys, 'argv', test_args):
        # CRITICAL FIX: Patch 'src.cli.roll_multiple_dice'
        with patch('src.cli.roll_multiple_dice', return_value=[5, 8]):
            main()
            captured = capsys.readouterr()
            assert "Rolling 2 D10 dice..." in captured.out
            assert "Individual rolls: [5, 8]" in captured.out
            assert "Total sum: 13" in captured.out
            assert captured.err == ""

def test_main_value_error_from_dice_roller(capsys):
    """
    Tests main's error handling when `roll_multiple_dice` raises a ValueError.
    Verifies error message to stderr and sys.exit(1).
    """
    # Simulate command: python src/cli.py (with args that would cause ValueError in real `roll_multiple_dice`,
    # but here the mock dictates the error)
    test_args = ['cli.py', '-n', '1', '-s', '6'] # Arguments are valid, but mock will raise error
    error_message = "Number of dice must be positive."
    with patch.object(sys, 'argv', test_args):
        # CRITICAL FIX: Patch 'src.cli.roll_multiple_dice'
        with patch('src.cli.roll_multiple_dice', side_effect=ValueError(error_message)):
            with pytest.raises(SystemExit) as excinfo:
                main()
            captured = capsys.readouterr()
            assert excinfo.value.code == 1 # Expect exit code 1 for application errors
            assert captured.out == ""
            assert f"Error: {error_message}" in captured.err

def test_main_argparse_error_invalid_type(capsys):
    """
    Tests main's handling of invalid argument types provided via command line.
    Verifies argparse error message to stderr and sys.exit(2).
    """
    # Simulate command: python src/cli.py -s abc (invalid type for sides)
    test_args = ['cli.py', '--sides', 'abc']
    with patch.object(sys, 'argv', test_args):
        # Argparse will raise SystemExit(2) before calling `roll_multiple_dice`
        with pytest.raises(SystemExit) as excinfo:
            main()
        captured = capsys.readouterr()
        assert excinfo.value.code == 2 # Argparse exits with code 2 for argument errors
        assert captured.out == ""
        assert "argument -s/--sides: invalid int value: 'abc'" in captured.err

def test_main_unexpected_error_during_roll(capsys):
    """
    Tests main's general error handling for unexpected exceptions from `roll_multiple_dice`.
    Verifies generic error message to stderr and sys.exit(1).
    """
    # Simulate command: python src/cli.py (with valid args, but an unexpected internal error)
    test_args = ['cli.py', '-n', '1', '-s', '6']
    unexpected_error_message = "A mysterious force prevented the dice from rolling."
    with patch.object(sys, 'argv', test_args):
        # CRITICAL FIX: Patch 'src.cli.roll_multiple_dice'
        with patch('src.cli.roll_multiple_dice', side_effect=Exception(unexpected_error_message)):
            with pytest.raises(SystemExit) as excinfo:
                main()
            captured = capsys.readouterr()
            assert excinfo.value.code == 1 # Expect exit code 1 for application errors
            assert captured.out == ""
            assert f"An unexpected error occurred: {unexpected_error_message}" in captured.err


# ============================================================================
# Edge Case Tests
# ============================================================================