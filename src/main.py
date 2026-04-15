import tkinter as tk
from src.game_ui import GameUI
from tkinter import messagebox

def main():
    """
    The main entry point for the 'Guess the Number' game application.

    Initializes the Tkinter root window, creates an instance of GameUI,
    and starts the Tkinter event loop. Includes basic error handling
    for the application's startup.
    """
    root = tk.Tk()
    try:
        # Initialize the GameUI, which in turn initializes GameLogic
        # Any errors during GameLogic or GameUI setup will be caught
        # by GameUI's internal error handling (messagebox and master.destroy)
        game_app = GameUI(root)
        # If GameUI initialization failed and called master.destroy(),
        # then the root window might already be destroyed.
        # Check if root is still alive before starting mainloop.
        if root.winfo_exists():
            root.mainloop()
    except Exception as e:
        # Catch any unexpected errors during the main setup process
        messagebox.showerror("Application Error", f"An unexpected error occurred during startup: {e}")
        if root.winfo_exists():
            root.destroy()

if __name__ == "__main__":
    main()