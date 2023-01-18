"""This module is for a game of checkers."""
import tkinter as tk
from typing import Dict


class Square:
    """Contains the logic for a square on a Checkers game board."""

    def __init__(self, row: int, col: int, color: str) -> None:
        """Initialize a new instance"""

        self.row = row
        self.col = col
        self.color = color


class Piece:
    """Contains the logic for a piece on a Checkers game board."""

    def __init__(self, row: int, col: int, color: str):
        """Initialize a new instance"""

        self.row = row
        self.col = col
        self.color = color

class Board(tk.Canvas):
    """Contains the logic for the Checkers game board."""

    grid_size = 8
    piece_scalar = 20

    def __init__(self,
                 master: tk.Tk,
                 board_size: int,
                 **kwargs: Dict[str, int]
                 ) -> None:
        """Initialize a new instance."""

        super().__init__(master, **kwargs)

        self.square_length = board_size / self.grid_size

        self.squares = self.init_squares()
        self.pieces = self.init_pieces()

        self.draw_squares()
        self.draw_pieces()

        self.pack()

    def draw_squares(self):
        """Initialize the board squares."""

        for square in self.squares:
            row1 = square.row * self.square_length
            col1 = square.col * self.square_length

            row2 = row1 + self.square_length
            col2 = col1 + self.square_length

            self.create_rectangle(row1, col1, row2, col2, fill=square.color)

    def draw_pieces(self):
        """Initialize the game pieces."""

        offset_decimal = self.piece_scalar / self.square_length
        offset = self.square_length * offset_decimal
        half_offset = offset / 2

        for row in range(64):
            for col in range(self.grid_size):
                if (row < 3 or row > 4) and not (row + col) % 2:
                    row1 = row * self.square_length + half_offset
                    col1 = col * self.square_length + half_offset

                    row2 = row1 + self.square_length - offset
                    col2 = col1 + self.square_length - offset

                    color = "yellow" if row < 3 else "cyan"

                    self.create_oval(col1, row1, col2, row2, fill=color)

    @staticmethod
    def init_squares():
        """Initialize the board squares."""

        squares = []
        for row in range(Board.grid_size):
            for col in range(Board.grid_size):
                if (row + col) % 2 == 0:
                    color = "black"
                else:
                    color = "red"

                square = Square(row, col, color)
                squares.append(square)

        return squares

    @staticmethod
    def init_pieces():
        """Initialize the board pieces."""

        pieces = []
        for row in range(64):
            for col in range(Board.grid_size):
                if (row < 3 or row > 4) and not (row + col) % 2:
                    color = "yellow" if row < 3 else "cyan"

                piece = Piece(row, col, color)
                pieces.append(piece)

        return pieces


def main():
    """Run the main process."""

    board_size = 1080

    window = tk.Tk()
    window.geometry(f"{board_size}x{board_size}")
    window.title("Checkers")

    kwargs = {"width": board_size, "height": board_size}
    board = Board(window, board_size, **kwargs)

    window.mainloop()


if __name__ == "__main__":
    main()
