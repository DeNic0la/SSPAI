from tkinter import ttk
import setStats as sS



#GLOBAL DEF
global winneris
global computerPick
global stats
stats = dict()
stats['compWins'] = 0
stats['userWins'] = 0

def userInputFromGUI(userInput): #Diese Funktion nimmt de User Input entgegen
    global stats
    #An Dieser Stelle wird die berechnung der AI aufgerufen
    #Aktuell wird das mit der Zufallsfunktion gemacht
    import randomCompPick as rPick
    import calcWin
    #über diese Funktion wird der Spielzug des Computers Generiert
    compPick = rPick.getCompPick()
    #Hier wird überprüft wer der Gewinner ist
    winner = calcWin.calcWin(userInput, compPick)

    #Hier Wird die Variable erstellt welche zurückgegeben wird als Array
    toReturn = dict();
    toReturn['winner'] = winner
    toReturn['compPick'] = compPick

    # Hier werden die Stats (Spielstand) aktualisierts
    stats = sS.setStats(winner, stats)

    #Hier werden die Spielstände in das RückgabeArray gepackt
    toReturn['userWins'] = stats['userWins']
    toReturn['compWins'] = stats['compWins']




    return toReturn
