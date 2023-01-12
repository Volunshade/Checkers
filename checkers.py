"""This module is for a game of checkers."""

import tkinter as tk

window = tk.Tk()
window.geometry("800x800")
window.title("Checkers")

canvas = tk.Canvas(window, width=800, height=800)

for row in range(8):
    for column in range(8):
        if (row + column) % 2 == 0:
            color = "black"
        else:
            color = "red"

        row1 = row*100
        column1 = column*100
        row2 = row1+100
        column2 = column1+100
        canvas.create_rectangle(row1, column1, row2, column2, fill = color)

canvas.pack()

window.mainloop()
