import tkinter as tk
# import customtkinter as ctk

root = tk.Tk()
root.title('Tkinter')

window_width = 300
window_height = 200
screen_width = root.winfo_screenwidth()    # pobranie rozmiaru ekranu
screen_height = root.winfo_screenheight()
center_x = int(screen_width/2 - window_width / 2)
center_y = int(screen_height/2 - window_height / 2)
root.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
print(screen_width, screen_height)

message1 = tk.Label(root, text='Witamy we Wrocławiu')
message1.pack()
message2 = tk.Label(root, text='')
message2.pack()
message3 = tk.Label(root, text='...')
message3.pack()

root.mainloop()