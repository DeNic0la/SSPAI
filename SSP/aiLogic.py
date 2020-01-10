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

    for tmp2 in range(len(mL.arrayAI)):
        print(mL.arrayAI[tmp2])

    le = sklearn.preprocessing.LabelEncoder()

    tUsername = list(data["Username"])
    tUsername.append(mL.arrayAI[0])
    Username = le.fit_transform(tUsername)

    tNumberOfPlayedGames = list(data["NumberOfPlayedGames"])
    tNumberOfPlayedGames.append(mL.arrayAI[1])
    NumberOfPlayedGames = le.fit_transform(tNumberOfPlayedGames)

    tPlayingStreak = list(data["PlayingStreak"])
    tPlayingStreak.append(mL.arrayAI[2])
    PlayingStreak = le.fit_transform(tPlayingStreak)

    tuserPick = list(data["userPick"])
    tuserPick.append(mL.arrayAI[3])
    userPick = le.fit_transform(tuserPick)

    tresult = list(data["result"])
    tresult.append(mL.arrayAI[4])
    result = le.fit_transform(tresult)

    tuserPick1 = list(data["userPick1"])
    tuserPick1.append(mL.arrayAI[5])
    userPick1 = le.fit_transform(tuserPick1)

    tresult1 = list(data["result1"])
    tresult1.append(mL.arrayAI[6])
    result1 = le.fit_transform(tresult1)

    tuserPick2 = list(data["userPick2"])
    tuserPick2.append(mL.arrayAI[7])
    userPick2 = le.fit_transform(tuserPick2)

    tresult2 = list(data["result2"])
    tresult2.append(mL.arrayAI[8])
    result2 = le.fit_transform(tresult2)

    tuserPick3 = list(data["userPick3"])
    tuserPick3.append(mL.arrayAI[9])
    userPick3 = le.fit_transform(tuserPick3)

    tresult3 = list(data["result3"])
    tresult3.append(mL.arrayAI[10])
    result3 = le.fit_transform(tresult3)

    tuserPick4 = list(data["userPick4"])
    tuserPick4.append(mL.arrayAI[11])
    userPick4 = le.fit_transform(tuserPick4)

    tresult4 = list(data["result4"])
    tresult4.append(mL.arrayAI[12])
    result4 = le.fit_transform(tresult4)

    tuserPick5 = list(data["userPick5"])
    tuserPick5.append(mL.arrayAI[13])
    userPick5 = le.fit_transform(tuserPick5)

    tresult5 = list(data["result5"])
    tresult5.append(mL.arrayAI[14])
    result5 = le.fit_transform(tresult5)

    tuserPick6 = list(data["userPick6"])
    tuserPick6.append(mL.arrayAI[15])
    userPick6 = le.fit_transform(tuserPick6)

    tresult6 = list(data["result6"])
    tresult6.append(mL.arrayAI[16])
    result6 = le.fit_transform(tresult6)

    tuserPick7 = list(data["userPick7"])
    tuserPick7.append(mL.arrayAI[17])
    userPick7 = le.fit_transform(tuserPick7)

    tresult7 = list(data["result7"])
    tresult7.append(mL.arrayAI[18])
    result7 = le.fit_transform(tresult7)

    tuserPick8 = list(data["userPick8"])
    tuserPick8.append(mL.arrayAI[19])
    userPick8 = le.fit_transform(tuserPick8)

    tresult8 = list(data["result8"])
    tresult8.append(mL.arrayAI[20])
    result8 = le.fit_transform(tresult8)

    tuserPick9 = list(data["userPick9"])
    tuserPick9.append(mL.arrayAI[21])
    userPick9 = le.fit_transform(tuserPick9)

    tresult9 = list(data["result9"])
    tresult9.append(mL.arrayAI[22])
    result9 = le.fit_transform(tresult9)

    # nextUserPick = le.fit_transform(list(data["nextUserPick"]))

    # inputForModel = np.array(zip(Username, NumberOfPlayedGames, PlayingStreak, userPick, result, userPick1, result1,
    #                             userPick2, result2, userPick3, result3, userPick4, result4, userPick5, result5, userPick6,
    #                             result6, userPick7, result7, userPick8, result8, userPick9, result9))
    inputNames = ["Username", "NumberOfPlayedGames", "PlayingStreak", "userPick", "result", "userPick1", "result1",
                  "userPick2", "result2", "userPick3", "result3", "userPick4", "result4", "userPick5", "result5",
                  "userPick6", "result6", "userPick7", "result7", "userPick8", "result8", "userPick9", "result9"]

    np.array(data.drop([toPredict], 1))
    ###LAtest DONE ++++++ Added [] @#@#@#@#@#@#@#

    nextPick = np.array(result9)
    useForLen = len(nextPick) - 1
    print("Gugurugu")
    # print(nextPick)

    # Input from Current
    inputFromCurrent = list(zip([np.array(Username[len(Username) - 1]),
                                 np.array(NumberOfPlayedGames[len(NumberOfPlayedGames) - 1]),
                                 np.array(PlayingStreak[len(PlayingStreak) - 1]), np.array(userPick[len(userPick) - 1]),
                                 np.array(result[len(result) - 1]), np.array(userPick1[len(userPick1) - 1]),
                                 np.array(result1[len(result1) - 1]), np.array(userPick2[len(userPick2) - 1]),
                                 np.array(result2[len(result2) - 1]), np.array(userPick3[len(userPick3) - 1]),
                                 np.array(result3[len(result3) - 1]), np.array(userPick4[len(userPick4) - 1]),
                                 np.array(result4[len(result4) - 1]), np.array(userPick5[len(userPick5) - 1]),
                                 np.array(result5[len(result5) - 1]), np.array(userPick6[len(userPick6) - 1]),
                                 np.array(result6[len(result6) - 1]), np.array(userPick7[len(userPick7) - 1]),
                                 np.array(result7[len(result7) - 1]), np.array(userPick8[len(userPick8) - 1]),
                                 np.array(result8[len(result8) - 1]), np.array(userPick9[len(userPick9) - 1]),
                                 np.array(result9[len(result9) - 1])]))

    print("Now Printing the Values for Current match in AI accaptable Format")
    for tmp3 in range(len(inputFromCurrent)):
        print(inputFromCurrent[tmp3])

    # We First But the Data from  The Past and the Data to calculate the Predict for together an then but it in AI Accaptable Format or how normal Humans say: Numbers
    # Now we need this very last part removed from the Array and put into its own Array

    inputForModel = []

    inputForModel.append(np.array(Username[:-1]))
    inputForModel.append(np.array(NumberOfPlayedGames[:-1]))
    inputForModel.append(np.array(PlayingStreak[:-1]))
    inputForModel.append(np.array(userPick[:-1]))
    inputForModel.append(np.array(result[:-1]))
    inputForModel.append(np.array(userPick1[:-1]))
    inputForModel.append(np.array(result1[:-1]))
    inputForModel.append(np.array(userPick2[:-1]))
    inputForModel.append(np.array(result2[:-1]))
    inputForModel.append(np.array(userPick3[:-1]))
    inputForModel.append(np.array(result3[:-1]))
    inputForModel.append(np.array(userPick4[:-1]))
    inputForModel.append(np.array(result4[:-1]))
    inputForModel.append(np.array(userPick5[:-1]))
    inputForModel.append(np.array(result5[:-1]))
    inputForModel.append(np.array(userPick6[:-1]))
    inputForModel.append(np.array(result6[:-1]))
    inputForModel.append(np.array(userPick7[:-1]))
    inputForModel.append(np.array(result7[:-1]))
    inputForModel.append(np.array(userPick8[:-1]))
    inputForModel.append(np.array(result8[:-1]))
    inputForModel.append(np.array(userPick9[:-1]))
    inputForModel.append(np.array(result9[:-1]))

    reShapedArray = []
    for cou in range(useForLen):
        tmpArray = []
        tmpArray.append(Username[cou])
        tmpArray.append(NumberOfPlayedGames[cou])
        tmpArray.append(PlayingStreak[cou])
        tmpArray.append(userPick[cou])
        tmpArray.append(result[cou])
        tmpArray.append(userPick1[cou])
        tmpArray.append(result1[cou])
        tmpArray.append(userPick2[cou])
        tmpArray.append(result2[cou])
        tmpArray.append(userPick3[cou])
        tmpArray.append(result3[cou])
        tmpArray.append(userPick4[cou])
        tmpArray.append(result4[cou])
        tmpArray.append(userPick5[cou])
        tmpArray.append(result5[cou])
        tmpArray.append(userPick6[cou])
        tmpArray.append(result6[cou])
        tmpArray.append(userPick7[cou])
        tmpArray.append(result7[cou])
        tmpArray.append(userPick8[cou])
        tmpArray.append(result8[cou])
        tmpArray.append(userPick9[cou])
        tmpArray.append(result9[cou])
        reShapedArray.append(tmpArray)
    # print(reShapedArray)

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
    model.add(keras.layers.Dense(23, input_dim=23, init='lecun_uniform', activation='tanh'))
    model.add(keras.layers.Dense(23, activation="relu"))
    model.add(keras.layers.Dense(3, activation="softmax"))

    for layer in model.layers:
        print(layer.output_shape)
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

    # inputForModel = np.array([[1, 2], [3, 4], [5, 6], [7, 8], [9, 10], [11, 12], [13, 14], [15, 16], [17, 18], [19, 20]])
    # result = np.array([3, 7, 11, 15, 19, 23, 27, 31, 35, 39])

    # HERE
    # HERE
    # HERE

    nextPick = []
    nUP = list(data["nextUserPick"])
    for A in range(len(list(data["nextUserPick"]))):
        nextPick.append(TextToArr(nUP[A]))
    # Format: Simulating input data, Result , epochs
    print("INPUTFORMODEL")
    print(np.array(inputForModel))
    print("RESHAPED")
    print(np.array(reShapedArray))
    print("NEXT PICK")
    print(np.array(nextPick))

    print("Lenge toPredict")
    # print(len(np.array(nextPick)))
    print("Länge von Reshaped und InputForModel")
    print(len(np.array(reShapedArray)))
    print(len(np.array(inputForModel)))
    pass
    model.fit(np.array(reShapedArray), np.array(nextPick), epochs=300, validation_split=0.1)
    print(inputFromCurrent)
    predictInput = []  # np.array()
    for i in range(len(inputFromCurrent)):
        print(inputFromCurrent[i][0])
        predictInput.append(int(inputFromCurrent[i][0]))
    addArray = np.array([predictInput])
    print(predictInput)
    print(np.transpose(predictInput))
    print("The ADD ARRAY:")
    print(addArray)
    print(np.transpose(addArray))
    AiPredict = model.predict(addArray)
    print(AiPredict)
    print("\nSchere Warscheinlichkeit:")
    print(((AiPredict[0][0]) * 100))
    print("\nStein Warscheinlichkeit:")
    print(((AiPredict[0][1]) * 100))
    print("\nPapier Warscheinlichkeit:")
    print(((AiPredict[0][2]) * 100))
    print("\n")
    print(np.argmax(AiPredict))

    ### np.argmax
    print("AI Predicts:")
    print(str(AiPredict))
    # test2 = AiPredict
    # AiPredict += 0.5
    # print(int(AiPredict))
    # AiPredictText = le.inverse_transform(np.array([int(AiPredict)]))
    # print(AiPredictText)
    # return AiPredictText

    # Input Data
    # prediction = model.predict([])
    # print(prediction)
    # print(model.predict([10, 11]))

    return smartPick(AiPredict[0])


