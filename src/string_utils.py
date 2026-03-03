"""src/string_utils.py"""
import string


def reverse_string(text: str) -> str:
    """
    Reverses a given string.

    Args:
        text (str): The string to reverse.

    Returns:
        str: The reversed string.

    Raises:
        TypeError: If the input is not a string.

    Example Usage:
        >>> reverse_string("hello")
        'olleh'
        >>> reverse_string("madam")
        'madam'
    """
    if not isinstance(text, str):
        raise TypeError("Input 'text' must be a string.")
    return text[::-1]


def count_vowels(text: str) -> int:
    """
    Counts the number of vowels (a, e, i, o, u) in a string, case-insensitive.

    Args:
        text (str): The string to count vowels in.

    Returns:
        int: The number of vowels in the string.

    Raises:
        TypeError: If the input is not a string.

    Example Usage:
        >>> count_vowels("hello")
        2
        >>> count_vowels("AEIOU")
        5
        >>> count_vowels("rhythm")
        0
    """
    if not isinstance(text, str):
        raise TypeError("Input 'text' must be a string.")
    return sum(1 for char in text.lower() if char in 'aeiou')


def count_letters(text: str) -> int:
    """
    Counts the number of alphabetic characters in a string.

    Args:
        text (str): The string to count letters in.

    Returns:
        int: The number of alphabetic characters in the string.

    Raises:
        TypeError: If the input is not a string.

    Example Usage:
        >>> count_letters("hello world")
        10
        >>> count_letters("abc123")
        3
        >>> count_letters("!@#$")
        0
    """
    if not isinstance(text, str):
        raise TypeError("Input 'text' must be a string.")
    return sum(1 for char in text if char.isalpha())


def is_palindrome(text: str) -> bool:
    """
    Checks if a given string is a palindrome, ignoring capitalization,
    spaces, and punctuation.

    Args:
        text (str): The string to check.

    Returns:
        bool: True if the string is a palindrome, False otherwise.

    Raises:
        TypeError: If the input is not a string.

    Example Usage:
        >>> is_palindrome("madam")
        True
        >>> is_palindrome("A man, a plan, a canal: Panama")
        True
        >>> is_palindrome("hello")
        False
    """
    if not isinstance(text, str):
        raise TypeError("Input 'text' must be a string.")
    cleaned = "".join(char for char in text.lower() if char.isalnum())
    return cleaned == cleaned[::-1]
