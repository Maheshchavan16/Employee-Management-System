from tkinter import *
import tkinter as tk
from tkinter import messagebox
import os
root = Tk()
root.geometry("300x200")


def getvals1():
    print("Login Successful")
def getvals2():
    print("Reset Successful")
'''def my_show():
    if(checkvalue.get()==1):
        eye.config(show='')
    else:
        eye.config(show='*')'''

def Reset():
    Usernameentry.delete(0,END)
    Passwordentry.delete(0,END)

def login():
    User=Username.get()
    code=Password.get() 

    if User=="demo" and code=="demo123":
        root=Toplevel()
        root.title("Bill")

    elif User=="" and code=="":
        messagebox.showerror("Invalid","please enter Username and Password")
    elif User=="":
        messagebox.showerror("Invalid","Username is required")
    elif code=="":
        messagebox.showerror("Invalid","The Password field is required")    
    elif User!="demo" and code!="demo123":
        messagebox.showerror("Invalid","invalid Username and Password")
    elif User!="demo":
        messagebox.showerror("Invalid","Please enter valid Username")
    elif code!="demo123":
        messagebox.showerror("Invalid","Please enter a valid Password")         

global Username
global Password

    
Label(root, text="Employee Login form", font="arial 15 bold").place(x=50,y=3)


Username=Label(root,text="Username")
Password=Label(root,text="Password")

Username.place(x=10,y=52)
Password.place(x=10,y=87)

Username = StringVar()
Password = StringVar()

Usernameentry = Entry(root, textvariable = Username)
Passwordentry = Entry(root, textvariable = Password)


Usernameentry.place(x=100,y=52)
Passwordentry.place(x=100,y=87)

'''eye = tk.Entry(root,font="arial 15 ",show='*',textvariable='eye_str')
eye.place(x=100,y=100)
checkvalue=IntVar(value=0)

Button = tk.Checkbutton(root,text='Show Password',variable=checkvalue,
	onvalue=1,offvalue=0,command=my_show)
Button.place(x=100,y=95) 
'''


Button(text="Login",command=getvals1).place(x=100,y=170)

Button(text="Reset",command=getvals2).place(x=170,y=170)

root.mainloop()
