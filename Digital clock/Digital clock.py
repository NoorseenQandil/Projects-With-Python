from tkinter import Label, Tk
import time

Window = Tk()
Window.title("Digital clock in python")
Window.geometry("500x200")
Window.resizable(0,0)
text_font=("Boulder", 80, 'bold')
background = "#008080"
foreground = "#F8F8FF"
border_width = 45
label = Label(Window, font=text_font, bg=background, fg=foreground, bd=border_width)
label.grid(row=0, column=1)
def digital():
    time_live = time.strftime("%H:%M:%S")
    label.config(text=time_live)
    label.after(200, digital)
digital()
Window.mainloop()  