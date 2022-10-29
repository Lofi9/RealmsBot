import tkinter
from tkinter import *
from PIL import ImageTk,Image
# original screen
root = Tk()
# root.iconbitmap("Icon/icon.ico")
root.geometry("300x200")
root.title("Chatbot")
label=Label(root,text="Please enter your name").pack(pady=10)
name1=Entry(root,width=35,borderwidth=5)
name1.pack(pady=10)

# move window center
def center(x):
    winWidth = x.winfo_reqwidth()
    winwHeight = x.winfo_reqheight()
    posRight = int(x.winfo_screenwidth() / 2 - winWidth / 2)
    posDown = int(x.winfo_screenheight() / 2 - winwHeight / 2)
    x.geometry("+{}+{}".format(posRight, posDown))

center(root)

def grids(x):
    g1 = Label(x,text=(" ")).grid(column=0,row=0)
    g2 = Label(x,text=(" ")).grid(column=1,row=0)
    g3 = Label(x,text=(" ")).grid(column=2,row=0)
    g4 = Label(x,text=(" ")).grid(column=3,row=0)
    g5 = Label(x,text=(" ")).grid(column=4,row=0)
    g6 = Label(x,text=(" ")).grid(column=5,row=0)
    g7 = Label(x,text=(" ")).grid(column=6,row=0)
    g8 = Label(x,text=(" ")).grid(column=7,row=0)
    g9 = Label(x,text=(" ")).grid(column=8,row=0)
    g10 = Label(x,text=(" ")).grid(column=9,row=0)
    g11 = Label(x,text=(" ")).grid(column=10,row=0)
    g12 = Label(x,text=(" ")).grid(column=11,row=0)
    g13 = Label(x,text=(" ")).grid(column=12,row=0)
    g14 = Label(x,text=(" ")).grid(column=13,row=0)
    gi15 = Label(x,text=(" ")).grid(column=14,row=0)
    g16 = Label(x,text=(" ")).grid(column=15,row=0)
    g17 = Label(x,text=(" ")).grid(column=16,row=0)
    g18 = Label(x,text=(" ")).grid(column=17,row=0)
    g19 = Label(x,text=(" ")).grid(column=18,row=0)
    g20 = Label(x,text=(" ")).grid(column=19,row=0)
    g21 = Label(x,text=(" ")).grid(column=20,row=0)
    g22 = Label(x,text=(" ")).grid(column=21,row=0)
    g23 = Label(x,text=(" ")).grid(column=22,row=0)
    g24 = Label(x,text=(" ")).grid(column=23,row=0)
    g25 = Label(x,text=(" ")).grid(column=24,row=0)
    g26 = Label(x,text=(" ")).grid(column=25,row=0)
    g27 = Label(x,text=(" ")).grid(column=0,row=1)
    g28 = Label(x,text=(" ")).grid(column=0,row=2)
    g29 = Label(x,text=(" ")).grid(column=0,row=3)
    g30 = Label(x,text=(" ")).grid(column=0,row=4)
    g31 = Label(x,text=(" ")).grid(column=0,row=5)
    g32 = Label(x,text=(" ")).grid(column=0,row=6)
    g33 = Label(x,text=(" ")).grid(column=0,row=7)
    g34 = Label(x,text=(" ")).grid(column=0,row=8)
    g35 = Label(x,text=(" ")).grid(column=0,row=9)
    g36 = Label(x,text=(" ")).grid(column=0,row=10)
    g37 = Label(x,text=(" ")).grid(column=0,row=11)
    g38 = Label(x,text=(" ")).grid(column=0,row=12)
    g39 = Label(x,text=(" ")).grid(column=0,row=13)
    g40 = Label(x,text=(" ")).grid(column=0,row=14)
    g41 = Label(x,text=(" ")).grid(column=0,row=15)
    g42 = Label(x,text=(" ")).grid(column=0,row=16)
    g43 = Label(x,text=(" ")).grid(column=0,row=17)
    g44 = Label(x,text=(" ")).grid(column=0,row=18)
    g45 = Label(x,text=(" ")).grid(column=0,row=19)
    g46 = Label(x,text=(" ")).grid(column=0,row=20)
    g47 = Label(x,text=(" ")).grid(column=0,row=21)
    g48 = Label(x,text=(" ")).grid(column=0,row=22)
    g49 = Label(x,text=(" ")).grid(column=0,row=23)
    g50 = Label(x,text=(" ")).grid(column=0,row=24)
    g51 = Label(x,text=(" ")).grid(column=0,row=25)

def quit():
    root.destroy()
def next():
    root.withdraw()
    q1 = Toplevel(root)
    q1.title("Plesantries")
    q1.geometry("450x200")
    center(q1)
    name2 = name1.get().title()
    Label(q1,text="How are you "+name2+"?").grid(column=12,row=1,columnspan=3)

    hru=Entry(q1,width=35,borderwidth=5)
    hru.grid(column=12,row=2,columnspan=3)
    hru2 = hru.get().title()
    grids(q1)
    center(q1)
    def next2():
        q1.withdraw()
        q2 = Toplevel(root)
        q2.title("Plesantries")
        q2.geometry("450x200")
        grids(q2)
        if hru2 == "Good" or "Ok" or "Alright":
            hru3 = Label(q2,text=f"I'm glad to hear you are doing {hru2}, {name2}")
            hru3.grid(column=12,row=1,columnspan=3)
        else:
            hru4 = Label(q2,text=f"I'm sorry to hear that {name2}")



        b2quit = Button(q2,text="Quit",command=quit).grid(column=14,row=3)
        center(q2)
    bnext2= Button(q1,text="Next",command=next2).grid(column=12,row=3)
    bquit = Button(q1,text="Quit",command=quit).grid(column=14,row=3)

btn = Button(root,text="Next",command=next).pack(pady=10)









mainloop()