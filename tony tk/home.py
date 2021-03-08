from tkinter import *
from tkinter import messagebox
import mysql.connector
from subprocess import *

root= Tk()
root.title("TONY TEXTILES")
root.geometry('1920x1080+0+0')
root.config(background="#42413f")
root.iconbitmap("rocket.png")

## DATABASE MANAGEMENT

con = mysql.connector.connect(host = "localhost", user = "root", passwd = "123456")
crs = con.cursor()

crs.execute("CREATE DATABASE IF NOT EXISTS tony_textiles;")
crs.execute("USE tony_textiles;")
crs.execute("CREATE TABLE IF NOT EXISTS customers (username varchar(25) PRIMARY KEY NOT NULL,password varchar(25) NOT NULL,name varchar(25) NOT NULL, mail_id varchar(25));")

con.commit()   

## FUNCTIONS

# SIGNING IN

def sign():
    global but6,but7,text1,text2
    but6.destroy()
    but7.destroy()
    text1.destroy()
    text2.destroy()
    new_frame= Frame(root,bg="#D1F2EB",bd=5)
    new_frame.place(relx=0.2,rely=0.11,relwidth=0.6,relheight=0.75)

    t1= Label(
        new_frame,
        text= "USERNAME:",
        background= "#D1F2EB",
        foreground= "#30110D",
        font= ("Candara",20),

    )

    t1.place(relx=0.323,rely=0.27)

    t2= Label(
        new_frame,
        text= "PASSWORD:",
        background= "#D1F2EB",
        foreground= "#30110D",
        font= ("Candara",20),

    )

    t2.place(relx=0.32,rely=0.35)

    t3= Label(
        new_frame,
        text= "NAME:",
        background= "#D1F2EB",
        foreground= "#30110D",
        font= ("Candara",20),

    )

    t3.place(relx=0.374,rely=0.43)

    t4= Label(
        new_frame,
        text= "MAIL ADDRESS:",
        background= "#D1F2EB",
        foreground= "#30110D",
        font= ("Candara",18),

    )

    t4.place(relx=0.3,rely=0.51)

    username_sign= Entry(
        new_frame,
        font= ("Corbel",18),           
    )

    username_sign.place(relx=0.5,rely=0.27)

    password_sign= Entry(
        new_frame,
        font= ("Corbel",18),
        
    )

    password_sign.place(relx=0.5,rely=0.35)

    name_sign= Entry(
        new_frame,
        font= ("Corbel",18),           
    )

    name_sign.place(relx=0.5,rely=0.43)

    mail_sign= Entry(
        new_frame,
        font= ("Corbel",18),
        
    )

    mail_sign.place(relx=0.5,rely=0.51)

    def customer_sign():
        username= username_sign.get()
        password= password_sign.get()
        name= name_sign.get()
        mail= mail_sign.get()
        
        crs.execute("SELECT username FROM customers;")
        rows= crs.fetchall()
        names= []
        for eachName in rows:
            names.append(str(eachName[0]))
        
        if username in names:
            messagebox.showwarning("TONY TEXTILES", "USER NAME ALREADY EXIST,\nTRY USE ANOTHER USERNAME.THIS NAME IS UNIQUE") 
        
        else:            
            if username=="" or password=="" or name=="" or mail=="":
                messagebox.showerror("TONY TEXTILES", "ALL FIELDS ARE REQUIRED")            
            elif username and password and name and mail:
                crs.execute(f"insert into customers values('{username}', '{password}', '{name}', '{mail}')") 
                con.commit()
                messagebox.showinfo("TONY TEXTILES", "WELCOME.\nENJOY PURCHASING WITH TONY TEXTILES.\nHAVE A NICE DAY.")
                Popen('python tk_final.py')
                exit()
            else:
                messagebox.showerror("TONY TEXTILES", "SOMETHING WENT WRONG.\nTRY AGAIN.")

    b1= Button(
        new_frame,
        text="SIGN UP",
        font=("Gabriola",20),
        background= "#F3860F",
        foreground="#F3F3F3",
        command = customer_sign,

    )
    b1.place(relx=0.32,rely=0.62,relheight=0.05, relwidth=0.4,bordermode=OUTSIDE)

    t5= Label(
        new_frame,
        text= "ALREADY A USER",
        background= "#D1F2EB",
        foreground= "#30110D",
        font= ("Candara",14),

    )

    t5.place(relx=0.45,rely=0.725)

    b2= Button(
        new_frame,
        text="LOG IN",
        font=("Gabriola",20),
        background= "#F3860F",
        foreground="#F3F3F3",
        command = log,

    )
    b2.place(relx=0.46,rely=0.77,relheight=0.05, relwidth=0.1,bordermode=OUTSIDE)

