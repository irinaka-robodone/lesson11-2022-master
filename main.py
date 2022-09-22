from mimetypes import init
import tkinter as tk
from tkinter import ttk
# import tkinter.scrolledtext as tksc
root = tk.Tk()
def osareta():
    print(intvar.get())

root.title("RPG")
root.geometry("300x300")
# var_spinbox=tk.StringVar()
# spinbox=tk.Spinbox(root,from_=0,to=10,increment=0.5,state="readonly",textvariable=var_spinbox)
frame=tk.LabelFrame(root,text="役職",foreground="black",labelanchor="n")
intvar=tk.IntVar()
intvar.set(0)
# comb = ttk.Combobox(root,values=("北海道","東北","関東","中部","近畿","中国","四国","九州沖縄"))
rd1 = tk.Radiobutton(frame,text="魔法使い",value=1,variable=intvar)
rd2 = tk.Radiobutton(frame,text="剣士",value=2,variable=intvar)
rd3 = tk.Radiobutton(frame,text="盾使い",value=3,variable=intvar)
# ck = tk.Checkbutton(text="チェックボックス",variable=boolvar)
# ld=tk.Listbox(root,listvariable=intvar,selectmode="multiple",height=5)
# # id = tk.Label(text="ラベル")
# en = tk.Entry(text="入力")
bt = tk.Button(text="OK",command =osareta)
# sc = tksc.ScrolledText(height = 5,width = 100)
# id.pack()
frame.pack()
rd1.pack()
rd2.pack()
rd3.pack()
# spinbox.pack()
bt.pack()
# bt.pack()

root.mainloop()
