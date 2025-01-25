from tkinter import *
from signup2 import New
import PIL
from PIL import ImageTk, Image
from login2 import Login
Startp=Tk()
Startp.geometry('800x450')
Startp.title('My Quiz')
Title = Label(Startp, text="Meme Quizer",width=45, bg='royalblue',fg="white", font=("Z003", 28, "bold"))
Title.place(x=0, y=0)
Startp.configure(bg='white')
def Go1():
    Startp.destroy()
    New()
def Go2():
    Startp.destroy()
    Login()
img = ImageTk.PhotoImage(Image.open("images.jpg"))
label = Label(Startp,image=img).place(x=270,y=80)
Sign=Button(Startp,text='Signup',command=Go1,width=10,bg='purple',fg='white',font=('P052',14,'bold')).place(x=250,y=350)
Log=Button(Startp,text='Login',command=Go2,width=10,bg='purple',fg='white',font=('P052',14,'bold')).place(x=400,y=350)
Quit=Button(Startp,text='Quit',command=Startp.destroy,width=5,bg="black", fg="white",font=("ariel",12," bold")).place(x=700,y=50)
Startp.mainloop()
