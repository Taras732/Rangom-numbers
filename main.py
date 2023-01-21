import tkinter as tk
from random import randint
win = tk.Tk()


def test_button_click():
    label_val.set(randint(1, 64))


my_button = tk.Button(
    win,
    text="Click me!",
    width=25,
    height=5,
    bg="lightgrey",
    fg="black",
    command=test_button_click
)

my_button.grid(column=0, row=0)
label_val = tk.IntVar()
my_Label = tk.Label(win, textvariable=label_val)
my_Label.grid(column=1, row=0)
win.mainloop()