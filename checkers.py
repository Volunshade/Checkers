"""This module is for a game of checkers."""
import tkinter as tk
from typing import Dict

from square import Square
from piece import Piece


class Board(tk.Canvas):
    """Contains the logic for the Checkers game board."""

    grid_size = 8


    def __init__(self,
                 master: tk.Tk,
                 board_size: int,
                 **kwargs: Dict[str, int]
                 ) -> None:
        """Initialize a new instance."""

        self.board_size = board_size

        super().__init__(master, **kwargs)

        self.bind("<Button-1>", self.left_click)

        _square_length = board_size / self.grid_size
        self.side_length = board_size / self.grid_size
        Square.update_side_length(_square_length)
        Piece.update_side_length(_square_length)

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



        col = int(event.x // self.side_length)
        row = int(event.y // self.side_length)
        print(event.x, col, " -> ", event.y, row)
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
                if (row < 3 or row > (Board.grid_size - 4)) and not (row + col) % 2:
                    color = "yellow" if row < 3 else "cyan"
                    piece = Piece(row, col, color)
                    pieces.append(piece)

        return pieces


def main():
    """Run the main process."""

    board_size = 800

    window = tk.Tk()
    window.title("Checkers")

    kwargs = {"width": board_size, "height": board_size}
    board = Board(window, board_size, **kwargs)

    window.mainloop()


if __name__ == "__main__":
    main()
