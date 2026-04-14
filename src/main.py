"""
This module serves as the main entry point for the 'Hello, World!' application.

It calls the greeting function from the `greeter` module and prints the result.
"""

from src.greeter import greet

def main() -> None:
    """
    Executes the main logic of the 'Hello, World!' application.

    This function attempts to retrieve a greeting string from the `greeter` module
    and prints it to the console. It includes basic error handling for unexpected
    issues during the greeting process.
    """
    try:
        message = greet()
        print(message)
    except Exception as e:
        # For a simple function like greet() which is designed to be robust
        # and not raise exceptions, this block primarily serves as a safeguard
        # against unexpected runtime issues or future modifications to greet().
        print(f"An unexpected error occurred while generating the greeting: {e}")
        # Optionally, re-raise the exception or exit with a non-zero status
        # sys.exit(1) # Requires import sys
    except KeyboardInterrupt:
        print("\nApplication interrupted by user.")


if __name__ == "__main__":
    main()