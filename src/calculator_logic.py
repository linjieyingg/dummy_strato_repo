def _is_numeric(value):
    """
    Helper function to check if a value is an integer or a float.
    """
    return isinstance(value, (int, float))

def add(a, b):
    """
    Adds two numbers.

    Args:
        a (int or float): The first number.
        b (int or float): The second number.

    Returns:
        int or float: The sum of a and b.

    Raises:
        TypeError: If either a or b is not a numeric type.
    """
    if not _is_numeric(a):
        raise TypeError("Input 'a' must be a numeric type (int or float).")
    if not _is_numeric(b):
        raise TypeError("Input 'b' must be a numeric type (int or float).")
    return a + b

def subtract(a, b):
    """
    Subtracts the second number from the first number.

    Args:
        a (int or float): The first number (minuend).
        b (int or float): The second number (subtrahend).

    Returns:
        int or float: The difference between a and b.

    Raises:
        TypeError: If either a or b is not a numeric type.
    """
    if not _is_numeric(a):
        raise TypeError("Input 'a' must be a numeric type (int or float).")
    if not _is_numeric(b):
        raise TypeError("Input 'b' must be a numeric type (int or float).")
    return a - b

def multiply(a, b):
    """
    Multiplies two numbers.

    Args:
        a (int or float): The first number.
        b (int or float): The second number.

    Returns:
        int or float: The product of a and b.

    Raises:
        TypeError: If either a or b is not a numeric type.
    """
    if not _is_numeric(a):
        raise TypeError("Input 'a' must be a numeric type (int or float).")
    if not _is_numeric(b):
        raise TypeError("Input 'b' must be a numeric type (int or float).")
    return a * b

def divide(a, b):
    """
    Divides the first number by the second number.

    Args:
        a (int or float): The dividend.
        b (int or float): The divisor.

    Returns:
        float: The result of the division.

    Raises:
        TypeError: If either a or b is not a numeric type.
        ValueError: If b is zero (division by zero).
    """
    if not _is_numeric(a):
        raise TypeError("Input 'a' must be a numeric type (int or float).")
    if not _is_numeric(b):
        raise TypeError("Input 'b' must be a numeric type (int or float).")
    if b == 0:
        raise ValueError("Cannot divide by zero.")
    return a / b