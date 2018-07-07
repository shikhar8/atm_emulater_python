import tkinter as tk
from tkinter import messagebox as mb
from tkinter import *

a = []
b = 0
n = 0


class sampleapp(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        container = Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)
        self.frames = {}
        for i in (homepage, pageone, pagetwo, pagethree):
            pagename = i.__name__
            frame = i(parent=container, controller=self)
            self.frames[pagename] = frame
            print(self.frames)
        self.show_frame('homepage')
    def show_frame(self, pname):
        frame = self.frames[pname]
        frame.tkraise()
        frame.grid(row=0, column=0, sticky="nsew")
class homepage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.config(height=20, width=100)
        label = tk.Label(self, text="WELCOME TO XYZ BANK", fg='blue', bg='white')
        label.config(font=("Courier", 20), height=5, width=40, padx=10, pady=10)
        label.grid(row=1, column=0)
        label.pack(pady=10, padx=10)
        button1 = tk.Button(self, text='CREATE NEW ACCOUNT', command=lambda: controller.show_frame("pageone"), bd=5)
        button1.config(font=('Courier', 10), height=1, width=20, padx=10, pady=10)
        button2 = tk.Button(self, text='CASH WITHDRAWL', command=lambda: controller.show_frame("pagetwo"), bd=5)
        button2.config(font=('Courier', 10), height=1, width=20, padx=10, pady=10)
        button1.pack(pady=8)
        button2.pack(pady=8)
        label2 = Label(self, text="")
        label2.config(height=5, width=40)
        label2.pack()
