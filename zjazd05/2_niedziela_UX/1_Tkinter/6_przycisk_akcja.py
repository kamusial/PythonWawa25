import tkinter as tk

def hello():
    print('Leci akcja')


root = tk.Tk()

# exit_button = tk.Button(text='Wyjscie', command=hello)
exit_button = tk.Button(text='Wyjscie', command=root.quit)
exit_button.pack(ipadx=10, ipady=50)   # wewnętrzne rozszerzenie

root.mainloop()