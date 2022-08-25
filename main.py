import tkinter as tk
import tkinter.scrolledtext as tksc

def get_textvalue():
    val_en=en.get()
    print(val_en)
    en.delete(0,tk.END)

def action_btn_press():
    print("ボタンを押すな")

root = tk.Tk()
root.title("実験")
root.geometry("800x300")

tx=tk.Text(height=5,width=100)
tx.pack()
tx.focus_set()

bt1=tk.Button(text="ボタン",bitmap="info",)
bt2=tk.Button(text="ボタン",bitmap="error",)
bt3=tk.Button(text="ボタン",bitmap="hourglass",)
bt4=tk.Button(text="ボタン",bitmap="question")
bt5=tk.Button(text="ボタン",bitmap="warning")

lb=tk.Label(text="ラベル")
en=tk.Entry(text="入力")
bt=tk.Button(text="ボタン",command=get_textvalue)

lb.pack()
en.pack()
en.focus_set()
bt.pack()

bt1.pack()
bt2.pack()
bt3.pack()
bt4.pack()
bt5.pack()

sc=tksc.ScrolledText(height=5,width=100)
sc.pack()
sc.focus_set()

root.mainloop()
