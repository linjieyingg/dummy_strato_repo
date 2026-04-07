import re

def binary_to_decimal(binary_str: str) -> int:
    """
    Converts a binary string to its decimal integer equivalent.

    This function takes a string representing a binary number (composed solely of '0's and '1's)
    and converts it into its corresponding base-10 integer value.

    Args:
        binary_str (str): The binary number as a string.

    Returns:
        int: The decimal integer representation of the binary string.

    Raises:
        TypeError: If `binary_str` is not a string.
        ValueError: If `binary_str` is empty, or contains characters other than '0' or '1'.

    Examples:
        >>> binary_to_decimal("101")
        5
        >>> binary_to_decimal("1111")
        15
        >>> binary_to_decimal("0")
        0
        >>> binary_to_decimal("10000000")
        128
    """
    if not isinstance(binary_str, str):
        raise TypeError("Input 'binary_str' must be a string.")
    
    if not binary_str:
        raise ValueError("Input 'binary_str' cannot be an empty string.")

    # Use a regular expression to check if the string contains only '0's and '1's
    if not re.fullmatch(r"[01]+", binary_str):
        raise ValueError("Input 'binary_str' must contain only '0's and '1's.")

    decimal_value = 0
    power = 0
    # Iterate through the binary string from right to left (least significant bit to most significant bit)
    for digit in reversed(binary_str):
        if digit == '1':
            decimal_value += 2**power
        power += 1
    
    return decimal_value

# Example of how this might be used or tested
if __name__ == "__main__":
    print(f"'101' in decimal is: {binary_to_decimal('101')}")
    print(f"'1111' in decimal is: {binary_to_decimal('1111')}")
    print(f"'0' in decimal is: {binary_to_decimal('0')}")
    print(f"'10000000' in decimal is: {binary_to_decimal('10000000')}")

    try:
        binary_to_decimal("102")
    except ValueError as e:
        print(f"Error for '102': {e}")

    try:
        binary_to_decimal("")
    except ValueError as e:
        print(f"Error for empty string: {e}")
    
    try:
        binary_to_decimal(101)
    except TypeError as e:
        print(f"Error for integer input: {e}")