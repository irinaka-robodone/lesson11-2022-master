import tkinter as tk
import tkinter.scrolledtext as tksc
import tkinter.ttk as  ttk

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
root.title("実験")
root.geometry("800x300")

stavar=tk.StringVar()
stavar.set(["北海道","東方","関東","中部","近畿","中国","四国","九州＿沖縄"])

boolvar=tk.BooleanVar()

frame=tk.LabelFrame(root,text="ラベルフレーム",foreground="black",labelanchor="n")

tx=tk.Text(height=5,width=100)
tx.pack()
tx.focus_set()

intvar=tk.IntVar()
intvar.set(0)

lb_risubo=tk.Listbox(root,listvariab=stavar,selectmode="multiple",height=5)

ct1=tk.Checkbutton(text="チェックボックス",variable=boolvar)
bt2=tk.Button(text="判定",command=get_check_two)
rb1=tk.Radiobutton(frame,text="ラジオボタン１",value=1,variable=intvar)
rb2=tk.Radiobutton(frame,text="ラジオボタン２",value=2,variable=intvar)
rb3=tk.Radiobutton(frame,text="ラジオボタン３",value=3,variable=intvar)
bt_risubo=tk.Button(text="選択値を出力",command=get_listitems)

#lb=tk.Label(text="ラベル")
en=tk.Entry(text="入力")
bt=tk.Button(text="ボタン",command=get_textvalue)

#lb.pack()
en.pack()
en.focus_set()
bt.pack()

frame.pack()
ct1.pack()
bt2.pack()
rb1.pack()
rb2.pack()
rb3.pack()
lb_risubo.pack()
bt_risubo.pack()

sc=tksc.ScrolledText(height=5,width=100)
sc.pack()
sc.focus_set()

root.mainloop()
