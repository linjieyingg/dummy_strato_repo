import math

def calculate_cylinder_volume(radius: float, height: float) -> float:
    """
    Calculates the volume of a cylinder given its radius and height.

    The formula for the volume of a cylinder is V = π * r^2 * h.

    Args:
        radius (float): The radius of the cylinder's base. Must be a non-negative number.
        height (float): The height of the cylinder. Must be a non-negative number.

    Returns:
        float: The calculated volume of the cylinder.

    Raises:
        TypeError: If radius or height is not a number (int or float).
        ValueError: If radius or height is a negative number.

    Examples:
        >>> calculate_cylinder_volume(1, 1)
        3.141592653589793
        >>> calculate_cylinder_volume(2.5, 3.0)
        58.90486225480862
    """
    if not isinstance(radius, (int, float)):
        raise TypeError("Radius must be a number (int or float).")
    if not isinstance(height, (int, float)):
        raise TypeError("Height must be a number (int or float).")

    if radius < 0:
        raise ValueError("Radius cannot be negative.")
    if height < 0:
        raise ValueError("Height cannot be negative.")

    volume = math.pi * (radius ** 2) * height
    return volume

# Example usage (for internal testing, not executed when imported)
if __name__ == "__main__":
    try:
        # Valid cases
        print(f"Volume of cylinder with radius 1, height 1: {calculate_cylinder_volume(1, 1)}")
        print(f"Volume of cylinder with radius 2.5, height 3.0: {calculate_cylinder_volume(2.5, 3.0)}")
        print(f"Volume of cylinder with radius 0, height 5: {calculate_cylinder_volume(0, 5)}") # Should be 0

        # Invalid type cases
        # calculate_cylinder_volume("1", 1) # This would raise TypeError
        # calculate_cylinder_volume(1, "1") # This would raise TypeError

        # Invalid value cases
        # calculate_cylinder_volume(-1, 1) # This would raise ValueError
        # calculate_cylinder_volume(1, -1) # This would raise ValueError

    except (TypeError, ValueError) as e:
        print(f"Error: {e}")