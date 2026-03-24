import math

def calculate_sphere_volume(radius: float) -> float:
    """
    Calculates the volume of a sphere given its radius.

    The formula used is V = (4/3) * pi * r^3.

    Args:
        radius (float): The radius of the sphere. Must be a non-negative number.

    Returns:
        float: The volume of the sphere.

    Raises:
        TypeError: If the radius is not a number (int or float).
        ValueError: If the radius is a negative number.

    Examples:
        >>> calculate_sphere_volume(0)
        0.0
        >>> calculate_sphere_volume(1)
        4.1887902047863905
        >>> calculate_sphere_volume(2.5)
        65.44984694978735
    """
    if not isinstance(radius, (int, float)):
        raise TypeError("Radius must be a number (int or float).")
    if radius < 0:
        raise ValueError("Radius cannot be negative.")

    volume = (4/3) * math.pi * (radius ** 3)
    return volume

if __name__ == "__main__":
    # Example usage:
    try:
        r1 = 5.0
        vol1 = calculate_sphere_volume(r1)
        print(f"The volume of a sphere with radius {r1} is: {vol1:.4f}")

        r2 = 0
        vol2 = calculate_sphere_volume(r2)
        print(f"The volume of a sphere with radius {r2} is: {vol2:.4f}")

        r3 = 3
        vol3 = calculate_sphere_volume(r3)
        print(f"The volume of a sphere with radius {r3} is: {vol3:.4f}")

        # Example of error handling for negative radius
        r_neg = -2.0
        # vol_neg = calculate_sphere_volume(r_neg) # This would raise ValueError
    except TypeError as e:
        print(f"Error: {e}")
    except ValueError as e:
        print(f"Error: {e}")

    # Example of error handling for invalid type
    try:
        r_invalid_type = "abc"
        vol_invalid = calculate_sphere_volume(r_invalid_type)
        print(f"The volume of a sphere with radius {r_invalid_type} is: {vol_invalid:.4f}")
    except TypeError as e:
        print(f"Error: {e}")
    except ValueError as e:
        print(f"Error: {e}")