from tkinter import *
from tkinter.scrolledtext import *
from tkinter import filedialog,simpledialog
from tkinter import messagebox
from tkinter.ttk import *
import re


filename = " "

root = Tk()
root.title("Notepad")

#scrolledtext
Notepad=ScrolledText(root,width=100,height=35)

#functions

def newfile():
    global filename
    filename = "Untitled"
    Notepad.delete(0.0,END)

def savefile():
    f = filedialog.asksaveasfile(mode='w',defaultextension='.txt')
    if f != None:
        data = Notepad.get('1.0',END)
    try :
        f.write(data)
    except :
        messagebox.showerror(title='error',message='File cannot be saved')

def saveas():
    f = filedialog.asksaveasfile(mode='w',defaultextension='.txt')
    data = Notepad.get('1.0',END)
    try :
        f.write(data.rstrip())
    except :
        messagebox.showerror(title='error',message='File cannot be saved')

def openfile():
    f = filedialog.askopenfile(mode='r')
    data=f.read()
    Notepad.delete(0.0,END)
    Notepad.insert(0.0,data)
    
def aboutcommand():
    label = messagebox.showinfo("About","just another Notepad \n Copyright \n No rights Reserved")

def handle_click(event):
    textPad.tag_config('Found',background='white',foreground='grey')
    
def find_pattern():
    Notepad.tag_remove("Found",'1.0',END)
    find = simpledialog.askstring("Find....","Enter text:")
    if find:
        idx = '1.0'
    while 1:
        idx = Notepad.search(find,idx,nocase=1,stopindex=END)
        if not idx:
            break
        lastidx = '%s+%dc' %(idx,len(find))
        Notepad.tag_add('Found',idx,lastidx)
        idx = lastidx
    Notepad.tag_config('Found',foreground='white',background='black')
    Notepad.bind("<1>",handle_click)  

def printme():
    label = messagebox.showinfo("Text","Welcome to text editor")

def exit_command():
    if messagebox.askyesno("Exit","Are you sure you want to exit?"):
        root.destroy()

#menu
menuM = Menu(root)
root.configure(menu=menuM)

fileM = Menu(menuM)
menuM.add_cascade(label='File', menu=fileM)
fileM.add_command(label='new',command=newfile)
fileM.add_command(label='open',command=openfile)
fileM.add_command(label='save',command=savefile)
fileM.add_command(label='SaveAs',command=saveas)
fileM.add_separator()
fileM.add_command(label='exit', command=root.destroy)

editM = Menu(menuM)
menuM.add_cascade(label='Edit', menu=editM)
editM.add_command(label='cut')
editM.add_command(label='copy')
editM.add_command(label='paste')
editM.add_command(label='redo')
editM.add_command(label='undo')

viewM = Menu(menuM)
menuM.add_cascade(label='View', menu=viewM)

helpM = Menu(menuM)
menuM.add_cascade(label='Help', menu=helpM)
helpM.add_command(label='about',command=aboutcommand)

findM = Menu(menuM)
menuM.add_cascade(label='Find', menu=findM)
findM.add_command(label='Find',command=find_pattern)

#AddingIcons

frame1 = Frame(root)
frame1.pack()

Image1 = PhotoImage(file='new_file.gif')
l1 = Label(frame1,text = 'New')
b1 = Button(frame1,image = Image1,command=newfile)
b1.grid(row=0,column=0)
l1.grid(row=1,column=0)

Image2 = PhotoImage(file='open_file.gif')
l2 = Label(frame1,text = 'Open')
b2 = Button(frame1,image = Image2,command=openfile)
b2.grid(row=0,column=1)
l2.grid(row=1,column=1)

Image5 = PhotoImage(file='save.gif')
l5 = Label(frame1,text = 'Save')
b5 = Button(frame1,image = Image5,command=saveas)
b5.grid(row=0,column=4)
l5.grid(row=1,column=4)

Image6 = PhotoImage(file='about.gif')
l6 = Label(frame1,text = 'About')
b6 = Button(frame1,image = Image6,command=aboutcommand)
b6.grid(row=0,column=5)
l6.grid(row=1,column=5)

Image7 = PhotoImage(file='find_text.gif')
l7 = Label(frame1,text = 'Find')
b7 = Button(frame1,image = Image7,command=find_pattern)
b7.grid(row=0,column=6)
l7.grid(row=1,column=6)


Notepad.pack()

root.mainloop()
