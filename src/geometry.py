def calculate_pyramid_volume(base_area, height):
    """
    Calculates the volume of a pyramid.

    Args:
        base_area (int or float): The area of the pyramid's base.
        height (int or float): The height of the pyramid.

    Returns:
        float: The volume of the pyramid.

    Raises:
        TypeError: If base_area or height is not a number.
        ValueError: If base_area or height is negative.
    """
    if not isinstance(base_area, (int, float)):
        raise TypeError("Base area must be a number.")
    if not isinstance(height, (int, float)):
        raise TypeError("Height must be a number.")
    if base_area < 0:
        raise ValueError("Base area cannot be negative.")
    if height < 0:
        raise ValueError("Height cannot be negative.")

    return (1/3) * float(base_area) * float(height)

def calculate_cube_volume(side_length):
    """
    Calculates the volume of a cube.

    Args:
        side_length (int or float): The length of one side of the cube.

    Returns:
        float: The volume of the cube.

    Raises:
        TypeError: If side_length is not a number.
        ValueError: If side_length is negative.
    """
    if not isinstance(side_length, (int, float)):
        raise TypeError("Side length must be a number.")
    if side_length < 0:
        raise ValueError("Side length cannot be negative.")
    
    return float(side_length ** 3)