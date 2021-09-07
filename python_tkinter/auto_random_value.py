# -*- coding: utf-8 -*-
"""
Created on Tue Sep  7 22:29:12 2021

@author: nkele
"""

import tkinter
import datetime
import random

root = tkinter.Tk()
root.geometry("400x200")

lab = tkinter.Label(root)
lab.pack()

def clock():
    # time = datetime.datetime.now().strftime("Time: %H:%M:%S")
    time = random.uniform(70, 100)
    lab.config(text=time)
    #lab['text'] = time
    root.after(1000, clock) # run itself again after 1000 ms

# run first time
clock()

root.mainloop()
