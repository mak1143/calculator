import tkinter as tk
import tkinter.messagebox
from tkinter.constants import SUNKEN

window = tk.Tk()
window.title("Calculator")


frame = tk.Frame(window, bg="skyblue", padx=40)
frame.pack()

entry = tk.Entry(frame, relief=SUNKEN, borderwidth=1, width=50)
entry.grid(row=0, column=0, columnspan=3, ipady=2, pady=2)


def click(num):
    entry.insert(tk.END, num)


def equal():
    try:
        results = str(eval(entry.get()))
        entry.delete(0, tk.END)
        entry.insert(0, results)
    except:
        tk.messagebox.showinfo("Error", "Syntax Error")


def clear():
    entry.delete(0, tk.END)


btns = [
    ("1", 1, 0),
    ("2", 1, 1),
    ("3", 1, 2),
    ("4", 2, 0),
    ("5", 2, 1),
    ("6", 2, 2),
    ("7", 3, 0),
    ("8", 3, 1),
    ("9", 3, 2),
    ("0", 4, 1),
    ("+", 5, 0),
    ("-", 5, 1),
    ("*", 5, 2),
    ("/", 6, 0),
    ("/", 6, 0),
]

for txt, r, c in btns:
    tk.Button(
        frame, text=txt, padx=15, pady=5, width=3, command=lambda t=txt: click(t)
    ).grid(row=r, column=c, pady=2)

tk.Button(frame, text="clear", padx=15, pady=5, width=12, command=clear).grid(
    row=6, column=1, columnspan=2, pady=2
)
tk.Button(frame, text="=", padx=15, pady=5, width=9, command=equal).grid(
    row=7, column=0, columnspan=3, pady=2
)

window.mainloop()
