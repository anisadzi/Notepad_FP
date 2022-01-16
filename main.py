"""Import Stuff from Tkinter"""
from tkinter import *
from tkinter.filedialog import *
from tkinter.messagebox import *
from tkinter.font import Font
from tkinter.scrolledtext import *

"""Import Stuff from other files"""
from notepad import filetab
from notepad import edittab
from notepad import formattab
from notepad import helptab

"""Setting window"""
root = Tk() #creates a blank parent widget

root.title(f"Notepad") #set title for the window
root.geometry("300x250+300+300") #creating fixed geometry of Tkinter window 300x250
root.minsize(500, 500) #set minimum size of root window (width, height)

"""Text setting"""
text = ScrolledText(root, state='normal', height=500, width=500, #state is used for text widget to respond
wrap='word', pady=2, padx=3, undo=True) #wrap is used to controls the display of lines that are too wide
text.pack(fill=Y, expand=1) #fill used to determines whether widget fills any extra space allocated to it by the packer, 
#or keeps its own minimal dimensions, and expand to expand according to the window size
text.focus_set() #used to set the focus on the desired widget if and only if the master window is focused

"""Creating menubar and calling other files """
menubar = Menu(root)

filetab.main(root, text, menubar)
edittab.main(root, text, menubar)
formattab.main(root, text, menubar)
helptab.main(root, text, menubar)
root.mainloop() #infinite loop which keeps the program running until the window closed manually