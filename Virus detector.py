from tkinter import *
from tkinter import messagebox
window = Tk()
window.geometry("200x200")

def message():

    messagebox.showwarning("ALERT!", "STOP VIRUS FOUND!")


btn = Button(window, text= "SCAN FOR VIRUS", command= message)
btn.place(x = 40, y = 80)

window.mainloop()

