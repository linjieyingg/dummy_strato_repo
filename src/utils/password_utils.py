import re

def has_number(s: str) -> bool:
    """
    Checks if a string contains at least one digit.

    This function iterates through the input string to determine if any
    of its characters are digits (0-9).

    Args:
        s (str): The string to check.

    Returns:
        bool: True if the string contains at least one digit, False otherwise.

    Raises:
        TypeError: If the input `s` is not a string.

    Examples:
        >>> has_number("hello123world")
        True
        >>> has_number("HelloWorld")
        False
        >>> has_number("12345")
        True
        >>> has_number("")
        False
    """
    if not isinstance(s, str):
        raise TypeError("Input 's' must be a string.")

    # A simple and efficient way to check for a digit
    return any(char.isdigit() for char in s)

    # Alternative using regular expressions (if re module is already used elsewhere or preferred)
    # return bool(re.search(r'\d', s))