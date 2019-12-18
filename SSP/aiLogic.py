#This Function Predicts the Next Move of the Player and Returns wath the Computer is Playing
import mainLogic as mL
import tensorflow as tf
import keras
import numpy as np
def getAIPick():
    pass


#DATA FORMAT:
#USER   NumberOfPlayedGames PlayingStreak LastMove    SecondLastMove  ThirdLastMove   FourthLastMove  SixtLastMove
#SeventLastMove EightLAstMove NinetLastMove NextMove
#last Move = What user Picked , who Wins


opendata = open('stats/userStats.csv')
inhalt = opendata.read()
data = []
zeilen = inhalt.split('\n')


for cur in range(len(zeilen)):
    spalten = zeilen[cur].split(';')
    print(spalten)
    data.append(spalten)
opendata.close()


model = keras.Sequential([
    keras.layers.Embedding(24,24),
    keras.layers.GlobalAveragePooling1D(),
    keras.layers.Dense(24, activation="relu"),
    keras.layers.Dense(1, activation="sigmoid")
])


model.compile(optimizer="adam", loss="binary_crossentropy", metrics=["accuracy"])

#Bring Data in a Format witch goes with model.fit
inputForModel = [[['0'] * len(data)] * 23]
result = [['0'] * len(data)]
print(len(data))
for cur2 in range(len(data) - 1):
    for pos in range(23):
        print(data[cur2][pos])
        inputForModel[cur2][pos] = data[cur2][pos]
    result[cur2] = data[cur2][23]
pass
# Format: Simulating input data, Result , epochs
model.fit(inputForModel, result, epochs=3 )

#Input Data
#prediction = model.predict([Nicola, 52, 20, Papier, userWin, Stein, compWin])
#print(prediction)