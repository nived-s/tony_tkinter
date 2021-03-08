from tkinter import *
import mysql.connector

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
new_frame_.place(relx=0.24,rely=0.25,relwidth=0.48,relheight=0.55)

con = mysql.connector.connect(host = "localhost", user = "root", passwd = "123456")
crs = con.cursor()
crs.execute("USE tony_textiles;")

con.commit()

heading= Label(
    new_frame,
    text= "TABLE:",
    background= "#D1F2EB",
    foreground= "black",
    font= ("Goudy Old Style",20),

)
heading.place(relx=0.42,rely=0.05)

search_text= Label(
    new_frame,
    text= "Search:",
    background= "#D1F2EB",
    foreground= "black",
    font= ("Goudy Old Style",17),

)
search_text.place(relx=0.25,rely=0.16)

dress_search= Entry(
        new_frame,
        font= ("Goudy Old Style",16),
    )
dress_search.config(width=40)
dress_search.place(relx=0.325,rely=0.16)


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
        
def search_update(e):
    search = e.widget.get()
    new_frame_.destroy()
    new_frame_within= Frame(new_frame,bg="white",bd=5)
    new_frame_within.place(relx=0.24,rely=0.25,relwidth=0.48,relheight=0.55)
    
    attributes=["Dress code ","   Dress Name    ",' colour ','   size   ',"   price    "]
    for attr in attributes:
        heading= Label(
            new_frame_within,
            text= attr,
            bg= "white",
            font=("Arial",15),
        )
        heading.grid(
            row=2,
            column= attributes.index(attr)
        )
        
    crs.execute('SELECT * FROM men_wear WHERE LOWER(item_name) LIKE "%' + search.lower() + '%";')
    search_info = crs.fetchall()
    search_database = []
    for i in search_info:
        search_database.append(i)
        
    for item in search_database:
        for detail in item:
            item_detail= Label(
                new_frame_within,
                text= detail,
                font= ("Arial",15),
                bg= "white"
            )
            item_detail.grid(
                row=database.index(item)+3,
                column= item.index(detail),
            )
        
            

dress_search.bind("<KeyRelease>", search_update)

def back_home():
    quit()

back_but= Button(
        new_frame,
        text="<< GO BACK",
        font=("Comic Sans MS",12),
        background= "BLUE",
        foreground="#D1F2EB",
        command = back_home,
    )
back_but.place(relx=0.425,rely=0.85,bordermode=OUTSIDE,relwidth=0.1)

root.mainloop()