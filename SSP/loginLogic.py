#this Function will ask The User to chose a Name, his Stats will be saved and Loaded under This name

from mainLogic import stats


def equals(self, other):
    return self == other


#This Function sereches the CSV file for an entered Username if one is Found it will enter the UserWin and Comp win into the mainLogic Global stats
def login(username):
    opendata = open('stats/users.csv')
    inhalt = opendata.read()

    tabbelle = []

    zeilen = inhalt.split('\n')

    for cur in range(len(zeilen)):
        spalten = zeilen[cur].split(';')
        tabbelle.append(spalten)

    for cur in range(len(zeilen)):
        if equals(tabbelle[cur][0], username):
            stats['userWins'] = int(tabbelle[cur][1])
            stats['compWins'] = int(tabbelle[cur][2])
            print(stats)
            print(tabbelle[cur][0])
    opendata.close()

