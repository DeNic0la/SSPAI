from pip._vendor.distlib.compat import raw_input

import loginLogic
from mainLogic import stats


def doLogin():
    username = raw_input("Geben sie Ihren Benutzernamen ein falls sie ohne Benutzernamen fortfahren möchten geben sie Y ein\n")
    loginLogic.login(username)
    win = stats['userWins']
    lose = stats['compWins']
    print("Ihr Benutzer hat bereits "+str(win)+" mal Gewonnen und "+str(lose)+" mal Verloren")