from tkinter import *
form1 = Tk()
label1 = Label(text = 'Name: ', 
               fg = 'black',
               bg = 'cyan',
               padx = 20,
               pady = 50,
               font = 'OpenSans 16').grid(row = 0, column = 0)
form1.geometry('1660x1040')
form1.configure(bg = 'cyan')
text_box = Entry(label1).grid(row = 0, column = 1)
label2 = Label(text = 'Password: ', 
               fg = 'black',
               bg = 'cyan',
               padx = 20,
               pady = 50,
               font = 'OpenSans 16').grid(row = 1, column = 0)
form1.geometry('1660x1040')
form1.configure(bg = 'cyan')
text_box2 = Entry(label2).grid(row = 1, column = 1)
form1.mainloop() 
