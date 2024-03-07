import tkinter as tk
from tkinter import ttk

root = tk.Tk()
btn_column = ttk.Button(root, text="I'm in column 3")
btn_column.grid(column=3)

my_label = ttk.Label(root, text="Hi")
my_label.grid(row=2, column=5, columnspan=5)

root.mainloop()
