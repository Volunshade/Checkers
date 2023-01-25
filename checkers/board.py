"""This module is for a game of checkers."""
import json
import logging
import tkinter as tk
from typing import Dict

from checkers.square import Square
from checkers.piece import Piece

logger = logging.getLogger(__name__)


class Board(tk.Canvas):
    """Contains the logic for the Checkers game board."""

    grid_size = 8

    def __init__(self,
                 master: tk.Tk,
                 board_size: int,
                 **kwargs: Dict[str, int]
                 ) -> None:
        """Initialize a new instance."""

        logger.info("Initializing a Board object.")

        self.board_size = board_size

        super().__init__(master, **kwargs)

        self.bind("<Button-1>", self.left_click)
        self.pack()

        self.init_board()

    @property
    def side_length(self) -> float:
        """The side length of a square based on the board size."""

        return self.board_size / self.grid_size

    def init_board(self) -> None:
        """Initialize the board canvas with squares and pieces."""

        Square.update_side_length(self.side_length)
        Piece.update_side_length(self.side_length)

        self.squares = self.init_squares()
        self.pieces = self.init_pieces()

        self.draw_squares()
        self.draw_pieces()

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

        logger.info(f"Left-click event captured, x={event.x} and y={event.y}")

        col = int(event.x // self.side_length)
        row = int(event.y // self.side_length)

        self.display(col, row)

    def display(self, col, row, verbose=False) -> None:
        """Give feedback to the console on the game state."""

        output = {}

        if verbose:
            output["grid_size"] = self.grid_size
            output["board_size"] = self.board_size
            output["side_length"] = self.side_length
        
        output["col"] = col
        output["row"] = row

        logger.info(json.dumps(output, indent=2))

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
