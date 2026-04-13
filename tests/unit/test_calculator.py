"""
Tests for src/calculator.py
"""

import pytest
# Removed unused imports: from unittest.mock import Mock, patch, MagicMock

# Removed sys.path manipulation, relying on standard Python module resolution
# or proper test runner configuration.
# Explicitly import functions from src.calculator as per critical constraints.
from src.calculator import add, subtract, multiply, divide


# ============================================================================
# Fixtures
# ============================================================================


# ============================================================================
# Tests for add()
# ============================================================================

def test_add_positive_integers():
    """
    Test add function with positive integers.
    """
    assert add(2, 3) == 5
    assert add(0, 10) == 10

def test_add_floats():
    """
    Test add function with floating-point numbers.
    """
    assert add(1.5, 2.5) == pytest.approx(4.0)
    assert add(-0.1, 0.2) == pytest.approx(0.1)

def test_add_mixed_types_and_negatives():
    """
    Test add function with mixed integer/float types and negative numbers.
    """
    assert add(5, -3) == 2
    assert add(-7, -8) == -15
    assert add(10, 0.5) == pytest.approx(10.5)
    assert add(-2.5, 1) == pytest.approx(-1.5)

def test_add_raises_type_error_for_non_numeric_a():
    """
    Test add function raises TypeError when the first argument is not numeric.
    """
    with pytest.raises(TypeError):
        add("hello", 5)
    with pytest.raises(TypeError):
        add([1, 2], 3)

def test_add_raises_type_error_for_non_numeric_b():
    """
    Test add function raises TypeError when the second argument is not numeric.
    """
    with pytest.raises(TypeError):
        add(5, "world")
    with pytest.raises(TypeError):
        add(10, None)


# ============================================================================
# Tests for subtract()
# ============================================================================

# Removed incorrect import: from src.module import subtract
# The 'subtract' function is now imported at the top of the file.

def test_subtract_positive_integers():
    """
    Tests subtraction of positive integers.
    """
    assert subtract(5, 3) == 2
    assert subtract(10, 7) == 3

def test_subtract_floats_and_negative_numbers():
    """
    Tests subtraction with floats and negative numbers, including mixed types.
    """
    assert subtract(5.5, 2.0) == pytest.approx(3.5)
    assert subtract(10, 15.5) == pytest.approx(-5.5)
    assert subtract(-5, -2) == -3
    assert subtract(0.0, 7.5) == pytest.approx(-7.5)

def test_subtract_edge_cases_zero_and_self_subtraction():
    """
    Tests edge cases like subtracting zero or a number from itself.
    """
    assert subtract(7, 0) == 7
    assert subtract(0, 7) == -7
    assert subtract(5, 5) == 0
    assert subtract(-3.5, -3.5) == pytest.approx(0.0)

def test_subtract_type_error_non_numeric_input():
    """
    Tests that a TypeError is raised for non-numeric inputs.
    """
    with pytest.raises(TypeError):
        subtract("hello", 5)
    with pytest.raises(TypeError):
        subtract(10, [1, 2])
    with pytest.raises(TypeError):
        subtract(None, 2.5)
    with pytest.raises(TypeError):
        subtract("a", "b")


# ============================================================================
# Tests for multiply()
# ============================================================================

# Removed incorrect import: from your_module import multiply
# The 'multiply' function is now imported at the top of the file.

def test_multiply_positive_integers():
    """
    Tests multiplication of two positive integers.
    """
    assert multiply(2, 3) == 6
    assert multiply(10, 5) == 50

def test_multiply_with_floats():
    """
    Tests multiplication involving float numbers, including mixed types.
    """
    assert multiply(2.5, 2.0) == pytest.approx(5.0)
    assert multiply(0.5, 0.5) == pytest.approx(0.25)
    assert multiply(10, 0.1) == pytest.approx(1.0)
    assert multiply(3.14, 2) == pytest.approx(6.28)

def test_multiply_with_zero_and_negative_numbers():
    """
    Tests multiplication with zero and negative numbers, and their combinations.
    """
    assert multiply(5, 0) == 0
    assert multiply(0, 7) == 0
    assert multiply(-2, 3) == -6
    assert multiply(4, -5) == -20
    assert multiply(-6, -7) == 42
    assert multiply(-1.5, 2) == pytest.approx(-3.0)

def test_multiply_with_identity_element():
    """
    Tests multiplication with 1, which is the identity element.
    """
    assert multiply(10, 1) == 10
    assert multiply(1, 10) == 10
    assert multiply(5.5, 1) == pytest.approx(5.5)
    assert multiply(1, -7) == -7

def test_multiply_raises_type_error_for_non_numeric_inputs():
    """
    Tests that multiply raises a TypeError when either input is not a numeric type.
    """
    with pytest.raises(TypeError):
        multiply("hello", 5)
    with pytest.raises(TypeError):
        multiply(10, "world")
    with pytest.raises(TypeError):
        multiply([1, 2], 3)
    with pytest.raises(TypeError):
        multiply(4, None)
    with pytest.raises(TypeError):
        multiply({"a": 1}, 5)


# ============================================================================
# Tests for divide()
# ============================================================================

# The 'divide' function is now imported at the top of the file.

def test_divide_positive_integers_happy_path():
    """
    Test division with two positive integers resulting in an integer.
    """
    result = divide(10, 2)
    assert result == pytest.approx(5.0)

def test_divide_float_inputs_and_result():
    """
    Test division with float inputs resulting in a float.
    """
    result = divide(7.0, 2.0)
    assert result == pytest.approx(3.5)

def test_divide_with_negative_numbers():
    """
    Test division involving negative numbers to ensure correct sign handling.
    """
    result = divide(10, -2)
    assert result == pytest.approx(-5.0)
    result = divide(-10, -2)
    assert result == pytest.approx(5.0)

def test_divide_by_zero_raises_value_error():
    """
    Test that dividing by zero raises a ValueError.
    """
    with pytest.raises(ValueError):
        divide(5, 0)

def test_divide_non_numeric_input_raises_type_error():
    """
    Test that division with non-numeric inputs (a or b) raises a TypeError.
    """
    with pytest.raises(TypeError):
        divide("10", 2)
    with pytest.raises(TypeError):
        divide(10, "2")
    with pytest.raises(TypeError):
        divide("10", "2")


# ============================================================================
# Edge Case Tests
# ============================================================================