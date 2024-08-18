from tkinter import *

root= Tk()
root.geometry('300x200')
root.title(Tk)

def Admin_login():
    root.destroy()
    ##import    idhar tera wla code ka .py file ka naam daal

def User_login():
    root.destroy()
    import sign_up.py
    
Label(root, text="EMPLOYEE MANAGEMENT SYSTEM", font="arial 12 bold").place(x=7,y=3)

Button(
    root, 
    text="Admin_login", 
    command=Admin_login
    ).place(x=50,y=100)

Button(
    root, 
    text="User_login", 
    command=User_login
    ).place(x=150,y=100)

root.mainloop()