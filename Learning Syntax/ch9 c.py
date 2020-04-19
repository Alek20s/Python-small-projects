# -*- coding: utf-8 -*-
"""
Created on Sun Feb 16 19:32:16 2020

@author: Aleks
"""

from tkinter import *
import tkinter.messagebox as box

window =Tk()
window.title('Message Box Example')

def dialog():
    var = box.askyesno('Message Box', 'Proceed?')
    if var == 1:
        box.showinfo( 'Yes Box', 'Prcoceedding...')
    else:
        box.showwarning('No Box', 'Canceling...')
btn = Button(window, text= 'Click', command = dialog)
btn.pack(padx =150, pady = 50)
window.mainloop()




        
        
        









