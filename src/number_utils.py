# src/number_utils.py
import numbers
from typing import Union

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

def check_number_sign(num: Union[int, float]) -> str:
    """
    Determines if a given number is positive, negative, or zero.

    Args:
        num (Union[int, float]): The number to check its sign.

    Returns:
        str: "positive" if the number is greater than zero.
             "negative" if the number is less than zero.
             "zero" if the number is exactly zero.

    Raises:
        TypeError: If the input `num` is not an int or float.

    Examples:
        >>> check_number_sign(5)
        'positive'
        >>> check_number_sign(-3.5)
        'negative'
        >>> check_number_sign(0)
        'zero'
        >>> check_number_sign(100.0)
        'positive'
        >>> try:
        ...     check_number_sign("abc")
        ... except TypeError as e:
        ...     print(e)
        Input must be a number (int or float).
    """
    if not isinstance(num, (int, float)):
        raise TypeError("Input must be a number (int or float).")

    if num > 0:
        return "positive"
    elif num < 0:
        return "negative"
    else:
        return "zero"