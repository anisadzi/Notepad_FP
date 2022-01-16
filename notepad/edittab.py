"""Import Stuff from Tkinter"""
from tkinter import *
from tkinter.simpledialog import *
from tkinter.filedialog import *
from tkinter.messagebox import *

"""The edit tab class"""
class Edit():
    def popup(self, event):
        self.rightClick.post(event.x_root, event.y_root) #procedure posts a menu at a given position on the screen

    def copy(self, *args): #*args allows you to do is take in more arguments than the number of formal arguments that you previously defined
        select = self.word.selection_get() #get text that has been selected
        self.clipboard = select

    def paste(self, *args):
        self.word.insert(INSERT, self.clipboard) #insert text that has been copied

    def cut(self, *args):
        select = self.word.selection_get()
        self.clipboard = select
        self.word.delete(SEL_FIRST, SEL_LAST) #delete text

    def selectAll(self, *args):
        self.word.tag_add(SEL, "1.0", END) #the method tags either the position defined by startindex, or a range delimited by the positions
        self.word.mark_set(0.0, END) #informs a new position to the given mark
        self.word.see(INSERT) #this method returns true if the text located at the index position is visible

    def undo(self, *args):
        self.word.edit_undo() #undoes the last edit action

    def redo(self, *args):
        self.word.edit_redo() #redoes the last edit action

    def find(self, *args):
        self.word.tag_remove('found', '1.0', END) #removes the tag
        target = askstring('Find', 'Search word:') #provide dialogs that prompt the user to enter a value of the desired type

        if target:
            idx = '1.0'
            while 1:
                idx = self.word.search(target, idx, nocase=1, stopindex=END) #searches pattern, stop index to limit the search

                if not idx: break
                lastidx = '%s+%dc' % (idx, len(target))

                self.word.tag_add('found', idx, lastidx)
                idx = lastidx
            self.word.tag_config('found', foreground='white', background='blue') #to change the value of options for the tag when
            #foreground is the color used for text, background is the color used for the text with this tag

    def __init__(self, word, root):
        self.clipboard = None
        self.word = word
        self.rightClick = Menu(root)


def main(root, word, menubar):

    comEdit = Edit(word, root)

    editmenu = Menu(menubar)
    #adding command, label, and the shortcut
    editmenu.add_command(label="Copy", command=comEdit.copy, accelerator="Ctrl+C")
    editmenu.add_command(label="Paste", command=comEdit.paste, accelerator="Ctrl+V")
    editmenu.add_command(label="Cut", command=comEdit.cut, accelerator="Ctrl+X")
    editmenu.add_command(label="Undo", command=comEdit.undo, accelerator="Ctrl+Z")
    editmenu.add_command(label="Redo", command=comEdit.redo, accelerator="Ctrl+Y")
    editmenu.add_command(label="Find", command=comEdit.find, accelerator="Ctrl+F")
    editmenu.add_separator()
    editmenu.add_command(label="Select All", command=comEdit.selectAll, accelerator="Ctrl+A")
    menubar.add_cascade(label="Edit", menu=editmenu)

    root.bind_all("<Control-z>", comEdit.undo)
    root.bind_all("<Control-y>", comEdit.redo)
    root.bind_all("<Control-f>", comEdit.find)
    root.bind_all("<Control-a>", comEdit.selectAll)

    comEdit.rightClick.add_command(label="Copy", command=comEdit.copy)
    comEdit.rightClick.add_command(label="Cut", command=comEdit.cut)
    comEdit.rightClick.add_command(label="Paste", command=comEdit.paste)
    comEdit.rightClick.add_separator()
    comEdit.rightClick.add_command(label="Select All", command=comEdit.selectAll)
    comEdit.rightClick.bind("<Control-q>", comEdit.selectAll)

    word.bind("<Button-3>", comEdit.popup)

    root.config(menu=menubar)
