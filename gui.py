from tkinter import *
from turtle import bgcolor

ishika = Tk()
label1 = Label(text = "Name: ", 
               font = "Helvetica 24 italic underline", 
               fg = 'black', 
               bg = 'pink', 
               padx = 50, 
               pady = 50).grid(row = 0, column = 0)
#label1.pack(anchor = 'nw')
ishika.title("GUI project")
ishika.geometry("1660x1040")
ishika.configure(bg = 'pink')
veer = Entry(label1, text = 'shinchan, nobita').grid(row = 0, column = 1)
button1 = Button(label1, text ='click me').grid(row = 3, column = 1)



ishika.mainloop()