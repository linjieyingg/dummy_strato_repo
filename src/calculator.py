def add(a, b):
    """
    Adds two numbers together.

    Args:
        a (int or float): The first number.
        b (int or float): The second number.

    Returns:
        int or float: The sum of a and b.

    Raises:
        TypeError: If either a or b is not a numeric type (int or float).
    """
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("Both inputs must be numeric (int or float).")
    return a + b

def subtract(a, b):
    """
    Subtracts the second number from the first.

    Args:
        a (int or float): The number to subtract from.
        b (int or float): The number to subtract.

    Returns:
        int or float: The difference between a and b.

    Raises:
        TypeError: If either a or b is not a numeric type (int or float).
    """
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("Both inputs must be numeric (int or float).")
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
        TypeError: If either a or b is not a numeric type (int or float).
    """
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("Both inputs must be numeric (int or float).")
    return a * b

def divide(a, b):
    """
    Divides the first number by the second number.

    Args:
        a (int or float): The numerator.
        b (int or float): The denominator.

    Returns:
        float: The result of the division.

    Raises:
        TypeError: If either a or b is not a numeric type (int or float).
        ValueError: If the denominator b is zero.
    """
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("Both inputs must be numeric (int or float).")
    if b == 0:
        raise ValueError("Cannot divide by zero.")
    return a / b