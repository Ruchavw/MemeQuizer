from tkinter import *
import mariadb
import sys
from tkinter import messagebox as mb
def Leaders():
    LB=Tk()
    LB.geometry('800x450')
    LB.title('My Quiz')
    Title = Label(LB, text="Meme Quizer",width=45, bg='royalblue',fg="white", font=("Z003", 28, "bold"))
    Title.place(x=0, y=0)
    LB.configure(bg='white')
    try:
        conn = mariadb.connect(
            user="~your username~",
            password="~password~",
            host="127.0.0.1",
            port=3306,
            database="~database name~"
            )
        cur=conn.cursor()
        cur.execute("SELECT Uname,Score FROM data")
        Ulabel = Label(LB,text = 'Player Name',width=16,bg='OliveDrab2',fg='black',font=('Palatino',22,'bold')).place(x=140,y=60)
        Slabel = Label(LB,text = 'Highest Score',width=16,bg='OliveDrab2',fg='black',font=('Palatino',22,'bold')).place(x=420,y=60)
        d=dict()
        for Uname,Score in cur:
            d[Uname]=int(Score)
        y_pos=120
        d1 = sorted(d.items(),key=lambda x:x[1],reverse=True)
        d2 = dict(d1)
        count=0
        for i in d2:
            label1 = Label(LB, text = i,width=16,bg='light coral',fg='black',font=('Palatino',18,'bold')).place(x=160,y=y_pos)
            label2 = Label(LB, text = d2[i],width=16,bg='light coral',fg='black',font=('Palatino',18,'bold')).place(x=440,y=y_pos)
            y_pos+=50
            count+=1
            if count==5:
                break
    except mariadb.Error as e:
        print(f"Error connecting to MariaDB Platform: {e}")
        sys.exit(1)
    quit = Button(LB,text='Thank  you',command=LB.destroy,width=10,bg="brown4", fg="white",font=("Z003",18," bold")).place(x=320,y=380)
    LB.mainloop()
