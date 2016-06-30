from tkinter import *
from tkinter import filedialog

print("adding variables...")

isSaved = None

"""
PYDOR
CREATED BY LYKAKSPARS
"""

filename = None

print("adding functions...")

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


print("Adding Root Tk...")
root = Tk()
root.title("pydor")
root.minsize(width=900, height=900)
root.maxsize(width=900, height=900)

print("Adding Text...")
text = Text(root, width=900, height=900)
text.pack()

print("Adding Menubar...")
menubar = Menu(root)
filemenu = Menu(menubar)
filemenu.add_command(label="New File")
filemenu.add_command(label="Open File", command=openFile)
filemenu.add_command(label="Save File", command=saveFile)
filemenu.add_command(label="Save As File", command=saveAs)
filemenu.add_separator()
filemenu.add_command(label="Quit", command=root.quit)
menubar.add_cascade(label="File", menu=filemenu)

print("Configuring the Root...")
root.config(menu=menubar)
print("Complete!")
root.mainloop()
