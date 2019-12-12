def getCompPick():
    import random
    toChose = ['Schere', 'Stein', 'Papier']
    for makeCompPick in random.sample(toChose, len(toChose)):
        return makeCompPick