from datetime import *
from tkinter.font import BOLD
import mysql.connector as my
from tkinter import *
from tkinter import messagebox
import time
from cricket import *
from football import *
from tennis import *
def connect():
    con=my.connect(host='localhost',
                   user='root',
                   passwd='',
                   database='abc' )
    return con

class Customer:
    def __init__(self):
        self.cust=Tk()
        self.cust.title("Stock selection")
        self.cust.config(bg="black")
        self.cust.geometry("450x400")
        self.cust.resizable(0,0)
        

class stock:
    
    def __init__(self):

        self.root = Tk()
        self.root.geometry( "500x450" )

        #cphoto= PhotoImage(file=r"pl project\cricket.png").subsample(3,3)
        btn=Button(text="cricket",fg="black",bg="white",height=5,width=10,font=("Helvetica",12,BOLD),command=cricket)
        btn.place(x=60,y=150)

        btn1=Button(text="football",fg="black",bg="white",height=5,width=10,font=("Helvetica",12,BOLD),command=football)
        btn1.place(x=190,y=150)

        btn2=Button(text="tennis",fg="black",bg="white",height=5,width=10,font=("Helvetica",12,BOLD),command=tennis)
        btn2.place(x=320,y=150)
        self.root.mainloop()
    
       
    

  
            

       
                    
        
        