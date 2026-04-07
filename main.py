import os
import re

def _update_readme_section(readme_file_path, section_header, entry_markdown, entry_title_prefix):
    """
    Updates or creates a specific section in the README.md file with new content.
    If the section exists, it adds the entry if not already present.
    If the section doesn't exist, it creates it and adds the entry.
    If the README.md file doesn't exist, it creates a basic one and adds the section and entry.

    Args:
        readme_file_path (str): The path to the README.md file.
        section_header (str): The markdown header for the section (e.g., "## Commands").
        entry_markdown (str): The markdown content for the entry to be inserted.
        entry_title_prefix (str): The markdown prefix for the entry's title (e.g., "###").
                                  Used to extract the title for duplicate checking.
    """
    print(f"Attempting to update README section: '{section_header}' with entry starting with '{entry_title_prefix}'...")

    entry_title_match = re.search(fr'^{re.escape(entry_title_prefix)}\s*(.*)', entry_markdown, re.MULTILINE)
    if not entry_title_match:
        print(f"Error: Could not extract entry title from markdown using prefix '{entry_title_prefix}'. Skipping entry.")
        return
    entry_title_line = f"{entry_title_prefix} {entry_title_match.group(1).strip()}"

    content = []
    if os.path.exists(readme_file_path):
        with open(readme_file_path, 'r', encoding='utf-8') as f:
            content = f.readlines()
    else:
        print(f"README file not found at {readme_file_path}. Creating a new one.")
        content = [
            "# Project Documentation\n",
            "This document is automatically generated.\n",
            "\n"
        ]

    section_found = False
    entry_found = False
    new_content = []
    i = 0

    while i < len(content):
        line = content[i]
        new_content.append(line)

        if line.strip() == section_header.strip():
            section_found = True
            # Check for existing entry under this section
            j = i + 1
            while j < len(content) and not content[j].strip().startswith('#'): # Look until next section header
                if content[j].strip() == entry_title_line.strip():
                    entry_found = True
                    print(f"Entry '{entry_title_line}' already exists under '{section_header}'. Skipping.")
                    break
                j += 1
            
            if not entry_found:
                # Insert new entry immediately after the section header or after existing entries in that section
                # Find where to insert: after existing entries of the same title prefix level
                insert_idx = i + 1
                while insert_idx < len(content) and content[insert_idx].strip() and not content[insert_idx].strip().startswith('## '):
                    # Check if the line is another entry of the same level
                    if content[insert_idx].strip().startswith(entry_title_prefix):
                        # Ensure we append after all existing entries of this level in this section
                        entry_scan_match = re.search(fr'^{re.escape(entry_title_prefix)}\s*(.*)', content[insert_idx], re.MULTILINE)
                        if entry_scan_match: # Check if it's a valid entry title line
                            insert_idx = content.index(content[insert_idx], insert_idx) + 1 # Advance past the current entry
                            # Keep advancing as long as lines are part of the current entry or empty lines between entries
                            while insert_idx < len(content) and not content[insert_idx].strip().startswith('#'):
                                insert_idx += 1
                            continue # Check from new insert_idx
                    insert_idx += 1 # If not another entry, just move to next line

                # Insert the new entry at the determined index
                # This ensures new entries are added in a structured way within the section, usually at the end.
                new_content.insert(insert_idx, "\n") # Add a blank line for spacing if needed
                new_content.insert(insert_idx + 1, entry_markdown + "\n\n")
                i += 2 # Adjust index for inserted lines
                print(f"Added new entry '{entry_title_line}' under section '{section_header}'.")
                entry_found = True # Mark as found/added to prevent re-adding

        i += 1

    if not section_found:
        print(f"Section '{section_header}' not found. Appending section and entry.")
        if not new_content or not new_content[-1].endswith('\n\n'):
            new_content.append("\n") # Ensure blank line before new section
        new_content.append(section_header + "\n")
        new_content.append(entry_markdown + "\n\n")

    try:
        with open(readme_file_path, 'w', encoding='utf-8') as f:
            f.writelines(new_content)
        print(f"README.md updated successfully at {readme_file_path}")
    except IOError as e:
        print(f"Error writing to README.md: {e}")

def update_readme_for_add_command():
    """Updates README.md with documentation for the 'add' command."""
    readme_path = "README.md"
    section_header = "## Commands"
    entry_prefix = "###"
    entry_markdown = """
### `add`
Adds two numbers together.
*   **Usage**: `python main.py add <num1> <num2>`
*   **Arguments**:
    *   `<num1>`: The first number (float).
    *   `<num2>`: The second number (float).
*   **Example**:
    *   `python main.py add 5 3` returns `8.0`.
"""
    _update_readme_section(readme_path, section_header, entry_markdown, entry_prefix)

