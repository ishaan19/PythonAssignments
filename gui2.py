#1

from tkinter import *
root = Tk()
dictt = {}
root.title('List')
root.geometry('250x250')
dictt= {'jia':7656767676,
        'maria':6565656565,
        'sam':6464646464,
        'tobo':6565656586,
        'smith':9898989898,
        'luv':9090909090}

frame1=Frame(root)
frame1.pack()

s = Scrollbar(frame1)
s.pack(side=RIGHT,fill=Y)
listL = Listbox(frame1,yscrollcommand=s.set)

for x in dictt:
    listL.insert(END,x)
    
listL.pack(side=LEFT,fill=X)
s.config(command = listL.yview)

root.mainloop()

#2

from tkinter import *
root = Tk()
dictt = {}
root.title('List')
root.geometry('250x250')
dictt= {'jia':7656767676,
        'maria':6565656565,
        'sam':6464646464,
        'tobo':6565656586,
        'smith':9898989898,
        'luv':9090909090}

frame1=Frame(root)
frame1.pack()

s = Scrollbar(frame1)
s.pack(side=RIGHT,fill=Y)
listL = Listbox(frame1,yscrollcommand=s.set)

for x in dictt:
    listL.insert(END,x)
    
listL.pack(side=LEFT,fill=X)
s.config(command = listL.yview)
def onclick():
    dictt[e1.get()]=e2.get()
    listL.insert(END,e1.get())

frame2 = Frame(root)
frame2.pack()

lbl1 = Label(frame2,text='Name')
lbl1.grid(row=0, column=0)

lbl2 = Label(frame2,text='Mobile number')
lbl2.grid(row=1, column=0)

e1 = Entry(frame2)
e1.grid(row=0,column=1)

e2 = Entry(frame2)
e2.grid(row=1,column=1)

textB = Button(frame2,text='Add it',bg='green', command=onclick)
textB.grid(row=2,column=1)

root.mainloop()


#3(extra question)


from tkinter import *
root = Tk()
root.title('SCROL')
root.geometry('10x50')

scrol = Scrollbar(root,orient=HORIZONTAL)
scrol.pack(side=BOTTOM,fill=X)


mylist = Listbox(root, xscrollcommand = scrol.set )
s=''
for x in range(100):
    s=s+str(x)
mylist.insert(END,s)

mylist.pack( side = LEFT, fill = BOTH )
scrol.config( command = mylist.xview )

root.mainloop()
