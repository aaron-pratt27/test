from tkinter import *
from PIL import ImageTk,Image
from tkinter import filedialog

root = Tk()
root.title("Slider")
root.geometry("400x400")

def show():
	myLabel = Label(root, text=var.get()).pack()

var = StringVar()

c = Checkbutton(root, text="Check this box", variable=var, onvalue="Pizza", offvalue="Burger")
c.deselect()
c.pack()



myButton = Button(root, text="Show Selection", command=show).pack()

mainloop()