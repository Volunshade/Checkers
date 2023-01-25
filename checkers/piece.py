"""This module is for a piece on a checkerboard."""
import logging
import tkinter as tk

logger = logging.getLogger(__name__)


class Piece:
    """Contains the logic for a piece on a Checkers game board."""

    piece_scalar = 20
    side_length = -1.0

    @classmethod
    def update_side_length(cls, new_square_length: float) -> None:
        """Update square length for all square instances."""

        cls.side_length = new_square_length

    def __init__(self, row: int, col: int, color: str):
        """Initialize a new instance"""

        self.row = row
        self.col = col
        self.color = color

    def draw(self, canvas: tk.Canvas) -> None:
        """Drawing a piece on a canvas."""

        offset_decimal = self.piece_scalar / self.side_length
        offset = self.side_length * offset_decimal
        half_offset = offset / 2

        row1 = self.row * self.side_length + half_offset
        col1 = self.col * self.side_length + half_offset

        row2 = row1 + self.side_length - offset
        col2 = col1 + self.side_length - offset

        canvas.create_oval(col1, row1, col2, row2, fill=self.color)
