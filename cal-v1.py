import tkinter as tk
import tkinter.messagebox

window = tk.Tk()
window.title("Calculator")
window.configure(bg="#1a1a2e")

frame = tk.Frame(
    window, bg="#1a1a2e", padx=10, pady=10,
    highlightbackground="#16213e", highlightthickness=2
)
frame.pack()

entry = tk.Entry(
    frame, relief=tk.FLAT, borderwidth=0, width=20,
    bg="#1a1a2e", fg="white", font=("Arial", 24),
    justify=tk.RIGHT, insertbackground="white"
)
entry.grid(row=0, column=0, columnspan=4, ipady=10, pady=(10, 20), sticky="ew")


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


def toggle_sign():
    current = entry.get()
    if current and current[0] == "-":
        entry.delete(0, 1)
    elif current:
        entry.insert(0, "-")


def percent():
    try:
        value = eval(entry.get()) / 100
        entry.delete(0, tk.END)
        entry.insert(0, str(value))
    except:
        pass


styles = {
    "number": {"bg": "#16213e", "fg": "white", "activebackground": "#2a2a4e", "font": ("Arial", 20, "bold")},
    "op": {"bg": "#e94560", "fg": "white", "activebackground": "#ffb080", "font": ("Arial", 20, "bold")},
    "top_op": {"bg": "#c0c0c0", "fg": "black", "activebackground": "#ffffff", "font": ("Arial", 20, "bold")},
    "equals": {"bg": "#e94560", "fg": "white", "activebackground": "#ffb080", "font": ("Arial", 20, "bold")},
    "decimal": {"bg": "#16213e", "fg": "white", "activebackground": "#2a2a4e", "font": ("Arial", 20, "bold")},
}

buttons = [
    ("AC", 1, 0, 1, "top_op", clear),
    ("+/-", 1, 1, 1, "top_op", toggle_sign),
    ("%", 1, 2, 1, "top_op", percent),
    ("\u00f7", 1, 3, 1, "op", lambda: click("/")),
    ("7", 2, 0, 1, "number", lambda: click("7")),
    ("8", 2, 1, 1, "number", lambda: click("8")),
    ("9", 2, 2, 1, "number", lambda: click("9")),
    ("\u00d7", 2, 3, 1, "op", lambda: click("*")),
    ("4", 3, 0, 1, "number", lambda: click("4")),
    ("5", 3, 1, 1, "number", lambda: click("5")),
    ("6", 3, 2, 1, "number", lambda: click("6")),
    ("-", 3, 3, 1, "op", lambda: click("-")),
    ("1", 4, 0, 1, "number", lambda: click("1")),
    ("2", 4, 1, 1, "number", lambda: click("2")),
    ("3", 4, 2, 1, "number", lambda: click("3")),
    ("+", 4, 3, 1, "op", lambda: click("+")),
    ("0", 5, 0, 2, "number", lambda: click("0")),
    (".", 5, 2, 1, "decimal", lambda: click(".")),
    ("=", 5, 3, 1, "equals", equal),
]

for text, row, col, colspan, style_key, cmd in buttons:
    style = styles[style_key]
    tk.Button(
        frame, text=text, relief=tk.FLAT, bd=0,
        bg=style["bg"], fg=style["fg"],
        activebackground=style["activebackground"],
        font=style["font"], width=5, height=2,
        command=cmd
    ).grid(row=row, column=col, columnspan=colspan, pady=2, padx=2, sticky="nsew")

for i in range(4):
    frame.grid_columnconfigure(i, weight=1)

window.mainloop()
