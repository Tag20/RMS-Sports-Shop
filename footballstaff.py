from tkinter import *
from tkinter.font import BOLD  
import mysql.connector as my
from tkinter import messagebox
def footballstaff():
    def action():
        try:
            con=my.connect(host='localhost',
                   user='root',
                   passwd='',
                   database='abc' )
            cur=con.cursor()
            cur.execute("UPDATE Football_stock SET Ball=Ball+'"+name.get()+"', Gloves=Gloves+'"+email.get()+"', Studs=Studs+'"+email1.get()+"', Shinpads=Shinpads+'"+email2.get()+"'")
            con.commit()
            messagebox.showinfo("Success" , "Registration Successfull" , parent = footstaffwin)
        except Exception as ez:
                messagebox.showerror("Error" , f"Error Due to : {str(ez)}", parent = footstaffwin) 

    footstaffwin  = Tk()
    footstaffwin.title("football stock")
    footstaffwin.geometry("600x250")
    footstaffwin.config(bg="black")

    label_name = Label(footstaffwin, text="update quantity of football",font="Helvetica  12",bg="black",fg="white")
    name = Entry(footstaffwin,width=30,font="Helvetica  12")
    label_name.place(x=20, y=20)
    name.place(x=230, y=20)

    label_email = Label(footstaffwin,text="update quantity of gloves",font="Helvetica  12",bg="black",fg="white")
    email = Entry(footstaffwin,width=30,font="Helvetica  12")
    label_email.place(x=20,y=60)
    email.place(x=230,y=60)

    label_stock = Label(footstaffwin,text="update quantity of studs",font="Helvetica  12",bg="black",fg="white")
    email1 = Entry(footstaffwin,width=30,font="Helvetica  12")
    label_stock.place(x=20,y=100)
    email1.place(x=230,y=100)

    label_shin = Label(footstaffwin,text="update quantity of shinpads",font="Helvetica  12",bg="black",fg="white")
    email2 = Entry(footstaffwin,width=30,font="Helvetica  12")
    label_shin.place(x=20,y=140)
    email2.place(x=230,y=140)

    btn=Button(footstaffwin,text="Update",fg="white",bg="black",height=1,width=6,font=("Helvetica",12,BOLD),command=action)
    btn.place(x=240,y=170)

    btn1=Button(footstaffwin,text="Back",fg="white",bg="black",height=1,width=6,font=("Helvetica",12,BOLD))
    btn1.place(x=350,y=170)

    footstaffwin.mainloop()