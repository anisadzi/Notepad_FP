"""Import Stuff from Tkinter"""
from tkinter import *
from tkinter.messagebox import *
import sys

"""The help tab class"""
class Help():
    def about(root):
        showinfo(title="About", message=f"This a notepad :))")


def main(root, text, menubar):

    help = Help()

    helpMenu = Menu(menubar)
    helpMenu.add_command(label="About", command=help.about)
    menubar.add_cascade(label="Help", menu=helpMenu)

    root.config(menu=menubar)