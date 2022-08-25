import tkinter as tk

root = tk.Tk()
root.title("https://www.youtube.com/")
root.geometry("10000x8000000000000000000000")
lb1=tk.Label(text="はじめしゃちょー(hajime)(非公式)")
bt1=tk.Button(text="何もならない")
lb1.pack()
bt1.pack()

def action_btn_press():
    print("うんこ太郎があなたのチャンネルを登録しました。")
    

bt=tk.Button(text="チャンネル登録",command=action_btn_press)


bt.pack()

def get_textvalue():
    val_en=en.get()
    print(val_en)

lb

root.mainloop()



