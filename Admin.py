import mysql.connector as my
from tkinter import *
from tkinter import messagebox
from stock import *


def connect():
    con=my.connect(host='localhost',
                   user='root',
                   passwd='',
                   database='abc' )
    return con

def emploginfunc():
    def switch():
        staff.destroy()
    def action():
       if lempid.get()=="" or password.get()=="":
            messagebox.showerror("Error",parent=staff)
       else:
            try:
                con=connect()
                cur=con.cursor()
                cur.execute("select * from employee where empid=%s and password=%s",(lempid.get(),password.get()))
                row=cur.fetchone()
                if row==None:
                    messagebox.showerror("Error" , "Invalid ID And Password", parent = staff)
                else:
                    messagebox.showinfo("Success" , "Successfully Login" , parent = staff)
                    b=Buy()
                    
                    switch()
                    
                    
                con.close()
            except Exception as ez:
                messagebox.showerror("Error" , f"Error Due to : {str(ez)}", parent = staff)
    staff=Tk()
    staff.title("signup")
    staff.config(background="black")
    staff.geometry("500x400")
    staff.resizable(0,0)
    eusname=Label(staff,text="Enter EMP ID:",font=("Helvetica",15),fg="white",bg="black")
    eusname.place(x=30,y=30)
    lempid=Entry(staff,textvariable=StringVar(),font=("Helvetica",12))
    lempid.place(x=200,y=30,height=30,width=200)
    epw=Label(staff,text="Enter password :",font=("Helvetica",15),fg="white",bg="black")
    epw.place(x=30,y=100)
    password=Entry(staff,textvariable=StringVar(),font=("Helvetica",12),show="*")
    password.place(x=200,y=100,height=30,width=200)
    logg=Button(staff, text = "Login" ,font='Helvetica 10 bold', command = action)
    logg.place(x=180,y=210)
    back=Button(staff, text = "back to customer login" ,font='Helvetica 10 bold', command = switch)
    back.place(x=180,y=290)