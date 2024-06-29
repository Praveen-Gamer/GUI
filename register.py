from tkinter import*
import mysql.connector
sqlr=mysql.connector.connect(host="localhost",user="root",password="root",database="guireg")


win=Tk()
win.geometry("400x250+250+100")
win.title("Register Form")
win.configure(bg="dark blue")

          
def insertdata():
    regno=int(reg.get())
    nam=name.get()
    cur=sqlr.cursor()
    ins="insert into register(red_no,name)values(%s,%s)"
    val=(regno,nam)
    cur.execute(ins,val)
    sqlr.commit()
    print("Data Inserted")
    

def showdata():
    r=reg.get()
    print(r)
    cur=sqlr.cursor()
    cur.execute("select * from register")
    res=cur.fetchall()
    for x in res:
        print(x)


def searchdata():
    r=reg.get()
    print(r)
    cur=sqlr.cursor()
    cur.execute("select name from register where red_no=%s",(r,))
    res=cur.fetchone()
    if res!=None:
        for x in res:
            print(x)
            name.delete(0,'end')
            name.insert(0,x)
    else:
        name.delete(0,'end')
        name.insert(0,"not found")


def editdata():
    regno=int(reg.get())
    nam=name.get()
    cur=sqlr.cursor()
    ins="update register set name=%s where red_no=%s"
    val=(nam,regno)
    cur.execute(ins,val)
    sqlr.commit()
    print(cur.rowcount," record(s) affected")


def deletedata():
    regno=int(reg.get())
    cur=sqlr.cursor()
    cur.execute("delete from register where red_no=%s",(regno,))
    sqlr.commit()
    print(cur.rowcount," record deleted")
    reg.delete(0,END)
    name.delete(0,END)
    reg.focus_set()





l1=Label(win,text="Register no:",font="Times 12 bold",fg="red",bg="black")
l1.place(x=50,y=20)
reg=Entry(win)
reg.place(x=140,y=20)
l2=Label(win,text="Name:",font="Times 12 bold",fg="red",bg="black")
l2.place(x=50,y=80)
name=Entry(win)
name.place(x=102,y=80)
b1=Button(win,text="Insert",bd=10,bg="yellow",command=insertdata)
b1.place(x=50,y=130)
b2=Button(win,text="Show All",bd=10,bg="dark grey",command=showdata)
b2.place(x=150,y=130)
b3=Button(win,text="Search",bd=10,bg="blue",command=searchdata)
b3.place(x=270,y=130)
b4=Button(win,text="Update",bd=10,bg="brown",command=editdata)
b4.place(x=103,y=190)
b5=Button(win,text="Delete",bd=10,bg="violet",command=deletedata)
b5.place(x=225,y=190)
win.mainloop()
    
    

    

