#this Function will ask The User to chose a Name, his Stats will be saved and Loaded under This name

import mainLogic as mL


def equals(self, other):
    return self == other


#This Function sereches the CSV file for an entered Username if one is Found it will enter the UserWin and Comp win into the mainLogic Global stats
def login(username):
    mL.user = username
    opendata = open('stats/users.csv')
    inhalt = opendata.read()
    tabbelle = []
    zeilen = inhalt.split('\n')
    countWin = 0
    countLose = 0

    for cur in range(len(zeilen)):
        spalten = zeilen[cur].split(';')
        tabbelle.append(spalten)

    for cur in range(len(zeilen)):
        if equals(tabbelle[cur][0], mL.user):
            if equals(tabbelle[cur][1], "user"):
                mL.stats['userWins'] += 1
            elif equals(tabbelle[cur][1], "comp"):
                mL.stats['compWins'] += 1
            elif equals(tabbelle[cur][1], "same"):
                mL.stats['same'] += 1
            mL.stats['GamesPlayedTotal'] += 1
            #print(mL.stats)
            #print(tabbelle[cur][0])





a = [1,2]
b = a
del a[:]

print(a)
print(b)