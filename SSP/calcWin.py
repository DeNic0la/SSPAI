def calcWin(userPick, compPick): #Diese Funktion überprüft anahnd von zwei Eingaben wer Gewonnen hat.
    if userPick == compPick:
        return "same"
    if userPick == "Schere":
        if compPick == "Stein":
            return "compWin"
        elif compPick == "Papier":
            return "userWin"
        else:
            print("This is Not Supopsed to Happen")
    if userPick == "Stein":
        if compPick == "Papier":
            return "compWin"
        elif compPick == "Schere":
            return "userWin"
        else:
            print("This is Not Supposed to Happen")
    if userPick == "Papier":
        if compPick == "Schere":
            return "compWin"
        elif compPick == "Stein":
            return "userWin"
        else:
            print("This is Not Supposed to Happen")
