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

con = mysql.connector.connect(host = "localhost", user = "root", passwd = "123456")
crs = con.cursor()
crs.execute("USE tony_textiles;")

con.commit()

## CANVAS SETUP

item= Label(
        new_frame,
        text="ITEM NAME :",
        font=("Goudy Old Style",18),
        background= "#D1F2EB",
        foreground="#000000",
    )

d_color= Label(
        new_frame,
        text="COLOUR :",
        font=("Goudy Old Style",18),
        background= "#D1F2EB",
        foreground="#000000",
    )

code= Label(
        new_frame,
        text="DRESS CODE :",
        font=("Goudy Old Style",18),
        background= "#D1F2EB",
        foreground="#000000",
    )

d_price= Label(
        new_frame,
        text="PRICE :",
        font=("Goudy Old Style",18),
        background= "#D1F2EB",
        foreground="#000000",
    )

d_size= Label(
        new_frame,
        text="SIZE :",
        font=("Goudy Old Style",18),
        background= "#D1F2EB",
        foreground="#000000",
    )

## ENTRY BOXES

item_entry= Entry(
        new_frame,
        font= ("Goudy Old Style",16),
    )

d_color_entry= Entry(
        new_frame,
        font= ("Goudy Old Style",16),
    )

code_entry= Entry(
        new_frame,
        font= ("Goudy Old Style",16),
    )

d_price_entry= Entry(
        new_frame,
        font= ("Goudy Old Style",16),
    )

## PLACING
item.place(relx=0.33,rely=0.16)
item_entry.place(relx=0.48,rely=0.16)
d_color.place(relx=0.355,rely=0.25)
d_color_entry.place(relx=0.48,rely=0.25)
code.place(relx=0.316,rely=0.34)
code_entry.place(relx=0.48,rely=0.34)
d_price.place(relx=0.385,rely=0.43)
d_price_entry.place(relx=0.48,rely=0.43)
d_size.place(relx=0.405,rely=0.52)

options= [
        "S",
        "M",
        "L"
    ]

clicked= StringVar()
clicked.set(options[0])

drop= OptionMenu(
        new_frame,
        clicked,
        *options,
    )
drop.configure(width=5,font=("Consolas",12))
drop.place(relx=0.48,rely=0.52)

## BUTTONS

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
        warning= Label(new_frame, text= "DRESS CODE ALREADY EXIST")
        warning.place(relx=0.44,rely=0.65)
        new_frame.after(2000,warning.destroy)
    else:
        item_name= item_entry.get()
        colour= d_color_entry.get()
        size= clicked.get()
        price= d_price_entry.get()

        if item_name and colour and size and price:
            crs.execute(f"insert into men_wear values('{d_code}', '{item_name}', '{colour}', '{size}', '{price}')")
            con.commit()
            messagebox.showinfo("TONY TEXTILES", "ITEM ADDED SUCCESSFULLY")
        
            quit()

cancel_but= Button(
        new_frame,
        text="CANCEL",
        font=("Comic Sans MS",12),
        background= "RED",
        foreground="#D1F2EB",
        command = cancel_pressed,
    )
cancel_but.place(relx=0.38,rely=0.7,bordermode=OUTSIDE,relwidth=0.1)

ok_but= Button(
        new_frame,
        text="OK",
        font=("Comic Sans MS",12),
        background= "green",
        foreground="#D1F2EB",
        command = ok_pressed,
    )
ok_but.place(relx=0.52,rely=0.7,bordermode=OUTSIDE,relwidth=0.1)

root.mainloop()