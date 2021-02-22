import tkinter as tk
from tkinter import *
from tkinter import ttk
import webbrowser
from tkinter import messagebox as msgbox
# import sqlite3 as sq
#from fpdf import FPDF
import datetime
import os

# Graphic User Interface
top = tk.Tk()
top.title('Application')
top.configure(background='white')

color1 = '#%02x%02x%02x' % (5, 36, 67)  # royal_blue
color2 = '#%02x%02x%02x' % (243, 183, 71)  # yellow


def openfb():
    webbrowser.open('https://www.facebook.com/komal.sinha.9275')


# function for home
def home():
    frame2 = Frame(top, bg='white', height=500, width=800)
    l1 = Label(frame2, text=" © 2021 - Komal Sinha", font=("Ubuntu", 12), width=30, bg='white')
    l2 = Label(frame2, text="Language", font=("Ubuntu", 44), width=35, bg='white')
    l3 = Label(frame2, text="Translator", font=("Ubuntu", 44), width=35, bg='white')
    #l4 = Label(frame2, image=inv)
    b5 = Button(frame2, image=fb_btn, command=openfb, borderwidth=0)
    #b6 = Button(frame2, image=twt_btn, command=opentwt, borderwidth=0)
    #b7 = Button(frame2, image=lnk_btn, command=openlnk, borderwidth=0)

    l1.pack()
    l2.pack()
    l3.pack()
    #l4.pack()
    b5.pack()
    #b6.pack()
    #b7.pack()

    l1.place(x=250, y=440)
    l2.place(x=-150, y=30)
    l3.place(x=-155, y=100)
    #l4.place(x=280, y=180)
    b5.place(x=330, y=460)
    #b6.place(x=370, y=460)
    #b7.place(x=410, y=460)

    frame2.pack()
    frame2.place(x=200, y=0)




    ##code for cancel buttton
    def cancel():
        top1.destroy()

    inv_type = ['--------------Select------------------', 'Tax_Invoice', 'Retail_Invoice']
    top1 = Toplevel()
    top1.title('Generate Invoice')
    top1.configure(bg='white')
    l5 = Label(top1, text="Invoice", font=("Ubuntu", 16), bg='white', fg=color1)
    l6 = Label(top1, text="Name:", font=("Ubuntu", 12), bg='white', fg=color1)
    l7 = Label(top1, text="Date:", font=("Ubuntu", 12), bg='white', fg=color1)
    l8 = Label(top1, text="Invoice Type:", font=("Ubuntu", 12), bg='white', fg=color1)
    l9 = Label(top1, text="Description:", font=("Ubuntu", 12), bg='white', fg=color1)
    l10 = Label(top1, text="Qty:", font=("Ubuntu", 12), bg='white', fg=color1)
    l11 = Label(top1, text="Amount:", font=("Ubuntu", 12), bg='white', fg=color1)
    l12 = Label(top1, text="Contact:", font=("Ubuntu", 12), bg='white', fg=color1)
    l13 = Label(top1, text="Email:", font=("Ubuntu", 12), bg='white', fg=color1)
    b8 = Button(top1, text="Submit", command='', font=("Ubuntu", 12), height=1, width=10, fg='white', bg=color1,
                relief=GROOVE)
    b9 = Button(top1, text="Cancel", command=cancel, font=("Ubuntu", 12), height=1, width=10, fg='white', bg=color1,
                relief=GROOVE)
    e1 = Entry(top1, bd=1, width=25)
    e2 = Entry(top1, bd=1, width=25)
    c3 = ttk.Combobox(top1, values=inv_type, width=24)
    e4 = Entry(top1, bd=1, width=25)
    e5 = Entry(top1, bd=1, width=25)
    e6 = Entry(top1, bd=1, width=25)
    e7 = Entry(top1, bd=1, width=25)
    e8 = Entry(top1, bd=1, width=25)
    l5.pack()
    l6.pack()
    l7.pack()
    l8.pack()
    l9.pack()
    l10.pack()
    l11.pack()
    l12.pack()
    l13.pack()
    b8.pack()
    b9.pack()
    e1.pack()
    e2.pack()
    c3.pack()
    e4.pack()
    e5.pack()
    e6.pack()
    e7.pack()
    e8.pack()
    l5.place(x=350, y=5)
    l6.place(x=50, y=50)
    l7.place(x=420, y=50)
    l8.place(x=50, y=110)
    l9.place(x=420, y=110)
    l10.place(x=50, y=170)
    l11.place(x=420, y=170)
    l12.place(x=50, y=230)
    l13.place(x=420, y=230)
    b8.place(x=270, y=300)
    b9.place(x=450, y=300)
    e1.place(x=160, y=50)
    e2.place(x=540, y=50)
    c3.current(0)
    c3.place(x=160, y=110)
    e4.place(x=540, y=110)
    e5.place(x=160, y=170)
    e6.place(x=540, y=170)
    e7.place(x=160, y=230)
    e8.place(x=540, y=230)
    top1.minsize(800, 400)
    top1.resizable(0, 0)
    top1.mainloop()

















