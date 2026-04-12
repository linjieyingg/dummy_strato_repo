"""
This is the main entry point for the CLI Calculator application.

It initializes and starts the command-line interface loop defined in `src/cli.py`,
making the calculator accessible to the user.
"""

from src.cli import main as cli_main

if __name__ == "__main__":
    cli_main()