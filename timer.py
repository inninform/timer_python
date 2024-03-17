import time
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import tkinter.messagebox
program = Tk()
program.title("timer")
program.geometry("200x140")
enter = ttk.Entry(program)
enter.pack()
btn = ttk.Button(program,text="enter")
btn.pack()
lbl = Label(program,text="")
lbl.pack(pady=20)
count = ttk.Button(program,text="start")
count.pack()
def ent():
    num = int(enter.get())
    lbl.config(text=num)
btn.config(command=ent)
def tim():
    om = int(enter.get())
    tn = abs(int(om))
    while tn > -1:
        s = tn
        print(s)
        lbl.config(text=s)
        time.sleep(1)
        tn -= 1
    tkinter.messagebox.showinfo(message="it's completed")

count.config(command=tim)
program.mainloop()