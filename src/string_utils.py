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


def count_vowels(s: str) -> int:
    """
    Counts the number of vowels (a, e, i, o, u, case-insensitive) in a string.

    Args:
        s (str): The input string.

    Returns:
        int: The number of vowels in the string.

    Raises:
        TypeError: If the input `s` is not a string.

    Example Usage:
        >>> count_vowels("Hello World")
        3
        >>> count_vowels("Python")
        1
        >>> count_vowels("AEIOU")
        5
        >>> count_vowels("rhythm")
        0
        >>> count_vowels("")
        0
    """
    if not isinstance(s, str):
        raise TypeError("Input 's' must be a string.")
    vowels = "aeiou"
    return sum(1 for char in s.lower() if char in vowels)


def capitalize_words(s: str) -> str:
    """
    Capitalizes the first letter of each word in a string.

    Args:
        s (str): The input string.

    Returns:
        str: The string with the first letter of each word capitalized.

    Raises:
        TypeError: If the input `s` is not a string.

    Example Usage:
        >>> capitalize_words("hello world")
        'Hello World'
        >>> capitalize_words("python programming")
        'Python Programming'
        >>> capitalize_words("  leading and trailing spaces  ")
        '  Leading And Trailing Spaces  '
        >>> capitalize_words("")
        ''
        >>> capitalize_words("already Capitalized")
        'Already Capitalized'
    """
    if not isinstance(s, str):
        raise TypeError("Input 's' must be a string.")
    return s.title()


def is_anagram(s1: str, s2: str) -> bool:
    """
    Checks if two strings are anagrams of each other.

    An anagram is a word or phrase formed by rearranging the letters of a
    different word or phrase, typically using all the original letters exactly once.
    This function ignores capitalization, spaces, and punctuation.

    Args:
        s1 (str): The first string.
        s2 (str): The second string.

    Returns:
        bool: True if the strings are anagrams, False otherwise.

    Raises:
        TypeError: If either `s1` or `s2` is not a string.

    Example Usage:
        >>> is_anagram("listen", "silent")
        True
        >>> is_anagram("Debit Card", "Bad Credit")
        True
        >>> is_anagram("hello", "world")
        False
        >>> is_anagram("A gentleman", "Elegant man")
        True
        >>> is_anagram("", "")
        True
        >>> is_anagram("a", "a")
        True
        >>> is_anagram("a", "b")
        False
        >>> is_anagram("restful", "fluster")
        True
    """
    if not isinstance(s1, str) or not isinstance(s2, str):
        raise TypeError("Both inputs 's1' and 's2' must be strings.")

    def clean_string(s):
        # Convert to lowercase and filter out non-alphanumeric characters
        return "".join(sorted([char for char in s.lower() if char.isalnum()]))

    cleaned_s1 = clean_string(s1)
    cleaned_s2 = clean_string(s2)

    return cleaned_s1 == cleaned_s2


def remove_spaces(s: str) -> str:
    """
    Removes all space characters from a string.

    Args:
        s (str): The input string.

    Returns:
        str: The string with all spaces removed.

    Raises:
        TypeError: If the input `s` is not a string.

    Example Usage:
        >>> remove_spaces("hello world")
        'helloworld'
        >>> remove_spaces("  leading and trailing spaces  ")
        'leadingandtrailingspaces'
        >>> remove_spaces("")
        ''
        >>> remove_spaces("nospaceshere")
        'nospaceshere'
        >>> remove_spaces("a b c d")
        'abcd'
    """
    if not isinstance(s, str):
        raise TypeError("Input 's' must be a string.")
    return s.replace(" ", "")


def find_longest_word(s: str) -> str:
    """
    Finds the longest word in a string.
    Words are separated by spaces. If multiple words have the same longest length,
    the first one encountered is returned. If the string is empty or contains no words,
    an empty string is returned.

    Args:
        s (str): The input string.

    Returns:
        str: The longest word found in the string. Returns an empty string
             if no words are found.

    Raises:
        TypeError: If the input `s` is not a string.

    Example Usage:
        >>> find_longest_word("The quick brown fox jumps over the lazy dog")
        'quick'
        >>> find_longest_word("a bb ccc dddd")
        'dddd'
        >>> find_longest_word("one two three four five")
        'three'
        >>> find_longest_word("apple banana cherry date")
        'cherry'
        >>> find_longest_word("")
        ''
        >>> find_longest_word("   ")
        ''
        >>> find_longest_word("word")
        'word'
    """
    if not isinstance(s, str):
        raise TypeError("Input 's' must be a string.")

    words = s.split()  # Splits by whitespace and removes empty strings
    if not words:
        return ""

    longest_word = ""
    for word in words:
        if len(word) > len(longest_word):
            longest_word = word
    return longest_word