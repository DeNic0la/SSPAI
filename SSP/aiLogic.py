# This Function Predicts the Next Move of the Player and Returns wath the Computer is Playing
import mainLogic as mL
import tensorflow as tf
import keras
import numpy as np
import pandas as pd
import sklearn
import sklearn
from sklearn import preprocessing


def getAIPick():
    pass


# DATA FORMAT:
# USER   NumberOfPlayedGames PlayingStreak LastMove    SecondLastMove  ThirdLastMove   FourthLastMove  SixtLastMove
# SeventLastMove EightLAstMove NinetLastMove NextMove
# last Move = What user Picked , who Wins

data = pd.read_csv("stats/userStats.csv", sep=";")
data = data[
    ["Username", "NumberOfPlayedGames", "PlayingStreak", "userPick", "result", "userPick1", "result1", "userPick2",
     "result2", "userPick3", "result3", "userPick4", "result4", "userPick5", "result5", "userPick6", "result6",
     "userPick7", "result7", "userPick8", "result8", "userPick9", "result9", "nextUserPick"]]
toPredict = "nextUserPick"

le = sklearn.preprocessing.LabelEncoder()
Username = le.fit_transform(list(data["Username"]))
NumberOfPlayedGames = le.fit_transform(list(data["NumberOfPlayedGames"]))
PlayingStreak = le.fit_transform(list(data["PlayingStreak"]))
userPick = le.fit_transform(list(data["userPick"]))
result = le.fit_transform(list(data["result"]))
userPick1 = le.fit_transform(list(data["userPick1"]))
result1 = le.fit_transform(list(data["result1"]))
userPick2 = le.fit_transform(list(data["userPick2"]))
result2 = le.fit_transform(list(data["result2"]))
userPick3 = le.fit_transform(list(data["userPick3"]))
result3 = le.fit_transform(list(data["result3"]))
userPick4 = le.fit_transform(list(data["userPick4"]))
result4 = le.fit_transform(list(data["result4"]))
userPick5 = le.fit_transform(list(data["userPick5"]))
result5 = le.fit_transform(list(data["result5"]))
userPick6 = le.fit_transform(list(data["userPick6"]))
result6 = le.fit_transform(list(data["result6"]))
userPick7 = le.fit_transform(list(data["userPick7"]))
result7 = le.fit_transform(list(data["result7"]))
userPick8 = le.fit_transform(list(data["userPick8"]))
result8 = le.fit_transform(list(data["result8"]))
userPick9 = le.fit_transform(list(data["userPick9"]))
result9 = le.fit_transform(list(data["result9"]))
nextUserPick = le.fit_transform(list(data["nextUserPick"]))

#inputForModel = np.array(zip(Username, NumberOfPlayedGames, PlayingStreak, userPick, result, userPick1, result1,
#                             userPick2, result2, userPick3, result3, userPick4, result4, userPick5, result5, userPick6,
#                             result6, userPick7, result7, userPick8, result8, userPick9, result9))
nextPick = np.array(nextUserPick)

inputForModel = []
inputForModel.append(Username)
inputForModel.append(NumberOfPlayedGames)
inputForModel.append(PlayingStreak)
inputForModel.append(userPick)
inputForModel.append(result)
inputForModel.append(userPick1)
inputForModel.append(result1)
inputForModel.append(userPick2)
inputForModel.append(result2)
inputForModel.append(userPick3)
inputForModel.append(result3)
inputForModel.append(userPick4)
inputForModel.append(result4)
inputForModel.append(userPick5)
inputForModel.append(result5)
inputForModel.append(userPick6)
inputForModel.append(result6)
inputForModel.append(userPick7)
inputForModel.append(result7)
inputForModel.append(userPick8)
inputForModel.append(result8)
inputForModel.append(userPick9)
inputForModel.append(result9)



# inputForModel = np.array(data.drop([toPredict], 1))
# result = np.array(data[toPredict])


# opendata = open('stats/userStats.csv')
# inhalt = opendata.read()
# data = []
# zeilen = inhalt.split('\n')


# for cur in range(len(zeilen)):
#   spalten = zeilen[cur].split(';')
#  print(spalten)
# data.append(spalten)
# opendata.close()


model = keras.Sequential()
model.add(keras.layers.Embedding(880000, 16))
model.add(keras.layers.GlobalAveragePooling1D())
model.add(keras.layers.Dense(23, activation="relu"))
model.add(keras.layers.Dense(1, activation="sigmoid"))


model.compile(optimizer="adam", loss="binary_crossentropy", metrics=["accuracy"])

# Bring Data in a Format witch goes with model.fit
# inputForModel = [['0' for xy in range(23)] for yx in range(len(data))]
# result = ['0' for xk in range(len(data))]
# print(len(data))
# for cur2 in range(len(data) - 1):
#   for pos in range(23):
#      print(data[cur2][pos])
#     inputForModel[cur2][pos] = data[cur2][pos]
# result[cur2] = data[cur2][23]
# print(result[cur2])

# TODO DELETE The FOLLOWING LINES UNTIL "HERE"

#inputForModel = np.array([[1, 2], [3, 4], [5, 6], [7, 8], [9, 10], [11, 12], [13, 14], [15, 16], [17, 18], [19, 20]])
#result = np.array([3, 7, 11, 15, 19, 23, 27, 31, 35, 39])

# HERE
# HERE
# HERE

# Format: Simulating input data, Result , epochs
model.fit(inputForModel, nextPick, epochs=30, validation_split=0.1)

# Input Data
# prediction = model.predict([Nicola, 52, 20, Papier, userWin, Stein, compWin])
# print(prediction)
#print(model.predict([10, 11]))
