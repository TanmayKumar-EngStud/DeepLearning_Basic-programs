
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split


f = pd.read_csv("new.csv")
HP, Attack, Defense, sAttack, sDefense, Speed, Gen = f.iloc[:,1:2], f.iloc[:,2:3], f.iloc[:,3:4], f.iloc[:,4:5], f.iloc[:,5:6], f.iloc[:,6:7], f.iloc[:,7:8]
 
fLegendary = f.iloc[:,8:9]
X = f.iloc[:,1:9]
y = f.iloc[:,8:9]

X_train, X_test, y_train, y_test = train_test_split(X,y, test_size=0.33,train_size=0.66,random_state=(None),shuffle=(True),stratify=(None))

from sklearn.preprocessing import StandardScaler
ssC = StandardScaler()
X_train = ssC.fit_transform(X_train)
X_test = ssC.transform(X_test)

# Applying Artificial Neural Network 
    #first importing all the necessary libraries :-
import keras
from keras.models import Sequential
from keras.layers import Dense
from keras.layers import LeakyReLU, PReLU, ELU
from keras.layers import Dropout

classifier = Sequential()

classifier.add(Dense(units=5, kernel_initializer ='he_uniform', activation="relu",input_dim = 8))

classifier.add(Dense(units=10, kernel_initializer ='he_uniform', activation="relu"))

classifier.add(Dense(units=10, kernel_initializer ='he_uniform', activation="relu"))

classifier.add(Dense(units=1, kernel_initializer ='glorot_uniform', activation="sigmoid"))

classifier.compile(optimizer= 'adam',loss='binary_crossentropy', metrics = ['accuracy'])

model_history= classifier.fit(X_train, y_train, validation_split=0.33, batch_size=3, epochs = 4)
