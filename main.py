from struct import pack
import tkinter as tk
import tkinter.scrolledtext as tksc
import tkinter.ttk as  ttk

def get_spinbox():
    print(var_spinbox.get())

def get_comb():
    print(comb.get())

def get_listitems():
    print(lb_risubo.curselection())


def get_check():
    if boolvar.get():
        print("読み込み済み")
    else:
        print("読み込み中")

def get_check_two():
    print(intvar.get())

def get_textvalue():
    val_en=en.get()
    print(val_en)
    en.delete(0,tk.END)

def action_btn_press():
    print("ボタンを押すな")

root = tk.Tk()
root.title("アンケート調査")
root.geometry("800x300")


lb1=tk.Label(text="あなた方はきのこの山とたけのこの里どちらは？")
lb2=tk.Label(text="どの位好き？")
lb3=tk.Label(text="なぜ(。´･ω･)?")



var_spinbox=tk.StringVar()
spinbox=tk.Spinbox(root,from_=0,to=100,increment=1,state="readonly",textvariable=var_spinbox)

stavar=tk.StringVar()

comb=ttk.Combobox(root,values=("犬","猫"))


boolvar=tk.BooleanVar()

frame=tk.LabelFrame(root,text="何匹飼っている？",foreground="black",labelanchor="n")

tx=tk.Text(height=5,width=100)
#tx.pack()
tx.focus_set()

intvar=tk.IntVar()
intvar.set(0)

lb_risubo=tk.Listbox(root,listvariab=stavar,selectmode="multiple",height=5)

ct1=tk.Checkbutton(text="チェックボックス",variable=boolvar)
#bt2=tk.Button(text="判定",command=get_check_two)
rb1=tk.Radiobutton(frame,text="0匹",value=0,variable=intvar)
rb2=tk.Radiobutton(frame,text="1匹",value=1,variable=intvar)
rb3=tk.Radiobutton(frame,text="2匹以上",value="？",variable=intvar)
bt_risubo=tk.Button(text="選択値を出力",command=get_listitems)

#lb=tk.Label(text="ラベル")
en=tk.Entry(text="入力")
bt=tk.Button(text="回答",command=get_spinbox)
bt2=tk.Button(text="回答",command=get_comb)
#lb.pack()
#en.pack()
en.focus_set()

lb1.pack()
comb.pack()
bt2.pack()
lb2.pack()
spinbox.pack()
bt.pack()


#ct1.pack()
#bt2.pack()
#rb1.pack()
#rb2.pack()
#rb3.pack()

frame.pack()
#lb_risubo.pack()
#bt_risubo.pack()

lb3.pack()
sc=tksc.ScrolledText(height=5,width=100)
sc.pack()
sc.focus_set()

root.mainloop()
