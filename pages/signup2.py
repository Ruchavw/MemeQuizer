from tkinter import *
from Difficulty import diff
from tkinter import messagebox as mb
import mariadb
import sys
def New():
    def new_user():
        usernameL = Label(sig,text="Enter username:",bg='wheat1',font=('Palatino',18,'bold')).place(x=150,y=155)
        username = StringVar()
        usernameE = Entry(sig,textvariable=username,width=20,font=('ariel',16)).place(x=400,y=150)
        passwordL = Label(sig,text="Enter password:",bg='wheat1',font=('Palatino',18,'bold')).place(x=150,y=205)
        password = StringVar()
        passwordE = Entry(sig,textvariable=password,show='*',width=20,font=('ariel',16)).place(x=400,y=200)
        repassL = Label(sig,text="Re-enter password:",bg='wheat1',font=('Palatino',18,'bold')).place(x=150,y=255)
        repass = StringVar()
        repassE = Entry(sig,textvariable=repass,show='*',width=20,font=('ariel',16)).place(x=400,y=250)
        def check():
            nonlocal username,password
            try:
                if username.get()=='':
                    raise ValueError
                elif password.get()=='':
                    raise NameError
                elif repass.get()=='':
                    raise TypeError
                elif repass.get()!=password.get():
                    raise IndexError
                else:
                    def create(u,p):
                        try:
                            conn = mariadb.connect(
                                user="~your username~",
                                password="~password~",
                                host="127.0.0.1",
                                port=3306,
                                database="~database name~"
                            )
                            cur=conn.cursor()
                            u="\'"+u+"\'"
                            p="\'"+p+"\'"
                            #print(u,p)
                            cur.execute(f"INSERT INTO data (Uname,Password,Score) VALUES ({u},{p},'0');")
                            #print(cur.execute("SELECT * FROM data;"))
                            cur.close()
                            conn.commit()
                            conn.close()
                        except mariadb.Error as e:
                            mb.showerror("Error","Unable to connect to Database")
                            #print(f"Error connecting to MariaDB Platform: {e}")
                            #sys.exit(1)
                    create(username.get(),password.get())
                    sig.destroy()
                    diff(username.get(),password.get())
            except ValueError:
                mb.showwarning('Error','Please enter username')
            except NameError:
                mb.showwarning('Error','Please enter password')
            except TypeError:
                mb.showwarning('Error','Please re-enter password')
            except IndexError:
                mb.showwarning('Error','Re-enterd Password does not match\nPlease check password')
        sup = Button(sig,text='Signup',command=check,width=10,bg='purple',fg='white',font=('P052',18,'bold')).place(x=350,y=320)
        quit = Button(sig,text='Quit',command=sig.destroy,width=5,bg="black", fg="white",font=("ariel",12," bold")).place(x=700,y=50)
    sig=Tk()
    sig.geometry('800x450')
    sig.title('My Quiz')
    Title = Label(sig, text="Meme Quizer",width=45, bg='royalblue',fg="white", font=("Z003", 28, "bold"))
    Title.place(x=0, y=0)
    sig.configure(bg='wheat1')
    new_user()
    sig.mainloop()
