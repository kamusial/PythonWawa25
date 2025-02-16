import tkinter as tk
from tkinter.messagebox import showinfo

root = tk.Tk()

def clicked():
    showinfo(title='Info', message='kliknięto')

icon = tk.PhotoImage(file='logo_png.png')
button = tk.Button(
    text='Przycisk',
    image=icon,
    compound=tk.TOP,
    command=clicked)
button.pack(ipadx=11, ipady=11, expand=True)
root.mainloop()