import pytest
from unittest.mock import Mock, patch, MagicMock
from typing import Any, List, Dict

# Import module under test
from src.calculator.operations import add, subtract, multiply, divide



# ============================================================================
# Fixtures
# ============================================================================


# ============================================================================
# Tests for add()
# ============================================================================

def test_add_positive_integers_correctly():
    """
    Test that add correctly sums two positive integers.
    """
    assert add(5, 3) == 8

def test_add_floats_and_mixed_types_correctly():
    """
    Test that add correctly sums floats and a mix of integers and floats.
    """
    assert add(2.5, 1.5) == 4.0
    assert add(7, 3.14) == 10.14
    assert add(-2.5, 1.0) == -1.5

def test_add_with_zero_and_negative_numbers():
    """
    Test add with zero and negative numbers.
    """
    assert add(0, 0) == 0
    assert add(5, 0) == 5
    assert add(0, -10) == -10
    assert add(-5, -3) == -8
    assert add(-5, 2) == -3

def test_add_raises_type_error_for_non_numeric_a():
    """
    Test that add raises TypeError when 'a' is not numeric.
    """
    with pytest.raises(TypeError) as excinfo:
        add('hello', 5)
    assert str(excinfo.value) == "'a' must be a numeric value (int or float)."

def test_add_raises_type_error_for_non_numeric_b():
    """
    Test that add raises TypeError when 'b' is not numeric.
    """
    with pytest.raises(TypeError) as excinfo:
        add(10, [2])
    assert str(excinfo.value) == "'b' must be a numeric value (int or float)."


# ============================================================================
# Tests for subtract()
# ============================================================================

def test_subtract_basic_integers_and_floats():
    """Test subtract with basic positive and negative integers, and floats."""
    assert subtract(5, 3) == 2
    assert subtract(10.0, 5.0) == 5.0
    assert subtract(7, 3.5) == 3.5
    assert subtract(3.5, 7) == -3.5
    assert subtract(-5, -3) == -2
    assert subtract(1000, 500) == 500
    assert subtract(0.1, 0.2) == pytest.approx(-0.1) # Using pytest.approx for float comparison

def test_subtract_with_zero_and_negatives():
    """Test subtract with zero and various combinations of negative numbers."""
    assert subtract(5, 0) == 5
    assert subtract(0, 5) == -5
    assert subtract(-5, 3) == -8
    assert subtract(5, -3) == 8
    assert subtract(0, 0) == 0
    assert subtract(0.0, -5.5) == 5.5

def test_subtract_type_error_non_numeric_a():
    """Test TypeError when 'a' is not a numeric type."""
    with pytest.raises(TypeError) as excinfo:
        subtract("hello", 5)
    assert str(excinfo.value) == "'a' must be a numeric value (int or float)."

    with pytest.raises(TypeError) as excinfo:
        subtract(None, 10)
    assert str(excinfo.value) == "'a' must be a numeric value (int or float)."

def test_subtract_type_error_non_numeric_b():
    """Test TypeError when 'b' is not a numeric type."""
    with pytest.raises(TypeError) as excinfo:
        subtract(10, "world")
    assert str(excinfo.value) == "'b' must be a numeric value (int or float)."

    with pytest.raises(TypeError) as excinfo:
        subtract(100, [1, 2])
    assert str(excinfo.value) == "'b' must be a numeric value (int or float)."


# ============================================================================
# Tests for multiply()
# ============================================================================


@pytest.mark.parametrize(
    "a, b, expected",
    [
        (2, 3, 6),                 # Positive integers
        (-2, 3, -6),               # Negative and positive integer
        (2, -3, -6),               # Positive and negative integer
        (-2, -3, 6),               # Negative integers
        (2.5, 2, 5.0),             # Float and integer
        (2, 2.5, 5.0),             # Integer and float
        (1.5, 2.5, 3.75),          # Floats
        (1000000, 2, 2000000),     # Large numbers
        (0.1, 0.2, pytest.approx(0.02)), # Small floats
        (5, 1, 5),                 # Identity multiplication
        (1, 5, 5),                 # Identity multiplication
    ]
)
def test_multiply_happy_path_integers_and_floats(a, b, expected):
    """
    Test multiply with various valid integer and float combinations,
    including positive, negative, and mixed types.
    """
    assert multiply(a, b) == expected

