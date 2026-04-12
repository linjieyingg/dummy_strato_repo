import argparse
from src.calculator.operations import add, subtract, multiply, divide

def main():
    """
    Main function to run the command-line interface for the calculator.

    Parses command-line arguments for an operation and two numbers,
    performs the calculation using functions from src.calculator.operations,
    and prints the result or an error message.
    """
    parser = argparse.ArgumentParser(
        description="A simple command-line calculator. Performs basic arithmetic "
                    "operations on two numbers.",
        formatter_class=argparse.RawTextHelpFormatter
    )

    parser.add_argument(
        "operation",
        type=str,
        choices=['add', 'subtract', 'multiply', 'divide'],
        help="The arithmetic operation to perform:\n"
             "  add     - addition\n"
             "  subtract- subtraction\n"
             "  multiply- multiplication\n"
             "  divide  - division"
    )
    parser.add_argument("num1", type=str, help="The first number (integer or float).")
    parser.add_argument("num2", type=str, help="The second number (integer or float).")

    args = parser.parse_args()

    # Map operation strings to functions
    operations_map = {
        'add': add,
        'subtract': subtract,
        'multiply': multiply,
        'divide': divide
    }

    # Retrieve the chosen operation function
    operation_func = operations_map[args.operation]

    try:
        # Convert string inputs to numeric types (float)
        # Using float to handle both integers and decimals flexibly.
        # The underlying operation functions will then validate more strictly if needed.
        number1 = float(args.num1)
        number2 = float(args.num2)

        # Perform the calculation
        result = operation_func(number1, number2)
        print(f"The result of {args.operation} {args.num1} and {args.num2} is: {result}")

    except ValueError:
        # Catch errors if num1 or num2 cannot be converted to float
        print(f"Error: Invalid numeric input. Please ensure '{args.num1}' and '{args.num2}' are valid numbers.")
    except TypeError as e:
        # Catch TypeErrors from the operations module (e.g., if validation in operations.py fails)
        print(f"Error: {e}")
    except ZeroDivisionError as e:
        # Catch specific ZeroDivisionError from the divide function
        print(f"Error: {e}")
    except Exception as e:
        # Catch any other unexpected errors
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()