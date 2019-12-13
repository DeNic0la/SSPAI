from tkinter import ttk
import setStats as sS



#GLOBAL DEF
global winneris
global computerPick
global stats
global user
stats = dict()
stats['compWins'] = 0
stats['userWins'] = 0
global PlayingStreak
global arrayAI
arrayAI = []
for cur in range(23):
    arrayAI.append("X")
PlayingStreak = 0

def userInputFromGUI(userInput): #Diese Funktion nimmt de User Input entgegen
    global stats
    global user
    global PlayingStreak
    global arrayAI
    #An Dieser Stelle wird die berechnung der AI aufgerufen
    #Aktuell wird das mit der Zufallsfunktion gemacht
    import randomCompPick as rPick
    import calcWin
    #Die Playingstreak wird erhöht (oder auf 1 Gesetzt für das ERste Spiel)
    PlayingStreak += 1
    #über diese Funktionen wird der Spielzug des Computers Generiert
    #No Need to call getInputAI cause its already been called last time and the Data There is Now Correct
    compPick = rPick.getCompPick()

    #Hier wird überprüft wer der Gewinner ist
    winner = calcWin.calcWin(userInput, compPick)


    #Hier Wird die Variable erstellt welche zurückgegeben wird als Array
    toReturn = dict();
    toReturn['winner'] = winner
    toReturn['compPick'] = compPick

    # Hier werden die Stats (Spielstand) aktualisierts
    #TODO Confirm it is Working
    stats = sS.setStats(winner, stats, userInput)
    sS.getInputAI(winner, userInput)

    #Hier werden die Spielstände in das RückgabeArray gepackt
    toReturn['userWins'] = stats['userWins']
    toReturn['compWins'] = stats['compWins']




    return toReturn
