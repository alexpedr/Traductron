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

dataframeFinal = pd.read_excel("./NUEVODATASET/final.xlsx",header=0)
del dataframeFinal["Unnamed: 0"]
del dataframeFinal["Unnamed: 0.1"]

#Lo desordenamos un poco
dataframeFinal = dataframeFinal.sample(frac=1)
print(dataframeFinal['valor']) #Comprobacion por 


X = dataframeFinal.iloc[:,:42]
Y = dataframeFinal.iloc[:,42]

X = np.array(X)
Y = np.array(Y)
X_train, X_test, y_train, y_test = train_test_split(X, Y, stratify=Y,random_state=1,train_size=0.75)


clasificador = MLPClassifier(random_state=1, max_iter=110000, hidden_layer_sizes=(10000)).fit(X_train, y_train)
print("Se ha acabado de entrenar")
resultado = clasificador.predict(X_test[:len(X_test)])
print(resultado)
print(y_test[:len(y_test)])

cantidadAciertoXLetra = np.zeros(26)
cantidadLetra = np.zeros(26)
contadorAciertos = 0
contador = 0
for i in range(len(y_test)):
    if resultado[i] == y_test[i]:
        contadorAciertos += 1
        cantidadAciertoXLetra[resultado[i]] += 1
    cantidadLetra[y_test[i]] += 1

probAciertoXLetra = np.zeros(26)
for i in range(len(cantidadLetra)):
    if cantidadLetra[i] != 0:
        probAciertoXLetra[i] = cantidadAciertoXLetra[i] / cantidadLetra[i] 
print(contadorAciertos,"aciertos de ",len(y_test))
print("Probabilidad de acierto por letra: ")
for i in range(len(probAciertoXLetra)):
    print(chr(65+i), ":", probAciertoXLetra[i], "con",int(cantidadLetra[i]), "apariciones en el test")
    
guardar = input("Quieres guardar esta red neuronal?(y/n)")
if(guardar == 'y'):
    nombreArchivo = "redNeuronal.sav"
    pickle.dump(clasificador, open(nombreArchivo,'wb'))
    print("Se ha guardado")
else:
    print("No se ha guardado")
