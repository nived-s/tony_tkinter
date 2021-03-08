from tkinter import *
from tkinter import messagebox
import mysql.connector

# WINDOW SETUP
root= Tk()
root.title("TONY TEXTILES")
root.geometry('1920x1080')
root.config(background="#ffffff")

back_image=PhotoImage(file="canvas.png")
back=Label(root,image=back_image)
back.place(relwidth=1,relheight=1)

new_frame= Frame(root,bg="#D1F2EB",bd=5)
new_frame.place(relx=0.2,rely=0.11,relwidth=0.6,relheight=0.75)

new_frame_= Frame(new_frame,bg="white",bd=5)
new_frame_.place(relx=0.26,rely=0.13,relwidth=0.46,relheight=0.5)

con = mysql.connector.connect(host = "localhost", user = "root", passwd = "123456")
crs = con.cursor()
crs.execute("USE tony_textiles;")

con.commit()

# CANVAS SETUP

t= Label(
    new_frame,
    text= "BUY DRESS:",
    background= "#D1F2EB",
    foreground= "#30110D",
    font= ("Goudy Old Style",18),

)
t.place(relx=0.43,rely=0.05)

t1= Label(
    text= "ENTER THE DRESS CODE \n BELOW..",
    background= "#D1F2EB",
    foreground= "#30110D",
    font= ("Goudy Old Style",17),

)
t1.place(relx=0.42,rely=0.6)

t2= Label(
    text= "CODE  :",
    background= "#D1F2EB",
    foreground= "#30110D",
    font= ("Goudy Old Style",17),

)
t2.place(relx=0.4,rely=0.67)

code_entry= Entry(
        new_frame,
        font= ("Goudy Old Style",16),
    )
code_entry.place(relx=0.42,rely=0.75)


# FUNCTIONS

def cancel_pressed():
    quit()

def ok_pressed():
    d_code=code_entry.get()
    
    crs.execute("SELECT d_code FROM men_wear;")
    rows= crs.fetchall()
    ids= []
    for id in rows:
        ids.append(str(id[0]))

    if d_code in ids:
        crs.execute(f"delete from men_wear where d_code = '{d_code}'")
        con.commit()
        messagebox.showinfo("TONY TEXTILES", "PURCHASE SUCCESSFULL")
        
        quit()
    else:
        messagebox.showinfo("TONY TEXTILES", "NO ITEM WITH THE ENTERED CODE,\nPLEASE RE-CHECK THE CODE.")       

# DECISION BUTTONS

cancel_but= Button(
        new_frame,
        text="<< CANCEL",
        font=("Comic Sans MS",12),
        background= "RED",
        foreground="#D1F2EB",
        command = cancel_pressed,
    )
cancel_but.place(relx=0.38,rely=0.85,bordermode=OUTSIDE,relwidth=0.1)

ok_but= Button(
        new_frame,
        text="OK >>",
        font=("Comic Sans MS",12),
        background= "green",
        foreground="#D1F2EB",
        command = ok_pressed,
    )
ok_but.place(relx=0.52,rely=0.85,bordermode=OUTSIDE,relwidth=0.1)

# DISPLAYING TABLE

attributes=["Dress code ","   Dress Name    ",' colour ','   size   ',"   price    "]
crs.execute("SELECT * FROM men_wear ORDER BY d_code;")

info= crs.fetchall()
database=[]

for i in info:
    database.append(i)

for attr in attributes:
    heading= Label(
        new_frame_,
        text= attr,
        bg= "white",
        font=("Arial",15),
    )
    heading.grid(
        row=2,
        column= attributes.index(attr)
    )

for item in database:
    for detail in item:
        item_detail= Label(
            new_frame_,
            text= detail,
            font= ("Arial",15),
            bg= "white"
        )
        item_detail.grid(
            row=database.index(item)+3,
            column= item.index(detail),
        )

root.mainloop()