import tkinter as tk
from tkinter import messagebox


def count():
    global counter
    counter += 1


def show():
    messagebox.showinfo(
        "",
        f"counter={str(counter)}, state={str(switch.get())}"
    )


window = tk.Tk()

switch = tk.IntVar()

counter = 0

button = tk.Button(window, text="Show", command=show)
button.pack()

checkbutton = tk.Checkbutton(window, text="Tick", variable=switch, command=count)
checkbutton.pack()

window.mainloop()
