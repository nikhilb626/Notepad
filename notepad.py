from tkinter import *
from tkinter.messagebox import showinfo
from tkinter.filedialog import askopenfilename,asksaveasfilename
import os


def cut():
    textArea.event_generate('<<Cut>>')


def copy():
    textArea.event_generate("<<Copy>>")

def paste():
    textArea.event_generate("<<Paste>>")


def about():
    showinfo("notepad","notepad by Nikhil")


def quitApp():
    root.destroy()



def newFile():
    global file
    root.title("untitled-Notepad")
    file=NONE
    textArea.delete(1.0,END)


def openFile():
    global file
    file=askopenfilename(defaultextension=".txt",filetypes=[("allfiles","*.*"),("Textdocuments","*.txt")])
    if file=="":
        file=None

    else:
        root.title(os.path.basename(file)+"-notepad")
        textArea.delete(1.0,END)
        f=open(file,"r")
        textArea.insert(1.0,f.read())



def saveFile():
    global file
    if file==None:
        file=asksaveasfilename(initialfile="untititled",defaultextension=".txt",filetypes=[("allfiles","*.*"),("textdocuments","*.txt")])
        if file=="":
            file=None

        else:
            # save as a new file
            f=open(file,"w")
            f.write(textArea.get(1.0,END))

            root.title(os.path.basename(file)*"-notepad")

    
    else:
        # save the file

        f=open(file,"w")
        f.write(textArea.get(1.0,END))
        f.close()







if __name__=='__main__':
    # basic tkinter setup
    root=Tk()
    root.title("untitled-notepad")
    root.geometry("600x700")



   

    # add text area
    textArea=Text(root,font="lucida 15")
    file=None

    textArea.pack(expand=TRUE,fill=BOTH)



    # lets create menu bar
    MenuBar=Menu(root)
    FileMenu=Menu(MenuBar,tearoff=0)

    FileMenu.add_command(label="New",command=newFile)
    FileMenu.add_command(label="Open",command=openFile)
    FileMenu.add_command(label="Save",command=saveFile)
    FileMenu.add_separator()
    FileMenu.add_command(label="Exit",command=quitApp)
    
    MenuBar.add_cascade(label="File",menu=FileMenu)

    root.config(menu=MenuBar)


    # edit menu

    EditMenu=Menu(MenuBar,tearoff=0,)

    EditMenu.add_command(label="Cut",command=cut)
    EditMenu.add_command(label="Copy",command=copy)
    EditMenu.add_command(label="paste",command=paste)


    MenuBar.add_cascade(label="Edit",menu=EditMenu)
    root.config(menu=MenuBar)



    # helpmenu

    HelpMenu=Menu(MenuBar,tearoff=0)
    HelpMenu.add_command(label="about",command=about)
    MenuBar.add_cascade(label="Help",menu=HelpMenu)

    root.config(menu=MenuBar)


    # add scrollbar

    scroll_bar=Scrollbar(textArea)
    scroll_bar.pack(side=RIGHT,fill=Y)

    scroll_bar.config(command=textArea.yview)
    textArea.config(yscrollcommand=scroll_bar.set)



    root.mainloop()
