import tkinter as tk
from src.game_logic import ClickerGameLogic


class ClickerGameUI:
    """
    Implements the tkinter graphical user interface for the clicker game.

    Connects UI elements (button, label) to the game logic provided by
    ClickerGameLogic.
    """

    def __init__(self, master: tk.Tk):
        """
        Initializes the ClickerGameUI.

        Sets up the main window, initializes the game logic, and creates
        the necessary UI widgets.

        Args:
            master (tk.Tk): The root Tkinter window.
        """
        self.master = master
        self.master.title("Clicker Game")
        self.master.geometry("300x200")
        self.master.resizable(False, False)  # Prevent window resizing

        self.game_logic: ClickerGameLogic | None = None
        try:
            self.game_logic = ClickerGameLogic()
        except Exception as e:
            # In a real application, you might log this error and show an error dialog.
            # For this simple case, we print to console and disable interaction.
            print(f"ERROR: Failed to initialize game logic: {e}")
            tk.messagebox.showerror(
                "Initialization Error",
                f"Failed to load game logic. Application cannot start.\nDetails: {e}"
            )
            self.master.destroy()
            return

        self._create_widgets()
        self._update_counter_display()

    def _create_widgets(self):
        """
        Creates and places the UI widgets (label, buttons) on the window.
        """
        # Counter Label
        self.counter_label = tk.Label(self.master, text="Count: 0", font=("Arial", 28, "bold"))
        self.counter_label.pack(pady=20)

        # Frame for buttons to arrange them horizontally
        button_frame = tk.Frame(self.master)
        button_frame.pack(pady=10)

        # Increment Button
        self.increment_button = tk.Button(
            button_frame,
            text="Click Me!",
            command=self._increment_button_click,
            font=("Arial", 16),
            width=10
        )
        self.increment_button.pack(side=tk.LEFT, padx=10)

        # Reset Button
        self.reset_button = tk.Button(
            button_frame,
            text="Reset",
            command=self._reset_button_click,
            font=("Arial", 12),
            width=8
        )
        self.reset_button.pack(side=tk.RIGHT, padx=10)

        # Disable buttons if game_logic failed to initialize
        if self.game_logic is None:
            self.increment_button.config(state=tk.DISABLED)
            self.reset_button.config(state=tk.DISABLED)
            self.counter_label.config(text="Error: Logic Unloaded")

    def _update_counter_display(self):
        """
        Retrieves the current counter value from game logic and updates
        the text of the UI's counter label.
        """
        if self.game_logic is None:
            self.counter_label.config(text="Error: Logic Missing")
            return

        try:
            current_count = self.game_logic.get_counter()
            self.counter_label.config(text=f"Count: {current_count}")
        except Exception as e:
            print(f"ERROR: Failed to retrieve counter value: {e}")
            self.counter_label.config(text="Error getting count")
            self.increment_button.config(state=tk.DISABLED)
            self.reset_button.config(state=tk.DISABLED)

    def _increment_button_click(self):
        """
        Handles the event when the 'Click Me!' button is pressed.
        Calls the game logic to increment the counter and updates the display.
        """
        if self.game_logic is None:
            print("WARNING: Increment attempted with no game logic.")
            return

        try:
            self.game_logic.increment_counter()
            self._update_counter_display()
        except Exception as e:
            print(f"ERROR: Failed to increment counter: {e}")
            tk.messagebox.showerror("Game Error", f"Could not increment counter.\nDetails: {e}")

    def _reset_button_click(self):
        """
        Handles the event when the 'Reset' button is pressed.
        Calls the game logic to reset the counter and updates the display.
        """
        if self.game_logic is None:
            print("WARNING: Reset attempted with no game logic.")
            return

        try:
            self.game_logic.reset_counter()
            self._update_counter_display()
        except Exception as e:
            print(f"ERROR: Failed to reset counter: {e}")
            tk.messagebox.showerror("Game Error", f"Could not reset counter.\nDetails: {e}")


if __name__ == "__main__":
    # Ensure the script runs only when executed directly
    root = tk.Tk()
    app = ClickerGameUI(root)
    root.mainloop()