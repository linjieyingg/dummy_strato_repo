import random

def roll_die(sides: int) -> int:
    """
    Simulates rolling a single die with a specified number of sides.

    Args:
        sides (int): The number of sides on the die. Must be a positive integer.

    Returns:
        int: The result of the die roll (an integer between 1 and `sides`, inclusive).

    Raises:
        ValueError: If `sides` is not a positive integer.
    """
    if not isinstance(sides, int) or sides <= 0:
        raise ValueError("Number of sides for the die must be a positive integer.")
    return random.randint(1, sides)

def roll_multiple_dice(num_dice: int, sides: int) -> list[int]:
    """
    Simulates rolling multiple dice of the same type.

    Args:
        num_dice (int): The number of dice to roll. Must be a positive integer.
        sides (int): The number of sides on each die. Must be a positive integer.

    Returns:
        list[int]: A list containing the result of each individual die roll.

    Raises:
        ValueError: If `num_dice` or `sides` is not a positive integer.
    """
    if not isinstance(num_dice, int) or num_dice <= 0:
        raise ValueError("Number of dice to roll must be a positive integer.")
    if not isinstance(sides, int) or sides <= 0:
        raise ValueError("Number of sides for each die must be a positive integer.")

    return [roll_die(sides) for _ in range(num_dice)]

def roll_and_sum_dice(num_dice: int, sides: int) -> int:
    """
    Simulates rolling multiple dice of the same type and calculates their total sum.

    This function is a convenience wrapper around `roll_multiple_dice` followed by summing
    the results.

    Args:
        num_dice (int): The number of dice to roll. Must be a positive integer.
        sides (int): The number of sides on each die. Must be a positive integer.

    Returns:
        int: The total sum of all individual die rolls.

    Raises:
        ValueError: If `num_dice` or `sides` is not a positive integer.
    """
    rolls = roll_multiple_dice(num_dice, sides)
    return sum(rolls)

if __name__ == '__main__':
    # Example Usage for testing
    print("--- Dice Roller Examples ---")

    try:
        # Single die roll
        d6_roll = roll_die(6)
        print(f"Rolling a d6: {d6_roll}")

        d20_roll = roll_die(20)
        print(f"Rolling a d20: {d20_roll}")

        # Multiple dice rolls (individual results)
        three_d6_rolls = roll_multiple_dice(3, 6)
        print(f"Rolling 3d6 (individual results): {three_d6_rolls}")
        print(f"Total of 3d6 individual rolls: {sum(three_d6_rolls)}")

        # Multiple dice rolls (summed total)
        two_d4_sum = roll_and_sum_dice(2, 4)
        print(f"Rolling 2d4 (summed): {two_d4_sum}")

        four_d8_sum = roll_and_sum_dice(4, 8)
        print(f"Rolling 4d8 (summed): {four_d8_sum}")

        # Error handling examples
        print("\n--- Error Handling Examples ---")
        try:
            roll_die(0)
        except ValueError as e:
            print(f"Caught expected error for d0: {e}")

        try:
            roll_multiple_dice(-1, 6)
        except ValueError as e:
            print(f"Caught expected error for -1d6: {e}")

        try:
            roll_and_sum_dice(2, 'six')
        except ValueError as e:
            print(f"Caught expected error for 2d'six': {e}")

    except Exception as e:
        print(f"An unexpected error occurred during example usage: {e}")