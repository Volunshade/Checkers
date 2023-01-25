"""This module is for a game of checkers."""
import tkinter as tk

from checkers.board import Board


def main() -> None:
    """Run the main process."""

    board_size = 800

    window = tk.Tk()
    window.title("Checkers")

    kwargs = {"width": board_size, "height": board_size}
    board = Board(window, board_size, **kwargs)

    window.mainloop()


if __name__ == "__main__":
    main()
