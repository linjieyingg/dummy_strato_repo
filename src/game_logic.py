import random

class GameLogic:
    """
    Manages the core business logic for the 'Guess the Number' game.

    This includes generating the target number, checking guesses, and
    maintaining the game state such as the number of attempts.
    """

    def __init__(self, min_num: int = 1, max_num: int = 100):
        """
        Initializes a new game session.

        Args:
            min_num (int): The minimum possible number for the target.
                            Must be an integer.
            max_num (int): The maximum possible number for the target.
                            Must be an integer and greater than or equal to min_num.

        Raises:
            TypeError: If min_num or max_num are not integers.
            ValueError: If min_num is greater than max_num.
        """
        if not isinstance(min_num, int):
            raise TypeError("min_num must be an integer.")
        if not isinstance(max_num, int):
            raise TypeError("max_num must be an integer.")
        if min_num > max_num:
            raise ValueError("min_num cannot be greater than max_num.")

        self._min_num: int = min_num
        self._max_num: int = max_num
        self._target_number: int = 0
        self._attempts_made: int = 0
        self._game_over: bool = False

        self.reset_game()

    def _generate_target_number(self) -> None:
        """
        Generates a random integer between _min_num and _max_num (inclusive)
        and sets it as the target number.
        """
        self._target_number = random.randint(self._min_num, self._max_num)

    def reset_game(self) -> None:
        """
        Resets the game state, generating a new target number and clearing
        the attempt count.
        """
        self._attempts_made = 0
        self._game_over = False
        self._generate_target_number()

    def check_guess(self, guess: int) -> str:
        """
        Checks the user's guess against the target number.

        Args:
            guess (int): The number guessed by the user.

        Returns:
            str: A message indicating if the guess was "Too low", "Too high",
                 or "Correct".

        Raises:
            TypeError: If the guess is not an integer.
            ValueError: If the guess is outside the allowed game range.
            RuntimeError: If the game is already over when a guess is made.
        """
        if self._game_over:
            raise RuntimeError("The game is over. Please reset to play again.")

        if not isinstance(guess, int):
            raise TypeError("Guess must be an integer.")
        if not (self._min_num <= guess <= self._max_num):
            raise ValueError(f"Guess must be between {self._min_num} and {self._max_num}.")

        self._attempts_made += 1

        if guess < self._target_number:
            return "Too low"
        elif guess > self._target_number:
            return "Too high"
        else:
            self._game_over = True
            return "Correct"

    def get_attempts_made(self) -> int:
        """
        Returns the number of attempts made so far in the current game.

        Returns:
            int: The current count of attempts.
        """
        return self._attempts_made

    def is_game_over(self) -> bool:
        """
        Indicates if the game has concluded (i.e., the correct number has been guessed).

        Returns:
            bool: True if the game is over, False otherwise.
        """
        return self._game_over

    def get_range(self) -> tuple[int, int]:
        """
        Returns the minimum and maximum numbers for the game's range.

        Returns:
            tuple[int, int]: A tuple containing (min_num, max_num).
        """
        return (self._min_num, self._max_num)

    def get_target_number(self) -> int:
        """
        Returns the target number to be guessed.
        This method is primarily for testing or revealing the number after game over.

        Returns:
            int: The hidden target number.
        """
        return self._target_number

    def set_target_number(self, target: int) -> None:
        """
        Sets a specific target number. Useful for testing or custom scenarios.

        Args:
            target (int): The number to set as the target.

        Raises:
            TypeError: If target is not an integer.
            ValueError: If target is outside the allowed game range.
        """
        if not isinstance(target, int):
            raise TypeError("Target number must be an integer.")
        if not (self._min_num <= target <= self._max_num):
            raise ValueError(f"Target number must be between {self._min_num} and {self._max_num}.")
        self._target_number = target
        self._attempts_made = 0
        self._game_over = False