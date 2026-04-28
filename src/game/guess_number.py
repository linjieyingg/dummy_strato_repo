import random

class GuessNumberGame:
    """
    Manages the core logic for a 'Guess the Number' game.

    This class handles generating a secret number, validating guesses,
    tracking attempts, and managing the game state (won/lost).
    """

    DEFAULT_MIN_NUMBER = 1
    DEFAULT_MAX_NUMBER = 100
    DEFAULT_MAX_ATTEMPTS = 10

    def __init__(self, min_num: int = None, max_num: int = None, max_attempts: int = None):
        """
        Initializes a new GuessNumberGame instance.

        Args:
            min_num (int, optional): The minimum possible number for the secret.
                                     Defaults to DEFAULT_MIN_NUMBER.
            max_num (int, optional): The maximum possible number for the secret.
                                     Defaults to DEFAULT_MAX_NUMBER.
            max_attempts (int, optional): The maximum number of guesses allowed.
                                          Defaults to DEFAULT_MAX_ATTEMPTS.

        Raises:
            ValueError: If min_num is greater than or equal to max_num,
                        or if max_attempts is not positive.
            TypeError: If min_num, max_num, or max_attempts are provided but are not integers.
        """
        # Set defaults if not provided
        self._min_num = min_num if min_num is not None else self.DEFAULT_MIN_NUMBER
        self._max_num = max_num if max_num is not None else self.DEFAULT_MAX_NUMBER
        self._max_attempts = max_attempts if max_attempts is not None else self.DEFAULT_MAX_ATTEMPTS

        # Type validation
        if not isinstance(self._min_num, int) or \
           not isinstance(self._max_num, int) or \
           not isinstance(self._max_attempts, int):
            raise TypeError("min_num, max_num, and max_attempts must be integers.")

        # Value validation
        if self._min_num >= self._max_num:
            raise ValueError(f"Minimum number ({self._min_num}) must be less than "
                             f"the maximum number ({self._max_num}).")
        if self._max_attempts <= 0:
            raise ValueError(f"Maximum attempts ({self._max_attempts}) must be a positive integer.")

        self._secret_number: int = 0  # To be set when game starts
        self._attempts_left: int = 0
        self._game_won: bool = False

        self.start_new_game()

    def _generate_secret_number(self) -> int:
        """
        Generates a random secret number within the configured range (inclusive).

        Returns:
            int: The randomly generated secret number.
        """
        return random.randint(self._min_num, self._max_num)

    def start_new_game(self) -> None:
        """
        Resets the game to a new state.

        A new secret number is generated, attempts are reset to max_attempts,
        and the game_won flag is cleared.
        """
        self._secret_number = self._generate_secret_number()
        self._attempts_left = self._max_attempts
        self._game_won = False

    def check_guess(self, guess: int) -> str:
        """
        Checks a player's guess against the secret number and updates the game state.

        Args:
            guess (int): The player's numerical guess.

        Returns:
            str: A feedback message ("Too high!", "Too low!", "Correct!",
                 "Game over - you lost! The number was X.", or "Game over - you won!").
                 If the game is already over, it returns a game over status message
                 without consuming an attempt.

        Raises:
            TypeError: If the guess is not an integer.
        """
        if not isinstance(guess, int):
            raise TypeError("Guess must be an integer.")

        # If game is already over, prevent further guesses, just report status
        if self.is_game_over():
            if self._game_won:
                return "Game over - you won!"
            else:
                return f"Game over - you lost! The number was {self._secret_number}."

        self._attempts_left -= 1
        feedback_message: str

        if guess < self._secret_number:
            feedback_message = "Too low!"
        elif guess > self._secret_number:
            feedback_message = "Too high!"
        else:
            self._game_won = True
            feedback_message = "Correct!"

        # After processing the guess, check if the game has now ended
        if self._game_won:
            return feedback_message
        elif self._attempts_left == 0:
            return f"{feedback_message} Game over - you lost! The number was {self._secret_number}."
        else:
            return feedback_message

    def is_game_over(self) -> bool:
        """
        Checks if the game has ended.

        The game is over if the player has won or if all attempts have been exhausted.

        Returns:
            bool: True if the game is over, False otherwise.
        """
        return self._game_won or self._attempts_left <= 0

    def is_game_won(self) -> bool:
        """
        Returns whether the current game has been won.

        Returns:
            bool: True if the game is won, False otherwise.
        """
        return self._game_won

    def get_remaining_attempts(self) -> int:
        """
        Returns the number of attempts left in the current game.

        Returns:
            int: The current count of remaining attempts.
        """
        return self._attempts_left

    def get_secret_number(self) -> int:
        """
        Returns the current secret number.

        This method is primarily for internal use, debugging, or revealing
        the number after a game ends.

        Returns:
            int: The secret number.
        """
        return self._secret_number

    def get_range(self) -> tuple[int, int]:
        """
        Returns the configured minimum and maximum numbers for the game.

        Returns:
            tuple[int, int]: A tuple containing (min_num, max_num).
        """
        return (self._min_num, self._max_num)

    def get_max_attempts(self) -> int:
        """
        Returns the total number of attempts initially allowed for the game.

        Returns:
            int: The maximum number of attempts.
        """
        return self._max_attempts