import tkinter as tk
import tkinter.messagebox as msgbox
from tkinter import *
import sqlite3 as sql
import reg

def loginfrm():
    form=tk.Tk()
    form.geometry('400x400')
    form.title("Login")
    lblhead=tk.Label(form,text="U15IG22S0062",font=("Arial",16,"bold"),fg="green")
    lblhead.grid(row=0,column=1,sticky=tk.W,padx=10,pady=10)

    conn = sql.connect('student.db')
    cursor = conn.cursor()

    #label widget of uucms no
    lbluno=tk.Label(form,text="UUCMS No")
    lbluno.grid(row=1,column=0,sticky=tk.W)
    #entry widget of uucms no
    etuno=tk.Entry(form,width=40)
    etuno.grid(row=1,column=1,padx=10,pady=5)
    #label widget of password
    lblpass=tk.Label(form,text="Password")
    lblpass.grid(row=2,column=0,sticky=tk.W)
    #entry widget of password
    etpass=tk.Entry(form,width=40,show="*")
    etpass.grid(row=2,column=1,padx=10,pady=5)
    
    #function of login button it verify the uucmsno and password
    def verify_login():
        uno=etuno.get()
        pas=etpass.get()
        cursor.execute('select * from student where uucmsno=? and password=?',(uno,pas))
        res=cursor.fetchone()
        if res:
            msgbox.showinfo("message","Login Success")
            etuno.delete(0,END)
            etpass.delete(0,END)
        else:
            msgbox.showerror("message","invalid password or username")
    
    #function of registration button event
    def showreg():
        form.destroy()
        reg.register1()

    #registraion button
    regbtn=tk.Button(form,text="Register",command=showreg)
    regbtn.grid(row=3,column=1,padx=80,pady=5,ipadx=10,ipady=5,sticky=tk.W)

     #login button 
    lgnbtn=tk.Button(form,text="Login",command=verify_login)
    lgnbtn.grid(row=3,column=1,pady=5,ipadx=10,ipady=5,sticky=tk.W)

    form.mainloop()

loginfrm()
