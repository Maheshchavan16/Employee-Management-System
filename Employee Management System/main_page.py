from tkinter import *
from tkinter import font
import os
root = Tk()
root.geometry("300x200")
root.title("EMPLOYEE MANAGEMENT SYSTEM")

def getvals1():
    print("User entered successful")
def getvals2():
    print("Admin entered Successful")


Label(root, text="Employee management system", font="arial 15 bold").place(x=7,y=3)

#Button


Button(text="User login",command=getvals1).place(x=70,y=100)


Button(text="Admin login",command=getvals2).place(x=170,y=100)



root.mainloop()