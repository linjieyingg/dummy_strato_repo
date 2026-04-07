import re

def is_palindrome(text: str) -> bool:
    """
    Checks if a given string is a palindrome, ignoring case and non-alphanumeric characters.

    A palindrome is a word, phrase, number, or other sequence of characters
    which reads the same backward as forward.

    Args:
        text (str): The input string to check.

    Returns:
        bool: True if the string is a palindrome, False otherwise.

    Raises:
        TypeError: If the input 'text' is not a string.

    Example:
        >>> is_palindrome("Racecar")
        True
        >>> is_palindrome("A man, a plan, a canal: Panama")
        True
        >>> is_palindrome("hello")
        False
        >>> is_palindrome("")
        True
        >>> is_palindrome("12321")
        True
    """
    if not isinstance(text, str):
        raise TypeError("Input must be a string.")

    # Convert to lowercase and remove all non-alphanumeric characters
    # This prepares the string for a clean palindrome check
    processed_text = re.sub(r'[^a-z0-9]', '', text.lower())

    # A string is a palindrome if it reads the same forwards and backwards.
    # We compare the processed string with its reversed version.
    return processed_text == processed_text[::-1]

def decimal_to_binary(decimal_num: int) -> str:
    """
    Converts a non-negative decimal integer to its binary representation.

    Args:
        decimal_num (int): The non-negative decimal integer to convert.

    Returns:
        str: The binary representation of the decimal number as a string.

    Raises:
        TypeError: If the input 'decimal_num' is not an integer.
        ValueError: If the input 'decimal_num' is negative.

    Example:
        >>> decimal_to_binary(0)
        '0'
        >>> decimal_to_binary(1)
        '1'
        >>> decimal_to_binary(10)
        '1010'
        >>> decimal_to_binary(255)
        '11111111'
    """
    if not isinstance(decimal_num, int):
        raise TypeError("Input must be an integer.")
    if decimal_num < 0:
        raise ValueError("Input must be a non-negative integer.")

    if decimal_num == 0:
        return '0'

    binary_representation = []
    temp_num = decimal_num
    while temp_num > 0:
        binary_representation.append(str(temp_num % 2))
        temp_num //= 2
    
    return "".join(binary_representation[::-1])