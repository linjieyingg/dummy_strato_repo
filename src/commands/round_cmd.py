import sys
from src.utils.math_utils import round_number_to_place

def run(args: list):
    """
    Executes the 'round' command.

    This command rounds a given number to a specified decimal place.
    If no decimal place is specified, it rounds to the nearest integer (0 decimal places).

    Usage:
        round <number_to_round> [decimal_place]

    Args:
        args (list): A list of command-line arguments following the 'round' command.
                     Expected: [<number_to_round>, [decimal_place]]
    """
    if not args:
        print("Error: Missing number to round.")
        print("Usage: round <number_to_round> [decimal_place]")
        sys.exit(1)

    number_str = args[0]
    decimal_place = 0  # Default to rounding to integer

    if len(args) > 2:
        print("Error: Too many arguments.")
        print("Usage: round <number_to_round> [decimal_place]")
        sys.exit(1)
    elif len(args) == 2:
        place_str = args[1]
        try:
            decimal_place = int(place_str)
        except ValueError:
            print(f"Error: Invalid decimal place '{place_str}'. Must be an integer.")
            sys.exit(1)
        if decimal_place < 0:
            print("Error: Decimal place cannot be negative.")
            sys.exit(1)

    try:
        number_to_round = float(number_str)
    except ValueError:
        print(f"Error: Invalid number '{number_str}'. Must be a numeric value.")
        sys.exit(1)

    try:
        rounded_number = round_number_to_place(number_to_round, decimal_place)
        print(f"Original number: {number_to_round}")
        print(f"Rounded to {decimal_place} decimal place(s): {rounded_number}")
    except Exception as e:
        # Catch any unexpected errors from the utility function
        print(f"An unexpected error occurred during rounding: {e}")
        sys.exit(1)

if __name__ == "__main__":
    # Example usage for standalone testing:
    print("--- Test Case 1: Round 3.14159 to 2 decimal places ---")
    run(["3.14159", "2"])
    print("\n--- Test Case 2: Round 10.5 to nearest integer (default) ---")
    run(["10.5"])
    print("\n--- Test Case 3: Round 7.89 to 0 decimal places ---")
    run(["7.89", "0"])
    print("\n--- Test Case 4: Round 123.456789 to 4 decimal places ---")
    run(["123.456789", "4"])
    print("\n--- Test Case 5: Error - No arguments ---")
    try:
        run([])
    except SystemExit:
        pass
    print("\n--- Test Case 6: Error - Invalid number ---")
    try:
        run(["abc", "2"])
    except SystemExit:
        pass
    print("\n--- Test Case 7: Error - Invalid decimal place ---")
    try:
        run(["3.14", "two"])
    except SystemExit:
        pass
    print("\n--- Test Case 8: Error - Too many arguments ---")
    try:
        run(["3.14", "2", "extra"])
    except SystemExit:
        pass
    print("\n--- Test Case 9: Error - Negative decimal place ---")
    try:
        run(["3.14", "-1"])
    except SystemExit:
        pass