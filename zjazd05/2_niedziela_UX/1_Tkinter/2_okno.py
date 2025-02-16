import tkinter as tk

root = tk.Tk()
root.title('Tkinter')
root.geometry('600x400+1300+100')

message1 = tk.Label(root, text='Witamy we Wrocławiu')
message1.pack()
message2 = tk.Label(root, text='')
message2.pack()
message3 = tk.Label(root, text='...')
message3.pack()

root.mainloop()