def update_readme_for_convert_command():
    """Updates README.md with documentation for the 'convert' command."""
    readme_path = "README.md"
    section_header = "## Commands"
    entry_prefix = "###"
    entry_markdown = """
### `convert`
Converts temperature between Celsius and Fahrenheit.
*   **Usage**: `python main.py convert <value> [unit]`
*   **Arguments**:
    *   `<value>`: The temperature value to convert (float).
    *   `[unit]`: Optional. The unit of the input value. Can be `C` (Celsius) or `F` (Fahrenheit). Defaults to `C`.
*   **Example**:
    *   `python main.py convert 25 C`: Converts 25 Celsius to Fahrenheit.
    *   `python main.py convert 77 F`: Converts 77 Fahrenheit to Celsius.
"""
    _update_readme_section(readme_path, section_header, entry_markdown, entry_prefix)

def update_readme_for_subtract_function():
    """Updates README.md with documentation for the 'subtract' function."""
    readme_path = "README.md"
    section_header = "## Functions"
    entry_prefix = "###"
    entry_markdown = """
### `subtract(minuend, subtrahend)`
Subtracts the subtrahend from the minuend.
*   **Inputs**: `minuend` (int or float), `subtrahend` (int or float).
*   **Outputs**: (int or float): The difference.
*   **Example**: `subtract(10, 3)` returns `7`.
"""
    _update_readme_section(readme_path, section_header, entry_markdown, entry_prefix)

def update_readme_for_is_even_or_odd_function():
    """Updates README.md with documentation for the 'is_even_or_odd' function."""
    readme_path = "README.md"
    section_header = "## Functions"
    entry_prefix = "###"
    entry_markdown = """
### `is_even_or_odd(num)`
Determines if a given integer (or float equivalent to an integer) is "even" or "odd".
*   **Inputs**: `num` (int or float): The number to check.
*   **Outputs**: (str): "even" or "odd".
*   **Raises**: `TypeError` if input is not int or float, `ValueError` if float has a fractional part.
*   **Example**: `is_even_or_odd(4)` returns `"even"`.
"""
    _update_readme_section(readme_path, section_header, entry_markdown, entry_prefix)

def update_readme_for_is_palindrome_function():
    """Updates README.md with documentation for the 'is_palindrome' function."""
    readme_path = "README.md"
    section_header = "## Functions"
    entry_prefix = "###"
    entry_markdown = """
### `is_palindrome(s)`
Checks if a given string is a palindrome (reads the same forwards and backward, ignoring case and non-alphanumeric characters).
*   **Inputs**: `s` (str): The string to check.
*   **Outputs**: (bool): `True` if it's a palindrome, `False` otherwise.
*   **Example**: `is_palindrome("Racecar")` returns `True`.
"""
    _update_readme_section(readme_path, section_header, entry_markdown, entry_prefix)

def update_readme_for_reverse_string_function():
    """Updates README.md with documentation for the 'reverse_string' function."""
    readme_path = "README.md"
    section_header = "## Functions"
    entry_prefix = "###"
    entry_markdown = """
### `reverse_string(s)`
Reverses a given string.
*   **Inputs**: `s` (str): The string to reverse.
*   **Outputs**: (str): The reversed string.
*   **Example**: `reverse_string("hello")` returns `"olleh"`.
"""
    _update_readme_section(readme_path, section_header, entry_markdown, entry_prefix)

def update_readme_for_count_vowels_function():
    """Updates README.md with documentation for the 'count_vowels' function."""
    readme_path = "README.md"
    section_header = "## Functions"
    entry_prefix = "###"
    entry_markdown = """
### `count_vowels(s)`
Counts the number of vowels (a, e, i, o, u, case-insensitive) in a string.
*   **Inputs**: `s` (str): The input string.
*   **Outputs**: (int): The count of vowels.
*   **Example**: `count_vowels("Hello World")` returns `3`.
"""
    _update_readme_section(readme_path, section_header, entry_markdown, entry_prefix)

def update_readme_for_capitalize_words_function():
    """Updates README.md with documentation for the 'capitalize_words' function."""
    readme_path = "README.md"
    section_header = "## Functions"
    entry_prefix = "###"
    entry_markdown = """
### `capitalize_words(s)`
Capitalizes the first letter of each word in a string.
*   **Inputs**: `s` (str): The input string.
*   **Outputs**: (str): The string with each word capitalized.
*   **Example**: `capitalize_words("hello world")` returns `"Hello World"`.
"""
    _update_readme_section(readme_path, section_header, entry_markdown, entry_prefix)

def update_readme_for_is_anagram_function():
    """Updates README.md with documentation for the 'is_anagram' function."""
    readme_path = "README.md"
    section_header = "## Functions"
    entry_prefix = "###"
    entry_markdown = """
### `is_anagram(s1, s2)`
Checks if two strings are anagrams of each other (contain the same characters with the same frequency, ignoring case and spaces).
*   **Inputs**: `s1` (str), `s2` (str): The two strings to compare.
*   **Outputs**: (bool): `True` if they are anagrams, `False` otherwise.
*   **Example**: `is_anagram("listen", "silent")` returns `True`.
"""
    _update_readme_section(readme_path, section_header, entry_markdown, entry_prefix)

