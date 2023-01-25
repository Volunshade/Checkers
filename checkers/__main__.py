"""This module is for a game of checkers."""
import logging
import logging.config
import tkinter as tk

from checkers.board import Board
from checkers.config import logger_config

logging.config.dictConfig(logger_config)
logger = logging.getLogger("checkers")


def main() -> None:
    """Run the main process."""

    logger.debug("Starting the main process.")

    board_size = 800

    window = tk.Tk()
    window.title("Checkers")

    kwargs = {"width": board_size, "height": board_size}
    board = Board(window, board_size, **kwargs)

    window.mainloop()


if __name__ == "__main__":
    main()
