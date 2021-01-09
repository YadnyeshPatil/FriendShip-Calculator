# Friendship calculator app using Python Tkinter
# @curious_.programmer

from tkinter import *
import tkinter.messagebox
import random as ra


# For Genrateing Random Numbers Form 0 - 100 
def genrator():  
   num =  ra.randint(0, 100)
   return num

# This is A Message Box For showin result
def msg(event):
    if (len(name1.get()) ==0 or len(name2.get()) == 0):
        tkinter.messagebox.showinfo('Error','Enter Valid Names..')
    else:
        tkinter.messagebox.showinfo('Result',f'The friendship strength Between {name1.get()} and {name2.get()}: {genrator()}%')
        
 
# Start 
window = Tk()
window.geometry("450x500")
window.resizable(width=False, height=False)
window.config(bg='#212125')
window.title("FriendShip Calculator")
icon = PhotoImage(file = "icon.png")
window.iconphoto(False, icon)
Label(window, text = 'FriendShip Calculator', font =('Verdana', 15)).pack(side = TOP, pady = 7)
img = PhotoImage(file="friends.png")
Label(window, image =img).pack()

name1 = StringVar()
name2 = StringVar()
L1 = Label(window, text="Your Name").pack(pady=5)
F1 = Entry(window,text=name1,bd =5).pack()
L2 = Label(window, text="Friend Name").pack(pady=5)           
F2 = Entry(window,text =name2, bd =5).pack()
b = Button(window, text='Calculate', padx=10, pady=10, font = "lucida 8 bold")
b.bind("<Button-1>", msg)
b.pack(pady=5)
window.mainloop()