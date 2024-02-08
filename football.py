from tkinter import *
from tkinter.font import BOLD 
def football():

    winfootball  = Tk()
    winfootball.title("football stock")
    winfootball.geometry("600x200")
    winfootball.config(bg="black")

    label_name = Label(winfootball, text="Enter quantity of football",font="Helvetica  12",bg="black", foreground="white")
    name = Entry(winfootball,width=30,font="Helvetica  12")
    label_name.place(x=20, y=20)
    name.place(x=230, y=20)

    label_email = Label(winfootball,text="Enter quantity of gloves",font="Helvetica  12",bg="black", foreground="white")
    email = Entry(winfootball,width=30,font="Helvetica  12")
    label_email.place(x=20,y=60)
    email.place(x=230,y=60)

    label_stock = Label(winfootball,text="Enter quantity of studs",font="Helvetica  12",bg="black", foreground="white")
    email = Entry(winfootball,width=30,font="Helvetica  12")
    label_stock.place(x=20,y=100)
    email.place(x=230,y=100)

    label_shin = Label(winfootball,text="Enter quantity of shinpads",font="Helvetica  12",bg="black", foreground="white")
    email = Entry(winfootball,width=30,font="Helvetica  12")
    label_shin.place(x=20,y=100)
    email.place(x=230,y=100)

    btn=Button(winfootball,text="Buy",fg="black",bg="white",height=1,width=6,font=("Helvetica",12,BOLD),command=lambda:btn())
    btn.place(x=240,y=150)

    btn1=Button(winfootball,text="Back",fg="black",bg="white",height=1,width=6,font=("Helvetica",12,BOLD),command=lambda:btn1())
    btn1.place(x=350,y=150)

    winfootball.mainloop()