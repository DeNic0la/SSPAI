# Imports Here
import random
from numpy.random.mtrand import random_integers
from pip._vendor.distlib.compat import raw_input

#Import my Own Files
import calcWin

# Imports end Here


# Begrüssung
print("Willkommen zum Schere-Stein-Papier Spiel. Sie Spielen Aktuell in der Konsole.\n\n")
playing = True
userWins = 0
compWins = 0
# Schere-Stein-Papier vom User erhalten
def getUserPick():
    # Diese Funktion gibt Schere, Stein oder Papier zurück anhand der eingabe des Users
    # Der Erste buchstabe ist gross, der rest Klein. Keine Leerzeichen.
    while True:
        userPickTMP = raw_input("Geben sie Schere, Stein oder Papier ein. Schreiben sie es dafür einfach aus.\n")
        if userPickTMP.lower() == "schere":
            print("Sie haben sich für Schere Entschieden")
            return "Schere"
        elif userPickTMP.lower() == "stein":
            print("Sie haben sich für Stein Entschieden")
            return "Stein"
        elif userPickTMP.lower() == "papier":
            print("Sie haben sich für Papier Entschieden")
            return "Papier"
        else:
            print("Ihre Eingabe wurde Nicht erkannt. Versuchen wir es Nochmals")
# Ende der Funktion

while playing:
    userPick = getUserPick()

    toChose = ['Schere', 'Stein', 'Papier']
    for makeCompPick in random.sample(toChose, len(toChose)):
        compPick = makeCompPick
    print("Der Computer hat sich für " + compPick + " Entschieden \n")
    win = calcWin.calcWin(userPick, compPick)
    if win == "same":
        print("Unentschieden")
    elif win == "userWin":
        print("Du Hast Gewonnen")
        userWins += 1
    elif win == "compWin":
        print("Du Hast Verloren")
        compWins += 1

    playAgain = raw_input("Wollen sie Nochmals spielen ? Y/N\n")
    if playAgain.lower() == 'n':
        playing = False
    elif playAgain == 'S':
        playing = True
        print("Du hast " + str(userWins) + " Mal Gewonnen und "+ str(compWins) + " Mal Verloren")
    else:
        playing = True

print("Das Spiel wird Abgebrochen\nDu hast " + str(userWins) + "Mal Gewonnen und "+ str(compWins) + "Mal Verloren")