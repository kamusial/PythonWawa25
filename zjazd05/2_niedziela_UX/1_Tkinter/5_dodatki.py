import tkinter as tk

root = tk.Tk()
root.title('Max i min okna')
root.geometry('600x400+1200+80')
root.minsize(300, 300)
root.maxsize(800, 500)
root.attributes('-alpha', 0.8)  # nieprzeźroczystość
root.attributes('-topmost', 1)  # onko zawsze na wierzchu
root.iconbitmap('logo.ico')

root.mainloop()