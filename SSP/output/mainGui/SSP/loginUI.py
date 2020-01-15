from pip._vendor.distlib.compat import raw_input

import loginLogic

import mainLogic as mL

def doLogin():

    username = raw_input("Geben sie Ihren Benutzernamen ein.\n")
    #mL.user = username
    loginLogic.login(username)
    win = mL.stats['userWins']
    lose = mL.stats['compWins']
    if win == 0 and lose == 0:
        print("Der Benutzer den du Angegeben hast Existiert noch nicht, es wurden keine Statistiken geladen.")
    else:
        print("Ihr Benutzer hat bereits "+str(win)+" mal Gewonnen und "+str(lose)+" mal Verloren")


