# -*- coding: utf-8 -*-
"""
Created on Wed Apr 27 16:36:00 2022

@author: PC
"""

from gtts import gTTS #pip install gtts
import os
from playsound import playsound #HAY QUE HACER pip install playsound==1.2.2, si decargamos la más nueva no funcionará

resultado = gTTS("Prueba", lang="es")

resultado.save("resultado.mp3")
playsound("resultado.mp3")

def generarSonido(numeroDeLetra):
    #El numero se supone que será de 0 a 27
    ASCII = numeroDeLetra + 65
    resultado = chr(ASCII)
    audio = gTTS(resultado, lang="es")
    resultado.save("resultado.mp3")
    playsound("resultado.mp3")