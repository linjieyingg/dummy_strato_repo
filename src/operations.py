def add(a, b):
    """
    Adds two numbers and returns their sum.

    Args:
        a (int or float): The first number.
        b (int or float): The second number.

    Returns:
        (int or float): The sum of 'a' and 'b'.

    Raises:
        TypeError: If either 'a' or 'b' is not an int or float.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("Argument 'a' must be an integer or a float.")
    if not isinstance(b, (int, float)):
        raise TypeError("Argument 'b' must be an integer or a float.")
    
    return a + b

def divide(numerator, denominator):
    """
    Divides two numbers and returns the quotient.

    Args:
        numerator (int or float): The number to be divided.
        denominator (int or float): The number to divide by.

    Returns:
        (float): The result of the division (numerator / denominator).

    Raises:
        TypeError: If either 'numerator' or 'denominator' is not an int or float.
        ValueError: If 'denominator' is zero.
    """
    if not isinstance(numerator, (int, float)):
        raise TypeError("Argument 'numerator' must be an integer or a float.")
    if not isinstance(denominator, (int, float)):
        raise TypeError("Argument 'denominator' must be an integer or a float.")
    
    if denominator == 0:
        raise ValueError("Cannot divide by zero.")
    
    return float(numerator) / denominator