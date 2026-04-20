import tkinter as tk
from src.game_ui import ClickerGameUI
from src.game_logic import ClickerGameLogic # Although ClickerGameUI imports it, it's good practice to ensure the main app has access or implicitly understands the full dependency chain if it were to manage logic directly. For this specific setup, UI handles logic init.


class ClickerGameApp:
    """
    The main application class for the Clicker Game.

    This class initializes the Tkinter root window, sets up the game's user
    interface, and starts the Tkinter event loop. It acts as the orchestrator
    for the entire application.
    """

    def __init__(self):
        """
        Initializes the ClickerGameApp.

        Sets up the main Tkinter window and instantiates the ClickerGameUI.
        Includes basic error handling for UI initialization.
        """
        self.root = tk.Tk()
        self.ui: ClickerGameUI | None = None

        try:
            self.ui = ClickerGameUI(self.root)
            # Check if UI initialization was successful and the root window still exists
            if not self.root.winfo_exists():
                print("WARNING: Tkinter root window was destroyed during UI initialization. "
                      "Application cannot proceed.")
                self.ui = None # Ensure self.ui is None if root was destroyed
        except Exception as e:
            print(f"ERROR: Failed to initialize ClickerGameUI: {e}")
            tk.messagebox.showerror(
                "Application Error",
                f"An unhandled error occurred during application startup: {e}"
            )
            # Ensure the root window is destroyed if an unhandled error occurs
            if self.root.winfo_exists():
                self.root.destroy()
            self.ui = None

    def run(self):
        """
        Starts the Tkinter event loop, launching the application.

        This method should only be called if the UI has been successfully
        initialized.
        """
        if self.ui and self.root.winfo_exists():
            print("Clicker Game application started.")
            self.root.mainloop()
            print("Clicker Game application closed.")
        else:
            print("Application cannot run because UI failed to initialize or "
                  "root window was destroyed.")


if __name__ == "__main__":
    app = ClickerGameApp()
    app.run()