import math
from typing import Union

# A mapping of common place names to the 'ndigits' argument for the built-in round() function.
# Positive values for decimal places, negative values for integer places.
_ROUNDING_PLACES = {
    'ones': 0,
    'units': 0,  # Alias for ones
    'tens': -1,
    'hundreds': -2,
    'thousands': -3,
    'ten thousands': -4,
    'hundred thousands': -5,
    'millions': -6,
    'billions': -9,
    'trillions': -12,
    # Decimal places
    'tenths': 1,
    'hundredths': 2,
    'thousandths': 3,
    'ten thousandths': 4,
    'hundred thousandths': 5,
    'millionths': 6,
    'billionths': 9,
    'trillionths': 12,
}

def round_number_to_place(number: Union[float, int], place: str) -> float:
    """
    Rounds a given number to a specified place value.

    This function provides a flexible way to round numbers by using a string
    to define the desired precision, such as 'tens', 'hundredths', 'thousands',
    'tenths', etc.

    Args:
        number (Union[float, int]): The number to be rounded. Can be an integer
                                    or a floating-point number.
        place (str): A string indicating the place value to round to. The string
                     is case-insensitive and leading/trailing whitespace is ignored.

                     Supported place values include:
                     - Integer places: 'ones' (or 'units'), 'tens', 'hundreds',
                       'thousands', 'ten thousands', 'hundred thousands',
                       'millions', 'billions', 'trillions'.
                     - Decimal places: 'tenths', 'hundredths', 'thousandths',
                       'ten thousandths', 'hundred thousandths', 'millionths',
                       'billionths', 'trillionths'.

    Returns:
        float: The rounded number. The return type is float to consistently
               handle rounding to decimal places and to maintain type compatibility,
               even if the input was an integer or rounded to an integer place.

    Raises:
        TypeError: If 'number' is not an int or float, or 'place' is not a string.
        ValueError: If the 'place' string is not recognized or supported.

    Example Usage:
        >>> round_number_to_place(123.456, 'tens')
        120.0
        >>> round_number_to_place(123.456, 'hundredths')
        123.46
        >>> round_number_to_place(789, 'hundreds')
        800.0
        >>> round_number_to_place(99.999, 'tenths')
        100.0
        >>> round_number_to_place(12345.6789, 'thousands')
        12000.0
        >>> round_number_to_place(0.00123, 'thousandths')
        0.001
        >>> round_number_to_place(5.5, 'ones') # Demonstrates "round half to even"
        6.0
        >>> round_number_to_place(4.5, 'ones') # Demonstrates "round half to even"
        4.0
    """
    if not isinstance(number, (int, float)):
        raise TypeError(f"Expected 'number' to be an int or float, but got {type(number).__name__}")
    if not isinstance(place, str):
        raise TypeError(f"Expected 'place' to be a string, but got {type(place).__name__}")

    normalized_place = place.lower().strip()

    if normalized_place not in _ROUNDING_PLACES:
        supported_places = ', '.join(sorted(_ROUNDING_PLACES.keys()))
        raise ValueError(f"Unrecognized rounding place: '{place}'. "
                         f"Supported places are: {supported_places}")

    ndigits = _ROUNDING_PLACES[normalized_place]

    # Python's built-in round() function implements "round half to even"
    # (also known as "banker's rounding"). If a different rounding behavior
    # (e.g., round half up) is consistently required across the application,
    # the 'decimal' module or custom logic should be employed.
    return round(number, ndigits)