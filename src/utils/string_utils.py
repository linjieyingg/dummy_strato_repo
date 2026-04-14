import re

def is_palindrome(text: str) -> bool:
    """
    Checks if a given string is a palindrome.

    A string is considered a palindrome if it reads the same forwards and
    backwards, ignoring case and non-alphanumeric characters.

    Args:
        text (str): The string to check.

    Returns:
        bool: True if the string is a palindrome, False otherwise.

    Raises:
        TypeError: If the input `text` is not a string.

    Examples:
        >>> is_palindrome("madam")
        True
        >>> is_palindrome("A man, a plan, a canal: Panama")
        True
        >>> is_palindrome("hello")
        False
        >>> is_palindrome("racecar!")
        True
        >>> is_palindrome("")
        True
        >>> is_palindrome("a")
        True
    """
    if not isinstance(text, str):
        raise TypeError("Input must be a string.")

    # Convert to lowercase and remove non-alphanumeric characters
    # using a regular expression.
    cleaned_text = re.sub(r'[^a-z0-9]', '', text.lower())

    # Compare the cleaned string with its reverse
    return cleaned_text == cleaned_text[::-1]

# You can add more string utility functions here in the future
# For example:
# def reverse_string(text: str) -> str:
#     if not isinstance(text, str):
#         raise TypeError("Input must be a string.")
#     return text[::-1]