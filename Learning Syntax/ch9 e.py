# -*- coding: utf-8 -*-
"""
Created on Sun Feb 16 21:56:40 2020

@author: Aleks
"""

from tkinter import *
import tkinter.messagebox as box

window =Tk()
window.title('Listbox Example')

frame = Frame(window)

listbox = Listbox(frame)
listbox.insert(1, 'HTMLS in easy steps')
listbox.insert(2, 'CSS3 in easy steps')
listbox.insert(3, 'JavaScript in easy steps')
listbox.insert(4, 'Python in easy speps')

def dialog():
    box.showinfo('Selection', 'Your Choice:' + listbox.get(listbox.curselection()))

btn = Button(frame, text = 'Choice', command = dialog)

btn.pack(side = RIGHT, padx =5)
listbox.pack(side = LEFT)
frame.pack(padx =30, pady =30)

window.mainloop()










