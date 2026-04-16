import tkinter as tk
from tkinter import messagebox
from src.expression_parser import ExpressionParser
from src.graph_evaluator import GraphEvaluator
import math

class GraphingUI:
    """
    A Tkinter-based graphical user interface for a mathematical graphing calculator.

    This UI allows users to input a mathematical expression, define an x-range,
    and specify the number of points to plot. It uses ExpressionParser to parse
    the input and GraphEvaluator to generate (x, y) coordinates, which are then
    displayed on a Tkinter Canvas.
    """

    CANVAS_WIDTH = 800
    CANVAS_HEIGHT = 600
    PADDING = 50  # Padding from canvas edges for axes and labels

    def __init__(self, master: tk.Tk):
        """
        Initializes the GraphingUI application.

        Args:
            master: The root Tkinter window.
        """
        self.master = master
        master.title("Python Graphing Calculator")

        self.expression_parser = ExpressionParser()

        # --- Variables ---
        self.expression_var = tk.StringVar(value="x**2")
        self.x_start_var = tk.StringVar(value="-10.0")
        self.x_end_var = tk.StringVar(value="10.0")
        self.num_points_var = tk.StringVar(value="500")
        self.error_message_var = tk.StringVar()

        # --- UI Setup ---
        self._create_widgets()

    def _create_widgets(self):
        """
        Creates and arranges all the Tkinter widgets for the UI.
        """
        # --- Input Frame ---
        input_frame = tk.Frame(self.master, padx=10, pady=10)
        input_frame.pack(side=tk.TOP, fill=tk.X)

        tk.Label(input_frame, text="Expression (e.g., sin(x), x**2 + 2*x - 1):").grid(row=0, column=0, sticky=tk.W)
        self.expression_entry = tk.Entry(input_frame, textvariable=self.expression_var, width=50)
        self.expression_entry.grid(row=0, column=1, columnspan=3, sticky=tk.EW, padx=5, pady=2)
        self.expression_entry.bind("<Return>", lambda event: self._plot_graph())

        tk.Label(input_frame, text="X Start:").grid(row=1, column=0, sticky=tk.W)
        self.x_start_entry = tk.Entry(input_frame, textvariable=self.x_start_var, width=15)
        self.x_start_entry.grid(row=1, column=1, sticky=tk.W, padx=5, pady=2)

        tk.Label(input_frame, text="X End:").grid(row=1, column=2, sticky=tk.W)
        self.x_end_entry = tk.Entry(input_frame, textvariable=self.x_end_var, width=15)
        self.x_end_entry.grid(row=1, column=3, sticky=tk.W, padx=5, pady=2)

        tk.Label(input_frame, text="Num Points:").grid(row=2, column=0, sticky=tk.W)
        self.num_points_entry = tk.Entry(input_frame, textvariable=self.num_points_var, width=15)
        self.num_points_entry.grid(row=2, column=1, sticky=tk.W, padx=5, pady=2)

        self.plot_button = tk.Button(input_frame, text="Plot", command=self._plot_graph)
        self.plot_button.grid(row=2, column=2, columnspan=2, sticky=tk.EW, padx=5, pady=5)

        # --- Error Message Label ---
        self.error_label = tk.Label(self.master, textvariable=self.error_message_var, fg="red", wraplength=self.CANVAS_WIDTH)
        self.error_label.pack(side=tk.TOP, fill=tk.X, padx=10)

        # --- Canvas for Graph ---
        self.canvas = tk.Canvas(self.master, width=self.CANVAS_WIDTH, height=self.CANVAS_HEIGHT, bg="white", bd=2, relief=tk.SUNKEN)
        self.canvas.pack(padx=10, pady=10)

        # Initial plot
        self._plot_graph()

    def _display_error(self, message: str):
        """Displays an error message in the UI."""
        self.error_message_var.set(message)
        messagebox.showerror("Plotting Error", message)

    def _clear_error(self):
        """Clears any displayed error messages."""
        self.error_message_var.set("")

    def _plot_graph(self):
        """
        Retrieves user input, parses the expression, evaluates it,
        and draws the resulting graph on the canvas.
        """
        self._clear_error()
        self.canvas.delete("all")  # Clear previous drawings

        try:
            expression_str = self.expression_var.get()
            x_start = float(self.x_start_var.get())
            x_end = float(self.x_end_var.get())
            num_points = int(self.num_points_var.get())

            if x_start >= x_end:
                raise ValueError("X Start must be less than X End.")
            if num_points < 2:
                raise ValueError("Number of points must be at least 2.")

            # 1. Parse the expression
            parsed_func = self.expression_parser.parse(expression_str)

            # 2. Evaluate the expression
            points = GraphEvaluator.evaluate_expression_for_range(
                parsed_func, x_start, x_end, num_points
            )

            # 3. Determine y-axis range for auto-scaling
            valid_y_values = [p[1] for p in points if not math.isnan(p[1])]
            if not valid_y_values:
                # If all y-values are NaN, use a default range or display a specific message
                self._display_error("No valid y-values could be computed for the given expression and range.")
                return

            y_min_data = min(valid_y_values)
            y_max_data = max(valid_y_values)

            # Add a small buffer to y-range for better visualization, unless it's a constant function
            if y_max_data == y_min_data:
                y_min_data -= 1.0
                y_max_data += 1.0
            else:
                y_buffer = (y_max_data - y_min_data) * 0.1
                y_min_data -= y_buffer
                y_max_data += y_buffer

            # 4. Draw axes and plot points
            self._draw_axes(x_start, x_end, y_min_data, y_max_data)
            self._draw_graph_line(points, x_start, x_end, y_min_data, y_max_data)

        except ValueError as e:
            self._display_error(f"Input Error: {e}")
        except SyntaxError as e:
            self._display_error(f"Expression Syntax Error: {e}")
        except Exception as e:
            # Catch any other unexpected errors during parsing or evaluation
            self._display_error(f"An unexpected error occurred: {e}")

    def _data_to_canvas_coords(self, x_data: float, y_data: float,
                               x_min_data: float, x_max_data: float,
                               y_min_data: float, y_max_data: float) -> tuple[float, float]:
        """
        Converts a data coordinate (x_data, y_data) to canvas pixel coordinates.

        Args:
            x_data: The x-value in the data coordinate system.
            y_data: The y-value in the data coordinate system.
            x_min_data: Minimum x-value of the data range.
            x_max_data: Maximum x-value of the data range.
            y_min_data: Minimum y-value of the data range.
            y_max_data: Maximum y-value of the data range.

        Returns:
            A tuple (x_canvas, y_canvas) representing the pixel coordinates on the canvas.
        """
        plot_width = self.CANVAS_WIDTH - 2 * self.PADDING
        plot_height = self.CANVAS_HEIGHT - 2 * self.PADDING

        # Calculate normalized positions (0 to 1)
        normalized_x = (x_data - x_min_data) / (x_max_data - x_min_data)
        normalized_y = (y_data - y_min_data) / (y_max_data - y_min_data)

        # Convert to canvas coordinates (origin at top-left, y increases downwards)
        x_canvas = self.PADDING + normalized_x * plot_width
        y_canvas = self.CANVAS_HEIGHT - self.PADDING - normalized_y * plot_height # Invert Y-axis

        return x_canvas, y_canvas

    def _draw_axes(self, x_min_data: float, x_max_data: float,
                   y_min_data: float, y_max_data: float):
        """
        Draws the X and Y axes on the canvas, including tick marks and labels.

        Args:
            x_min_data: The minimum x-value of the plotted data range.
            x_max_data: The maximum x-value of the plotted data range.
            y_min_data: The minimum y-value of the plotted data range.
            y_max_data: The maximum y-value of the plotted data range.
        """
        canvas = self.canvas
        # Drawing area boundaries
        left = self.PADDING
        right = self.CANVAS_WIDTH - self.PADDING
        top = self.PADDING
        bottom = self.CANVAS_HEIGHT - self.PADDING

        # Draw X-axis
        x_axis_y_canvas = self._data_to_canvas_coords(0, 0, x_min_data, x_max_data, y_min_data, y_max_data)[1]
        x_axis_y_canvas = max(top, min(bottom, x_axis_y_canvas)) # Clamp x-axis to be within plot area

        canvas.create_line(left, x_axis_y_canvas, right, x_axis_y_canvas, fill="gray", arrow=tk.LAST)
        canvas.create_text(right + 10, x_axis_y_canvas, text="X", anchor=tk.W)

        # Draw Y-axis
        y_axis_x_canvas = self._data_to_canvas_coords(0, 0, x_min_data, x_max_data, y_min_data, y_max_data)[0]
        y_axis_x_canvas = max(left, min(right, y_axis_x_canvas)) # Clamp y-axis to be within plot area

        canvas.create_line(y_axis_x_canvas, bottom, y_axis_x_canvas, top, fill="gray", arrow=tk.LAST)
        canvas.create_text(y_axis_x_canvas, top - 10, text="Y", anchor=tk.S)

        # Draw X-axis tick marks and labels
        x_range_data = x_max_data - x_min_data
        num_x_ticks = 10
        x_tick_interval = x_range_data / num_x_ticks
        for i in range(num_x_ticks + 1):
            x_data = x_min_data + i * x_tick_interval
            x_canvas_coord = self._data_to_canvas_coords(x_data, 0, x_min_data, x_max_data, y_min_data, y_max_data)[0]
            canvas.create_line(x_canvas_coord, x_axis_y_canvas - 5, x_canvas_coord, x_axis_y_canvas + 5, fill="gray")
            if abs(x_data) > 1e-9: # Avoid showing -0.0
                canvas.create_text(x_canvas_coord, x_axis_y_canvas + 15, text=f"{x_data:.1f}", anchor=tk.N)
            else:
                canvas.create_text(x_canvas_coord, x_axis_y_canvas + 15, text="0", anchor=tk.N)

        # Draw Y-axis tick marks and labels
        y_range_data = y_max_data - y_min_data
        num_y_ticks = 10
        y_tick_interval = y_range_data / num_y_ticks
        for i in range(num_y_ticks + 1):
            y_data = y_min_data + i * y_tick_interval
            y_canvas_coord = self._data_to_canvas_coords(0, y_data, x_min_data, x_max_data, y_min_data, y_max_data)[1]
            canvas.create_line(y_axis_x_canvas - 5, y_canvas_coord, y_axis_x_canvas + 5, y_canvas_coord, fill="gray")
            if abs(y_data) > 1e-9: # Avoid showing -0.0
                canvas.create_text(y_axis_x_canvas - 15, y_canvas_coord, text=f"{y_data:.1f}", anchor=tk.E)


    def _draw_graph_line(self, points: list[tuple[float, float]],
                         x_min_data: float, x_max_data: float,
                         y_min_data: float, y_max_data: float):
        """
        Draws the graph line on the canvas using the evaluated points.
        NaN values cause breaks in the line.

        Args:
            points: A list of (x, y) data coordinates.
            x_min_data: Minimum x-value of the data range.
            x_max_data: Maximum x-value of the data range.
            y_min_data: Minimum y-value of the data range.
            y_max_data: Maximum y-value of the data range.
        """
        canvas_points = []
        for x_data, y_data in points:
            if not math.isnan(y_data):
                x_canvas, y_canvas = self._data_to_canvas_coords(x_data, y_data,
                                                                  x_min_data, x_max_data,
                                                                  y_min_data, y_max_data)
                canvas_points.append((x_canvas, y_canvas))
            else:
                # If a NaN is encountered, draw the segment accumulated so far
                # and then reset for the next segment.
                if len(canvas_points) > 1:
                    self.canvas.create_line(canvas_points, fill="blue", width=2)
                canvas_points = [] # Start a new segment after a NaN

        # Draw any remaining segment after the loop finishes
        if len(canvas_points) > 1:
            self.canvas.create_line(canvas_points, fill="blue", width=2)

if __name__ == "__main__":
    root = tk.Tk()
    app = GraphingUI(root)
    root.mainloop()