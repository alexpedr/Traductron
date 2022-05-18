# -*- coding: utf-8 -*-
"""
Created on Wed Mar 16 12:19:59 2022

@author: PC
"""
import pandas as pd
import numpy as np 

#axis = 0
final = pd.read_excel("./NUEVODATASET/A1.xlsx")

for valorLetra in range(65,90):
    letra = chr(valorLetra)
    for i in range(1, 4):
        letra1 = str(letra) + str(i)
        if (valorLetra == 65 and i == 1):
            x=0
        else:
            v='./NUEVODATASET/' + letra1 + ".xlsx"
            tabla = pd.read_excel('./NUEVODATASET/' + letra1 + ".xlsx")
            final = pd.concat([final, tabla], axis=0)

    
final.to_excel("./NUEVODATASET/final.xlsx")