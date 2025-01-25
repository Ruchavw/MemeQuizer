from tkinter import *
from tkinter import messagebox as mb
import json
import csv
from meme_display import memedisp
import mariadb
import sys
def Quiz(use,pas,level):
    def display_result():
        wrong_count = data_size - correct
        correctc = f"Correct: {correct}"
        wrong = f"Wrong: {wrong_count}"
        score = int(correct / int(data_size) * 100)
        result = f"Score: {score}%"
        mb.showinfo("Result", f"{result}\n{correctc}\n{wrong}")
    def check_ans(q_no):
        if opt_selected.get() == answer[q_no]:
            return True
    def next_btn():
        nonlocal q_no, correct
        if check_ans(q_no):
            correct += 1
        q_no += 1
        if q_no==data_size:
            display_result()
            """with open('passwd.csv','r') as pwd:
                csvreader=csv.reader(pwd)
                for i in range(csvreader):
                    if i['Uname']==use:
                        count = i
            with open('passwd.csv','a') as pd:
                header=['Uname','Password','Score']
                csvwriter=csv.DictWriter(pd,fieldnames=header, index=count)
                score = int(correct / int(data_size) * 100)
                data={'Uname':use,'Password':pas,'Score':score}
                csvwriter.writerow(data)"""
                                    #i['Score']=csvwriter.write(score)
            currentscore = int(correct / int(data_size) * 100)
            try:
                conn = mariadb.connect(
                    user="~your usename~",
                    password="~password~",
                    host="127.0.0.1",
                    port=3306,
                    database="~database name~"
                    )
                cur=conn.cursor()
                cur.execute("SELECT Uname,Score FROM data")
                for Uname, Score in cur:
                    if use == Uname:
                        if int(Score)>=currentscore:
                            highscore = Score
                            break
                        else:
                            highscore = currentscore
                            break
                scorestr="\'"+str(highscore)+"\'"
                user="\'"+use+"\'"
                pasw="\'"+pas+"\'"
                cur.execute(f"UPDATE data set Score={scorestr} WHERE Uname={user};")
                #print(cur.execute("SELECT * FROM data;"))
                cur.close()
                conn.commit()
                conn.close()
            except mariadb.Error as e:
                mb.showerror("Error","Unable to connect to Database")
                #print(f"Error connecting to MariaDB Platform: {e}")
                #sys.exit(1)
            m.destroy()
            memedisp(use,pas,currentscore)
        else:
            display_question()
            display_options()
    def buttons():
        next_button = Button(m, text="Next",command=next_btn,width=10,bg="blue",fg="white",font=("ariel",16,"bold"))
        next_button.place(x=350,y=380)
        quit_button = Button(m, text="Quit", command=m.destroy,width=5,bg="black", fg="white",font=("ariel",12," bold"))
        quit_button.place(x=700,y=50)
    def display_options():
        val=0
        opt_selected.set(0)
        for option in options[q_no]:
            opts[val]['text']=option
            val+=1
    def display_question():
        nonlocal q_no
        qi_no = Label(m, text=question[q_no], width=60,font=( 'ariel' ,16, 'bold' ),bg='white', anchor= 'w' )
        qi_no.place(x=40, y=100)
    def display_title():
        Title = Label(m, text="Meme Quizer",width=45, bg='royalblue',fg="white", font=("Z003", 28, "bold"))
        Title.place(x=0, y=0)
    def radio_buttons():
        nonlocal opt_selected
        q_list = []
        y_pos = 180
        while len(q_list) < 4:
            radio_btn = Radiobutton(m,text=" ",variable=opt_selected,bg='white', value = len(q_list)+1,font = ("ariel",14))
            q_list.append(radio_btn)
            radio_btn.place(x = 100, y = y_pos)
            y_pos += 40
        return q_list
    m = Tk()
    m.geometry("800x450")
    m.title("My Quiz")
    with open(level) as f:
        data = json.load(f)
    question = (data['question'])
    options = (data['options'])
    answer = (data[ 'answer'])
    q_no=0
    display_title()
    display_question()
    opt_selected=IntVar()
    opts=radio_buttons()
    display_options()
    buttons()
    data_size=len(question)
    correct=0
    m.configure(bg='white')
    m.mainloop()
