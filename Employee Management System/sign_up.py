from tkinter import *
from tkinter import messagebox
import os
root = Tk()
root.geometry("300x200+50+50")

def getvals1():
    print("Conform Successful")
def getvals2():
    print("Reset Successful")  

def sign_up():
    User=Username.get()
    code=Password.get() 
    Email=Email.get()

    if User=="demo" and code=="demo123":
        root=Toplevel(root)
        root.title("Bill")

    elif User=="" and code=="":
        messagebox.showerror("Invalid","please enter Username and Password")
    elif User=="":
        messagebox.showerror("Invalid","Username is required")
    elif code=="":
        messagebox.showerror("Invalid","The Password field is required")
    elif Email=="":
        messagebox.showerror("Invalid","Email id is required")        
    elif User!="demo" and code!="demo123":
        messagebox.showerror("Invalid","invalid Username and Password")
    elif User!="demo":
        messagebox.showerror("Invalid","Please enter valid Username")
    elif code!="demo123":
        messagebox.showerror("Invalid","Please enter a valid Password") 
    elif Email!="demo@gmail.com":
        messagebox.showerror("Invalid","Please enter valid Email id")                            
        

global Username
global Password
global Email

    
Label(root, text="Employee sign_up form", font="arial 15 bold").place(x=50,y=3)
Username=Label(root,text="Username")
Password=Label(root,text="Password")
Email=Label(root,text="Eamil")

Username.place(x=10,y=52)
Password.place(x=10,y=83)
Email.place(x=10,y=112)

Username = StringVar
Password = StringVar
Email = StringVar
checkvalue = IntVar

Usernameentry = Entry(root, textvariable = Username)
Passwordentry = Entry(root, textvariable = Password)
Emailentry = Entry(root, textvariable = Email)

Usernameentry.place(x=100,y=52)
Passwordentry.place(x=100,y=83)
Emailentry.place(x=100,y=112)

def Reset():
    Usernameentry.delete(0,END)
    Passwordentry.delete(0,END)
    Emailentry.delete(0,END)


Button(text="Conform",command=getvals1).place(x=100,y=150)

Button(text="Reset",command=getvals2).place(x=170,y=150)

root.mainloop()

