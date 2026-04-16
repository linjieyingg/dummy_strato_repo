import math # Not strictly needed for float('nan'), but common in numerical contexts.

class GraphEvaluator:
    """
    Evaluates a given mathematical expression function over a specified range of x-values
    to generate (x, y) coordinates suitable for plotting.

    This utility class expects a callable expression function (e.g., one produced
    by ExpressionParser.parse) that takes a single numerical argument 'x'.
    It generates a series of x-values within the given range and computes the
    corresponding y-values, handling potential evaluation errors by marking
    undefined points as NaN (Not a Number).
    """

    @staticmethod
    def evaluate_expression_for_range(
        parsed_expression_func, x_start: float, x_end: float, num_points: int
    ) -> list[tuple[float, float]]:
        """
        Evaluates a mathematical expression function across a range of x-values.

        Generates 'num_points' evenly spaced x-values between 'x_start' and 'x_end'
        (inclusive), evaluates the 'parsed_expression_func' for each x, and returns
        a list of (x, y) coordinate tuples. If the expression evaluation fails for
        a specific x-value (e.g., due to domain errors like sqrt(-1), division by zero,
        or other runtime errors), the corresponding y-value will be set to float('nan').

        Args:
            parsed_expression_func: A callable function that takes a single
                                    numeric argument (x) and returns a numeric result.
                                    This function is typically the output of
                                    ExpressionParser.parse().
            x_start: The starting x-value of the range.
            x_end: The ending x-value of the range.
            num_points: The number of (x,y) points to generate. Must be at least 2
                        to define a meaningful range.

        Returns:
            A list of tuples, where each tuple is an (x, y) coordinate.
            y-values will be float('nan') if evaluation fails for that x.

        Raises:
            TypeError: If parsed_expression_func is not callable, or x_start,
                       x_end are not numbers, or num_points is not an integer.
            ValueError: If num_points is less than 2.
        """
        # Validate input types
        if not callable(parsed_expression_func):
            raise TypeError("parsed_expression_func must be a callable function.")
        if not isinstance(x_start, (int, float)):
            raise TypeError("x_start must be a number.")
        if not isinstance(x_end, (int, float)):
            raise TypeError("x_end must be a number.")
        if not isinstance(num_points, int):
            raise TypeError("num_points must be an integer.")

        # Validate input values
        if num_points < 2:
            raise ValueError("num_points must be at least 2 to define a range for plotting.")

        # Ensure start and end values are floats for consistent arithmetic
        x_start = float(x_start)
        x_end = float(x_end)

        coordinates: list[tuple[float, float]] = []

        # Calculate the step size for x-values
        # (num_points - 1) is used because we want 'num_points' values including start and end
        step = (x_end - x_start) / (num_points - 1)

        for i in range(num_points):
            # Calculate the current x-value
            x = x_start + i * step
            
            # Adjust the last x-value to be exactly x_end to counteract
            # potential floating-point inaccuracies
            if i == num_points - 1:
                x = x_end

            y: float
            try:
                # Evaluate the expression for the current x-value
                # Convert result to float, as the expression might return int or other numeric type
                y = float(parsed_expression_func(x))
            except (ValueError, TypeError, ZeroDivisionError, OverflowError, NameError, Exception):
                # Catch common mathematical errors (e.g., log of negative, sqrt of negative,
                # division by zero) and any other unexpected runtime exceptions during evaluation.
                # Mark such points as NaN for graceful plotting.
                y = float('nan')
            
            coordinates.append((x, y))

        return coordinates