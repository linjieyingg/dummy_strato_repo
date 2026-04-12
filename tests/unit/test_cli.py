import pytest
import sys
from io import StringIO
from unittest.mock import patch

# Import module under test
from src.calculator.cli import main # Import the actual main function


# ============================================================================
# Fixtures
# ============================================================================

# Dummy operations for testing purposes, mimicking the behavior of the real ones
# These mocks ensure that the 'operations_map' can retrieve callables and their exceptions
def mock_add(a, b):
    # The actual cli.py converts inputs to float before calling,
    # so these mocks primarily ensure correct return values and specific exceptions.
    # The TypeError checks here are mainly for completeness if cli.py were to change.
    if not isinstance(a, (int, float)):
        raise TypeError("'a' must be a numeric value (int or float).")
    if not isinstance(b, (int, float)):
        raise TypeError("'b' must be a numeric value (int or float).")
    return a + b
def mock_subtract(a, b):
    if not isinstance(a, (int, float)):
        raise TypeError("'a' must be a numeric value (int or float).")
    if not isinstance(b, (int, float)):
        raise TypeError("'b' must be a numeric value (int or float).")
    return a - b
def mock_multiply(a, b):
    if not isinstance(a, (int, float)):
        raise TypeError("'a' must be a numeric value (int or float).")
    if not isinstance(b, (int, float)):
        raise TypeError("'b' must be a numeric value (int or float).")
    return a * b
def mock_divide(a, b):
    if not isinstance(a, (int, float)):
        raise TypeError("'a' must be a numeric value (int or float).")
    if not isinstance(b, (int, float)):
        raise TypeError("'b' must be a numeric value (int or float).")
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero.") # Match the actual message in src/calculator/operations.py
    return a / b

# Mock the entire src.calculator.operations module
@pytest.fixture(autouse=True)
def mock_operations_module(monkeypatch):
    """
    Mocks the src.calculator.operations module with dummy functions
    to isolate cli.py during testing.
    """
    class MockOperations:
        # Use staticmethod or just functions directly if they don't depend on self
        add = staticmethod(mock_add)
        subtract = staticmethod(mock_subtract)
        multiply = staticmethod(mock_multiply)
        divide = staticmethod(mock_divide)

    # When src/calculator/cli.py does 'from src.calculator.operations import ...',
    # it will get these mock functions instead of the real ones.
    monkeypatch.setitem(sys.modules, 'src.calculator.operations', MockOperations())


# --- Pytest test cases ---

def test_main_add_integers_happy_path(monkeypatch, capsys):
    """
    Test main function with a valid 'add' operation and integer inputs.
    """
    monkeypatch.setattr(sys, 'argv', ['calculator.py', 'add', '10', '5'])
    main()
    captured = capsys.readouterr()
    assert captured.out.strip() == "The result of add 10 and 5 is: 15.0"

def test_main_divide_float_result_happy_path(monkeypatch, capsys):
    """
    Test main function with a valid 'divide' operation and float inputs.
    """
    monkeypatch.setattr(sys, 'argv', ['calculator.py', 'divide', '10.0', '4'])
    main()
    captured = capsys.readouterr()
    assert captured.out.strip() == "The result of divide 10.0 and 4 is: 2.5"

def test_main_subtract_negative_numbers(monkeypatch, capsys):
    """
    Test main function with 'subtract' operation and negative numbers.
    """
    monkeypatch.setattr(sys, 'argv', ['calculator.py', 'subtract', '-5', '-10'])
    main()
    captured = capsys.readouterr()
    assert captured.out.strip() == "The result of subtract -5 and -10 is: 5.0"

def test_main_invalid_num1_input_error(monkeypatch, capsys):
    """
    Test main function with an invalid (non-numeric) input for num1.
    Expect a ValueError handled by main's error message.
    """
    monkeypatch.setattr(sys, 'argv', ['calculator.py', 'add', 'hello', '5'])
    main()
    captured = capsys.readouterr()
    expected_error_msg = "Error: Invalid numeric input. Please ensure 'hello' and '5' are valid numbers."
    assert captured.out.strip() == expected_error_msg

def test_main_zero_division_error(monkeypatch, capsys):
    """
    Test main function with 'divide' operation where num2 is zero.
    Expect a ZeroDivisionError handled by main's error message.
    """
    monkeypatch.setattr(sys, 'argv', ['calculator.py', 'divide', '10', '0'])
    main()
    captured = capsys.readouterr()
    # The error message should match the mock_divide function's error
    expected_error_msg = "Error: Cannot divide by zero."
    assert captured.out.strip() == expected_error_msg

def test_main_invalid_operation_exits_system(monkeypatch, capsys):
    """
    Test main function with an invalid operation string.
    argparse should raise SystemExit.
    """
    monkeypatch.setattr(sys, 'argv', ['calculator.py', 'invalid_op', '10', '5'])
    with pytest.raises(SystemExit):
        main()
    # argparse prints its own error message to stderr before exiting
    # We can't easily capture its specific error message as it's to stderr and part of SystemExit logic.
    # The important part is that it exits with SystemExit.
    # We can optionally check stderr if needed, but it's often verbose and parser-dependent.
    captured = capsys.readouterr()
    assert "invalid choice: 'invalid_op'" in captured.err


# ============================================================================
# Edge Case Tests
# ============================================================================