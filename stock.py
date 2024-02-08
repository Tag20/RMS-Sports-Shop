from datetime import *
from tkinter.font import BOLD
import mysql.connector as my
from tkinter import *
from tkinter import messagebox
from cricketstaff import *
from footballstaff import *
from tennisstaff import *

def connect():
    con=my.connect(host='localhost',
                   user='root',
                   passwd='',
                   database='abc' )
    return con

class Buy:
    def __init__(self):
        self.staff=Tk()
        self.staff.title("Stock update")
        self.staff.config(background="black")
        self.staff.geometry("450x400")
        self.staff.resizable(0,0)

        btn=Button(self.staff,text="cricket",fg="black",bg="white",height=5,width=10,font=("Helvetica",12,BOLD),command=cricket1)
        btn.place(x=50,y=150)

        btn1=Button(self.staff,text="football",fg="black",bg="white",height=5,width=10,font=("Helvetica",12,BOLD),command=footballstaff)
        btn1.place(x=180,y=150)

        btn2=Button(self.staff,text="tennis",fg="black",bg="white",height=5,width=10,font=("Helvetica",12,BOLD),command=tennisstaff)
        btn2.place(x=310,y=150)
           

     
