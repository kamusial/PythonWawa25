import tkinter as tk
from tkinter.messagebox import showinfo
import customtkinter as ctk

def clicked_entry():
    msg = f'Wpisałeś: {entry_text.get()}'
    showinfo(title='Pole ENTRY', message=msg)
    print('Kliknęto')
    print(f'Wpisano {entry_text.get()}')

def clicked_text():
    # Pobiera tekst od początku ("1.0") do końca (tk.END)
    content = text_field.get('1.0', tk.END)
    showinfo(title='POte tekstowe TEXT', message=content)

root = ctk.CTk()   # główne okno Custom Tkinter
entry_text = tk.StringVar()

frame = tk.Frame()
frame.pack(padx=50, pady=50)
label = tk.Label(frame, text='Wpisz cos')
label.pack()
entry = tk.Entry(frame, textvariable=entry_text, show='*', font=('Helvetica', 20))
entry.pack(ipadx=100, ipady=30)
text_field = tk.Text(frame, height=3, width=40)
text_field.pack()
button1 = tk.Button(frame, text='Entry', command=clicked_entry)
button1.pack(fill='x', ipady=5, pady=5)
button2 = tk.Button(frame, text='Text', command=clicked_text)
button2.pack()

root.mainloop()