"""
main.py

This script serves as the primary entry point for the graphing calculator application.
It imports the graphing_ui module from the 'src' directory and launches its main
calculator UI function.
"""

import sys
import os

# --- Path Configuration for Module Imports ---
# Get the directory where this script (main.py) is located.
# This assumes main.py is in the project's root directory.
current_script_dir = os.path.dirname(os.path.abspath(__file__))

# Add the project's root directory to sys.path.
# This allows Python to find and import packages like 'src'.
if current_script_dir not in sys.path:
    sys.path.insert(0, current_script_dir)

# --- Module Import ---
try:
    # Import the graphing_ui module from the 'src' package.
    from src import graphing_ui
except ModuleNotFoundError:
    print("Error: The 'src' module or 'graphing_ui' within it was not found.", file=sys.stderr)
    print("Please ensure the 'src' directory is present in the project root "
          "and contains 'graphing_ui.py'.", file=sys.stderr)
    sys.exit(1)
except ImportError as e:
    print(f"Error importing graphing_ui: {e}", file=sys.stderr)
    print("Please check the 'src/graphing_ui.py' file for syntax errors or missing dependencies.", file=sys.stderr)
    sys.exit(1)


def main():
    """
    Main function to launch the graphing calculator UI.

    This function attempts to call the `run_calculator` function from the
    `graphing_ui` module. It includes basic error handling for cases where
    the function is missing or encounters a runtime error.
    """
    print("Launching Graphing Calculator UI...")
    try:
        # Call the main function to start the graphing calculator UI.
        # This function is expected to be defined in src/graphing_ui.py.
        graphing_ui.run_calculator()
    except AttributeError:
        print("Error: 'graphing_ui' module does not have a 'run_calculator' function.", file=sys.stderr)
        print("Please ensure src/graphing_ui.py defines a 'run_calculator()' function.", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(f"An unexpected error occurred while running the calculator UI: {e}", file=sys.stderr)
        sys.exit(1)
    print("Graphing Calculator UI session ended.")


if __name__ == "__main__":
    main()