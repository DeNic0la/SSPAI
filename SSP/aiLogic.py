#This Function Predicts the Next Move of the Player and Returns wath the Computer is Playing
import mainLogic as mL
import tensorflow as tf
import keras
import numpy as np
def getAIPick():



#DATA FORMAT:
#USER   NumberOfPlayedGames PlayingStreak LastMove    SecondLastMove  ThirdLastMove   FourthLastMove  SixtLastMove
#SeventLastMove EightLAstMove NinetLastMove NextMove
#


data = #An dieser Stelle eine Funktion aufrufen um

model = keras.Sequential([
    keras.layers.Embedding(10,10),
    keras.layers.GlobalAveragePooling1D(),
    keras.layers.Dense(10, activation="relu"),
    keras.layers.Dense(1, activation="sigmoid")
])


model.compile(optimizer="adam", loss="binary_crossentropy", metrics=["accuracy"])

# Format: Simulating input data, Result
model.fit()

#Input Data
prediction = model.predict()