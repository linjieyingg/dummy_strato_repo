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