"""
This module provides core arithmetic operations: addition, subtraction,
multiplication, and division.

Each function includes input validation to ensure arguments are numeric
and handles specific arithmetic errors like division by zero.
"""


def _validate_numeric_input(value, param_name):
    """
    Helper function to validate if an input is a numeric type (int or float).

    Args:
        value: The input value to validate.
        param_name (str): The name of the parameter being validated, used in
                          error messages.

    Raises:
        TypeError: If the value is not an int or float.
    """
    if not isinstance(value, (int, float)):
        raise TypeError(f"'{param_name}' must be a numeric value (int or float).")


def add(a, b):
    """
    Adds two numbers together.

    Args:
        a (int or float): The first number.
        b (int or float): The second number.

    Returns:
        int or float: The sum of a and b.

    Raises:
        TypeError: If 'a' or 'b' is not a numeric type (int or float).
    """
    _validate_numeric_input(a, 'a')
    _validate_numeric_input(b, 'b')
    return a + b


def subtract(a, b):
    """
    Subtracts the second number from the first.

    Args:
        a (int or float): The number to subtract from (minuend).
        b (int or float): The number to subtract (subtrahend).

    Returns:
        int or float: The difference between a and b.

    Raises:
        TypeError: If 'a' or 'b' is not a numeric type (int or float).
    """
    _validate_numeric_input(a, 'a')
    _validate_numeric_input(b, 'b')
    return a - b


def multiply(a, b):
    """
    Multiplies two numbers together.

    Args:
        a (int or float): The first number.
        b (int or float): The second number.

    Returns:
        int or float: The product of a and b.

    Raises:
        TypeError: If 'a' or 'b' is not a numeric type (int or float).
    """
    _validate_numeric_input(a, 'a')
    _validate_numeric_input(b, 'b')
    return a * b


def divide(a, b):
    """
    Divides the first number by the second.

    Args:
        a (int or float): The numerator (dividend).
        b (int or float): The denominator (divisor).

    Returns:
        float: The result of the division.

    Raises:
        TypeError: If 'a' or 'b' is not a numeric type (int or float).
        ZeroDivisionError: If 'b' is zero.
    """
    _validate_numeric_input(a, 'a')
    _validate_numeric_input(b, 'b')
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero.")
    return a / b