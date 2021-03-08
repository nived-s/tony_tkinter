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
new_frame_.place(relx=0.26,rely=0.15,relwidth=0.46,relheight=0.5)

con = mysql.connector.connect(host = "localhost", user = "root", passwd = "123456")
crs = con.cursor()
crs.execute("USE tony_textiles;")

con.commit()

# CANVAS SETUP

t= Label(
    new_frame,
    text= "MODIFY PRICE:",
    background= "#D1F2EB",
    foreground= "#30110D",
    font= ("Goudy Old Style",18),

)
t.place(relx=0.41,rely=0.07)

t1= Label(
    text= "ENTER DRESS CODE OF WHICH,\n THE PRICE TO BE CHANGED..",
    background= "#D1F2EB",
    foreground= "#30110D",
    font= ("Goudy Old Style",14),

)
t1.place(relx=0.42,rely=0.64)

t2= Label(
    text= "CODE  :",
    background= "#D1F2EB",
    foreground= "#30110D",
    font= ("Goudy Old Style",16),

)
t2.place(relx=0.412,rely=0.70)

t3= Label(
    text= "NEW PRICE  :",
    background= "#D1F2EB",
    foreground= "#30110D",
    font= ("Goudy Old Style",16),

)
t3.place(relx=0.385,rely=0.735)

code_entry= Entry(
        new_frame,
        font= ("Goudy Old Style",16),
    )
code_entry.place(relx=0.43,rely=0.79)

price_entry= Entry(
        new_frame,
        font= ("Goudy Old Style",16),
    )
price_entry.place(relx=0.43,rely=0.84)


# FUNCTIONS

def cancel_pressed():
    quit()

def ok_pressed():
    d_code=code_entry.get()
    price=price_entry.get()
    
    crs.execute("SELECT d_code FROM men_wear;")
    rows= crs.fetchall()
    ids= []
    for id in rows:
        ids.append(str(id[0]))

    if d_code in ids:
        crs.execute("update men_wear set price='"+str(price)+"' where d_code='"+str(d_code)+"';")  
        con.commit()
        messagebox.showinfo("TONY TEXTILES", "PRICE SUCCESSFULLY MODIFIED")
        
        quit()
    else:
        messagebox.showinfo("TONY TEXTILES", "NO ITEM WITH THE ENTERED CODE")
        

# DECISION BUTTONS

cancel_but= Button(
        new_frame,
        text="<< CANCEL",
        font=("Comic Sans MS",12),
        background= "RED",
        foreground="#D1F2EB",
        command = cancel_pressed,
    )
cancel_but.place(relx=0.38,rely=0.9,bordermode=OUTSIDE,relwidth=0.1)

ok_but= Button(
        new_frame,
        text="OK >>",
        font=("Comic Sans MS",12),
        background= "green",
        foreground="#D1F2EB",
        command = ok_pressed,
    )
ok_but.place(relx=0.52,rely=0.9,bordermode=OUTSIDE,relwidth=0.1)

# SHOWING TABLE

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