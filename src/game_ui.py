import tkinter as tk
from tkinter import messagebox
from src.game_logic import GameLogic

class GameUI:
    """
    Implements the graphical user interface for the 'Guess the Number' game
    using Tkinter. It handles user input (guesses), displays feedback,
    and interacts with the GameLogic module.
    """

    def __init__(self, master: tk.Tk):
        """
        Initializes the GameUI.

        Args:
            master (tk.Tk): The root Tkinter window.
        """
        self.master = master
        self.master.title("Guess The Number")
        # Set a fixed size for simplicity and consistency
        self.master.geometry("400x300")
        self.master.resizable(False, False)

        try:
            # Instantiate the game logic with default range (1-100)
            self.game_logic = GameLogic()
        except (TypeError, ValueError) as e:
            messagebox.showerror("Game Initialization Error", f"Failed to initialize game logic: {e}")
            master.destroy() # Close the application if logic fails to initialize
            return

        self._create_widgets()
        self._reset_game_ui() # Initialize UI elements based on game logic state

    def _create_widgets(self) -> None:
        """
        Creates and places all Tkinter widgets for the game UI.
        """
        # --- Main Frame for organizing widgets ---
        main_frame = tk.Frame(self.master, padx=20, pady=20)
        main_frame.pack(expand=True)

        # --- Title Label ---
        self.title_label = tk.Label(
            main_frame,
            text="Guess The Number!",
            font=("Helvetica", 16, "bold")
        )
        self.title_label.pack(pady=(0, 10))

        # --- Feedback/Instructions Label ---
        self.feedback_label = tk.Label(
            main_frame,
            text="",
            font=("Helvetica", 12),
            wraplength=300 # Ensure text wraps if it's too long
        )
        self.feedback_label.pack(pady=(5, 10))

        # --- Guess Input Frame ---
        guess_frame = tk.Frame(main_frame)
        guess_frame.pack(pady=5)

        tk.Label(guess_frame, text="Your guess:", font=("Helvetica", 10)).pack(side=tk.LEFT, padx=(0, 5))
        self.guess_entry = tk.Entry(guess_frame, width=10, font=("Helvetica", 10))
        self.guess_entry.pack(side=tk.LEFT)
        # Bind the Enter key to the guess submission for better UX
        self.guess_entry.bind("<Return>", lambda event: self._check_guess())

        self.guess_button = tk.Button(
            guess_frame,
            text="Submit Guess",
            command=self._check_guess,
            font=("Helvetica", 10)
        )
        self.guess_button.pack(side=tk.LEFT, padx=(10, 0))

        # --- Attempts Label ---
        self.attempts_label = tk.Label(
            main_frame,
            text="Attempts: 0",
            font=("Helvetica", 10)
        )
        self.attempts_label.pack(pady=10)

        # --- Reset Button ---
        self.reset_button = tk.Button(
            main_frame,
            text="Play Again",
            command=self._reset_game_ui,
            font=("Helvetica", 10)
        )
        self.reset_button.pack(pady=10)

    def _update_feedback(self, message: str, color: str = "black") -> None:
        """
        Updates the feedback label with the given message and color.

        Args:
            message (str): The message to display.
            color (str): The color of the message text.
        """
        self.feedback_label.config(text=message, fg=color)

    def _update_attempts(self) -> None:
        """
        Updates the attempts label with the current number of attempts from GameLogic.
        """
        self.attempts_label.config(text=f"Attempts: {self.game_logic.attempts_made}")

    def _enable_input(self, enable: bool) -> None:
        """
        Enables or disables the guess entry and submit button.

        Args:
            enable (bool): True to enable, False to disable.
        """
        state = tk.NORMAL if enable else tk.DISABLED
        self.guess_entry.config(state=state)
        self.guess_button.config(state=state)

    def _check_guess(self) -> None:
        """
        Handles the user's guess submission.
        Validates input, processes the guess using GameLogic, and updates the UI.
        """
        if self.game_logic.game_over:
            self._update_feedback("Game over! Press 'Play Again' to restart.", "blue")
            return

        guess_str = self.guess_entry.get()
        self.guess_entry.delete(0, tk.END) # Clear the entry field after getting input

        try:
            guess = int(guess_str)

            # Validate if the guess is within the game's defined range
            if not (self.game_logic.min_num <= guess <= self.game_logic.max_num):
                self._update_feedback(
                    f"Please guess a number between {self.game_logic.min_num} and {self.game_logic.max_num}.",
                    "orange"
                )
                return

            result = self.game_logic.check_guess(guess)
            self._update_attempts()

            if result == "Too low!":
                self._update_feedback("Too low! Try a higher number.", "red")
            elif result == "Too high!":
                self._update_feedback("Too high! Try a lower number.", "red")
            elif result == "Correct!":
                self._update_feedback(
                    f"Congratulations! You guessed the number {self.game_logic.target_number} "
                    f"in {self.game_logic.attempts_made} attempts!",
                    "green"
                )
                self._enable_input(False) # Disable input after a win
            else:
                # This case should ideally not be reached if GameLogic is robust
                self._update_feedback("An unexpected game state occurred.", "red")

        except ValueError:
            # Handle non-integer input
            messagebox.showerror("Invalid Input", "Please enter a valid whole number.")
            self._update_feedback("Invalid input. Please enter a number.", "orange")
        except Exception as e:
            # Catch any other unexpected errors during guess processing
            messagebox.showerror("Error", f"An unexpected error occurred: {e}")
            self._update_feedback("An error occurred. Please try again.", "red")

    def _reset_game_ui(self) -> None:
        """
        Resets the game state in GameLogic and updates all UI elements
        to start a new game.
        """
        self.game_logic.reset_game()
        self._update_feedback(
            f"I'm thinking of a number between {self.game_logic.min_num} and {self.game_logic.max_num}. Guess it!",
            "black"
        )
        self._update_attempts()
        self.guess_entry.delete(0, tk.END) # Clear any text in the entry field
        self._enable_input(True) # Ensure input widgets are enabled for a new game

# Main execution block to run the Tkinter application
if __name__ == "__main__":
    root = tk.Tk()
    app = GameUI(root)
    # Only start mainloop if GameUI was successfully initialized
    if hasattr(app, 'game_logic'):
        root.mainloop()