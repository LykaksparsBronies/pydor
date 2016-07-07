from tkinter import *
import tkinter.filedialog
import subprocess

root = Tk()
root.title("ChangeLog")
root.minsize(width=300, height=300)
root.maxsize(width=300, height=300)

labelt = Label(root, text='CHANGELOG')
labelt.pack()

root.mainloop() 