def TextToArr(inputText):
    if inputText == "Schere":
        return [1, 0, 0]
    elif inputText == "Stein":
        return [0, 1, 0]
    elif inputText == "Papier":
        return [0, 0, 1]
    else:
        print("You Vegan just made a Big Mistake...")
        return "LMAO"


def ArrToText(inputArr):
    if inputArr == [1, 0, 0]:
        return "Schere"
    if inputArr == [0, 1, 0]:
        return "Stein"
    if inputArr == [0, 0, 1]:
        return "Papier"
    else:
        print(
            "You Just gave us an Input with more than one Activatet Play This is Not Possible. I am Just Gone Print "
            "some Errors Lol ")
        print("Just kidding i am Not, You suck LOL")
        return "LMAO"


def ArgMaxPredictToText(inp):
    if inp == 0:
        return "Schere"
    if inp == 1:
        return "Stein"
    if inp == 2:
        return "Papier"
    print("Fehler bei ARG MAX TO TEXT !!!!")


def smartPick(AiArray):
    rec = np.argmax(AiArray)
    if (AiArray[np.argmax(AiArray)] - AiArray[np.argmin(AiArray)]) >= 0.3:
        if AiArray[3 - (np.argmax(AiArray) + np.argmin(AiArray))] < 0.3:
            return ArgMaxPredictToText(isBeaten(rec))
        elif AiArray[rec] >= 0.8:
            return ArgMaxPredictToText(isBeaten(rec))

    return ArgMaxPredictToText(Beats(np.argmin(AiArray)))


def isBeaten(inp):
    if inp == 0:
        return 1
    if inp == 1:
        return 2
    if inp == 2:
        return 0
    else:
        print("Ein Fehler ist Aufgetreten bei isBeaten")
        return "GUGUS"


def Beats(inp):
    if inp == 0:
        return 2
    if inp == 1:
        return 0
    if inp == 2:
        return 1
    else:
        print("Ein Fehler ist Aufgetreten bei Beats")
        return "GUGUS V2"
