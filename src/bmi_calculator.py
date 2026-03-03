def calculate_bmi(weight_kg: float, height_m: float) -> float:
    """
    Calculates the Body Mass Index (BMI) given weight in kilograms and height in meters.

    BMI is a measure that uses your height and weight to work out if your weight is
    healthy. It's calculated using the formula: weight (kg) / [height (m)]^2.

    Args:
        weight_kg (float): The person's weight in kilograms.
        height_m (float): The person's height in meters.

    Returns:
        float: The calculated Body Mass Index.

    Raises:
        TypeError: If either weight_kg or height_m is not a number (int or float).
        ValueError: If weight_kg or height_m is non-positive, or if height_m is zero.
    """
    if not isinstance(weight_kg, (int, float)):
        raise TypeError("Weight must be a numeric value (integer or float).")
    if not isinstance(height_m, (int, float)):
        raise TypeError("Height must be a numeric value (integer or float).")

    if weight_kg <= 0:
        raise ValueError("Weight must be a positive value.")
    if height_m <= 0:
        if height_m == 0:
            raise ValueError("Height cannot be zero, as it would lead to division by zero.")
        else:
            raise ValueError("Height must be a positive value.")

    bmi = weight_kg / (height_m ** 2)
    return bmi

if __name__ == "__main__":
    # Example Usage and Demonstrations
    print("--- BMI Calculator Examples ---")

    # Valid cases
    try:
        bmi1 = calculate_bmi(70, 1.75)
        print(f"Weight: 70kg, Height: 1.75m -> BMI: {bmi1:.2f}") # Expected: 22.86
    except (TypeError, ValueError) as e:
        print(f"Error calculating BMI: {e}")

    try:
        bmi2 = calculate_bmi(95.5, 1.83)
        print(f"Weight: 95.5kg, Height: 1.83m -> BMI: {bmi2:.2f}") # Expected: 28.56
    except (TypeError, ValueError) as e:
        print(f"Error calculating BMI: {e}")

    # Invalid weight (non-numeric)
    print("\n--- Testing Invalid Inputs ---")
    try:
        calculate_bmi("70", 1.75)
    except TypeError as e:
        print(f"Caught expected TypeError for non-numeric weight: {e}")
    except ValueError as e:
        print(f"Caught unexpected ValueError: {e}")

    # Invalid height (non-numeric)
    try:
        calculate_bmi(70, [1.75])
    except TypeError as e:
        print(f"Caught expected TypeError for non-numeric height: {e}")
    except ValueError as e:
        print(f"Caught unexpected ValueError: {e}")

    # Invalid weight (zero)
    try:
        calculate_bmi(0, 1.75)
    except ValueError as e:
        print(f"Caught expected ValueError for zero weight: {e}")
    except TypeError as e:
        print(f"Caught unexpected TypeError: {e}")

    # Invalid weight (negative)
    try:
        calculate_bmi(-70, 1.75)
    except ValueError as e:
        print(f"Caught expected ValueError for negative weight: {e}")
    except TypeError as e:
        print(f"Caught unexpected TypeError: {e}")

    # Invalid height (zero)
    try:
        calculate_bmi(70, 0)
    except ValueError as e:
        print(f"Caught expected ValueError for zero height: {e}")
    except TypeError as e:
        print(f"Caught unexpected TypeError: {e}")

    # Invalid height (negative)
    try:
        calculate_bmi(70, -1.75)
    except ValueError as e:
        print(f"Caught expected ValueError for negative height: {e}")
    except TypeError as e:
        print(f"Caught unexpected TypeError: {e}")

    print("\n--- End of Examples ---")