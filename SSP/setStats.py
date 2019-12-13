# This Function sets The Global Array Stats
import csv
import mainLogic as mL


def setStats(winneris, stats, userPick):
    if winneris == "same":
        return stats
    elif winneris == "compWin":
        stats['compWins'] += 1
        writeStatsToCSV("comp", userPick)
        return stats
    elif winneris == "userWin":
        stats['userWins'] += 1
        writeStatsToCSV("user", userPick)
        return stats


def writeStatsToCSV(winner, userPlayed):
    toWrite = []
    toWrite.append(mL.user)
    if winner == "comp":
        toWrite.append("lose")
    if winner == "user":
        toWrite.append("win")
    toWrite.append(userPlayed)
    print(toWrite)
    #with open('stats/users.csv', 'a', newline='') as csvfile:
    #    writer = csv.writer(csvfile, delimiter=';')
    #    writer.writerow(toWrite)


def getInputAI(winner, userPlayed):
    # Diese Werte Werden Jede Runde Überschrieben
    # Her we First have to ADD the Outcome of the Last Round to the Field 22
    # After That we can Move the Array and Update the Values so it is Read vor The AI as Input for The Predict

    #TODO Update [22]
    mL.arrayAI[22] = userPlayed
    #TODO Print to CSV if Everything is Filled
    if mL.PlayingStreak >= 9:
        with open('stats/users.csv', 'a', newline='') as csvfile:
            writer = csv.writer(csvfile, delimiter=';')
            writer.writerow(mL.arrayAI)

    mL.arrayAI[0] = mL.user
    AllGamesPlayed = mL.stats['compWins'] + mL.stats['userWins']
    mL.arrayAI[1] = str(AllGamesPlayed)
    mL.arrayAI[2] = str(mL.PlayingStreak)

    # This Function Moves Every ArrayValue by 2
    for old in range(3, 21):
        new = old + 2
        mL.arrayAI[new] = mL.arrayAI[old]

    # Die Zwei Werte um Neu Hinzuzufügen [SSP] [W/L]
    mL.arrayAI[3] = userPlayed
    mL.arrayAI[4] = winner
