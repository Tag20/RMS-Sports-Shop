import mysql.connector as my
from tkinter import *
from tkinter import messagebox
from Admin import emploginfunc
from customer import *
def clear():
    lusername.delete(0,END)
    password.delete(0,END)

def close():
    win.destroy()

def connect():
    con=my.connect(host='localhost',
                   user='root',
                   passwd='',
                   database='abc' )
    return con


def loginfunc():
    if lusername.get()=="" or password.get()=="":
        messagebox.showerror("Error",parent=win)
    else:
        try:
            con=connect()
            cur=con.cursor()
            logu=lusername.get()
            logpass=password.get()
            cur.execute("select * from customers where username=%s and password=%s",(lusername.get(),password.get()))
            row=cur.fetchone()
            if row==None:
                messagebox.showerror("Error" , "Invalid User Name And Password", parent = win)
            else:
                messagebox.showinfo("Success" , "Successfully Login" , parent = win)
                c=Customer
                close()
                c1=stock()
            con.close()
        except Exception as ez:
            messagebox.showerror("Error" , f"Error Due to : {str(ez)}", parent = win)
            

def signupfunc():
    def action():
        if username.get()=="" or email.get()=="" or phone.get()=="" or passw.get()=="":
            messagebox.showerror("Error" , "All Fields Are Required" , parent = winsignup)
        elif passw.get()!=rpassw.get():
            messagebox.showerror("Error" , "Password & Confirm Password Should Be Same" , parent = winsignup)
        else:
            try:
                con=connect()
                cur=con.cursor()
                
                print("gg")
                x=1
                if x==0:
                    messagebox.showerror("Error" , "User Name Already Exits", parent = winsignup)
                else:
                    cur.execute("insert into customers(username,email,phone,password) values(%s,%s,%s,%s)",
                                (
                                    username.get(),email.get(),phone.get(),passw.get()
                                ))
                    con.commit()
                    con.close()
                    messagebox.showinfo("Success" , "Registration Successfull" , parent = winsignup)
                    clear()
                    switch()
            except Exception as ez:
                messagebox.showerror("Error" , f"Error Due to : {str(ez)}", parent = winsignup)    
    def switch():
        winsignup.destroy()
    
    def clear():
        username.delete(0,END)
        email.delete(0,END)
        phone.delete(0,END)
        passw.delete(0,END)
    
    winsignup=Tk()
    winsignup.title("signup")
    winsignup.config(background="black")
    winsignup.geometry("640x480")
    winsignup.resizable(0,0)

    username=StringVar()
    ename=Label(winsignup,text="Enter Username:",font=("Helvetica",15),fg="white",bg="black")
    ename.place(x=30,y=30)
    username=Entry(winsignup,textvariable=username,font=("Helvetica",12))
    username.place(x=200,y=30,height=30,width=200)

    eemail=Label(winsignup,text="Enter Email ID:",font=("Helvetica",15),fg="white",bg="black")
    eemail.place(x=30,y=90)
    email=Entry(winsignup,textvariable=StringVar(),font=("Helvetica",12))
    email.place(x=200,y=90,height=30,width=200)

    ephone=Label(winsignup,text="Contact number :",font=("Helvetica",15),fg="white",bg="black")
    ephone.place(x=30,y=150)
    phone=Entry(winsignup,textvariable="",font=("Helvetica",12))
    phone.place(x=200,y=150,height=30,width=200)

    epw=Label(winsignup,text="Enter password :",font=("Helvetica",15),fg="white",bg="black")
    epw.place(x=30,y=210)
    passw=Entry(winsignup,textvariable=StringVar(),font=("Helvetica",12),show="*")
    passw.place(x=240,y=210,height=30,width=200)
    erpw=Label(winsignup,text="Re-enter password :",font=("Helvetica",15),fg="white",bg="black")
    erpw.place(x=30,y=270)
    rpassw=Entry(winsignup,textvariable=StringVar(),font=("Helvetica",12),show="*")
    rpassw.place(x=240,y=270,height=30,width=200)
    
    signupp=Button(winsignup, text = "Signup" ,font='Helvetica 10 bold', command = action)
    signupp.place(x=180,y=410)
    
    btn_login = Button(winsignup, text = "Clear" ,font='Helvetica 10 bold' , command = clear)
    btn_login.place(x=300, y=410)
    
    sign_up_btn = Button(winsignup , text="Switch To Login" , command = switch )
    sign_up_btn.place(x=450 , y =20)
    
    
    winsignup.mainloop()
    
con=connect()
mycur=con.cursor()
mycur.execute("CREATE TABLE if not exists customers (username VARCHAR(255),email VARCHAR(255),phone VARCHAR(255), password VARCHAR(255))")
mycur.execute("CREATE TABLE if not exists Employee (empid VARCHAR(255), password VARCHAR(255))")
mycur.execute("CREATE TABLE if not exists Cricket_stock (Bat INT,Ball INT,Stumps INT,Helmet INT)")
mycur.execute("CREATE TABLE if not exists Football_stock (Ball INT,Gloves INT,Studs INT,Shinpads INT)")
mycur.execute("CREATE TABLE if not exists Tennis_stock (Racket INT,Ball INT,Net INT)")

win=Tk()
win.title("SPORTSHUB")
win.config(background="black")
win.geometry("640x480")
#bg = PhotoImage(file = r"C:\Users\rhythm rambhia\Desktop\sportshub.png")
win.resizable(0,0)


eusname=Label(win,text="Enter Username:",font=("Helvetica",15),fg="white",bg="black")
eusname.place(x=30,y=30)


lusername=Entry(win,textvariable=StringVar(),font=("Helvetica",12))
lusername.place(x=200,y=30,height=30,width=200)


epw=Label(win,text="Enter password :",font=("Helvetica",15),fg="white",bg="black")
epw.place(x=30,y=100)


password=Entry(win,textvariable=StringVar(),font=("Helvetica",12),show="*")
password.place(x=200,y=100,height=30,width=200)


btn_login = Button(win, text = "Login" ,font='Helvetica 10 bold',command = loginfunc)
btn_login.place(x=200, y=200)

btn_login = Button(win, text = "Clear" ,font='Helvetica 10 bold', command = clear)
btn_login.place(x=260, y=200)

sign_up_btn = Button(win , text="Switch To Sign up" , command = signupfunc )
sign_up_btn.place(x=500 , y =400)

adminlog = Button(win , text="Switch To Staff login" , command = emploginfunc )
adminlog.place(x=500 , y =350)


win.mainloop()