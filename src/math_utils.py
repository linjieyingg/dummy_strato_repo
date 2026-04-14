import math

def is_perfect_square(n: int) -> bool:
    """
    Checks if a given integer is a perfect square.

    A perfect square is an integer that can be expressed as the product of
    an integer by itself; that is, the square of an integer.

    Args:
        n: The integer to check.

    Returns:
        True if n is a perfect square, False otherwise.

    Raises:
        TypeError: If the input 'n' is not an integer.

    Examples:
        >>> is_perfect_square(4)
        True
        >>> is_perfect_square(9)
        True
        >>> is_perfect_square(2)
        False
        >>> is_perfect_square(0)
        True
        >>> is_perfect_square(-1)
        False
    """
    if not isinstance(n, int):
        raise TypeError("Input 'n' must be an integer.")

    if n < 0:
        return False

    # math.isqrt is available from Python 3.8+ and is robust for large integers.
    # It returns the integer square root.
    root = math.isqrt(n)
    return root * root == n

# Example of how to use it (for self-testing, not part of the module function)
if __name__ == '__main__':
    print(f"Is 4 a perfect square? {is_perfect_square(4)}")       # Expected: True
    print(f"Is 9 a perfect square? {is_perfect_square(9)}")       # Expected: True
    print(f"Is 2 a perfect square? {is_perfect_square(2)}")       # Expected: False
    print(f"Is 0 a perfect square? {is_perfect_square(0)}")       # Expected: True
    print(f"Is -1 a perfect square? {is_perfect_square(-1)}")     # Expected: False
    print(f"Is 16 a perfect square? {is_perfect_square(16)}")     # Expected: True
    print(f"Is 100000000 a perfect square? {is_perfect_square(100000000)}") # Expected: True (10000*10000)

    try:
        is_perfect_square(4.0)
    except TypeError as e:
        print(f"Caught expected error: {e}") # Expected: TypeError: Input 'n' must be an integer.

    try:
        is_perfect_square("abc")
    except TypeError as e:
        print(f"Caught expected error: {e}") # Expected: TypeError: Input 'n' must be an integer.