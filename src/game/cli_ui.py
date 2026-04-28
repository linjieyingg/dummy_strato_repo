import sys

class CliUI:
    """
    Handles all command-line user interactions for the game,
    such as displaying messages, prompts, and receiving user input.
    """

    @staticmethod
    def display_welcome_message(min_num: int, max_num: int, max_attempts: int) -> None:
        """
        Displays a welcome message to the player, including game rules.

        Args:
            min_num (int): The minimum number in the guessing range.
            max_num (int): The maximum number in the guessing range.
            max_attempts (int): The total number of attempts allowed.
        """
        print("-" * 50)
        print("         GUESS THE NUMBER GAME         ")
        print("-" * 50)
        print(f"I'm thinking of a number between {min_num} and {max_num}.")
        print(f"You have {max_attempts} attempts to guess it.")
        print("Good luck!\n")

    @staticmethod
    def prompt_for_guess(attempt_num: int, max_attempts: int) -> int:
        """
        Prompts the user to enter their guess and validates the input.

        Handles non-integer input and allows graceful exit via Ctrl+D.

        Args:
            attempt_num (int): The current attempt number (1-indexed).
            max_attempts (int): The total number of allowed attempts.

        Returns:
            int: The valid integer guess entered by the user.
        """
        while True:
            try:
                guess_str = input(f"Attempt {attempt_num}/{max_attempts}: Enter your guess: ")
                guess = int(guess_str)
                return guess
            except ValueError:
                CliUI.display_error_message("Invalid input. Please enter a whole number.")
            except EOFError:
                # Handle Ctrl+D or end of input stream
                CliUI.display_feedback("\nExiting game. Goodbye!") # Changed display_message to display_feedback
                sys.exit(0) # Exit the program gracefully

    @staticmethod
    def display_feedback(message: str) -> None:
        """
        Displays general feedback or information to the user.

        Args:
            message (str): The message to display.
        """
        print(message)

    @staticmethod
    def display_win_message(secret_number: int, attempts_taken: int) -> None:
        """
        Displays a message when the player successfully guesses the number.

        Args:
            secret_number (int): The number that was guessed.
            attempts_taken (int): The number of attempts it took to guess correctly.
        """
        print(f"\n🎉 Congratulations! You guessed the number {secret_number} correctly!")
        print(f"It took you {attempts_taken} attempts.")
        print("-" * 50)

    @staticmethod
    def display_lose_message(secret_number: int) -> None:
        """
        Displays a message when the player runs out of attempts.

        Args:
            secret_number (int): The secret number that was not guessed.
        """
        print(f"\nGame Over! You ran out of attempts.")
        print(f"The secret number was {secret_number}.")
        print("Better luck next time!")
        print("-" * 50)

    @staticmethod
    def prompt_to_play_again() -> bool:
        """
        Asks the user if they want to play another round.

        Returns:
            bool: True if the user wants to play again, False otherwise.
        """
        while True:
            try:
                choice = input("\nDo you want to play again? (yes/no): ").strip().lower()
                if choice in ['yes', 'y']:
                    return True
                elif choice in ['no', 'n']:
                    return False
                else:
                    CliUI.display_error_message("Invalid input. Please enter 'yes' or 'no'.")
            except EOFError:
                # Handle Ctrl+D during play again prompt
                CliUI.display_feedback("\nExiting game. Goodbye!") # Changed display_message to display_feedback
                sys.exit(0)

    @staticmethod
    def display_error_message(message: str) -> None:
        """
        Displays an error message to the user.

        Args:
            message (str): The error message to display.
        """
        print(f"ERROR: {message}", file=sys.stderr)