# loginLogic.login(username)
# win = mL.stats['userWins']
# lose = mL.stats['compWins']
import tkinter as tk

import loginLogic
#import mainGui as mGui


def BtnLoginClick():
    User = LoginField.get()
    print(User)
    loginLogic.login(User)
    loginWin.destroy()



def printLogin():
    global loginWin
    loginWin = tk.Tk()

    loginWin.geometry("600x450+650+150")
    loginWin.title("Login to SSPAI")
    loginWin.configure(background="#868686")

    tk.Label(loginWin, text="Geben sie Bitte ihren Namen ein um Fortzufahren", font=("Rubik", 17),
             background="#868686").pack()

    BtnLogin = tk.Button(loginWin)
    BtnLogin.place(relx=0.25, rely=0.689, relheight=0.076, relwidth=0.523)
    BtnLogin.configure(activebackground="#ececec")
    BtnLogin.configure(activeforeground="#000000")
    BtnLogin.configure(background="#ffffff")
    BtnLogin.configure(borderwidth="0")
    BtnLogin.configure(disabledforeground="#a3a3a3")
    BtnLogin.configure(foreground="#000000")
    BtnLogin.configure(highlightbackground="#d9d9d9")
    BtnLogin.configure(highlightcolor="black")
    BtnLogin.configure(pady="0")
    BtnLogin.configure(command=lambda: BtnLoginClick())
    BtnLogin.configure(text="Login")

    global LoginField
    LoginField = tk.Entry(loginWin)
    LoginField.place(relx=0.25, rely=0.444, relheight=0.076, relwidth=0.523)
    LoginField.configure(background="white")
    LoginField.configure(font=("Rubik", 12))
    LoginField.configure(foreground="black")
    LoginField.configure(highlightbackground="#d9d9d9")
    LoginField.configure(highlightcolor="black")
    LoginField.configure(insertbackground="black")
    LoginField.configure(selectbackground="#c4c4c4")
    LoginField.configure(selectforeground="black")

    loginWin.mainloop()

