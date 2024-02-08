from tkinter import *
from tkinter.font import BOLD  
import mysql.connector as my
from tkinter import messagebox
def cricket1():
    def action():
        try:
            con=my.connect(host='localhost',
                   user='root',
                   passwd='',
                   database='abc' )
            cur=con.cursor()
            cur.execute("UPDATE cricket_stock SET Bat=Bat+'"+name.get()+"', Ball=Ball+'"+email1.get()+"', Stumps=Stumps+'"+email.get()+"', Helmet=Helmet+'"+email2.get()+"'")
            con.commit()
            messagebox.showinfo("Success" , "Registration Successfull" , parent = crickstaffwin)
        except Exception as ez:
                messagebox.showerror("Error" , f"Error Due to : {str(ez)}", parent = crickstaffwin) 
                
        
    crickstaffwin  = Tk()
    crickstaffwin.title("cricket stock update")
    crickstaffwin.geometry("600x250")
    crickstaffwin.config(bg="black")
    label_bat = Label(crickstaffwin, text="update quantity of bats",font="Helvetica  12",bg="black",fg="white")
    name = Entry(crickstaffwin,width=30,font="Helvetica  12",textvariable=IntVar())
    label_bat.place(x=20, y=20)
    name.place(x=220, y=20)

    label_ball = Label(crickstaffwin,text="update quantity of balls",font="Helvetica  12",bg="black",fg="white")
    email1 = Entry(crickstaffwin,width=30,font="Helvetica  12",textvariable=IntVar())
    label_ball.place(x=20,y=60)
    email1.place(x=220,y=60)

    label_stumps = Label(crickstaffwin,text="update quantity of stumps",font="Helvetica  12",bg="black",fg="white")
    email = Entry(crickstaffwin,width=30,font="Helvetica  12",textvariable=IntVar())
    label_stumps.place(x=20,y=100)
    email.place(x=220,y=100)

    label_helmet = Label(crickstaffwin,text="update quantity of helmet",font="Helvetica  12",bg="black",fg="white")
    email2 = Entry(crickstaffwin,width=30,font="Helvetica  12",textvariable=IntVar())
    label_helmet.place(x=20,y=140)
    email2.place(x=220,y=140)

    btn=Button(crickstaffwin,text="Update",fg="white",bg="black",height=1,width=6,font=("Helvetica",12,BOLD),command=action)
    btn.place(x=240,y=180)

    btn1=Button(crickstaffwin,text="Back",fg="white",bg="black",height=1,width=6,font=("Helvetica",12,BOLD))
    btn1.place(x=350,y=180)

    crickstaffwin.mainloop()