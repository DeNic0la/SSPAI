# This Function sets The Global Array Stats
import csv
import mainLogic as mL


def setStats(winneris, stats, userPick):
    if winneris == "same":
        writeStatsToCSV("same")
        return stats
    elif winneris == "compWin":
        stats['compWins'] += 1
        writeStatsToCSV("comp")
        return stats
    elif winneris == "userWin":
        stats['userWins'] += 1
        writeStatsToCSV("user")
        return stats


def writeStatsToCSV(winner):
    toWrite = [mL.user]
    if winner == "comp":
        toWrite.append("comp")
    if winner == "user":
        toWrite.append("user")
    if winner == "same":
        toWrite.append("same")
    print(toWrite)
    with open('stats/users.csv', 'a', newline='') as csvfile:
        writer = csv.writer(csvfile, delimiter=';')
        writer.writerow(toWrite)


def setInputAI(winner, userPlayed):
    # Diese Werte Werden Jede Runde Überschrieben
    # Her we First have to ADD the Outcome of the Last Round to the Field 22
    # After That we can Move the Array and Update the Values so it is Read vor The AI as Input for The Predict

    #TODO Update [23]
    mL.arrayAI[23] = userPlayed
    #TODO Print to CSV if Everything is Filled
    if mL.PlayingStreak >= 11:
        with open('stats/userStats.csv', 'a', newline='') as csvfile:
            writer = csv.writer(csvfile, delimiter=';')
            writer.writerow(mL.arrayAI)

    mL.arrayAI[0] = mL.user
    mL.arrayAI[1] = str(mL.stats['GamesPlayedTotal'])
    mL.arrayAI[2] = str(mL.PlayingStreak)

    # This Function Moves Every ArrayValue by 2
    new = 22
    for q in range(1, 19):
        old = new - 2
        mL.arrayAI[new] = mL.arrayAI[old]
        new -= 1

    # Die Zwei Werte um Neu Hinzuzufügen [SSP] [W/L]
    mL.arrayAI[3] = userPlayed
    mL.arrayAI[4] = winner
