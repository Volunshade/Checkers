"""This module is for a game of checkers."""

import tkinter as tk

window = tk.Tk()
window.geometry("800x800")
window.title("Checkers")

canvas = tk.Canvas(window, width=800, height=800)

top_left = (0, 0)
bot_right = (400, 400)
canvas.create_rectangle(*top_left,  *bot_right, fill="black")

top_left = (400, 0)
bot_right = (800, 400)
canvas.create_rectangle(*top_left,  *bot_right, fill="red")

top_left = (0, 400)
bot_right = (400, 800)
canvas.create_rectangle(*top_left,  *bot_right, fill="red")

top_left = (400, 400)
bot_right = (800, 800)
canvas.create_rectangle(*top_left,  *bot_right, fill="black")

canvas.pack()

window.mainloop()
