from tkinter import *
from tkinter import messagebox 
import math
root = Tk()
root.geometry("300x300")
# root.iconbitmap('C:\Users\KIIT\Documents\Python Project\GUI Project\Mini Project\Half_Life_II.ico')
root.minsize(340,200)
root.maxsize(340,200)
root.title("Combination")
def combination():
    if n.get()>=r.get():
        combi = float(math.factorial(int(n.get()))/(math.factorial(int(r.get()))*math.factorial(int(n.get()-r.get()))))
        messagebox.showinfo(f"Combination of N={n.get()} R={r.get()}",f"Combination = {combi}")
    else:
        messagebox.showinfo("ERROR!","Sorry Operation cant be done!")
Label(root,text=" Welcome to Combination Project ",font="Cascadia 14 bold italic",bg="gray",fg="black").place(x=10,y=10)
Label(text="N",font="Cascadia 10 bold").place(x=80,y=50)
n = IntVar()
Entry(root,textvariable=n).place(x=150,y=50)
Label(text="R",font="Cascadia 10 bold").place(x=80,y=80)
r = IntVar()
Entry(root,textvariable=r).place(x=150,y=80)
Button(text="Calculate",bg="gray",fg="red",command=combination).place(x=150,y=110)
root.mainloop()
