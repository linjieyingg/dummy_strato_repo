import argparse
from src.operations import add as operations_add
from src.operations import divide as operations_divide # New import
from src.bmi_calculator import calculate_bmi
from src.grade_calculator import calculate_letter_grade

def add_command(args):
    """
    Handles the 'add' command, calculating the sum of two numbers.
    It takes two float arguments, num1 and num2, calls the operations.add function,
    and prints the result. Includes basic error handling for the operation.
    """
    try:
        result = operations_add(args.num1, args.num2)
        print(f"Result: {result}")
    except TypeError as e:
        # This catch might be redundant if argparse types are strict,
        # but good for robustness if operations.add expects specific types.
        print(f"Error: Invalid argument type provided to add operation. {e}")
    except Exception as e:
        # Catch any other unexpected errors from the add operation
        print(f"An unexpected error occurred during the add operation: {e}")

def divide_command(args):
    """
    Handles the 'divide' command, calculating the quotient of two numbers.
    It takes two float arguments, num1 (numerator) and num2 (denominator),
    calls the operations.divide function, and prints the result.
    Includes error handling for zero division and other potential issues.
    """
    try:
        result = operations_divide(args.num1, args.num2)
        print(f"Result: {result}")
    except ZeroDivisionError as e:
        print(f"Error: {e}")
    except TypeError as e:
        # This catch might be redundant if argparse types are strict,
        # but good for robustness if operations.divide expects specific types.
        print(f"Error: Invalid argument type provided to divide operation. {e}")
    except Exception as e:
        # Catch any other unexpected errors from the divide operation
        print(f"An unexpected error occurred during the divide operation: {e}")

def bmi_command(args):
    """
    Handles the 'bmi' command, calculating the Body Mass Index (BMI).
    It takes weight in kilograms and height in meters, calls the bmi_calculator.calculate_bmi
    function, and prints the result. Includes error handling for calculation.
    """
    try:
        bmi_value = calculate_bmi(args.weight, args.height)
        print(f"Your BMI: {bmi_value:.2f}")
    except ValueError as e:
        # Catches errors related to invalid input values (e.g., non-positive weight/height)
        print(f"Error calculating BMI: {e}")
    except TypeError as e:
        # Catches errors related to incorrect input types (should be handled by argparse `type=float`,
        # but kept for robustness if `calculate_bmi` has internal type checks).
        print(f"Error: Invalid argument type provided to BMI calculation. {e}")
    except Exception as e:
        # Catch any other unexpected errors during BMI calculation
        print(f"An unexpected error occurred during BMI calculation: {e}")

def grade_command(args):
    """
    Handles the 'grade' command, calculating the letter grade for a given score.
    It takes a float argument 'score', calls the grade_calculator.calculate_letter_grade
    function, and prints the result. Includes error handling for calculation.
    """
    try:
        letter_grade = calculate_letter_grade(args.score)
        print(f"Score {args.score} corresponds to grade: {letter_grade}")
    except ValueError as e:
        print(f"Error calculating grade: {e}")
    except TypeError as e:
        # Catches errors related to incorrect input types (should be handled by argparse `type=float`,
        # but kept for robustness if `calculate_letter_grade` has internal type checks).
        print(f"Error: Invalid argument type provided to grade calculation. {e}")
    except Exception as e:
        print(f"An unexpected error occurred during grade calculation: {e}")

def main():
    """
    Main function to parse command-line arguments and execute calculator operations.
    It sets up an argparse CLI with subparsers for 'add', 'divide', 'bmi', and 'grade' commands.
    """
    parser = argparse.ArgumentParser(
        description="A simple command-line calculator for various operations."
    )

    subparsers = parser.add_subparsers(dest="command", help="Available commands")

    # --- Add 'add' command subparser ---
    add_parser = subparsers.add_parser(
        "add",
        help="Add two numbers together."
    )
    add_parser.add_argument(
        "num1",
        type=float,
        help="The first number to add."
    )
    add_parser.add_argument(
        "num2",
        type=float,
        help="The second number to add."
    )
    add_parser.set_defaults(func=add_command)

    # --- Add 'divide' command subparser ---
    divide_parser = subparsers.add_parser(
        "divide",
        help="Divide two numbers (numerator / denominator)."
    )
    divide_parser.add_argument(
        "num1",
        type=float,
        help="The numerator."
    )
    divide_parser.add_argument(
        "num2",
        type=float,
        help="The denominator (cannot be zero)."
    )
    divide_parser.set_defaults(func=divide_command)

    # --- Add 'bmi' command subparser ---
    bmi_parser = subparsers.add_parser(
        "bmi",
        help="Calculate Body Mass Index (BMI)."
    )
    bmi_parser.add_argument(
        "--weight",
        type=float,
        required=True,
        help="Weight in kilograms (e.g., 70.5)."
    )
    bmi_parser.add_argument(
        "--height",
        type=float,
        required=True,
        help="Height in meters (e.g., 1.75)."
    )
    bmi_parser.set_defaults(func=bmi_command)

    # --- Add 'grade' command subparser ---
    grade_parser = subparsers.add_parser(
        "grade",
        help="Calculate a letter grade based on a numeric score."
    )
    grade_parser.add_argument(
        "score",
        type=float,
        help="The numeric score (e.g., 85.5) to convert to a letter grade."
    )
    grade_parser.set_defaults(func=grade_command)

    args = parser.parse_args()

    if hasattr(args, 'func'):
        args.func(args)
    else:
        # If no subparser command is given, print help
        parser.print_help()

if __name__ == "__main__":
    main()