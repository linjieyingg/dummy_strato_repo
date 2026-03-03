import pytest
from src.calculator import multiply

def test_multiply_integers():
    """
    Tests multiplication with positive integers.
    """
    assert multiply(2, 3) == 6
    assert multiply(10, 5) == 50
    assert multiply(1, 1) == 1

def test_multiply_floats():
    """
    Tests multiplication with floating-point numbers.
    """
    assert multiply(2.5, 2.0) == 5.0
    assert multiply(0.5, 0.5) == 0.25
    assert multiply(1.0, 3.14) == 3.14
    assert pytest.approx(multiply(0.1, 0.2)) == 0.02 # Use pytest.approx for float comparisons

def test_multiply_negative_numbers():
    """
    Tests multiplication with negative numbers, including mixed signs.
    """
    assert multiply(-2, 3) == -6
    assert multiply(2, -3) == -6
    assert multiply(-2, -3) == 6
    assert multiply(-5.0, 1.5) == -7.5

def test_multiply_by_zero():
    """
    Tests multiplication where one operand is zero.
    """
    assert multiply(5, 0) == 0
    assert multiply(0, 100) == 0
    assert multiply(0.0, 3.14) == 0.0
    assert multiply(-7, 0) == 0

def test_multiply_large_numbers():
    """
    Tests multiplication with large integer numbers.
    """
    assert multiply(1000000, 2) == 2000000
    assert multiply(123456789, 987654321) == 121932631112635269

def test_multiply_with_one():
    """
    Tests multiplication where one of the operands is 1 or -1.
    """
    assert multiply(10, 1) == 10
    assert multiply(1, -5) == -5
    assert multiply(-1, -7) == 7
    assert multiply(3.14, 1.0) == 3.14