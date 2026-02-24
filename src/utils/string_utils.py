import collections

def reverse_string(s: str) -> str:
    """
    Reverses a given string `s`.

    Args:
        s (str): The input string to be reversed.

    Returns:
        str: The reversed string.

    Raises:
        TypeError: If the input `s` is not a string.

    Example:
        >>> reverse_string("hello")
        'olleh'
        >>> reverse_string("Python")
        'nohtyP'
        >>> reverse_string("")
        ''
    """
    if not isinstance(s, str):
        raise TypeError("Input must be a string.")
    return s[::-1]

def count_vowels(s: str) -> int:
    """
    Counts the number of vowels (a, e, i, o, u, case-insensitive) in a given string.

    Args:
        s (str): The input string.

    Returns:
        int: The total count of vowels in the string.

    Raises:
        TypeError: If the input `s` is not a string.

    Example:
        >>> count_vowels("Hello World")
        3
        >>> count_vowels("AEIOU")
        5
        >>> count_vowels("rhythm")
        0
        >>> count_vowels("")
        0
    """
    if not isinstance(s, str):
        raise TypeError("Input must be a string.")
    vowels = "aeiou"
    return sum(1 for char in s if char.lower() in vowels)

def count_alphabetic_characters(s: str) -> int:
    """
    Counts the number of alphabetic characters (a-z, A-Z) in a given string.

    Args:
        s (str): The input string.

    Returns:
        int: The total count of alphabetic characters.

    Raises:
        TypeError: If the input `s` is not a string.

    Example:
        >>> count_alphabetic_characters("Hello World!")
        10
        >>> count_alphabetic_characters("123abcDEF")
        6
        >>> count_alphabetic_characters("!@#$%^")
        0
        >>> count_alphabetic_characters("")
        0
    """
    if not isinstance(s, str):
        raise TypeError("Input must be a string.")
    return sum(1 for char in s if char.isalpha())

# Example usage (for demonstration, not part of production code usually)
if __name__ == "__main__":
    print(f"Reversed 'hello': {reverse_string('hello')}")
    print(f"Vowel count in 'Programming is fun': {count_vowels('Programming is fun')}")
    print(f"Alphabetic character count in 'Python 3.9.5!': {count_alphabetic_characters('Python 3.9.5!')}")

    try:
        reverse_string(123)
    except TypeError as e:
        print(f"Error for reverse_string with non-string input: {e}")

    try:
        count_vowels(None)
    except TypeError as e:
        print(f"Error for count_vowels with non-string input: {e}")

    try:
        count_alphabetic_characters([1, 2, 3])
    except TypeError as e:
        print(f"Error for count_alphabetic_characters with non-string input: {e}")