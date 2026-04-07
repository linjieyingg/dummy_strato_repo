def calculate_pyramid_volume(base_area: float, height: float) -> float:
    """
    Calculates the volume of a pyramid given its base area and height.

    The formula for the volume of a pyramid is V = (1/3) * base_area * height.

    Args:
        base_area (float): The area of the pyramid's base. Must be a non-negative number.
        height (float): The perpendicular height of the pyramid. Must be a non-negative number.

    Returns:
        float: The calculated volume of the pyramid.

    Raises:
        TypeError: If `base_area` or `height` is not a number (int or float).
        ValueError: If `base_area` or `height` is a negative number.

    Examples:
        >>> calculate_pyramid_volume(base_area=9.0, height=4.0)
        12.0
        >>> calculate_pyramid_volume(base_area=0.0, height=5.0)
        0.0
        >>> calculate_pyramid_volume(base_area=10.5, height=3.0)
        10.5
    """
    if not isinstance(base_area, (int, float)):
        raise TypeError("base_area must be a number (int or float).")
    if not isinstance(height, (int, float)):
        raise TypeError("height must be a number (int or float).")

    if base_area < 0:
        raise ValueError("base_area cannot be negative.")
    if height < 0:
        raise ValueError("height cannot be negative.")

    volume = (1 / 3) * base_area * height
    return float(volume)