from tkinter import *
from tkinter.font import BOLD 
import mysql.connector as my
from tkinter import messagebox
def tennisstaff():
    def action():
        try:
            con=my.connect(host='localhost',
                   user='root',
                   passwd='',
                   database='abc' )
            cur=con.cursor()
            cur.execute("UPDATE Tennis_stock SET Racket=Racket+'"+name.get()+"', Ball=Ball+'"+email.get()+"', Net=Net+'"+email1.get()+"'")
            con.commit()
            messagebox.showinfo("Success" , "Registration Successfull" , parent = tennisstaffwin )
        except Exception as ez:
                messagebox.showerror("Error" , f"Error Due to : {str(ez)}", parent = tennisstaffwin ) 
    tennisstaffwin  = Tk()
    tennisstaffwin.title("Tennis stock")
    tennisstaffwin.geometry("600x200")
    tennisstaffwin.config(bg="black")

    label_name = Label(tennisstaffwin, text="update quantity of racket",font="Helvetica  12",bg="black",fg="white")
    name = Entry(tennisstaffwin,width=30,font="Helvetica  12")
    label_name.place(x=20, y=20)
    name.place(x=230, y=20)

    label_email = Label(tennisstaffwin,text="update quantity of balls",font="Helvetica  12",bg="black",fg="white")
    email = Entry(tennisstaffwin,width=30,font="Helvetica  12")
    label_email.place(x=20,y=60)
    email.place(x=230,y=60)

    label_stock = Label(tennisstaffwin,text="update quantity of net",font="Helvetica  12",bg="black",fg="white")
    email1 = Entry(tennisstaffwin,width=30,font="Helvetica  12")
    label_stock.place(x=20,y=100)
    email1.place(x=230,y=100)


    btn=Button(tennisstaffwin,text="update",fg="white",bg="black",height=1,width=6,font=("Helvetica",12,BOLD),command=action)
    btn.place(x=240,y=150)

    btn1=Button(tennisstaffwin,text="Back",fg="white",bg="black",height=1,width=6,font=("Helvetica",12,BOLD),command=action)
    btn1.place(x=350,y=150)

    tennisstaffwin.mainloop()