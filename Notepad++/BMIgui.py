# -*- coding: utf-8 -*-

from Tkinter import *
from ttk import *

root = Tk()
root.title(u"計算 BMI 程式")

bmimessage = StringVar()
bmimessage.set(u"請輸入身高、體重")

def bmi():
	h = float(hentry.get())
	w = float(wentry.get())
	value = w / (h**2)
	bmist = "%.2f" %(value)
	m = "你的 BMI 是" + bmist + "。"
	bmimessage.set(m)

hlabel = Label(root, text = u"身高 (m)")
hlabel.grid(row=0, column=0, sticky=W)

hentry = Entry(root)
hentry.grid(row=0, column=1)

wlabel = Label(root, text = u"體重 (kg)")
wlabel.grid(row=1, column=0, sticky=W)

wentry = Entry(root)
wentry.grid(row=1, column=1)

b = Button(root, text = u"計算 BMI", command = bmi)
b.grid(row=2,column=1, sticky=E)

message = Label(root, textvariable = bmimessage)
message.grid(row=3, column=0, rowspan=2)

root.mainloop()

