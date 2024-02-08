from tkinter import *
from tkinter.font import BOLD 
def tennis():

    wintennis  = Tk()
    wintennis.title("tennis stock")
    wintennis.geometry("600x200")
    wintennis.config(bg="black")

    label_name = Label(wintennis, text="Enter quantity of racket",font="Helvetica  12",bg="black", foreground="white")
    name = Entry(wintennis,width=30,font="Helvetica  12")
    label_name.place(x=20, y=20)
    name.place(x=230, y=20)

    label_email = Label(wintennis,text="Enter quantity of balls",font="Helvetica  12",bg="black", foreground="white")
    email = Entry(wintennis,width=30,font="Helvetica  12")
    label_email.place(x=20,y=60)
    email.place(x=230,y=60)

    label_stock = Label(wintennis,text="Enter quantity of net",font="Helvetica  12",bg="black", foreground="white")
    email = Entry(wintennis,width=30,font="Helvetica  12")
    label_stock.place(x=20,y=100)
    email.place(x=230,y=100)


    btn=Button(wintennis,text="Buy",fg="black",bg="white",height=1,width=6,font=("Helvetica",12,BOLD),command=lambda:btn())
    btn.place(x=240,y=150)

    btn1=Button(wintennis,text="Back",fg="black",bg="white",height=1,width=6,font=("Helvetica",12,BOLD),command=lambda:btn1())
    btn1.place(x=350,y=150)

    wintennis.mainloop()