import os

def _update_readme_section(readme_file_path, section_header, entry_markdown, entry_title_prefix="###"):
    """
    Helper function to update or create a specific section in README.md.

    This function reads the README.md file, searches for the specified section header.
    If the section is found, it attempts to insert the new markdown entry right after it.
    If the section is not found, it appends the section header and the entry to the end of the file.
    If the README.md file does not exist, it creates a new one with a basic structure,
    including the specified section and entry.

    Args:
        readme_file_path (str): Path to the README.md file.
        section_header (str): The header of the section to update (e.g., "## Commands").
        entry_markdown (str): The markdown content to insert into the section.
        entry_title_prefix (str): The markdown prefix for the entry's main title (e.g., "###").
                                  Used to identify the entry for duplication checks.
    """
    # Extract the main title from the entry_markdown to check for existing entries
    entry_title_line = None
    for line in entry_markdown.splitlines():
        if line.strip().startswith(entry_title_prefix):
            entry_title_line = line.strip()
            break
    
    if not entry_title_line:
        # Fallback if entry_title_prefix doesn't match, or for simpler entries
        # Use the first non-empty line as a fallback identifier
        first_non_empty_line = next((line.strip() for line in entry_markdown.splitlines() if line.strip()), "")
        if first_non_empty_line:
            entry_title_line = first_non_empty_line
            print(f"Warning: Falling back to first non-empty line as entry title for section '{section_header}': {entry_title_line}")
        else:
            print(f"Warning: Could not extract entry title from markdown for section '{section_header}'. Cannot check for duplicates effectively.")
            entry_title_line = "Unknown Entry" # Placeholder for logging


    try:
        if os.path.exists(readme_file_path):
            with open(readme_file_path, 'r', encoding='utf-8') as f:
                content_lines = f.readlines()

            # Check if the specific entry title already exists to prevent duplication
            # This is a more robust check than the entire markdown string, which might vary in whitespace
            if any(entry_title_line in line for line in content_lines):
                print(f"'{entry_title_line}' documentation already exists in README.md. Skipping update for '{section_header}'.")
                return

            updated_content = []
            section_found = False
            entry_inserted = False

            for i, line in enumerate(content_lines):
                updated_content.append(line)
                if line.strip() == section_header.strip() and not entry_inserted:
                    # Insert the new documentation right after the header
                    # Ensure consistent spacing with two newlines after the inserted content
                    updated_content.append(entry_markdown.strip() + "\n\n")
                    entry_inserted = True
                    section_found = True
            
            if not section_found:
                # If the target section was not found, add it to the end of the file
                # Ensure there's a newline before adding new section if the file doesn't end with one
                if updated_content and not updated_content[-1].endswith('\n'):
                    updated_content.append('\n')
                updated_content.append(f"\n{section_header}\n")
                updated_content.append(entry_markdown.strip() + "\n\n")
                entry_inserted = True
            
            if entry_inserted:
                with open(readme_file_path, 'w', encoding='utf-8') as f:
                    f.writelines(updated_content)
                print(f"README.md updated with '{entry_title_line}' documentation under '{section_header}'.")
            else:
                # This case should ideally not be reached if the entry wasn't present and section logic worked
                print(f"No changes made for '{entry_title_line}' in '{section_header}' despite an attempt to update.")


        else:
            # Create a new README.md with a basic structure and the target section and entry
            with open(readme_file_path, 'w', encoding='utf-8') as f:
                f.write("# Project Title\n\n")
                f.write("A short description of your project.\n\n")
                f.write(f"{section_header}\n")
                f.write(entry_markdown.strip() + "\n\n")
            print(f"README.md created and populated with '{entry_title_line}' documentation under '{section_header}'.")

    except IOError as e:
        print(f"Error updating README.md: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


def update_readme_for_add_command():
    """
    Updates or creates the README.md file to include documentation for the 'add' command
    under the 'Commands' section.

    If 'README.md' exists, it attempts to find the 'Commands' section and insert
    the 'add' command details. If the 'Commands' section does not exist, it will
    be added to the end of the file. If 'README.md' does not exist, it will be
    created with a basic structure including the 'add' command documentation.
    """
    readme_file_path = "README.md"
    commands_section_header = "## Commands"
    add_command_entry_markdown = """
### add

**Syntax:** `add <item_name>`

**Description:**
Adds a new item to the tracking system. The item name should be a single word
or a string enclosed in quotes if it contains spaces.

**Example Usage:**
""" # The Example Usage: is empty as per the provided content.

    _update_readme_section(readme_file_path, commands_section_header, add_command_entry_markdown, entry_title_prefix="###")


def update_readme_for_subtract_function():
    """
    Updates or creates the README.md file to include documentation for the 'subtract' function
    under the 'Functions' section.

    If 'README.md' exists, it attempts to find the 'Functions' section and insert
    the 'subtract' function details. If the 'Functions' section does not exist, it will
    be added to the end of the file. If 'README.md' does not exist, it will be
    created with a basic structure including the 'subtract' function documentation.
    """
    readme_file_path = "README.md"
    functions_section_header = "## Functions"
    subtract_function_entry_markdown = """
### subtract

**Syntax:** `subtract(number1, number2)`

**Description:**
Calculates the difference between two numbers (number1 - number2). Both numbers should be integers or floats.

**Example Usage:**
"""
    _update_readme_section(readme_file_path, functions_section_header, subtract_function_entry_markdown, entry_title_prefix="###")


def update_readme_for_is_even_or_odd_function():
    """
    Updates or creates the README.md file to include documentation for the 'is_even_or_odd' function
    under the 'Functions' section.

    If 'README.md' exists, it attempts to find the 'Functions' section and insert
    the 'is_even_or_odd' function details. If the 'Functions' section does not exist, it will
    be added to the end of the file. If 'README.md' does not exist, it will be
    created with a basic structure including the 'is_even_or_odd' function documentation.
    """
    readme_file_path = "README.md"
    functions_section_header = "## Functions"
    is_even_or_odd_entry_markdown = """
### is_even_or_odd

**Syntax:** `is_even_or_odd(number)`

**Description:**
Checks if a given number is even or odd. It primarily applies to integers and floating-point numbers that are exact integers (e.g., `4.0`, `-2.0`). For non-integer floating-point numbers (e.g., `2.5`, `3.14`), it returns 'Neither Even Nor Odd', as these are not traditionally classified as even or odd.

**Example Usage:**
"""
    _update_readme_section(readme_file_path, functions_section_header, is_even_or_odd_entry_markdown, entry_title_prefix="###")


def update_readme_for_is_palindrome_function():
    """
    Updates or creates the README.md file to include documentation for the 'is_palindrome' function
    under the 'Functions' section.

    If 'README.md' exists, it attempts to find the 'Functions' section and insert
    the 'is_palindrome' function details. If the 'Functions' section does not exist, it will
    be added to the end of the file. If 'README.md' does not exist, it will be
    created with a basic structure including the 'is_palindrome' function documentation.
    """
    readme_file_path = "README.md"
    functions_section_header = "## Functions"
    is_palindrome_entry_markdown = """
### is_palindrome

**Syntax:** `is_palindrome(text)`

**Description:**
Checks if a given string `text` is a palindrome. A palindrome is a word, phrase, number, or other sequence of characters which reads the same backward as forward, ignoring capitalization, spaces, and punctuation.

**Example Usage:**