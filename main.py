import argparse
from src.operations import add as operations_add

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

def main():
    """
    Main function to parse command-line arguments and execute calculator operations.
    It sets up an argparse CLI with a subparser for the 'add' command.
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

    # --- Other commands would go here ---
    # Example:
    # subtract_parser = subparsers.add_parser("subtract", help="Subtract two numbers")
    # subtract_parser.add_argument("num1", type=float, help="The first number")
    # subtract_parser.add_argument("num2", type=float, help="The second number")
    # subtract_parser.set_defaults(func=subtract_command)

    args = parser.parse_args()

    if hasattr(args, 'func'):
        args.func(args)
    else:
        # If no subparser command is given, print help
        parser.print_help()

if __name__ == "__main__":
    main()