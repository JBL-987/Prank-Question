from tkinter import *
from tkinter import messagebox
import random

def yes():
    messagebox.showinfo('','Thanks bro')
    quit()

def motionMouse(event):
    btnNo.place(x=random.randint(0, 500), y=random.randint(0, 500))

root = Tk()
root.title ("Question")
root.geometry ("800x800")
root.resizable(width=False, height=False)
root['bg'] = 'white'    

label = Label(root, text='Are you Gay?', font='Arial 20 bold', bg = 'white').pack()
btnNo = Button(root, text='no',font='Arial 20 bold')
btnNo.place(x=170, y=100)
btnNo.bind('<Enter>', motionMouse)
btnYes = Button(root, text='Yes',font='Arial 20 bold',command=yes).place(x=350, y=400)

root.mainloop()