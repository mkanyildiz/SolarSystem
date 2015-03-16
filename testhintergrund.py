__author__ = 'mdorfinger'

import tkinter as tk
 
app_win = tk.Tk()
app_win.title("Solarsystem")
app_win.geometry('960x540')

customFont = ('Arial', 24, 'bold')

back_gnd = tk.Canvas(app_win)
back_gnd.pack(expand=True, fill='both')
 
back_gnd_image = tk.PhotoImage(file="splash.png")
back_gnd.create_image(0, 0, anchor='nw', image=back_gnd_image)
 
button = tk.Button(None, text="Start", bd=1, height=1, width=8, font=customFont)
back_gnd.create_window(30,30, window=button, anchor='nw')


app_win.mainloop()
