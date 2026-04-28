import pytest
import random
from unittest.mock import patch

from src.game.guess_number import GuessNumberGame

class TestGuessNumberGame:
    """
    Unit tests for the GuessNumberGame class in src/game/guess_number.py.
    This suite focuses on the initialization, parameter validation,
    and secret number generation aspects of the game logic.
    """

    def test_init_defaults(self):
        """
        Tests if the GuessNumberGame initializes with default parameters
        when no arguments are provided.
        """
        game = GuessNumberGame()
        assert game._min_num == GuessNumberGame.DEFAULT_MIN_NUMBER
        assert game._max_num == GuessNumberGame.DEFAULT_MAX_NUMBER
        assert game._max_attempts == GuessNumberGame.DEFAULT_MAX_ATTEMPTS
        assert hasattr(game, '_secret_number')
        assert GuessNumberGame.DEFAULT_MIN_NUMBER <= game._secret_number <= GuessNumberGame.DEFAULT_MAX_NUMBER
        assert game._attempts_left == GuessNumberGame.DEFAULT_MAX_ATTEMPTS

    def test_init_custom_parameters(self):
        """
        Tests if the GuessNumberGame initializes correctly with custom
        min_num, max_num, and max_attempts.
        """
        custom_min = 10
        custom_max = 20
        custom_attempts = 5
        game = GuessNumberGame(min_num=custom_min, max_num=custom_max, max_attempts=custom_attempts)
        assert game._min_num == custom_min
        assert game._max_num == custom_max
        assert game._max_attempts == custom_attempts
        assert hasattr(game, '_secret_number')
        assert custom_min <= game._secret_number <= custom_max
        assert game._attempts_left == custom_attempts

    @pytest.mark.parametrize("min_num, max_num", [
        (10, 10),  # min_num equals max_num
        (20, 10),  # min_num greater than max_num
        (0, 0)
    ])
    def test_init_value_error_min_ge_max(self, min_num, max_num):
        """
        Tests that GuessNumberGame raises a ValueError if min_num is
        greater than or equal to max_num.
        """
        with pytest.raises(ValueError, match="min_num must be less than max_num"):
            GuessNumberGame(min_num=min_num, max_num=max_num)

    @pytest.mark.parametrize("max_attempts", [
        0,   # zero attempts
        -1,  # negative attempts
        -10
    ])
    def test_init_value_error_non_positive_attempts(self, max_attempts):
        """
        Tests that GuessNumberGame raises a ValueError if max_attempts is
        not a positive integer.
        """
        with pytest.raises(ValueError, match="max_attempts must be a positive integer"):
            GuessNumberGame(max_attempts=max_attempts)

    @pytest.mark.parametrize("min_num, max_num, max_attempts", [
        ("1", 100, 10),
        (1, "100", 10),
        (1, 100, "10"),
        (1.0, 100, 10),
        (1, 100.0, 10),
        (1, 100, 10.0),
        (None, None, "invalid") # only one invalid type
    ])
    def test_init_type_error_for_non_integers(self, min_num, max_num, max_attempts):
        """
        Tests that GuessNumberGame raises a TypeError if min_num, max_num,
        or max_attempts are provided but are not integers.
        """
        # Ensure that only the arguments being tested are passed, defaults for others
        # if a default is None in test, it will use class default.
        params = {}
        if min_num is not None:
            params['min_num'] = min_num
        if max_num is not None:
            params['max_num'] = max_num
        if max_attempts is not None:
            params['max_attempts'] = max_attempts

        with pytest.raises(TypeError, match="min_num, max_num, and max_attempts must be integers"):
            GuessNumberGame(**params)

    @patch('random.randint')
    def test_secret_number_generation(self, mock_randint):
        """
        Tests that the secret number is generated using random.randint
        within the specified range.
        """
        # Configure the mock to return a specific number
        mock_randint.return_value = 50

        min_val = 1
        max_val = 100
        game = GuessNumberGame(min_num=min_val, max_num=max_val)

        # Assert that random.randint was called with the correct range
        mock_randint.assert_called_once_with(min_val, max_val)
        # Assert that the game's secret number is what the mock returned
        assert game._secret_number == 50

    # Test initial attempts left
    def test_initial_attempts_left(self):
        """
        Tests that _attempts_left is correctly initialized to max_attempts.
        """
        game_default = GuessNumberGame()
        assert game_default._attempts_left == GuessNumberGame.DEFAULT_MAX_ATTEMPTS

        custom_attempts = 7
        game_custom = GuessNumberGame(max_attempts=custom_attempts)
        assert game_custom._attempts_left == custom_attempts

# Note: The provided `src/game/guess_number.py` code snippet was incomplete
# beyond the __init__ method's initial parameter processing.
# Therefore, tests for game logic methods like `make_guess`, `is_game_over`,
# `has_won`, `get_feedback`, etc., are not included here as their
# implementation details were not available. These would be added once
# those methods are fully defined in the source file.