import argparse
import sys

# Import game logic and UI components
from game.guess_number import GuessNumberGame
from game.cli_ui import CliUI

def main():
    """
    Main entry point for running the 'Guess the Number' game.

    This function parses command-line arguments for game parameters,
    initializes the game logic, and orchestrates the user interface
    interactions to guide the player through the game.
    """
    parser = argparse.ArgumentParser(
        description="Play the 'Guess the Number' game.",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter
    )
    parser.add_argument(
        '--min',
        type=int,
        help=f"Minimum number for the guessing range (default: {GuessNumberGame.DEFAULT_MIN_NUMBER})"
    )
    parser.add_argument(
        '--max',
        type=int,
        help=f"Maximum number for the guessing range (default: {GuessNumberGame.DEFAULT_MAX_NUMBER})"
    )
    parser.add_argument(
        '--attempts',
        type=int,
        help=f"Maximum number of guesses allowed (default: {GuessNumberGame.DEFAULT_MAX_ATTEMPTS})"
    )
    args = parser.parse_args()

    # Initialize the game logic component
    game: GuessNumberGame = None
    try:
        # Pass parsed arguments directly. If None, GuessNumberGame will use its defaults.
        game = GuessNumberGame(min_num=args.min, max_num=args.max, max_attempts=args.attempts)
    except (ValueError, TypeError) as e:
        print(f"Error initializing game: {e}", file=sys.stderr)
        sys.exit(1)

    # Display the welcome message using the game's configured parameters
    # Accessing protected attributes for display purposes, assuming they are available
    # and contain the finalized game configuration.
    CliUI.display_welcome_message(game._min_num, game._max_num, game._max_attempts)

    # Game loop
    while not game.is_game_over():
        try:
            # Calculate the current attempt number for the UI prompt
            current_attempt_num = game._max_attempts - game._remaining_attempts + 1
            guess = CliUI.prompt_for_guess(current_attempt_num, game._max_attempts)
        except EOFError:
            print("\nGame aborted by user. Goodbye!")
            sys.exit(0)
        # CliUI.prompt_for_guess is designed to handle invalid input internally
        # and re-prompt, so no further ValueError catch is needed here for input.

        # Process the player's guess
        feedback = game.make_guess(guess)

        if feedback == "too high":
            print("Your guess is too high!")
        elif feedback == "too low":
            print("Your guess is too low!")
        elif feedback == "correct":
            print(
                f"\n🎉 Congratulations! You guessed the number {game._secret_number} "
                f"in {current_attempt_num} attempts."
            )
            break  # Game won, exit the loop

        # Provide feedback on remaining attempts if the game is not yet over
        if not game.is_game_over():
            print(f"Attempts left: {game._remaining_attempts}\n")

    # After the loop, if the game was not won, it means attempts ran out
    if not game.is_won():
        print(f"\n😞 Sorry, you ran out of attempts! The secret number was {game._secret_number}.")
        print("Game Over.")


if __name__ == "__main__":
    main()