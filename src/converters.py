def meters_to_centimeters(meters):
    """
    Converts a length from meters to centimeters.

    Args:
        meters (int or float): The length in meters to convert.

    Returns:
        float: The equivalent length in centimeters.

    Raises:
        TypeError: If the input 'meters' is not an integer or a float.

    Example:
        >>> meters_to_centimeters(1.5)
        150.0
        >>> meters_to_centimeters(2)
        200.0
    """
    if not isinstance(meters, (int, float)):
        raise TypeError("Input 'meters' must be an integer or a float.")
    
    return float(meters * 100)

if __name__ == "__main__":
    # Example Usage
    print(f"1.5 meters is {meters_to_centimeters(1.5)} centimeters.")
    print(f"2 meters is {meters_to_centimeters(2)} centimeters.")
    print(f"0.75 meters is {meters_to_centimeters(0.75)} centimeters.")

    # Example of error handling
    try:
        meters_to_centimeters("abc")
    except TypeError as e:
        print(f"Error: {e}")

    try:
        meters_to_centimeters([1, 2])
    except TypeError as e:
        print(f"Error: {e}")