# function for exit
def close():
    msg = msgbox.askquestion('Exit Application', 'Are you sure you want to exit the app')
    if msg == 'yes':
        top.destroy()


# Images
fb_btn = PhotoImage(file='facebook.png')
# twt_btn = PhotoImage(file='twitter.png')
# lnk_btn = PhotoImage(file='linkedin.png')
# inv = PhotoImage(file='inv.png')
# my = PhotoImage(file='settings.png')

# Widgets
l1 = Label(top, text=" © 2021 - Komal Sinha", font=("Ubuntu", 12), width=30, bg='white')
l2 = Label(top, text="Language", font=("Ubuntu", 44), width=35, bg='white')
l3 = Label(top, text="Translator", font=("Ubuntu", 44), width=35, bg='white')
#l4 = Label(top, image=inv)
f1 = Frame(top, bg=color1, bd=2, height=600, width=200)
# f2 = Frame(top, bg='steel blue', bd=2, height=40, width=1000)
# f3 = Frame(top, bg='coral', bd=2, height=30, width=1000)
b1 = Button(top, text="Home", command=home, font=("Ubuntu", 11), height=2, width=20, fg='white', bg=color1,
            relief=GROOVE)

b3 = Button(top, text="Translate", command='', font=("Ubuntu", 11), height=2, width=20, fg='white',
            bg=color1, relief=GROOVE)
b4 = Button(top, text="Exit", command=close, font=("Ubuntu", 11), height=2, width=20, fg='white', bg=color1,
            relief=GROOVE)
b5 = Button(top, image=fb_btn, command=openfb, borderwidth=0)
# b6 = Button(top, image=twt_btn, command=opentwt, borderwidth=0)
# b7 = Button(top, image=lnk_btn, command=openlnk, borderwidth=0)
# l15 = Label(f1, image = my)

# Pack
l1.pack()
l2.pack()
l3.pack()
#l4.pack()
# l15.pack()
f1.pack()
# f2.pack()
# f3.pack()
b1.pack()

b3.pack()
b4.pack()
b5.pack()
#b6.pack()
#b7.pack()

# Place X and Y
l1.place(x=450, y=440)
l2.place(x=50, y=30)
l3.place(x=45, y=100)
#l4.place(x=480, y=180)
# l15.place(x=10,y=5)

f1.place(x=0, y=0)
# f2.place(x=0,y=0)
# f3.place(x=0,y=520)
b1.place(x=3, y=150)
b3.place(x=3, y=220)
b4.place(x=3, y=290)
b5.place(x=530, y=460)
#b6.place(x=570, y=460)
#b7.place(x=610, y=460)

top.minsize(1000, 500)
top.resizable(0, 0)
top.mainloop()