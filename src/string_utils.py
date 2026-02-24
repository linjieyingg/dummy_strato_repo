import string

def is_palindrome(text: str) -> bool:
    """
    Checks if a given string `text` is a palindrome.

    A palindrome is a word, phrase, number, or other sequence of characters
    which reads the same backward as forward, ignoring capitalization, spaces,
    and punctuation.

    Args:
        text (str): The string to check.

    Returns:
        bool: True if the string is a palindrome, False otherwise.

    Raises:
        TypeError: If the input `text` is not a string.

    Example Usage:
        >>> is_palindrome("madam")
        True
        >>> is_palindrome("A man, a plan, a canal: Panama")
        True
        >>> is_palindrome("Racecar")
        True
        >>> is_palindrome("hello")
        False
        >>> is_palindrome("No lemon, no melon")
        True
        >>> is_palindrome("")
        True
        >>> is_palindrome("  !@#$%^  ")
        True
    """
    if not isinstance(text, str):
        raise TypeError("Input 'text' must be a string.")

    # Convert to lowercase and filter out non-alphanumeric characters
    # This handles capitalization, spaces, and punctuation as per requirements
    cleaned_text_chars = [char for char in text.lower() if char.isalnum()]
    cleaned_text = "".join(cleaned_text_chars)

    # An empty string or a string with only non-alphanumeric characters
    # (resulting in an empty cleaned_text) is considered a palindrome.
    # For example, is_palindrome("!@#") will result in cleaned_text=""
    # and "" == ""[::-1] will be True.
    return cleaned_text == cleaned_text[::-1]