from tkinter import *
from tkinter import messagebox as mb
from Difficulty import diff
import mariadb
import sys
def Login():
    def login():
        usernamel = Label(best, text="Username :",bg='wheat1',font=('Palatino',22,'bold')).place(x=150,y=150)
        username = StringVar(best)
        usernameE = Entry(best, textvariable=username, width=20,font=('ariel',18)).place(x=350, y=150)
        passwordl = Label(best, text=" Password :",bg='wheat1',font=('Palatino',22,'bold')).place(x=150,y=200)
        password = StringVar(best)
        passwordE = Entry(best, textvariable=password, width=20, show="*",font=('ariel',18)).place(x=350, y=200)
        def check():
            nonlocal username, password
            try:
                if (username.get()==''):
                    raise ValueError
                elif (password.get()==''):
                    raise NameError
                else: 
                    def validate(u,p):
                        try:
                            conn = mariadb.connect(
                                user="~your username~",
                                password="~password~",
                                host="127.0.0.1",
                                port=3306,
                                database="~database name~"
                            )
                            cur=conn.cursor()
                            cur.execute("SELECT Uname,Password FROM data")
                            cat=0
                            for Uname, Password in cur:
                                if u==Uname and p==Password:
                                    cat=1
                            cur.close()
                            conn.close()
                            if cat==1:
                                return True
                            else:
                                return False
                        except mariadb.Error as e:
                            mb.showerror("Error","Unable to connect to Database")
                            #print(f"Error connecting to MariaDB Platform: {e}")
                            #sys.exit(1)
                    val=validate(username.get(),password.get())
                    def nextp():
                        best.destroy()
                        diff(username.get(),password.get())
                    if val==True:
                        nextp()
                    else:
                        raise TypeError
            except ValueError:
                mb.showwarning("Error","Please enter username")
            except NameError:
                mb.showwarning("Error","Please enter password")
            except TypeError:
                mb.showwarning("Error","Incorrect username or password")
        Login = Button(best, text="Login", command=check,width=10,bg='purple',fg='white',font=('P052',18,'bold')).place(x=350,y=300)
        Quit = Button(best, text="Quit", command=best.destroy,width=5,bg="black", fg="white",font=("ariel",12," bold")).place(x=700,y=50)
    best = Tk()
    best.geometry('800x450')
    best.title("My Quiz")
    Title = Label(best, text="Meme Quizer",width=45, bg='royalblue',fg="white", font=("Z003", 28, "bold"))
    Title.place(x=0, y=0)
    best.configure(bg='wheat1')
    login()
    best.mainloop() 
