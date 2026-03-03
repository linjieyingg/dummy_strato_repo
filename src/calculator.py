# src/calculator.py

def multiply(num1: float, num2: float) -> float:
    """
    Multiplies two numbers and returns their product.

    This function takes two floating-point numbers or integers and returns
    their product as a float.

    Args:
        num1 (float): The first number to multiply.
        num2 (float): The second number to multiply.

    Returns:
        float: The product of num1 and num2.

    Examples:
        >>> multiply(5, 3)
        15.0
        >>> multiply(2.5, 4)
        10.0
        >>> multiply(-2, 0.5)
        -1.0
    """
    return num1 * num2