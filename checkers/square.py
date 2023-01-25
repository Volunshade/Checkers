"""This module is for squares on a checkerboard."""
import logging
import tkinter as tk

logger = logging.getLogger(__name__)


class Square:
    """Contains the logic for a square on a Checkers game board."""

    side_length = -1.0

    @classmethod
    def update_side_length(cls, new_square_length: float) -> None:
        """Update square length for all square instances."""

        cls.side_length = new_square_length

    def __init__(self, row: int, col: int, color: str) -> None:
        """Initialize a new instance"""

        self.row = row
        self.col = col
        self.color = color

    def draw(self, canvas: tk.Canvas) -> None:
        """Drawing a square on a canvas."""

        row1 = self.row * self.side_length
        col1 = self.col * self.side_length

        row2 = row1 + self.side_length
        col2 = col1 + self.side_length

        canvas.create_rectangle(row1, col1, row2, col2, fill=self.color)
