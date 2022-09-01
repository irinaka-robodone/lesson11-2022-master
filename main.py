import tkinter as tk
root = tk.Tk()
def osareta ():
    val_en=en.get()
    print(val_en)
    en.delete(0,tk.END)

root.title("             たいとるです")
root.geometry("800x300")
id = tk.Label(text="ラベル")
en = tk.Entry(text="入力")
bt = tk.Button(text="ボタン",command=osareta)

id.pack()
en.pack()
en.focus_set()
bt.pack()

root.mainloop()
