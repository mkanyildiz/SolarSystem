import tkinter as tk
 
app_win = tk.Tk()
app_win.title("Solarsystem")
app_win.geometry('960x540')
 
back_gnd = tk.Canvas(app_win)
back_gnd.pack(expand=True, fill='both')
 
back_gnd_image = tk.PhotoImage(file="splash.png")
back_gnd.create_image(0, 0, anchor='nw', image=back_gnd_image)
 
button = tk.Button(None, text="Button", bd=1, highlightthickness=0)
back_gnd.create_window(50,20, window=button, anchor='nw')


app_win.mainloop()
