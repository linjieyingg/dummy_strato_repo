"""
This module provides general-purpose string utility functions.
"""

def has_number(text: str) -> bool:
    """
    Checks if the given string contains at least one digit.

    Args:
        text: The input string to check.

    Returns:
        True if the string contains one or more digits, False otherwise.

    Raises:
        TypeError: If the input `text` is not a string.

    Examples:
        >>> has_number("hello")
        False
        >>> has_number("world123")
        True
        >>> has_number("no numbers here!")
        False
        >>> has_number("42 is the answer")
        True
        >>> has_number("")
        False
    """
    if not isinstance(text, str):
        raise TypeError("Input 'text' must be a string.")

    for char in text:
        if char.isdigit():
            return True
    return False