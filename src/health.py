def calculate_bmi(weight_kg: float, height_m: float) -> float:
    """
    Calculates the Body Mass Index (BMI) given a person's weight in kilograms
    and height in meters.

    The BMI is a measure that uses your height and weight to work out if your
    weight is healthy. It is calculated using the formula:
    BMI = weight (kg) / (height (m))^2

    Args:
        weight_kg (float): The person's weight in kilograms. Must be a positive
                           numeric value.
        height_m (float): The person's height in meters. Must be a positive
                          numeric value.

    Returns:
        float: The calculated Body Mass Index.

    Raises:
        TypeError: If either `weight_kg` or `height_m` is not a numeric type
                   (int or float).
        ValueError: If either `weight_kg` or `height_m` is zero or negative.
    """
    # Validate input types
    if not isinstance(weight_kg, (int, float)):
        raise TypeError("Weight must be a numeric type (integer or float).")
    if not isinstance(height_m, (int, float)):
        raise TypeError("Height must be a numeric type (integer or float).")

    # Validate input values
    if weight_kg <= 0:
        raise ValueError("Weight must be a positive number.")
    if height_m <= 0:
        raise ValueError("Height must be a positive number.")

    # Calculate BMI
    bmi = weight_kg / (height_m ** 2)

    return bmi