# LOGING IN

def log():
    global but6,but7,text1,text2
    but6.destroy()
    but7.destroy()
    text1.destroy()
    text2.destroy()
    new_frame= Frame(root,bg="#D1F2EB",bd=5)
    new_frame.place(relx=0.2,rely=0.11,relwidth=0.6,relheight=0.75)

    t1= Label(
        new_frame,
        text= "USERNAME:",
        background= "#D1F2EB",
        foreground= "#30110D",
        font= ("Candara",20),
    )

    t1.place(relx=0.32,rely=0.32)

    t2= Label(
        new_frame,
        text= "PASSWORD:",
        background= "#D1F2EB",
        foreground= "#30110D",
        font= ("Candara",20),
    )

    t2.place(relx=0.32,rely=0.4)

    e1= Entry(
        new_frame,
        font= ("Corbel",18),  
    )

    e1.place(relx=0.5,rely=0.32)

    e2= Entry(
        new_frame,
        font= ("Corbel",18),
    )
    e2.config(show='*')

    e2.place(relx=0.5,rely=0.4)

    def customer_check():        
        username_check= e1.get()
        password_check= e2.get()
        
        if username_check=="" or password_check=="" :
            messagebox.showerror("TONY TEXTILES", "ALL FIELDS ARE REQUIRED")
            
        elif username_check and password_check:
            crs.execute("SELECT username FROM customers;")
            rows= crs.fetchall()
            ids= []
            for id in rows:
                ids.append(str(id[0]))
            
            if username_check in ids:
                #check for password
                crs.execute("SELECT password FROM customers where username='"+str(username_check)+"';")
                real_pass= crs.fetchone()
                if password_check == real_pass[0]:
                    Popen('python tk_final.py')
                    exit()
                    
                else:
                    messagebox.showwarning("TONY TEXTILES", "INCORRECT PASSWORD.")            
            else:
                #user not signed up show to signup
                messagebox.showwarning("TONY TEXTILES", "NO USER AVAILABLE WITH THE ENTERED USERNAME,\nTRY SIGNUP.")

    b1= Button(
        new_frame,
        text="LOG IN",
        font=("Gabriola",20),
        background= "#F3860F",
        foreground="#F3F3F3",
        command = customer_check,
    )
    b1.place(relx=0.32,rely=0.53,relheight=0.05, relwidth=0.4,bordermode=OUTSIDE)

    t3= Label(
        new_frame,
        text= "DON'T HAVE AN ACCOUNT",
        background= "#D1F2EB",
        foreground= "#30110D",
        font= ("Candara",14),
    )

    t3.place(relx=0.41,rely=0.63)

    b2= Button(
        new_frame,
        text="SIGN UP",
        font=("Gabriola",20),
        background= "#F3860F",
        foreground="#F3F3F3",
        command = sign,
    )
    b2.place(relx=0.46,rely=0.68,relheight=0.05, relwidth=0.1,bordermode=OUTSIDE)


## TITLES

text1= Label(
    text= "- TONY TEXTILES -",
    background= "#42413f",
    foreground= "#FF8000",
    font= ("Gabriola",130),

)
text1.place(relx=0.26,rely=0.17)

text2= Label(
    text= "Start Purchasing..",
    background= "#42413f",
    foreground= "#FFFFFF",
    font= ("Gill Sans MT",40),

)
text2.place(relx=0.42,rely=0.45)

## BUTTONS

#/6/ SIGNUP

but6= Button(
    root,
    text= 'SIGN UP',
    background= "#d58d10",
    foreground= "#ffffff",
    font= ("Meiryo",16),
    width= 18,
    height= 1,
    activeforeground= "#d58d10",
    command= sign

)
but6.place(relx=0.458,rely=0.58)

#/7/ LOGIN

but7= Button(
    root,
    text= 'LOGIN',
    background= "#d58d10",
    foreground= "#ffffff",
    font= ("Meiryo",16),
    width= 18,
    height= 1,
    activeforeground= "#d58d10",
    command= log

)
but7.place(relx=0.458,rely=0.65)

root.mainloop()