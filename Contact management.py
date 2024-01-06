from tkinter import *
from tkinter import messagebox
from db import Database
d1 = Database('C:/Users/Public/Documents/contacts.db')
win = Tk()
win.geometry('800x400')
win.title('Contacts')
win.configure(bg = '#75ACEF')
win.resizable(0 , 0)
def populate():
    list1.delete(0 , END)
    a = d1.fetch()
    for i in a:
        list1.insert(END , i)
def clear():
    e1.delete(0 , END)
    e2.delete(0 , END)
    e3.delete(0 , END)
    e4.delete(0 , END)
def insert():
    if e1.get() == '' or e2.get() == '' or e3.get() == '' or e4.get() == '':
        messagebox.showwarning('Warning' , 'Pleas fill all blanks')
        clear()
    else:
        d1.insert(e1.get() , e2.get() , e3.get() , e4.get())
        list1.insert(END , f'{d1.cur.lastrowid} {e1.get()} {e2.get()} ({e3.get()}) : {e4.get()}')
        clear()
def close():
    x = messagebox.askyesno('Warning' , 'Are you sure to exit ?')
    if x == True:
        win.destroy()
def delete():
    b = list1.curselection()
    c = list1.get(b)
    d1.remove(int(c[0]))
    populate()
def update():
    d = list1.curselection()
    e = list1.get(d)
    d1.update(int(e[0]), e1.get(), e2.get(), e3.get(), e4.get())
    populate()
    messagebox.showinfo('Contacts' , 'sucssufuly updated')
    clear()
def search():
    if e4.get() != '':
        a = list(d1.search_phone(str(e4.get())))
        clear()
        e1.insert(0 , a[1])
        e2.insert(0 , a[2])
        e3.insert(0 , a[3])
        e4.insert(0 , a[4])
    
    else:
        messagebox.showwarning('Warning!' , "you can only search phone number")

l1 = Label(win , text = 'name :' , bg = '#75ACEF' , fg = '#000000' , font = '30')
l1.place(x = 130 , y = 80)
l2 = Label(win , text = 'last name :' , bg = '#75ACEF' , fg = '#000000' , font = '30')
l2.place(x = 130 , y = 110)
l3 = Label(win , text = 'adress :', bg = '#75ACEF' , fg = '#000000' , font = '30')
l3.place(x = 130 , y = 140)
l4 = Label(win , text = 'phone :', bg = '#75ACEF' , fg = '#000000' , font = '30')
l4.place(x = 130 , y = 170)
e1 = Entry(win , font = '30')
e1.place(x = 180 , y = 80)
e2 = Entry(win , font = '30')
e2.place(x = 210 , y = 110)
e3 = Entry(win , font = '30')
e3.place(x = 190 , y = 140)
e4 = Entry(win , font = '30')
e4.place(x = 185 , y = 170)
b1 = Button(win , text = 'insert' , font = '30'  , command = insert)
b1.place(x = 180 , y = 250)
b2 = Button(win , text = 'show list' , font = '30'  , command = populate)
b2.place(x = 170 , y = 210)
b3 = Button(win , text = 'delete' , font = '30' , command = delete)
b3.place(x = 260 , y = 250)
b4 = Button(win , text = "exit" , font = '10' , command = close)
b4.place(x = 185 , y = 290)
b5 = Button(win , text = 'update' , font = '30' , command = update)
b5.place(x = 260 , y = 210)
b6 = Button(win , text = "search" , font = '10' , command = search)
b6.place(x = 257 , y = 290)
list1 = Listbox(win , width = 60 , height = 12)
list1.place(x = 410 , y = 60)
win.mainloop()
