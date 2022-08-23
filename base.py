from tkinter import *
from PIL import ImageTk,Image

root = Tk()
root.title("Base")

def open():
	global my_img
	top = Toplevel()
	top.title("My second Window")
	my_img = ImageTk.PhotoImage(Image.open("orange.png"))
	my_label = Label(top, image=my_img).pack()
	btn2 = Button(top, text="Close Window", command=top.destroy).pack()

btn = Button(root, text="Open Second Window", command=open).pack()


mainloop()