@pytest.mark.parametrize(
    "a, b, expected",
    [
        (0, 5, 0),                 # Zero times positive
        (5, 0, 0),                 # Positive times zero
        (0, -5, 0),                # Zero times negative
        (-5, 0, 0),                # Negative times zero
        (0.0, 5, 0.0),             # Float zero times positive
        (5, 0.0, 0.0),             # Positive times float zero
        (0, 0, 0),                 # Zero times zero
    ]
)
def test_multiply_with_zero(a, b, expected):
    """
    Test multiply when one or both operands are zero.
    """
    assert multiply(a, b) == expected


@pytest.mark.parametrize(
    "a, b, expected",
    [
        (True, 5, 5),      # True (1) * 5 = 5
        (False, 5, 0),     # False (0) * 5 = 0
        (5, True, 5),      # 5 * True (1) = 5
        (5, False, 0),     # 5 * False (0) = 0
        (True, True, 1),   # True (1) * True (1) = 1
        (False, False, 0), # False (0) * False (0) = 0
    ]
)
def test_multiply_with_booleans(a, b, expected):
    """
    Test multiply with boolean values, which are treated as integers (1 for True, 0 for False).
    """
    assert multiply(a, b) == expected


@pytest.mark.parametrize(
    "a, b, param_name",
    [
        ("hello", 5, 'a'),           # String for 'a'
        (None, 5, 'a'),              # None for 'a'
        ([1, 2], 5, 'a'),            # List for 'a'
        ({'key': 1}, 5, 'a'),        # Dictionary for 'a'
    ]
)
def test_multiply_type_error_for_a(a, b, param_name):
    """
    Test that multiply raises TypeError when the first argument 'a' is not a numeric type.
    """
    with pytest.raises(TypeError) as excinfo:
        multiply(a, b)
    assert str(excinfo.value) == f"'{param_name}' must be a numeric value (int or float)."


@pytest.mark.parametrize(
    "a, b, param_name",
    [
        (5, "world", 'b'),           # String for 'b'
        (5, None, 'b'),              # None for 'b'
        (5, [1, 2], 'b'),            # List for 'b'
        (5, {'key': 1}, 'b'),        # Dictionary for 'b'
    ]
)
def test_multiply_type_error_for_b(a, b, param_name):
    """
    Test that multiply raises TypeError when the second argument 'b' is not a numeric type.
    """
    with pytest.raises(TypeError) as excinfo:
        multiply(a, b)
    assert str(excinfo.value) == f"'{param_name}' must be a numeric value (int or float)."


# ============================================================================
# Tests for divide()
# ============================================================================

def test_divide_positive_integers_happy_path():
    """Test division of two positive integers."""
    assert divide(10, 2) == 5.0
    assert divide(7, 2) == 3.5

def test_divide_positive_floats_happy_path():
    """Test division of two positive floats."""
    assert divide(10.0, 2.0) == 5.0
    assert divide(7.5, 2.5) == 3.0
    assert divide(10.0, 3.0) == pytest.approx(3.3333333333333335)

def test_divide_with_negative_numbers():
    """Test division involving negative numbers."""
    assert divide(-10, 2) == -5.0
    assert divide(10, -2) == -5.0
    assert divide(-10, -2) == 5.0
    assert divide(5, -2) == -2.5

def test_divide_zero_by_non_zero():
    """Test division of zero by a non-zero number."""
    assert divide(0, 5) == 0.0
    assert divide(0.0, -2.5) == 0.0

def test_divide_by_one():
    """Test division by one, an edge case."""
    assert divide(10, 1) == 10.0
    assert divide(7.5, 1) == 7.5
    assert divide(-5, 1) == -5.0

def test_divide_type_error_for_a():
    """Test TypeError when 'a' is not a numeric type."""
    with pytest.raises(TypeError) as excinfo:
        divide("10", 2)
    assert str(excinfo.value) == "'a' must be a numeric value (int or float)."

def test_divide_type_error_for_b():
    """Test TypeError when 'b' is not a numeric type."""
    with pytest.raises(TypeError) as excinfo:
        divide(10, [2])
    assert str(excinfo.value) == "'b' must be a numeric value (int or float)."

def test_divide_zero_division_error():
    """Test ZeroDivisionError when 'b' is zero."""
    with pytest.raises(ZeroDivisionError) as excinfo:
        divide(10, 0)
    assert str(excinfo.value) == "Cannot divide by zero."

def test_divide_zero_division_error_with_float_zero():
    """Test ZeroDivisionError when 'b' is float zero."""
    with pytest.raises(ZeroDivisionError) as excinfo:
        divide(10, 0.0)
    assert str(excinfo.value) == "Cannot divide by zero."


# ============================================================================
# Edge Case Tests
# ============================================================================