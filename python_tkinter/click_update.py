

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



