from tkinter import *

window = Tk()
window.geometry("200x300")
window.title("Main")

def topwin():
    top = Toplevel()
    top.geometry("180x100")
    top.title("Top level")
    lbl2 = Label(top, text = "This is top level window")
    lbl2.pack()


lbl = Label(window, text = "This is root window")
lbl.pack()
btn = Button(window, text = "Click here to open another window", command = topwin)
btn.pack()
