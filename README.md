---


## `tests/test_geometry.py`

This file contains a comprehensive suite of unit tests for the `calculate_pyramid_volume` function, ensuring its correctness across various valid inputs, edge cases, and error conditions.

### Key Components:

*   **Class**: `TestGeometry(unittest.TestCase)`
    *   **Purpose**: This class inherits from `unittest.TestCase` and groups all the individual test methods for the `calculate_pyramid_volume` function.
    *   **Methods**:
        *   `test_valid_positive_integers(self)`: Tests with valid positive integer inputs for base area and height.
        *   `test_valid_positive_floats(self)`: Tests with valid positive float inputs for base area and height.
        *   `test_zero_base_area(self)`: Tests the function's behavior when `base_area` is zero.
        *   `test_zero_height(self)`: Tests the function's behavior when `height` is zero.
        *   `test_both_zero(self)`: Tests when both `base_area` and `height` are zero.
        *   `test_large_inputs(self)`: Tests with large numeric inputs (integers and floats) to check precision and scale.
        *   `test_negative_base_area(self)`, `test_negative_height(self)`, `test_both_negative(self)`: Verify that a `ValueError` is raised when base area or height (or both) are negative.
        *   `test_non_numeric_base_area(self)`, `test_non_numeric_height(self)`, `test_non_numeric_both(self)`: Verify that a `TypeError` is raised when base area or height (or both) are non-numeric types.
    *   **Inputs**: Each test method takes `self` as an implicit argument.
    *   **Outputs/Side Effects**: Each method calls `calculate_pyramid_volume` with specific parameters and uses `self.assertAlmostEqual` to check the returned value against an expected result, or `self.assertRaisesRegex` to confirm that expected exceptions (`ValueError`, `TypeError`) are raised with specific messages. The methods themselves do not return values; their "output" is the success or failure of the assertions.

### Dependencies:

*   `unittest`: Python's built-in unit testing framework.
*   `src.geometry.calculate_pyramid_volume`: The function under test, imported from the `src` directory.

---


## `tests/utils_test.py`

---


## How to Run the Calculator

To run the command-line interface (CLI) for the calculator, execute the following command from the project root directory: