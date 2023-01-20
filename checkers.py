"""This module is for a game of checkers."""
import tkinter as tk
from typing import Dict


class Square:
    """Contains the logic for a square on a Checkers game board."""

    square_length = -1.0

    @classmethod
    def update_square_length(cls, new_square_length: float) -> None:
        """Update square length for all square instances."""

        cls.square_length = new_square_length

    def __init__(self, row: int, col: int, color: str) -> None:
        """Initialize a new instance"""

        self.row = row
        self.col = col
        self.color = color

    def draw(self, canvas: tk.Canvas) -> None:
        """Drawing a square on a canvas."""

        row1 = self.row * self.square_length
        col1 = self.col * self.square_length

        row2 = row1 + self.square_length
        col2 = col1 + self.square_length

        canvas.create_rectangle(row1, col1, row2, col2, fill=self.color)


class Piece:
    """Contains the logic for a piece on a Checkers game board."""

    piece_scalar = 20

    def __init__(self, row: int, col: int, color: str):
        """Initialize a new instance"""

        self.row = row
        self.col = col
        self.color = color

    def draw(self, canvas: tk.Canvas) -> None:
        """Drawing a piece on a canvas."""

        offset_decimal = self.piece_scalar / Square.square_length
        offset = Square.square_length * offset_decimal
        half_offset = offset / 2

        row1 = self.row * Square.square_length + half_offset
        col1 = self.col * Square.square_length + half_offset

        row2 = row1 + Square.square_length - offset
        col2 = col1 + Square.square_length - offset

        canvas.create_oval(col1, row1, col2, row2, fill=self.color)

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

        self.bind("<Button-1>", self.left_click)

        _square_length = board_size / self.grid_size
        Square.update_square_length(_square_length)

        self.squares = self.init_squares()
        self.pieces = self.init_pieces()

        self.draw_squares()
        self.draw_pieces()

        self.pack()

    def draw_squares(self):
        """Initialize the board squares."""

        for square in self.squares:
            square.draw(self)

    def draw_pieces(self):
        """Initialize the game pieces."""

        for piece in self.pieces:
            piece.draw(self)

    def left_click(self, event: tk.Event) ->  None:
        """Callback function for the board left click event."""

        print(event.x, event.y)
        pass

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
        for row in range(Board.grid_size):
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
    window.title("Checkers")

    kwargs = {"width": board_size, "height": board_size}
    board = Board(window, board_size, **kwargs)

    window.mainloop()


if __name__ == "__main__":
    main()
