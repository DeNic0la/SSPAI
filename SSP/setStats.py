#This Function sets The Global Array Stats



def setStats(winneris, stats):
    if winneris == "same":
        return stats
    elif winneris == "compWin":
        stats['compWins'] += 1
        return stats
    elif winneris == "userWin":
        stats['userWins'] += 1
        return stats