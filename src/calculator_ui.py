import tkinter as tk
from tkinter import messagebox
# Importing calculator functions from the sibling module `src.calculator`.
# The repository context implies that `multiply` and `divide` functions
# also exist in `src.calculator` with similar signatures to `add` and `subtract`.
from src.calculator import add, subtract, multiply, divide


class CalculatorApp:
    """
    A simple calculator application with a graphical user interface (GUI)
    built using Python's built-in Tkinter library. It constructs the window,
    buttons for digits and operations, a display field, and manages user interactions.
    It calls functions from `src.calculator` to perform the actual computations
    based on user input.
    """

    def __init__(self, master):
        """
        Initializes the CalculatorApp GUI and sets up its internal state.

        Args:
            master (tk.Tk): The root Tkinter window for the application.
        """
        self.master = master
        master.title("Calculator")
        master.resizable(False, False)  # Make window non-resizable for consistent look

        # StringVar to hold the current input/display value in the Entry widget
        self.input_text = tk.StringVar()
        # Internal string to build the current number being typed by the user
        self.expression = ""

        # Input display field (Entry widget)
        # Set to 'readonly' to prevent direct keyboard input into the display
        self.input_field = tk.Entry(master, textvariable=self.input_text,
                                    font=('arial', 20, 'bold'),
                                    bd=5, insertwidth=4, width=14,
                                    justify='right', state='readonly')
        self.input_field.grid(row=0, column=0, columnspan=4, padx=5, pady=5)

        self.create_buttons()

        # Internal state variables for calculator logic
        self.first_operand = None  # Stores the first number of an ongoing operation
        self.operator = None       # Stores the selected arithmetic operator (+, -, *, /)
        # Flag to indicate if the next digit pressed should start a new number
        # (e.g., after an operator has been selected or a calculation has been performed)
        self.waiting_for_second_operand = False

    def create_buttons(self):
        """
        Creates and places all calculator buttons on the GUI using a grid layout.
        The 'C' (Clear) button spans all columns at the top.
        Digits, decimal point, and arithmetic operators form a 4x4 grid below it.
        """
        # Create and place the 'C' (Clear) button, spanning all 4 columns
        tk.Button(self.master, text='C', width=22, height=2,
                  font=('arial', 15, 'bold'),
                  command=self.clear_all, bg='#ff6666', fg='white',
                  relief='raised', bd=2).grid(row=1, column=0, columnspan=4, padx=2, pady=2)

        # Define the layout for the rest of the buttons (digits, decimal, operators, equals)
        buttons_layout = [
            ['7', '8', '9', '/'],
            ['4', '5', '6', '*'],
            ['1', '2', '3', '-'],
            ['.', '0', '=', '+']
        ]

        # Starting row for these buttons, after the 'C' button (which is on row 1)
        row_val = 2

        for row_buttons in buttons_layout:
            col_val = 0
            for button_text in row_buttons:
                button_command = None
                button_bg = '#f0f0f0'  # Default light grey for digits
                button_fg = 'black'

                if button_text in ['/', '*', '-', '+']:
                    # Assign `set_operator` command for operator buttons
                    button_command = lambda b=button_text: self.set_operator(b)
                    button_bg = '#ffa500'  # Orange background for operators
                    button_fg = 'white'
                elif button_text == '=':
                    # Assign `calculate` command for the equals button
                    button_command = self.calculate
                    button_bg = '#4CAF50'  # Green background for equals
                    button_fg = 'white'
                else:  # Digits and decimal point
                    # Assign `button_press` command for digits and decimal
                    button_command = lambda b=button_text: self.button_press(b)
                    if button_text == '.':
                        button_bg = '#e0e0e0' # Slightly darker for decimal

                # Create and place the button
                tk.Button(self.master, text=button_text, width=5, height=2,
                          font=('arial', 15, 'bold'),
                          command=button_command, bg=button_bg, fg=button_fg,
                          relief='raised', bd=2).grid(row=row_val, column=col_val, padx=2, pady=2)
                col_val += 1
            row_val += 1

    def button_press(self, char):
        """
        Handles button presses for digits (0-9) and the decimal point (.).
        Appends the character to the current `self.expression` or starts a new
        expression if `self.waiting_for_second_operand` is true.

        Args:
            char (str): The digit or decimal point character pressed.
        """
        if self.waiting_for_second_operand:
            # If waiting for the second operand, start a new expression
            self.expression = str(char)
            self.waiting_for_second_operand = False
        else:
            # Prevent multiple decimal points in a single number
            if char == '.' and '.' in self.expression:
                return
            # If starting a number with a decimal, prepend "0."
            if not self.expression and char == '.':
                self.expression = "0."
            else:
                self.expression += str(char)
        
        # Update the display field with the current expression
        self.input_text.set(self.expression)

    def set_operator(self, op):
        """
        Handles operator button presses (+, -, *, /).
        Stores the current number as `self.first_operand` and the selected operator.
        If an operator is pressed consecutively after another, it implicitly
        performs the pending calculation first to chain operations (e.g., 5 + 3 +).

        Args:
            op (str): The operator character pressed.
        """
        try:
            # If there's an existing expression, parse it as a potential operand
            if self.expression:
                current_value = float(self.expression)
                if self.first_operand is not None and self.operator is not None:
                    # If an operation is already pending, calculate the result first
                    # The result from calculate() will update self.first_operand
                    self.calculate()
                    # Ensure current_value is updated from the result if calculate was called
                    current_value = self.first_operand
                else:
                    self.first_operand = current_value
            elif self.first_operand is None:
                # If no expression and no first_operand (e.g., operator pressed first), do nothing
                # Or if operator pressed after initial clear
                return

            self.operator = op
            self.waiting_for_second_operand = True
            # Display the first operand (or intermediate result) on the screen
            self.input_text.set(self._format_result(self.first_operand))

        except ValueError:
            messagebox.showerror("Error", "Invalid number format for operand.")
            self.clear_all()
        except Exception as e:
            messagebox.showerror("Error", f"An unexpected error occurred: {e}")
            self.clear_all()

    def calculate(self):
        """
        Performs the calculation when the '=' button is pressed.
        It retrieves the second operand, calls the appropriate function from `src.calculator`,
        and displays the result. It handles common calculator behaviors like
        "5 + =" (repeating the first operand) and error conditions.
        """
        # If there's no pending operation (`first_operand` or `operator` is missing),
        # but there is a number in the display, just validate and re-display it.
        if self.first_operand is None or self.operator is None:
            if self.expression:
                try:
                    float(self.expression)  # Validate it's a number
                    self.input_text.set(self._format_result(float(self.expression)))
                except ValueError:
                    messagebox.showerror("Error", "Invalid number format.")
                    self.clear_all()
            return  # Nothing to calculate

        second_operand = None
        current_display_value = self.input_text.get()

        # Determine the second operand for the calculation
        if self.waiting_for_second_operand and not self.expression:
            # Case: User pressed an operator, then immediately '=',
            # implying the second operand is the same as the first operand (e.g., 5 + = should be 10)
            second_operand = self.first_operand
        elif current_display_value:
            try:
                second_operand = float(current_display_value)
            except ValueError:
                messagebox.showerror("Error", "Invalid number format for second operand.")
                self.clear_all()
                return
        else:
            # This case should ideally not be reached if the state is managed correctly,
            # but acts as a fallback for missing second operand.
            messagebox.showerror("Error", "Missing second operand for calculation.")
            self.clear_all()
            return
        
        result = None
        try:
            # Call the appropriate calculator function based on the stored operator
            if self.operator == '+':
                result = add(self.first_operand, second_operand)
            elif self.operator == '-':
                result = subtract(self.first_operand, second_operand)
            elif self.operator == '*':
                result = multiply(self.first_operand, second_operand)
            elif self.operator == '/':
                result = divide(self.first_operand, second_operand)
            
            # Display the result and update the calculator's state for subsequent operations
            self.input_text.set(self._format_result(result))
            self.expression = str(result)  # Set internal expression to result for next input if it's a digit
            self.first_operand = result    # The result becomes the new first operand for chaining operations
            self.operator = None           # Clear the operator as the current calculation is complete
            self.waiting_for_second_operand = True # Ready for a new number or operator

        except TypeError as e:
            # Catch TypeErrors from `src.calculator` functions (e.g., non-numeric input)
            messagebox.showerror("Calculation Error", f"Type Error: {e}")
            self.clear_all()
        except ZeroDivisionError:
            # Catch ZeroDivisionError specifically for division by zero
            messagebox.showerror("Calculation Error", "Cannot divide by zero.")
            self.clear_all()
        except Exception as e:
            # Catch any other unexpected errors during calculation
            messagebox.showerror("Calculation Error", f"An unexpected error occurred: {e}")
            self.clear_all()

    def clear_all(self):
        """
        Resets all internal calculator state variables and clears the display.
        This function is typically triggered by the 'C' button.
        """
        self.expression = ""
        self.input_text.set("")
        self.first_operand = None
        self.operator = None
        self.waiting_for_second_operand = False

    def _format_result(self, value):
        """
        Helper method to format the numerical result, displaying whole numbers
        without a trailing '.0' (e.g., "10" instead of "10.0").

        Args:
            value (int or float): The numerical result to format.

        Returns:
            str: The formatted string representation of the result.
        """
        if isinstance(value, (int, float)):
            if value == int(value):  # Check if the float is a whole number
                return str(int(value))
        return str(value)


# Main execution block to create and run the Tkinter application
if __name__ == "__main__":
    root = tk.Tk()
    app = CalculatorApp(root)
    root.mainloop()