def update_readme_for_remove_spaces_function():
    """Updates README.md with documentation for the 'remove_spaces' function."""
    readme_path = "README.md"
    section_header = "## Functions"
    entry_prefix = "###"
    entry_markdown = """
### `remove_spaces(s)`
Removes all spaces from a string.
*   **Inputs**: `s` (str): The input string.
*   **Outputs**: (str): The string with all spaces removed.
*   **Example**: `remove_spaces("hello world")` returns `"helloworld"`.
"""
    _update_readme_section(readme_path, section_header, entry_markdown, entry_prefix)

def update_readme_for_find_longest_word_function():
    """Updates README.md with documentation for the 'find_longest_word' function."""
    readme_path = "README.md"
    section_header = "## Functions"
    entry_prefix = "###"
    entry_markdown = """
### `find_longest_word(sentence)`
Finds the longest word in a sentence.
*   **Inputs**: `sentence` (str): The input sentence.
*   **Outputs**: (str): The longest word found. If multiple words have the same maximum length, returns the first one encountered.
*   **Example**: `find_longest_word("The quick brown fox jumps")` returns `"quick"`.
"""
    _update_readme_section(readme_path, section_header, entry_markdown, entry_prefix)

def update_readme_for_celsius_to_fahrenheit_function():
    """Updates README.md with documentation for the 'celsius_to_fahrenheit' function."""
    readme_path = "README.md"
    section_header = "## Functions"
    entry_prefix = "###"
    entry_markdown = """
### `celsius_to_fahrenheit(celsius)`
Converts a temperature from Celsius to Fahrenheit.
*   **Inputs**: `celsius` (float): The temperature in Celsius.
*   **Outputs**: (float): The equivalent temperature in Fahrenheit.
*   **Example**: `celsius_to_fahrenheit(0)` returns `32.0`.
"""
    _update_readme_section(readme_path, section_header, entry_markdown, entry_prefix)

def update_readme_for_check_number_sign_function():
    """Updates README.md with documentation for the 'check_number_sign' function."""
    readme_path = "README.md"
    section_header = "## Functions"
    entry_prefix = "###"
    entry_markdown = """
### `check_number_sign(number)`
Determines the sign of a given number.
*   **Inputs**: `number` (int or float): The number to check.
*   **Outputs**: (str): "positive" if greater than 0, "negative" if less than 0, or "zero" if equal to 0.
*   **Example**: `check_number_sign(5)` returns `"positive"`.
"""
    _update_readme_section(readme_path, section_header, entry_markdown, entry_prefix)

def update_readme_for_absolute_value_function():
    """Updates README.md with documentation for the 'absolute_value' function."""
    readme_path = "README.md"
    section_header = "## Functions"
    entry_prefix = "###"
    entry_markdown = """
### `absolute_value(num)`
Returns the absolute value of a given number.
*   **Inputs**: `num` (int or float): The number for which to find the absolute value.
*   **Outputs**: (int or float): The absolute value of the number.
*   **Example**: `absolute_value(-5)` returns `5`.
"""
    _update_readme_section(readme_path, section_header, entry_markdown, entry_prefix)

def update_readme_for_meters_to_centimeters_function():
    """Updates README.md with documentation for the 'meters_to_centimeters' function."""
    readme_path = "README.md"
    section_header = "## Functions"
    entry_prefix = "###"
    entry_markdown = """
### `meters_to_centimeters(meters)`
Converts a length from meters to centimeters.
*   **Inputs**: `meters` (int or float): The length in meters.
*   **Outputs**: (float): The equivalent length in centimeters.
*   **Example**: `meters_to_centimeters(1)` returns `100.0`.
"""
    _update_readme_section(readme_path, section_header, entry_markdown, entry_prefix)


if __name__ == "__main__":
    print("Starting README update process...")
    try:
        # Commands
        update_readme_for_add_command()
        update_readme_for_convert_command() # New command documentation

        # Functions
        update_readme_for_subtract_function()
        update_readme_for_is_even_or_odd_function()
        update_readme_for_is_palindrome_function()
        update_readme_for_reverse_string_function()
        update_readme_for_count_vowels_function()
        update_readme_for_capitalize_words_function()
        update_readme_for_is_anagram_function()
        update_readme_for_remove_spaces_function()
        update_readme_for_find_longest_word_function()
        update_readme_for_celsius_to_fahrenheit_function() # New function documentation
        update_readme_for_check_number_sign_function() # New function documentation
        update_readme_for_absolute_value_function() # New function documentation
        update_readme_for_meters_to_centimeters_function() # New function documentation

        print("README update process completed.")
    except Exception as e:
        print(f"An error occurred during README update: {e}")