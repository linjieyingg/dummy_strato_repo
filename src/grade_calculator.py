from typing import Union

def calculate_grade(score: Union[int, float]) -> str:
    """
    Converts a numeric score (0-100) into a letter grade (A, B, C, D, F)
    based on a standard grading scale.

    Args:
        score (Union[int, float]): The numeric score to convert.
                                   Must be between 0 and 100, inclusive.

    Returns:
        str: The corresponding letter grade (A, B, C, D, or F).

    Raises:
        TypeError: If the score is not an int or float.
        ValueError: If the score is outside the valid range of 0 to 100.
    """
    if not isinstance(score, (int, float)):
        raise TypeError("Score must be a numeric value (integer or float).")

    if not (0 <= score <= 100):
        raise ValueError("Score must be between 0 and 100, inclusive.")

    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"

if __name__ == "__main__":
    # Example Usage and Demonstrations
    print("--- Grade Calculator Examples ---")

    # Valid scores
    print(f"Score 95: {calculate_grade(95)}")    # Expected: A
    print(f"Score 80: {calculate_grade(80)}")    # Expected: B
    print(f"Score 72.5: {calculate_grade(72.5)}") # Expected: C
    print(f"Score 60: {calculate_grade(60)}")    # Expected: D
    print(f"Score 45: {calculate_grade(45)}")    # Expected: F
    print(f"Score 100: {calculate_grade(100)}")  # Expected: A
    print(f"Score 0: {calculate_grade(0)}")      # Expected: F

    # Error handling demonstrations
    print("\n--- Error Handling ---")

    # Test case: score below 0
    try:
        print(f"Score -5: {calculate_grade(-5)}")
    except ValueError as e:
        print(f"Caught expected error for score -5: {e}")

    # Test case: score above 100
    try:
        print(f"Score 105: {calculate_grade(105)}")
    except ValueError as e:
        print(f"Caught expected error for score 105: {e}")

    # Test case: non-numeric string input
    try:
        print(f"Score 'ninety': {calculate_grade('ninety')}")
    except TypeError as e:
        print(f"Caught expected error for score 'ninety': {e}")

    # Test case: non-numeric list input
    try:
        print(f"Score [90]: {calculate_grade([90])}")
    except TypeError as e:
        print(f"Caught expected error for score [90]: {e}")

    # Test case: None input
    try:
        print(f"Score None: {calculate_grade(None)}")
    except TypeError as e:
        print(f"Caught expected error for score None: {e}")