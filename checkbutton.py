from tkinter import *
from tkinter.messagebox import *
root=Tk()
root.geometry('300x200')
def show():

    s="You have selected "+ Checkbutton1.get() + Checkbutton2.get() + Checkbutton3.get() + Checkbutton4.get()
    showinfo("Output", s)
    root.destroy()
w=Label(root,text='Select your Hobbies...')
w.pack()
Checkbutton1=StringVar()
Checkbutton2=StringVar()
Checkbutton3=StringVar()
Checkbutton4=StringVar()
b=Checkbutton(root,text='Singing',variable=Checkbutton1,onvalue="Singing",offvalue='')
a=Checkbutton(root,text='Dancing',variable=Checkbutton2,onvalue='Dancing',offvalue='')
c=Checkbutton(root,text='Sleeping',variable=Checkbutton3,onvalue='Sleeping',offvalue='')
d=Checkbutton(root,text='Studying',variable=Checkbutton4,onvalue='Studying',offvalue='')
e=Button(root,text='Done',command=show)
f=Button(root,text='Exit',command=root.destroy)
b.pack()
a.pack()
c.pack()
d.pack()
e.pack()
f.pack()
mainloop()
