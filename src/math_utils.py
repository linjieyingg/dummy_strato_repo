"""
This module provides general mathematical utility functions.
"""

def calculate_cube_volume(side: float) -> float:
    """
    Calculates the volume of a cube given its side length.

    Args:
        side (float): The length of one side of the cube. Must be a non-negative number.

    Returns:
        float: The volume of the cube (side * side * side).

    Raises:
        TypeError: If 'side' is not a number (int or float).
        ValueError: If 'side' is a negative number.

    Examples:
        >>> calculate_cube_volume(3)
        27.0
        >>> calculate_cube_volume(2.5)
        15.625
        >>> calculate_cube_volume(0)
        0.0
    """
    if not isinstance(side, (int, float)):
        raise TypeError("Side length must be a number (int or float).")
    if side < 0:
        raise ValueError("Side length cannot be negative.")

    return side ** 3

if __name__ == '__main__':
    # Example usage and testing
    try:
        print(f"Volume of cube with side 3: {calculate_cube_volume(3)}")
        print(f"Volume of cube with side 2.5: {calculate_cube_volume(2.5)}")
        print(f"Volume of cube with side 0: {calculate_cube_volume(0)}")
        
        # Test error handling
        # calculate_cube_volume(-5) # This should raise ValueError
        # calculate_cube_volume("abc") # This should raise TypeError

    except (TypeError, ValueError) as e:
        print(f"Error: {e}")