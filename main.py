import tkinter as tk
from tkinter import ttk
# import tkinter.scrolledtext as tksc
root = tk.Tk()
def osareta():
    print(var_spinbox.get())

root.title("たいとるです")
root.geometry("300x300")
var_spinbox=tk.StringVar()
spinbox=tk.Spinbox(root,from_=0,to=10,increment=0.5,state="readonly",textvariable=var_spinbox)
# frame=tk.LabelFrame(root,text="ラベルフレーム",foreground="black",labelanchor="n")
# strvar=tk.StringVar()
# comb = ttk.Combobox(root,values=("北海道","東北","関東","中部","近畿","中国","四国","九州沖縄"))
# rd1 = tk.Radiobutton(frame,text="ラジオボタン1",value=1,variable=strvar)
# rd2 = tk.Radiobutton(frame,text="ラジオボタン2",value=2,variable=strvar)
# rd3 = tk.Radiobutton(frame,text="ラジオボタン3",value=3,variable=strvar)
# ck = tk.Checkbutton(text="チェックボックス",variable=boolvar)
# ld=tk.Listbox(root,listvariable=strvar,selectmode="multiple",height=5)
# # id = tk.Label(text="ラベル")
# en = tk.Entry(text="入力")
bt = tk.Button(text="選択値を出力",command =osareta)
# sc = tksc.ScrolledText(height = 5,width = 100)
# id.pack()
# frame.pack()
# rd1.pack()
# rd2.pack()
# rd3.pack()
spinbox.pack()
bt.pack()
# bt.pack()

root.mainloop()
