import random
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox as mbox



def getRandomNum():
    # global rannum
    num1 = int(upper_entry.get())
    num2 = int(lower_entry.get())
    num = random.randint(num1, num2)
    mbox.showinfo("result", f"Number = {num}")
    # mbox.showerror("ldmsa", "sdbfuds jhsavdhjf sjhfvjssbs dwjfjh")
    # rannum = ttk.Label(root, text=f"Number = {num}")
    # rannum.place(x=20, y=200)


root = tk.Tk()
root.geometry("400x200")
upperlabel = ttk.Label(root, text="enter value from : ")
upperlabel.place(x=20, y=0)
upper_entry = ttk.Entry(root)
upper_entry.place(x=20, y=30)
upper_entry.focus()

lowerlabel = ttk.Label(root, text='to : ')
lowerlabel.place(x=20, y=60)

lower_entry = ttk.Entry(root)
lower_entry.place(x=20, y=90)

subnitbtn = ttk.Button(root, text="Generate Random Number", command=getRandomNum)
subnitbtn.place(x=20, y=120)

root.mainloop()