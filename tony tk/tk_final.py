from tkinter import *
import mysql.connector
from subprocess import Popen
from PIL import Image,ImageTk


root= Tk()
root.title("TONY TEXTILES")
root.geometry('1920x1080')
root.config(background="#ffffff")
root.iconbitmap("rocket.png")

back_image=PhotoImage(file="canvas.png")
back=Label(root,image=back_image)
back.place(relwidth=1,relheight=1)


## FUNCTIONS

# BUY PRODUCT

def buy():
    """global but1,but2,but3,but4,but5,text3
    but1.destroy()
    but2.destroy()
    but3.destroy()
    but4.destroy()
    but5.destroy()
    text3.destroy()
    new_frame= Frame(root,bg="#D1F2EB",bd=5)
    new_frame.place(relx=0.2,rely=0.11,relwidth=0.6,relheight=0.75)"""
    
    Popen("python buy.py")

# view_table

def view_table():
    """global but1,but2,but3,but4,but5,text3
    but1.destroy()
    but2.destroy()
    but3.destroy()
    but4.destroy()
    but5.destroy()
    text3.destroy()
    new_frame= Frame(root,bg="#D1F2EB",bd=5)
    new_frame.place(relx=0.2,rely=0.11,relwidth=0.6,relheight=0.75)"""
    Popen("python database.py")
    
# ADD PRODUCT

def add():
    Popen("python add.py")
    


# MODIFY PRICE

def modify():
    '''global but1,but2,but3,but4,but5,text3
    but1.destroy()
    but2.destroy()
    but3.destroy()
    but4.destroy()
    but5.destroy()
    text3.destroy()
    new_frame= Frame(root,bg="#D1F2EB",bd=5)
    new_frame.place(relx=0.2,rely=0.11,relwidth=0.6,relheight=0.75)'''

    Popen("python modify_price.py")


# CLOSE WINDOW

def closing():
    exit()


## HEADING

text3= Label(
    text= "TONY TEXTILES",
    background= "#ffffe6",
    foreground= "#30110D",
    font= ("Candara",70),

)
text3.place(relx=0.345,rely=0.19)

## BUTTONS

#/1/ BUY DRESS
but1= Button(
    root,
    text="BUY DRESS",
    font=("Comic Sans MS",17),
    background= "#F3860F",
    foreground="#F3F3F3",
    command = buy,

    )
but1.place(relx=0.38,rely=0.4,bordermode=OUTSIDE)

#/2/ ADD DRESS

but2=Button(
    root,
    text="ADD DRESS",
    font=("Comic Sans MS",17),
    background= "#F3860F",
    foreground="#F3F3F3",
    command= add
    )

but2.place(relx=0.38,rely=0.53,bordermode=OUTSIDE)

#/3/ VIEW TABLE DRESS

but3=Button(
    root,
    text="VIEW TABLE",
    font=("Comic Sans MS",17),
    background= "#F3860F",
    foreground="#F3F3F3",
    command= view_table
    )
but3.place(relx=0.53,rely=0.4,bordermode=OUTSIDE,relwidth=0.1)

#/4/ MODIFY PRICE

but4=Button(
    root,
    text="MODIFY PRICE",
    font=("Comic Sans MS",17),
    background= "#F3860F",
    foreground="#F3F3F3",
    command= modify

    )
but4.place(relx=0.53,rely=0.53,bordermode=OUTSIDE)

#/5/ EXIT SHOP
but5=Button(
    root,
    text="QUIT",
    font=("Comic Sans MS",15),
    background= "#94F526",
    foreground="black",
    command =closing,
    
    )
but5.place(relx=0.38,rely=0.64,relheight=0.05, relwidth=0.2485,bordermode=OUTSIDE)




 
root.mainloop()
