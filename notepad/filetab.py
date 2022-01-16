"""Import Stuff from Tkinter"""
from tkinter import *
from tkinter.filedialog import *
from tkinter.messagebox import *
import sys

"""The file tab class"""
class File():
    def newFile(self):
        self.defaultfilename = "Untitled" #default file name
        self.text.delete(0.0, END)

    def saveFile(self):
        try:
            txt = self.text.get(0.0, END)
            f = open(self.filename, 'w') #saving file
            f.write(txt)
            f.close()
        except:
            self.saveAs()

    def saveAs(self):
        f = asksaveasfile(mode='w', defaultextension='.txt') #save as option with default txt
        txt = self.text.get(0.0, END)
        try:
            f.write(txt.rstrip()) #rstrip() removes characters from the right based on the argument 
            #(a string specifying the set of characters to be removed)
        except:
            showerror(title="Oops!", message="Failed to save file...")

    def openFile(self):
        f = askopenfile(mode='r') #opening file
        self.defaultfilename = f.name
        txt = f.read()
        self.text.delete(0.0, END)
        self.text.insert(0.0, txt)

    def quit(self):
        answer = askyesno(title="Quit", message="Are you sure you want to quit?")
        if answer == True:
            self.root.destroy() #destroy all widgets and exit mainloop

    def __init__(self, text, root):
        self.defaultfilename = None
        self.text = text
        self.root = root


def main(root, text, menubar):
    filemenu = Menu(menubar)
    comFile = File(text, root)
    #adding command, label
    filemenu.add_command(label="New", command=comFile.newFile)
    filemenu.add_command(label="Open", command=comFile.openFile)
    filemenu.add_command(label="Save", command=comFile.saveFile)
    filemenu.add_command(label="Save As...", command=comFile.saveAs)
    filemenu.add_separator()
    filemenu.add_command(label="Quit", command=comFile.quit)
    menubar.add_cascade(label="File", menu=filemenu)
    root.config(menu=menubar)


