import tkinter as tk
import mainLogic as mL
#Imports Form mainLogic


try:
    import ttk
except ImportError:
    import tkinter.ttk as ttk
global font9




font9 = "-family Rubik -size 9 -weight normal -slant roman "  \
            "-underline 0 -overstrike 0"


mainWin = tk.Tk()
mainWin.geometry("1100x687+371+169")
mainWin.title("TSSPAITWADYAIAY")
#Titel des Guis wird Erstellt
tk.Label(mainWin, text="Willkommen bei SSPAI", font=("Rubik", 50)).pack()
tk.Label(mainWin, text="Wählen sie zwischen Schere, Stein und Papier aus.", font=("Rubik", 20)).pack()


#Diese Funktion Ruft die Main Logic auf und nimmt ihre Werte entgegen un packt diese Anschliessend in Variabeln
def callUserInputFromGUI(inputOfUser):
    outcome = mL.userInputFromGUI(inputOfUser)
    computerPick = outcome['compPick']
    winner = outcome['winner']
    drawCompPick(computerPick)
    drawStats(winner)


def drawCompPick(computerPick):
    Notify = ttk.Label()
    Notify.place(relx=0.318, rely=0.684, height=39, width=408)
    Notify.configure(background="#d9d9d9")
    Notify.configure(foreground="#000000")
    Notify.configure(font=("Rubik", 10))
    Notify.configure(relief="flat")
    Notify.configure(anchor='center')
    Notify.configure(text="Der Computer hat sich für " + computerPick + " Entschieden")


def drawStats(winner):
    if winner == "same":
        winMessage = "Es steht Unentschieden"
    elif winner == "userWin":
        winMessage = "Du hast Gewonnen"
    else:
        winMessage = "Du hast Verloren"

    Notify = ttk.Label()
    Notify.place(relx=0.318, rely=0.784, height=39, width=408)
    Notify.configure(background="#d9d9d9")
    Notify.configure(foreground="#000000")
    Notify.configure(font=("Rubik", 10))
    Notify.configure(relief="flat")
    Notify.configure(anchor='center')
    Notify.configure(text=winMessage)


#Der Schere Knopf
BtnSchere = tk.Button()
BtnSchere.place(relx=0.091, rely=0.306, height=200, width=200)
BtnSchere.configure(activebackground="#ffffff")
BtnSchere.configure(activeforeground="#000000")
BtnSchere.configure(background="#ffffff")
BtnSchere.configure(borderwidth="0.2")
BtnSchere.configure(command= lambda: callUserInputFromGUI("Schere"))
BtnSchere.configure(disabledforeground="#a3a3a3")
BtnSchere.configure(foreground="#000000")
BtnSchere.configure(highlightbackground="#d4d4d4")
BtnSchere.configure(highlightcolor="black")
#Bild des Buttons
imgSchere = tk.PhotoImage(file="img/200Schere.png")
BtnSchere.configure(image=imgSchere)
BtnSchere.configure(overrelief="flat")
BtnSchere.configure(padx="0")
BtnSchere.configure(pady="0")

#Knopf Stein
BtnStein = tk.Button()
BtnStein.place(relx=0.409, rely=0.306, height=200, width=200)
BtnStein.configure(activebackground="#ffffff")
BtnStein.configure(activeforeground="#000000")
BtnStein.configure(background="#ffffff")
BtnStein.configure(borderwidth="0.2")
BtnStein.configure(command=lambda: callUserInputFromGUI("Stein"))
BtnStein.configure(disabledforeground="#a3a3a3")
BtnStein.configure(foreground="#000000")
BtnStein.configure(highlightbackground="#d4d4d4")
BtnStein.configure(highlightcolor="black")
#Bild des Buttons
imgStein = tk.PhotoImage(file="img/200Stein.png")
BtnStein.configure(image=imgStein)
BtnStein.configure(padx="0")
BtnStein.configure(pady="0")

#Knopf Papier
BtnPapier = tk.Button()
BtnPapier.place(relx=0.727, rely=0.306, height=200, width=200)
BtnPapier.configure(activebackground="#ffffff")
BtnPapier.configure(activeforeground="#000000")
BtnPapier.configure(background="#ffffff")
BtnPapier.configure(borderwidth="0.2")
BtnPapier.configure(command=lambda: callUserInputFromGUI("Papier"))
BtnPapier.configure(disabledforeground="#a3a3a3")
BtnPapier.configure(foreground="#000000")
BtnPapier.configure(highlightbackground="#d4d4d4")
BtnPapier.configure(highlightcolor="black")
#Bild des Buttons
imgPapier = tk.PhotoImage(file="img/200Papier.png")
BtnPapier.configure(image=imgPapier)
BtnPapier.configure(padx="0")
BtnPapier.configure(pady="0")


mainWin.mainloop()
