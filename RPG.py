from mimetypes import init
from multiprocessing.sharedctypes import Value
import tkinter as tk
from tkinter import ttk
def yakusyo(a):
    if a ==1:
        root2 =tk.Tk()
        root2.title("RPG")
        root2.geometry("300x300")
        # rd1 = tk.Radiobutton(frame,text="魔法使いa",value=1,variable=intvar, command= yakusyo)
        # rd2 = tk.Radiobutton(frame,text="剣士",value=2,variable=intvar, command= yakusyo)
        # rd3 = tk.Radiobutton(frame,text="盾使い",value=3,variable=intvar, command= yakusyo)
        root2.mainloop()
root = tk.Tk()
def osareta():
    print(intvar.get())

root.title("RPG")
root.geometry("300x300")

frame=tk.LabelFrame(root,text="役職",foreground="black",labelanchor="n")
intvar=tk.IntVar()
intvar.set(0)

rd1 = tk.Radiobutton(frame,text="魔法使い",value=1,variable=intvar, command= yakusyo(1))
rd2 = tk.Radiobutton(frame,text="剣士",value=2,variable=intvar, command= yakusyo(2))
rd3 = tk.Radiobutton(frame,text="盾使い",value=3,variable=intvar, command= yakusyo(3))
bt = tk.Button(text="OK",command =osareta)
frame.pack()
rd1.pack()
rd2.pack()
rd3.pack()
bt.pack()
root.mainloop()

