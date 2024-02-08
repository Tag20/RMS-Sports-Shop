from tkinter import *
from tkinter.font import BOLD  
def cricket():
    wincricket  = Tk()
    wincricket.title("cricket stock")
    wincricket.geometry("600x250")
    wincricket.config(bg="black")
    label_bat = Label(wincricket, text="Bats(1 Dozen-3600Rs)",font="Helvetica  12",bg="black", foreground="white")
    name = Entry(wincricket,width=30,font="Helvetica  12")
    label_bat.place(x=20, y=20)
    name.place(x=220, y=20)

    label_ball = Label(wincricket,text="Balls(1 Dozen-360Rs)",font="Helvetica  12",bg="black", foreground="white")
    email = Entry(wincricket,width=30,font="Helvetica  12")
    label_ball.place(x=20,y=60)
    email.place(x=220,y=60)

    label_stumps = Label(wincricket, fg=("black"), text="Stumps(1 Dozen-600Rs)",font="Helvetica  12",bg="black", foreground="white")
    email = Entry(wincricket,width=30,font="Helvetica  12")
    label_stumps.place(x=20,y=100)
    email.place(x=220,y=100)

    label_helmet = Label(wincricket,text="Helmet(Per peice-300Rs)",font="Helvetica  12",bg="black", foreground="white")
    email = Entry(wincricket,width=30,font="Helvetica  12")
    label_helmet.place(x=20,y=140)
    email.place(x=220,y=140)

    btn=Button(wincricket,text="Buy",fg="black",bg="white",height=1,width=6,font=("Helvetica",12,BOLD))
    btn.place(x=240,y=180)

    btn1=Button(wincricket,text="Back",fg="black",bg="white",height=1,width=6,font=("Helvetica",12,BOLD))
    btn1.place(x=350,y=180)

    wincricket.mainloop()