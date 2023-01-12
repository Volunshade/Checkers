"""This module is for a game of checkers."""
import tkinter as tk
from typing import Dict


class Board(tk.Canvas):
    """Contains the logic for the Checkers game board."""

    grid_size = 8

    def __init__(self,
                 master: tk.Tk,
                 board_size: int,
                 **kwargs: Dict[str, int]
                 ) -> None:
        """Initialize a new instance."""

        super().__init__(master, **kwargs)

        self.square_length = board_size / self.grid_size

    def draw_squares(self):
        """Initialize the board squares."""

        for row in range(self.grid_size):
            for col in range(self.grid_size):
                if (row + col) % 2 == 0:
                    color = "black"
                else:
                    color = "red"

                row1 = row * self.square_length
                col1 = col * self.square_length

                row2 = row1 + self.square_length
                col2 = col1 + self.square_length

                self.create_rectangle(row1, col1, row2, col2, fill=color)


def main():
    """Run the main process."""

    board_size = 720

    window = tk.Tk()
    window.geometry(f"{board_size}x{board_size}")
    window.title("Checkers")

    kwargs = {"width": board_size, "height": board_size}
    board = Board(window, board_size, **kwargs)
    board.draw_squares()
    board.pack()

    window.mainloop()


if __name__ == "__main__":
    main()
