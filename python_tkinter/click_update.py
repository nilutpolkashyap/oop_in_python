# -*- coding: utf-8 -*-
"""
Created on Tue Sep  7 19:05:48 2021

@author: nkele
"""

import tkinter
import time

def update_the_label():
    updated_text = time.strftime("The GM time now is %H:%M:%S.", time.gmtime())
    w.configure(text = updated_text)

root = tkinter.Tk()
root.geometry("400x400")
w = tkinter.Label(root, text = "Hello, world!")
b = tkinter.Button(root, text = "Update the label", command = update_the_label)
w.pack()
b.pack()

root.mainloop()     



from tkinter import *
import datetime

root = Tk()

lab = Label(root)
lab.pack()

def clock():
    time = datetime.datetime.now().strftime("Time: %H:%M:%S")
    lab.config(text=time)
    #lab['text'] = time
    root.after(1000, clock) # run itself again after 1000 ms

# run first time
clock()

root.mainloop()