from tkinter import *
from tkinter import messagebox as mb
from quiz_code import Quiz
from PIL import ImageTk, Image
def diff(u,p):
    Diff=Tk()
    Diff.geometry('800x450')
    Diff.title('My Quiz')
    Title = Label(Diff, text="Meme Quizer",width=45, bg='royalblue',fg="white", font=("Z003", 28, "bold"))
    Title.place(x=0, y=0)
    Diff.configure(bg='misty rose')
    Ask = Label(Diff, text='Please select level:',bg='misty rose',font=('Palatino',20,'bold')).place(x=160,y=130)
    #listbox=Listbox(Diff,height = 3, width = 8, bg = "grey", activestyle = 'dotbox')
    def levele():
        file='easy.json'
        #mb.showinfo('level',file)
        Diff.destroy()
        Quiz(u,p,file)
    def levelm():
        file='medium.json'
        #mb.showinfo('level',file)
        Diff.destroy()
        Quiz(u,p,file)
    def levelex():
        file='expert.json'
        #mb.showinfo('level',file)
        Diff.destroy()
        Quiz(u,p,file)
    """b1=Button(Diff, text='easy',command=levele)
    listbox.insert(1, b1)
    #listbox.insert(1, "easy", command=levele)
    #listbox.insert(2, "medium", command=levelm)
    #listbox.insert(3, "expert", command=levelex)
    listbox.place(x=130,y=90)"""
    def radio():
        opt_selected=IntVar()
        opt_selected.set(0)
        btn1 = Radiobutton(Diff,text='Easy',variable=opt_selected,command=levele,bg='misty rose',font=('Palatino',16,'bold')).place(x=210,y=180)
        btn2 = Radiobutton(Diff,text='Medium',variable=opt_selected,command=levelm,bg='misty rose',font=('Palatino',16,'bold')).place(x=210,y=230)
        btn1 = Radiobutton(Diff,text='Expert',variable=opt_selected,command=levelex,bg='misty rose',font=('Palatino',16,'bold')).place(x=210,y=280)
    radio()
    Quit=Button(Diff,text='Quit',command=Diff.destroy,width=5,bg="black", fg="white",font=("ariel",12," bold")).place(x=700,y=50)
    img = ImageTk.PhotoImage(Image.open("go.png"))
    label = Label(Diff,image=img).place(x=530,y=130)
    Diff.mainloop()
