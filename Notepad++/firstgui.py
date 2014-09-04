# -*- coding: utf-8 -*-

from Tkinter import *
from ttk import *
import webbrowser
from random import *

root = Tk()
root.title(u"我的第一個GUI")


s = StringVar()
s.set("*")

def go():
	r = randint(1,51)
	s.set(str(r))

def go2():
    webbrowser.open("http://nbviewer.ipython.org/github/c3h3/NCCU-PyData-Courses-2013Spring/blob/master/Lecture1/crawler/Lecture2_WebCrawler.ipynb")



mypic = PhotoImage(file = "boyya.gif")
showpic = Label(root, image = mypic)
showpic.pack()

myLabel = Label(root, text = u"請按鈕:")
myLabel.pack()

b = Button(root, text = u"打開神秘網頁...", command = go)
b.pack()

root.mainloop()