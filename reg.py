import tkinter as tk
from tkinter import *
from tkinter import ttk, messagebox
import sqlite3 as sql

#defining the register button
def register1():
    conn = sql.connect('student.db')
    cursor = conn.cursor()
    #creating a table
    cursor.execute('''
    create table if not exists student
    (
    uucmsno varchar(10),
    name varchar(10),
    course varchar(5),
    sem varchar(5),
    gen varchar(8),
    password varchar(10),
    primary key(uucmsno)
    )
    ''')
    conn.commit()
    print("table created")

    form=tk.Tk()
    form.geometry('1230x530')
    form.title("Register form")

    lblhead=tk.Label(form,text="U15IG22S0062",font=("Arial",16,"bold"),fg="green")
    lblhead.grid(row=0,column=1,sticky=tk.W,padx=10,pady=10)
    #Label and Entry of UUCMSNO
    lbluno=tk.Label(form,text="UUCMS NO",)
    lbluno.grid(row=1,column=0,sticky=tk.W)
    euno=tk.Entry(form,width=40)
    euno.grid(row=1,column=1,sticky=tk.W)

    #Label and Entry of name
    lblname=tk.Label(form,text="NAME    ")
    lblname.grid(row=2,column=0,sticky=tk.W)
    ename=tk.Entry(form,width=40)
    ename.grid(row=2,column=1,sticky=tk.W)

    #Label and Entry of course using optionmenu
    lblcrs=tk.Label(form,text="COURSE   ")
    lblcrs.grid(row=3,column=0,sticky=tk.W)
    ecrs=tk.Entry(form,width=40)
    ecrs=tk.StringVar(form)
    ecrs.set("Select Course     ")
    ecrs_opt=tk.OptionMenu(form,ecrs,"BCA","Bcom","Bsc","BA")
    ecrs_opt.grid(row=3,column=1,padx=10,pady=5,sticky=tk.W)

    #Label and Entry of sem using optionmenu
    lblsem=tk.Label(form,text="SEMESTER     ")
    lblsem.grid(row=4,column=0,sticky=tk.W)
    esem=tk.Entry(form,width=40)
    esem=tk.StringVar(form)
    esem.set("Select Sem")
    esem_opt=tk.OptionMenu(form,esem,"I","II","III","IV","v","VI")
    esem_opt.grid(row=4,column=1,padx=10,pady=5,sticky=tk.W)

    #Label and Entry of gender using radiobutton
    lblgender=tk.Label(form,text="GENDER")
    lblgender.grid(row=5,column=0,sticky=tk.W)

    egen=tk.StringVar()
    egen.set("male")

    egenmale=tk.Radiobutton(form, text="male", variable=egen, value="male")
    egenmale.grid(row=5,column=1,padx=10,pady=5,sticky=tk.W)
    egenfemale=tk.Radiobutton(form, text="female", variable=egen, value="female")
    egenfemale.grid(row=5,column=1,padx=80,pady=5)

    #Label and Entry of password
    lblpas=tk.Label(form,text="PASSWORD")
    lblpas.grid(row=6,column=0,sticky=tk.W)
    epas=tk.Entry(form,width=40,show="*")
    epas.grid(row=6,column=1,sticky=tk.W)

    #save button function
    def save():
        uno=euno.get()
        name=ename.get()
        crs=ecrs.get()
        sem=esem.get() 
        gen=egen.get()
        pas=epas.get()
        cursor.execute('''
        insert into student (uucmsno, name, course, sem, gen, password) values(?,?,?,?,?,?) 
        ''',(uno,name,crs,sem,gen,pas))
        conn.commit()
        messagebox.showinfo("Message","Data Saved Successfully")
        euno.delete(0, END)
        ename.delete(0, END)
        esem.set("Select Sem")
        ecrs.set("Select Course")
        epas.delete(0, END)

    #display button function
    def display():
        # Treeview for displaying data
        tree = ttk.Treeview(form, columns=('UUCMSNO', 'name', 'course', 'sem', 'gender','password'), show='headings')
        tree.heading('UUCMSNO', text='UUCMS No')
        tree.heading('name', text='Name')
        tree.heading('course', text='Course')
        tree.heading('sem', text='Semester')
        tree.heading('gender', text='Gender')
        tree.heading('password', text='Password')
        tree.grid(row=8, column=0, columnspan=3, padx=10, pady=10)
        #fetch data from database
        cursor.execute('select * from student')
        rows=cursor.fetchall()
        for row in rows:
            tree.insert('', END,values=row)
    #save button 
    savebtn=tk.Button(form,text="SAVE",command=save)
    savebtn.grid(row=7,column=1,sticky=tk.W,padx=0,pady=20,ipadx=10,ipady=5)
    #display button
    disbtn=tk.Button(form,text="DISPLAY",command=display)
    disbtn.grid(row=7,column=1,sticky=tk.W,padx=80,pady=20,ipadx=10,ipady=5)

    form.mainloop()
