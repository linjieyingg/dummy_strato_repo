# src/number_utils.py
import numbers

def is_even_or_odd(num):
    """
    Determines if a given number is even or odd.

    This function primarily checks the parity of integers. If a float is provided,
    it checks if the float is numerically equivalent to an integer (e.g., 4.0).
    If it has a significant fractional part (e.g., 4.5), a ValueError is raised
    as the concept of even/odd is not strictly applicable.

    Args:
        num (int or float): The number to check.

    Returns:
        str: "even" if the number is even, "odd" if the number is odd.

    Raises:
        TypeError: If the input `num` is not an int or float.
        ValueError: If a float with a non-zero fractional part is provided,
                    indicating it's not an integer.

    Examples:
        >>> is_even_or_odd(4)
        'even'
        >>> is_even_or_odd(7)
        'odd'
        >>> is_even_or_odd(0)
        'even'
        >>> is_even_or_odd(-2)
        'even'
        >>> is_even_or_odd(5.0)
        'odd'
        >>> try:
        ...     is_even_or_odd(4.5)
        ... except ValueError as e:
        ...     print(e)
        Cannot determine even/odd for non-integer float: 4.5. Parity is only defined for integers.
        >>> try:
        ...     is_even_or_odd("hello")
        ... except TypeError as e:
        ...     print(e)
        Input must be a number (int or float).
    """
    if not isinstance(num, numbers.Number):
        raise TypeError("Input must be a number (int or float).")

    if isinstance(num, float):
        if not num.is_integer():
            raise ValueError(
                f"Cannot determine even/odd for non-integer float: {num}. "
                "Parity is only defined for integers."
            )
        # Convert float equivalent to an integer (e.g., 5.0 becomes 5)
        num = int(num)

    # Now 'num' is guaranteed to be an integer
    if num % 2 == 0:
        return "even"
    else:
        return "odd"