from tkinter import *
from tkinter import filedialog

isSaved = None

"""
PYDOR 0.1
CREATED BY LYKAKSPARS
"""

filename = None

def newFile():
    global filename
    filename = "Untitled"
    text.delete(0.0, END)
    isSaved = None

def saveAs():
    f = asksaveasfile(node="w", defaultextension="*.*")
    t = text.get(0.0, END)
    try:
        f.write(t.rstrip())
        isSaved = True
    except:
        showerror(title="Oops!", message="Unable to save file...")

def saveFile():
    global filename
    t = text.get(0.0, END)
    f = open(filename, 'w')
    f.write(t)
    f.close()
    isSaved = True

def openFile():
    f = askopenfile(node='r')
    t = f.read()
    text.delete(0.0, END)
    text.insert(0.0, t)
    isSaved = None

root = Tk()
root.title("pydor")
root.minsize(width=900, height=900)
root.maxsize(width=900, height=900)

text = Text(root, width=900, height=900)
text.pack()

menubar = Menu(root)
filemenu = Menu(menubar)
filemenu.add_command(label="New File")
filemenu.add_command(label="Open File", command=openFile)
filemenu.add_command(label="Save File", command=saveFile)
filemenu.add_command(label="Save As File", command=saveAs)
filemenu.add_separator()
filemenu.add_command(label="Quit", command=root.quit)
menubar.add_cascade(label="File", menu=filemenu)

root.config(menu=menubar)
root.mainloop()
