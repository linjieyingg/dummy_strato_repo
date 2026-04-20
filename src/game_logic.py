class ClickerGameLogic:
    """
    Manages the core business logic for a clicker game, handling the counter state.

    This class provides methods to increment, reset, and retrieve the current
    value of the game's primary counter.
    """

    def __init__(self):
        """
        Initializes the ClickerGameLogic with the counter set to zero.
        """
        self._counter = 0

    def increment_counter(self):
        """
        Increments the game counter by one.

        The counter value is always a non-negative integer.
        """
        self._counter += 1

    def reset_counter(self):
        """
        Resets the game counter to zero.
        """
        self._counter = 0

    def get_counter(self) -> int:
        """
        Retrieves the current value of the game counter.

        Returns:
            int: The current value of the counter.
        """
        return self._counter

# Example of how to use this class (for demonstration, not part of the final file)
if __name__ == "__main__":
    game_logic = ClickerGameLogic()
    print(f"Initial counter: {game_logic.get_counter()}")

    game_logic.increment_counter()
    game_logic.increment_counter()
    print(f"Counter after 2 increments: {game_logic.get_counter()}")

    game_logic.reset_counter()
    print(f"Counter after reset: {game_logic.get_counter()}")

    for _ in range(5):
        game_logic.increment_counter()
    print(f"Counter after 5 more increments: {game_logic.get_counter()}")