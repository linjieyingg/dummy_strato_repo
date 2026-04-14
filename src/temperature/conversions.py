"""
This module provides utility functions for temperature unit conversions.
Currently supports conversions from Celsius to Fahrenheit.
"""

def celsius_to_fahrenheit(celsius: float) -> float:
    """
    Converts a temperature from Celsius to Fahrenheit.

    The formula used is: F = C * 9/5 + 32

    Args:
        celsius (float): The temperature in degrees Celsius.

    Returns:
        float: The equivalent temperature in degrees Fahrenheit.

    Raises:
        TypeError: If the input 'celsius' is not a numeric type (int or float).
        ValueError: Although not strictly necessary for this formula,
                    could be added for future functions requiring specific ranges.
                    For now, any numeric value is valid.
    """
    if not isinstance(celsius, (int, float)):
        raise TypeError("Input 'celsius' must be a numeric type (int or float).")

    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

# Future functions could be added here, e.g.:
# def fahrenheit_to_celsius(fahrenheit: float) -> float:
#     """Converts Fahrenheit to Celsius."""
#     if not isinstance(fahrenheit, (int, float)):
#         raise TypeError("Input 'fahrenheit' must be a numeric type (int or float).")
#     celsius = (fahrenheit - 32) * 5/9
#     return celsius

# def celsius_to_kelvin(celsius: float) -> float:
#     """Converts Celsius to Kelvin."""
#     if not isinstance(celsius, (int, float)):
#         raise TypeError("Input 'celsius' must be a numeric type (int or float).")
#     kelvin = celsius + 273.15
#     return kelvin

# def kelvin_to_celsius(kelvin: float) -> float:
#     """Converts Kelvin to Celsius."""
#     if not isinstance(kelvin, (int, float)):
#         raise TypeError("Input 'kelvin' must be a numeric type (int or float).")
#     if kelvin < 0:
#         raise ValueError("Kelvin temperature cannot be below absolute zero (0 K).")
#     celsius = kelvin - 273.15
#     return celsius