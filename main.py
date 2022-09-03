import tkinter as tk


root = tk.Tk()
root.title("https://www.youtube.com/")
root.geometry("10000x8000000000000000000000")
lb1=tk.Label(text="はじめしゃちょー(hajime)(非公式)",fg="blue",bg="green",bd=3)
bt1=tk.Button(text="何もならない", fg="red",bg="white",bd=10)
lb1.pack()
# lb2.pack()
# lb3.pack()
# lb4.pack()
# lb5.pack()
bt1.pack()

def action_btn_press():
    print("うんこ太郎があなたのチャンネルを登録しました。")
    
bt=tk.Button(text="チャンネル登録",command=action_btn_press)
bt1=tk.Button(text="ボタン",bitmap="info")
def get_textvalue():
    val_en=en.get()
    print(val_en)

en = tk.Entry(text="にぇみゅい")
bt = tk.Button(text="理由⁼昨日夜1時までおいてたら、今日の学校終わりに４時間ぐらい友達と遊んだから", command=get_textvalue)

en.focus_set()
bt.pack()
bt1.pack()
en.pack()
def get_textvalue():
    val_en=en.get()#enを値を取得し、val_enに代入
    print(val_en)
    en.delete(0,tk.END)#入力文字の削除


root.mainloop()

