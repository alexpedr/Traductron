# -*- coding: utf-8 -*-
"""
Created on Wed Mar 16 12:12:49 2022

@author: PC
"""

import pandas as pd
import numpy as np 
import matplotlib.pyplot as plt
import sklearn
from sklearn.neural_network import MLPClassifier

from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
from math import sqrt
from sklearn.metrics import r2_score

import pickle

dataframeFinal = pd.read_excel("./LETRAS/final.xlsx",header=0)
del dataframeFinal["Unnamed: 0"]
del dataframeFinal["Unnamed: 0.1"]

#Lo desordenamos un poco
dataframeFinal = dataframeFinal.sample(frac=1)
print(dataframeFinal['valor']) #Comprobacion por 


X = dataframeFinal.iloc[:,:42]
Y = dataframeFinal.iloc[:,42]

X = np.array(X)
Y = np.array(Y)
X_train, X_test, y_train, y_test = train_test_split(X, Y, stratify=Y,random_state=1)


clasificador = MLPClassifier(random_state=1, max_iter=300).fit(X_train, y_train)
print(clasificador.predict(X_test[:10]))

nombreArchivo = "redNeuronal.sav"
pickle.dump(clasificador, open(nombreArchivo,'wb'))


