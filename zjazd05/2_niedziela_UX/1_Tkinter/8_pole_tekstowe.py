import tkinter as tk
from tkinter.messagebox import showinfo

def clicked1():
    msg = f'Wpisałeś: {entry_text.get()}'
    showinfo(title='Info', message=msg)
    print('Kliknęto')
    print(f'Wpisano {entry_text.get()}')



root = tk.Tk()
entry_text = tk.StringVar()

frame = tk.Frame()
frame.pack(padx=50, pady=50)
label = tk.Label(frame, text='Wpisz cos')
label.pack()
entry = tk.Entry(frame, textvariable=entry_text, font=('Helvetica', 20))
entry.pack(ipadx=100, ipady=30)
text_field = tk.Text(frame, height=3, width=40)
text_field.pack()
button1 = tk.Button(frame, text='Entry', command=clicked1)
button1.pack()
button2 = tk.Button(frame, text='Text', command=clicked2)
button2.pack()

root.mainloop()