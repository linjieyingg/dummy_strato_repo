import sys
from src.calculator_logic import add, subtract

def _parse_input(user_input):
    """
    Parses the user's input string into two numbers and an operator.

    Args:
        user_input (str): The input string from the user, e.g., "5 + 3".

    Returns:
        tuple: A tuple containing (num1, operator, num2).
               Returns (None, None, None) if parsing fails.
    """
    parts = user_input.split()

    if len(parts) != 3:
        print("Invalid input format. Please use 'number operator number' (e.g., '5 + 3').")
        return None, None, None

    try:
        num1 = float(parts[0])
        operator = parts[1]
        num2 = float(parts[2])
    except ValueError:
        print("Invalid numbers provided. Please ensure numbers are numeric (e.g., integers or floats).")
        return None, None, None

    return num1, operator, num2

def main():
    """
    Implements the command-line interface for the calculator.
    Handles user input, calls arithmetic functions, and displays results or errors.
    """
    print("Welcome to the CLI Calculator!")
    print("Enter 'quit' or 'exit' to stop the calculator.")
    print("Example: 5 + 3 or 10.5 - 2")

    while True:
        user_input = input("calc> ").strip().lower()

        if user_input in ("quit", "exit"):
            print("Exiting calculator. Goodbye!")
            break

        num1, operator, num2 = _parse_input(user_input)

        if num1 is None:  # Parsing failed
            continue

        result = None
        try:
            if operator == '+':
                result = add(num1, num2)
            elif operator == '-':
                result = subtract(num1, num2)
            else:
                print(f"Unsupported operator: '{operator}'. Only '+' and '-' are supported.")
                continue

            # Display result, converting to int if it's a whole number for cleaner output
            if result == int(result):
                print(f"Result: {int(result)}")
            else:
                print(f"Result: {result}")

        except TypeError as e:
            # This should ideally be caught by _parse_input's float conversion,
            # but serves as a safeguard against non-numeric types if logic changes.
            print(f"Error: {e}")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()