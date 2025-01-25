from tkinter import *
from PIL import ImageTk, Image
from leaderboard import Leaders
def memedisp(u,p,s):
    meme = Tk()
    meme.geometry('800x450')
    meme.title('My Quiz')
    if s==100:
        img = ImageTk.PhotoImage(Image.open("lookingLikeAWow.jpg"))
    elif s>=75:
        img = ImageTk.PhotoImage(Image.open("thinking.jpg"))
    elif s>=50:
        img = ImageTk.PhotoImage(Image.open("aayein.jpg"))
    elif s>=25:
        img = ImageTk.PhotoImage(Image.open("disappointed.jpg"))
    else:
        img = ImageTk.PhotoImage(Image.open("moyemoye.jpg"))
    Title = Label(meme, text="Meme Quizer",width=45, bg='royalblue',fg="white", font=("Z003", 28, "bold"))
    Title.place(x=0, y=0)
    meme.configure(bg='white')
    label = Label(meme,image=img).place(x=250,y=80)
    quit = Button(meme,text='Quit',command=meme.destroy,width=5,bg="black", fg="white",font=("ariel",12," bold")).place(x=700,y=50)
    def nextp():
        meme.destroy()
        Leaders()
    Leaderp = Button(meme,text='Leader Board',command=nextp,width=15,bg='purple',fg='white',font=('P052',18,'bold')).place(x=280,y=350)
    meme.mainloop()
