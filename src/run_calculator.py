import tkinter as tk
from src.calculator_ui import CalculatorApp

def main():
    """
    Main entry point for launching the Calculator GUI application.

    This function initializes the Tkinter root window, instantiates the
    CalculatorApp, and starts the Tkinter event loop, making the calculator
    application interactive.
    """
    root = tk.Tk()
    app = CalculatorApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()