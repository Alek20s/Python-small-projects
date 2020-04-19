from tkinter import *
import tkinter.messagebox as box

window = Tk()
window.title('Entry Example- Successfull Learning Python')

frame = Frame(window)
entry = Entry(frame)

def dialog():
    box.showinfo('Greetings', 'Welcome  ' + entry.get()+ '. How are you?')

btn = Button(frame, text = 'Enter Name', command = dialog)
btn.pack(side =RIGHT, padx =15)
entry.pack(side = LEFT)
frame.pack(padx =50, pady =40)

window.mainloop()


    
    