def subtract(minuend, subtrahend):
    """
    Calculates the difference between two numbers.

    Args:
        minuend (int | float): The number from which to subtract.
        subtrahend (int | float): The number to subtract from the minuend.

    Returns:
        int | float: The result of minuend - subtrahend.

    Raises:
        TypeError: If either minuend or subtrahend is not an int or float.

    Examples:
        >>> subtract(10, 5)
        5
        >>> subtract(5.5, 2.0)
        3.5
        >>> subtract(0, 10)
        -10
    """
    if not isinstance(minuend, (int, float)):
        raise TypeError("Minuend must be an integer or a float.")
    if not isinstance(subtrahend, (int, float)):
        raise TypeError("Subtrahend must be an integer or a float.")

    return minuend - subtrahend


if __name__ == "__main__":
    # Example usage and basic tests
    print(f"10 - 5 = {subtract(10, 5)}")
    print(f"5.5 - 2.0 = {subtract(5.5, 2.0)}")
    print(f"0 - 10 = {subtract(0, 10)}")
    print(f"10 - 0 = {subtract(10, 0)}")

    # Test with negative numbers
    print(f"-5 - 3 = {subtract(-5, 3)}")
    print(f"10 - (-5) = {subtract(10, -5)}")

    # Test error handling
    try:
        subtract("hello", 5)
    except TypeError as e:
        print(f"Error: {e}")

    try:
        subtract(10, "world")
    except TypeError as e:
        print(f"Error: {e}")

    try:
        subtract([1, 2], 5)
    except TypeError as e:
        print(f"Error: {e}")

    try:
        subtract(10, None)
    except TypeError as e:
        print(f"Error: {e}")