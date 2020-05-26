from tkinter import *
from tkinter.messagebox import showinfo
from tkinter.filedialog import askopenfilename,asksaveasfilename
import os

def newfile():
    global file
    root.title("NOTEPAD")
    file=NONE
    TextArea.delete(1.0,END)
def openfile():
    global file
    file=askopenfilename(defaultextension=".txt",filetypes=[("All Files","*.*"),("Text Documents","*.txt")])

    if file=="":
        file=NONE
    else:
        root.title(os.path.basename(file) + "-Notepad")
        TextArea.delete(1.0,END)
        f=open(file,"r")
        TextArea.insert(1.0,f.read())
        f.close()


def savefile():
    global file
    if file == NONE:
        file=asksaveasfilename(initialfile='Untitled',defaultextension=".txt",filetypes=[("All Files","*.*"),("Text Documents","*.txt")])
        if file=="":
            file=NONE
        else:
            f=open(file,"w")
            f.write(TextArea.get(1.0,END))
            f.close()

            root.title(os.path.basename(file)+"-Notepad")
            print("File saved")
    else:
        f = open(file, "w")
        f.write(TextArea.get(1.0, END))
        f.close()


def quitapp():
    root.destroy()

def copy():
    TextArea.event_generate("<<Copy>>")

def paste():
    TextArea.event_generate("<<Paste>>")

def cut():
    TextArea.event_generate(("<<Cut>>"))

def viewhelp():
    showinfo("HELP","May I help you")
    print("Mail us at @goyal.tanivji@gmail.com")

def aboutit():
    showinfo("Notepad","Notepad by code with Taniv")

root = Tk()

root.geometry("500x500")

root.title("NOTEPAD")

#textarea
TextArea=Text(root,font='lucida 13')
file=NONE
TextArea.pack(expand=2,fill='both')

#menubar
MenuBar=Menu(root)

#file menu starts
FileMenu=Menu(MenuBar,tearoff=0)

#to open file
FileMenu.add_command(label="New",command=newfile)

#already exists file
FileMenu.add_command(label="open",command=openfile)

#to save current file
FileMenu.add_command(label='Save',command=savefile)
FileMenu.add_separator()
FileMenu.add_command(label="Exit",command=quitapp)
MenuBar.add_cascade(label="File",menu=FileMenu)
root.config(menu=MenuBar)
#file menu ends

#edit menu starts
EditMenu=Menu(MenuBar,tearoff=0)

#to copy file
EditMenu.add_command(label="Copy",command=copy)

#to paste file
EditMenu.add_command(label='Paste',command=paste)

#to cut file
EditMenu.add_command(label="Cut",command=cut)
MenuBar.add_cascade(label="Edit",menu=EditMenu)
root.config(menu=MenuBar)
#EDIT MENU ENDS

#HELP MENU STARTS
HelpMenu=Menu(MenuBar,tearoff=0)

#to help
HelpMenu.add_command(label="ViewHelp",command=viewhelp)
HelpMenu.add_separator()
#about
HelpMenu.add_command(label='About it',command=aboutit)
MenuBar.add_cascade(label="Help",menu=HelpMenu)
root.config(menu=MenuBar)
#HELP MENU ENDS

#scrollbar
Scroll=Scrollbar(TextArea)
Scroll.pack(side='right',fill='y')
Scroll.config(command=TextArea.yview)
TextArea.config(yscrollcommand=Scroll.set)

root.mainloop()
