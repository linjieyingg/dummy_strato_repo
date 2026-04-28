import argparse
import sys

# Import game logic and UI components
# FIX: Change imports to be absolute from the 'src' package
from src.game.guess_number import GuessNumberGame
from src.game.cli_ui import CliUI

def play_single_game(game: GuessNumberGame):
    """
    Manages the core game loop for a single round of 'Guess the Number'.

    Args:
        game (GuessNumberGame): An initialized GuessNumberGame instance.
    """
    # Display the welcome message using the game's configured parameters
    # FIX: Use public getter methods instead of protected attributes
    min_num, max_num = game.get_range()
    CliUI.display_welcome_message(min_num, max_num, game.get_max_attempts())

    # Game loop for a single round
    while not game.is_game_over():
        try:
            # Calculate the current attempt number for the UI prompt
            # FIX: Use public getter methods instead of protected attributes
            current_attempt_num_display = game.get_max_attempts() - game.get_remaining_attempts() + 1
            guess = CliUI.prompt_for_guess(current_attempt_num_display, game.get_max_attempts())
        except EOFError:
            # This is primarily caught within CliUI.prompt_for_guess, but kept here for robustness
            # or if prompt_for_guess ever changes its exit behavior.
            CliUI.display_feedback("\nGame aborted by user. Goodbye!")
            sys.exit(0)

        # Process the player's guess
        # FIX: Change make_guess to check_guess
        feedback = game.check_guess(guess)
        CliUI.display_feedback(feedback) # Display the feedback from the game logic

        # If game is not over after the guess, provide remaining attempts feedback.
        if not game.is_game_over():
            # FIX: Use public getter methods instead of protected attributes
            CliUI.display_feedback(f"Attempts left: {game.get_remaining_attempts()}\n")

    # After the loop, the game is over. Determine if it was a win or loss.
    # FIX: Use is_game_won() for explicit win/loss check and CliUI messages
    if game.is_game_won():
        # attempts_taken = MaxAttempts - RemainingAttempts (as remaining is decremented on winning guess)
        attempts_taken = game.get_max_attempts() - game.get_remaining_attempts()
        CliUI.display_win_message(game.get_secret_number(), attempts_taken)
    else:
        CliUI.display_lose_message(game.get_secret_number())

def main():
    """
    Main entry point for running the 'Guess the Number' game.
    Handles argument parsing and the play-again loop.
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

    while True: # Outer loop for playing multiple games
        game: GuessNumberGame = None
        try:
            # Pass parsed arguments directly. If None, GuessNumberGame will use its defaults.
            game = GuessNumberGame(min_num=args.min, max_num=args.max, max_attempts=args.attempts)
        except (ValueError, TypeError) as e:
            print(f"Error initializing game: {e}", file=sys.stderr)
            sys.exit(1)

        play_single_game(game) # Play one round

        if not CliUI.prompt_to_play_again():
            CliUI.display_feedback("Thanks for playing! Goodbye!")
            break # Exit the outer play-again loop

if __name__ == "__main__":
    main()