class pageone(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        lframe = Frame(self)
        lframe.pack(side=LEFT)
        l1 = Label(lframe, text='account number', bg='light blue')
        l1.config(font=('Courier', 10), height=1, width=40)
        l1.grid(row=1, column=0, padx=8, pady=8)
        l2 = Label(lframe, text='username', bg='light blue')
        l2.config(font=('Courier', 10), height=1, width=40)
        l2.grid(row=2, column=0, padx=8, pady=8)
        l3 = Label(lframe, text='userpin', bg='light blue')
        l3.config(font=('Courier', 10), height=1, width=40)
        l3.grid(row=3, column=0, padx=8, pady=8)
        l4 = Label(lframe, text='cash amount', bg='light blue')
        l4.config(font=('Courier', 10), height=1, width=40)
        l4.grid(row=4, column=0, padx=8, pady=8)
        rframe = Frame(self)
        rframe.pack(side=RIGHT)
        e1 = Entry(rframe, bd=8)
        e1.config(width=40)
        e1.grid(row=4, column=0)
        e2 = Entry(rframe, bd=8)
        e2.config(width=40)
        e2.grid(row=6, column=0)
        e3 = Entry(rframe, bd=8)
        e3.config(width=40)
        e3.grid(row=7, column=0)
        e4 = Entry(rframe, bd=8)
        e4.config(width=40)
        e4.grid(row=8, column=0)
        bframe = Frame(self)
        bframe.pack(side=BOTTOM)
        def createaccount():
            import sqlite3
            db = sqlite3.connect('ATM3')
            cur = db.cursor()
            try:
                cur.execute(
                    '''CREATE TABLE ATM3(accountnumber TEXT PRIMARY KEY,username TEXT,userpin TEXT,balance INT)''')
            except:
                pass
            try:
                d = []
                from tkinter import messagebox as mb
                print(e1.get())
                d.append(e1.get())
                d.append(e2.get())
                d.append(e3.get())
                d.append(int(e4.get()))
                for i in d:
                    if i == '':
                        mb.showwarning('failure', "all entry should be filled")
                        controller.show_frame('homepage')
                if cur.execute('''INSERT INTO ATM3(accountnumber,username,userpin,balance) VALUES(?,?,?,?)''',
                               (d[0], d[1], d[2], d[3])):
                    mb.showinfo('success', 'account created succesfully')
            except:
                mb.showwarning('failure', "invalid entry please try again")
            db.commit()
            controller.show_frame('homepage')
        b1 = Button(bframe, text='create account', command=createaccount)
        b1.config(font=('Courier', 10), height=1, width=15)
        b1.grid(row=1, column=0, padx=8, pady=10)
        b2 = Button(bframe, text='exit', command=controller.quit)
        b2.config(font=('Courier', 10), height=1, width=15)
        b2.grid(row=1, column=1, padx=8, pady=10)
class pagetwo(tk.Frame):
    global a
    global b

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        lframe = Frame(self)
        lframe.pack(side=LEFT)
        rframe = Frame(self)
        rframe.pack(side=RIGHT)
        bframe = Frame(self)
        bframe.pack(side=BOTTOM)
        l1 = Label(lframe, text='account number', bg='pink')
        l1.config(font=('Courier', 20), height=1, width=18)
        l1.grid(row=1, column=0, padx=10, pady=6)
        l2 = Label(lframe, text='userpin', bg='pink')
        l2.config(font=('Courier', 20), height=1, width=18)
        l2.grid(row=2, column=0, padx=10, pady=6)
        e1 = Entry(rframe, bd=10)
        e1.config(width=35)
        e2 = Entry(rframe, bd=10)
        e2.config(width=35)
        def gm():
            d = []
            d.append(e1.get())
            d.append(e2.get())
            import sqlite3
            db = sqlite3.connect('ATM3')
            cur = db.cursor()
            cur.execute('''SELECT * FROM ATM3 WHERE accountnumber=? AND userpin=?  ''', (d[0], d[1]))
            a.append(cur.fetchone())
            print(a)
            print()
            if a[-1] != None:
                controller.show_frame('pagethree')
            else:
                mb.showwarning('sorry', 'wrong username password')
                controller.show_frame('homepage')
        b1 = Button(bframe, text='submit', command=gm, bg='light blue')
        e1.grid(row=0, column=1)
        e2.grid(row=1, column=1)
        b1.config(font=('Courier', 20), height=1, width=20)
        b1.grid(row=1, column=1, padx=10, pady=10)
class pagethree(tk.Frame):
    global a
    global b
    global n

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label1 = Label(self, text='WELCOME', bg='light blue')
        label1.config(font=('Courier', 25), height=4, width=40)
        label1.pack()
        label2 = Label(self, text='enter transaction amount')
        label2.config(font=('Courier', 15), height=2, width=40)
        label2.pack()
        entry = Entry(self, bd=6)
        entry.config(width=20)
        def withdraw():
            global n
            if n == 0:
                b = int(entry.get())
                # controller.show_frame('pagefour')
                am = b
                import sqlite3
                db = sqlite3.connect('ATM3')
                cur = db.cursor()
                print(a)
                if b % 50 == 0 and b<a[0][-1]:
                    x = {}
                    x[1000] = int((am / 1000))
                    am = am % 1000
                    x[500] = int((am / 500))
                    am = am % 500
                    x[100] = int(((am / 100)))
                    am = am % 100
                    x[50] = int(((am / 50)))
                    for i, j in x.items():
                        ae = [str(i), "*", str(j), "=", str(i * j)]
                        ae = ''.join(ae)
                        l1 = Label(self, text=ae)
                        l1.config(font=('Courier', 10), height=1)
                        l1.pack()
                    ae1 = ['total amount=', str(b)]
                    ae1 = ''.join(ae1)
                    l2 = Label(self, text=ae1)
                    l2.config(font=('Courier', 10), height=1)
                    l2.pack()
                    l3 = Label(self, text='Thank you for using HPES Bank')
                    l3.config(font=('Courier', 10), height=1)
                    l3.pack()
                    c = int((a[0][-1] - b))
                    cur.execute('''UPDATE ATM3 SET balance=? WHERE accountnumber=?''', ((c), (a[0][0])))
                    db.commit()
                    cur.execute('SELECT * FROM ATM3 WHERE accountnumber=?', (a[0][0],))
                    z = cur.fetchall()
                    print(z)
                    ae2 = ['balance left', str(z[0][-1])]
                    ae2 = ''.join(ae2)
                    l4 = Label(self, text=ae2)
                    l4.config(font=('Courier',10),height=1)
                    l4.pack()
                    n += 1
                elif b%50!=0:
                    mb.showwarning('transaction failed', 'amount should be in multiple of 50')
                elif b>a[0][-1]:
                    mb.showwarning('transaction failed','amount entered is more than available balance')

        button1 = Button(self, text='click here to withdraw cash', command=withdraw, bg='yellow')
        button1.config(font=('Courier', 10), height=2, width=30)
        entry.pack()
        label3 = Label(self)
        label3.config(font=('Courier', 15), width=40)
        label3.pack()
        button1.pack()            
obj = sampleapp()
obj.mainloop()
