import argparse
import sys
from src.dice_roller import roll_multiple_dice

def main():
    """
    Parses command-line arguments for rolling dice, calls the dice rolling logic,
    and displays the results to the user.
    """
    parser = argparse.ArgumentParser(
        description="Rolls one or more dice with a specified number of sides."
    )
    parser.add_argument(
        "-n", "--num-dice",
        type=int,
        default=1,
        help="The number of dice to roll (default: 1)."
    )
    parser.add_argument(
        "-s", "--sides",
        type=int,
        default=6,
        help="The number of sides on each die (default: 6)."
    )

    args = parser.parse_args()

    try:
        rolls = roll_multiple_dice(args.num_dice, args.sides)
        total_sum = sum(rolls)

        print(f"Rolling {args.num_dice} D{args.sides} dice...")
        print(f"Individual rolls: {rolls}")
        print(f"Total sum: {total_sum}")

    except ValueError as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(f"An unexpected error occurred: {e}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()