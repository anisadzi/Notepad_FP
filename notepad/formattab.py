"""Import Stuff from Tkinter"""
from tkinter import *
from tkinter.colorchooser import askcolor
from tkinter.font import Font, families
from tkinter.scrolledtext import *

import time
import sys

"""The format tab class"""
class Format():
    def __init__(self, word):
        self.word = word

    def changeBackgroundColor(self):
        (triple, hexstr) = askcolor() #converts a number or binary data value to text formatted as a hexadecimal number
        if hexstr:  #converts a number to text formatted as a hexadecimal number
            self.word.config(bg=hexstr)

    def changeFontColor(self):
        (triple, hexstr) = askcolor() #converts a number or binary data value to text formatted as a hexadecimal number
        if hexstr: #converts a number to text formatted as a hexadecimal number
            self.word.config(fg=hexstr)

    def bold(self, *args): #bold text option
        try:
            current_tags = self.word.tag_names("sel.first")
            if "bold" in current_tags:
                self.word.tag_remove("bold", "sel.first", "sel.last")
            else:
                self.word.tag_add("bold", "sel.first", "sel.last")
                bold_font = Font(self.word, self.word.cget("font")) #cget method to get text option value of label
                bold_font.configure(weight="bold") #query or modify the options for a specified tagname
                self.word.tag_configure("bold", font=bold_font)
        except:
            pass

    def italic(self, *args): #italic text option
        try:
            current_tags = self.word.tag_names("sel.first")
            if "italic" in current_tags:
                self.word.tag_remove("italic", "sel.first", "sel.last")
            else:
                self.word.tag_add("italic", "sel.first", "sel.last")
                italic_font = Font(self.word, self.word.cget("font"))
                italic_font.configure(slant="italic")
                self.word.tag_configure("italic", font=italic_font)
        except:
            pass

    def underline(self, *args): #underline word option
        try:
            current_tags = self.word.tag_names("sel.first")
            if "underline" in current_tags:
                self.word.tag_remove("underline", "sel.first", "sel.last")
            else:
                self.word.tag_add("underline", "sel.first", "sel.last")
                underline_font = Font(self.word, self.word.cget("font"))
                underline_font.configure(underline=1)
                self.word.tag_configure("underline", font=underline_font)
        except:
            pass

    def overstrike(self, *args):   #overstrike word option
        try:
            current_tags = self.word.tag_names("sel.first")
            if "overstrike" in current_tags:
                self.word.tag_remove("overstrike", "sel.first", "sel.last")
            else:
                self.word.tag_add("overstrike", "sel.first", "sel.last")
                overstrike_font = Font(self.word, self.word.cget("font"))
                overstrike_font.configure(overstrike=1)
                self.word.tag_configure("overstrike", font=overstrike_font)
        except:
            pass

    def addDate(self): #adding date to note
        full_date = time.localtime()
        day = str(full_date.tm_mday) #day
        month = str(full_date.tm_mon) #month
        year = str(full_date.tm_year) #year
        date = " "+ day + '/' + month + '/' + year #adding all together
        self.word.insert(INSERT, date, "a")


def main(root, word, menubar):
    comFormat = Format(word)

    fontoptions = families(root) #default font and size
    font = Font(family="Arial", size=10)
    word.configure(font=font)

    formatMenu = Menu(menubar)

    fontsubmenu = Menu(formatMenu, tearoff=0)
    sizesubmenu = Menu(formatMenu, tearoff=0)

    for option in fontoptions: #font options
        fontsubmenu.add_command(label=option, command=lambda option=option: font.configure(family=option))
    for value in range(1, 31): #size options
        sizesubmenu.add_command(label=str(value), command=lambda value=value: font.configure(size=value))

    #adding command, label, and the shortcut
    formatMenu.add_command(label="Change Background", command=comFormat.changeBackgroundColor)
    formatMenu.add_command(label="Change Font Color", command=comFormat.changeFontColor)
    formatMenu.add_cascade(label="Font", underline=0, menu=fontsubmenu)
    formatMenu.add_cascade(label="Size", underline=0, menu=sizesubmenu)
    formatMenu.add_command(label="Bold", command=comFormat.bold, accelerator="Ctrl+B")
    formatMenu.add_command(label="Italic", command=comFormat.italic, accelerator="Ctrl+I")
    formatMenu.add_command(label="Underline", command=comFormat.underline, accelerator="Ctrl+U")
    formatMenu.add_command(label="Overstrike", command=comFormat.overstrike, accelerator="Ctrl+T")
    formatMenu.add_command(label="Add Date", command=comFormat.addDate)
    menubar.add_cascade(label="Format", menu=formatMenu)

    root.bind_all("<Control-b>", comFormat.bold)
    root.bind_all("<Control-i>", comFormat.italic)
    root.bind_all("<Control-u>", comFormat.underline)
    root.bind_all("<Control-T>", comFormat.overstrike)

    root.grid_columnconfigure(0, weight=1)
    root.resizable(True, True)

    root.config(menu=menubar)
