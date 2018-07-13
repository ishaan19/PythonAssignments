#1

from tkinter import *
root = Tk()
hwL = Label(root, text='Hello World !!')
hwL.pack()
exitB = Button(root,text='Exit',width=25,command=root.destroy)
exitB.pack()
root.mainloop()


#2

from tkinter import *
root = Tk()
def onclick():
    r = Tk()
    labL = Label(r,text='You clicked on the right button!')
    labL.pack()
    
root.title('Hello')

textB = Button(root,text='Click Me',bg='green', command=onclick)
textB.pack()

exitB = Button(root,text='Exit',width=25,command=root.destroy)
exitB.pack()
root.mainloop()

#3

from tkinter import *
root = Tk()
def onclick():
    r = Tk()
    labL = Label(r,text='You clicked on the right button!')
    labL.pack()
    
root.title('Window')
frame_ = Frame(root,bg='black')
frame_.pack(fill=X)
l1L = Label(frame_,text='Click on any button',bg='white')
l1L.pack()

textB = Button(frame_,text='Click Me',bg='green', command=onclick)
textB.pack()

exitB = Button(frame_,text='Exit',width=25,command=root.destroy)
exitB.pack()

root.mainloop()

#4

from tkinter import *
root = Tk()
def onclick():
    print(input1.get())
    
root.title('Window')
frame_ = Frame(root,bg='black')
frame_.pack(fill=X)
l1L = Label(frame_,text='Enter name',bg='blue')
l1L.pack()

input1 = Entry(root)
input1.pack()
textB = Button(root,text='Click Me',bg='green', command=onclick)
textB.pack()

exitB = Button(root,text='Exit',width=25,command=root.destroy)
exitB.pack()

root.mainloop()
