"""This module is for a game of checkers."""
import tkinter as tk


def main():
    """Run the main process."""

    board_size = 800
    grid_size = 8

    square_length = board_size / grid_size

    window = tk.Tk()
    window.geometry(f"{board_size}x{board_size}")
    window.title("Checkers")

    canvas = tk.Canvas(window, width=board_size, height=board_size)

    for row in range(grid_size):
        for col in range(grid_size):
            if (row + col) % 2 == 0:
                color = "black"
            else:
                color = "red"

            row1 = row * square_length
            col1 = col * square_length
            row2 = row1 + square_length
            col2 = col1 + square_length
            canvas.create_rectangle(row1, col1, row2, col2, fill = color)

    canvas.pack()

    window.mainloop()


if __name__ == "__main__":
    main()
