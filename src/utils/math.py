import numbers

def absolute_value(num: int | float) -> int | float:
    """
    Returns the absolute value of a given number.

    This function takes an integer or a float and returns its absolute value.
    The absolute value of a number is its distance from zero, always a non-negative number.

    Args:
        num (int | float): The number for which to calculate the absolute value.
                           Must be an integer or a float.

    Returns:
        int | float: The absolute value of the input number. The return type
                     will match the input type if it's an int, or be a float
                     if the input was a float.

    Raises:
        TypeError: If the input 'num' is not an integer or a float.

    Examples:
        >>> absolute_value(5)
        5
        >>> absolute_value(-10)
        10
        >>> absolute_value(3.14)
        3.14
        >>> absolute_value(-0.5)
        0.5
        >>> absolute_value(0)
        0
    """
    if not isinstance(num, numbers.Number) or isinstance(num, bool):
        # We specifically check for numbers.Number (excluding bool, which is a subclass of int)
        # to ensure it's a numeric type that abs() can handle naturally.
        raise TypeError("Input 'num' must be an integer or a float.")
    
    return abs(num)