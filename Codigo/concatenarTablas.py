# -*- coding: utf-8 -*-
"""
Created on Wed Mar 16 12:19:59 2022

@author: PC
"""
import pandas as pd
import numpy as np 

#axis = 0
final = pd.read_excel("./LETRAS/A.xlsx")

for valorLetra in range(66,90):
    letra = chr(valorLetra)
    tabla = pd.read_excel('./LETRAS/' + letra +".xlsx")
    final = pd.concat([final,tabla],axis=0)
    
final.to_excel("./LETRAS/final.xlsx")