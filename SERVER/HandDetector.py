# -*- coding: utf-8 -*-
"""
Created on Fri May 27 18:12:55 2022

@author: PC
"""


import cv2
import mediapipe as mp
import time
import copy as cp
import pandas as pd
import pickle
import numpy as np


class handDetector():
    def __init__(self, mode = False, maxHands = 2, detectionCon = 0.5, trackCon = 0.5):
        self.mode = mode
        self.maxHands = maxHands
        self.detectionCon = detectionCon
        self.trackCon = trackCon

        self.mpHands = mp.solutions.hands
        self.hands = self.mpHands.Hands(static_image_mode=False, max_num_hands=2, min_detection_confidence=0.5, min_tracking_confidence=0.5)
        self.mpDraw = mp.solutions.drawing_utils
        
    def findHands(self,img, draw = True):
        imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        self.results = self.hands.process(imgRGB)
        # print(results.multi_hand_landmarks)

        if self.results.multi_hand_landmarks:
            for handLms in self.results.multi_hand_landmarks:
                if draw:
                    self.mpDraw.draw_landmarks(img, handLms, self.mpHands.HAND_CONNECTIONS)
        return img
    
    def imprimirPosiciones(self, img, handNo = 0, draw = True):
        if self.results.multi_hand_landmarks:
            myHand = self.results.multi_hand_landmarks #Son 21 valores
            print("[ ")
            for punto in myHand:
                for lm in punto.landmark:
                    h, w, c = img.shape
                    cx, cy = int(lm.x * w), int(lm.y * h) #Las posiciones .x y .y son normalizadas, por eso se multiplica por el tamaño de anhura y altura de la pantalla
                    print(cx,cy)
                    if draw:
                        cv2.circle(img, (cx, cy), 3, (255, 0, 255), cv2.FILLED)
                print(" ]")
    def guardarValores(self, img, handNo = 0, draw = True):
        lista = [] #Deberia tener 42 valores, son 21 puntos y cada punto tiene un X y Y.
        if self.results.multi_hand_landmarks:
            myHand = self.results.multi_hand_landmarks #Son 21 valores
            for punto in myHand:
                for lm in punto.landmark:
                    h, w, c = img.shape
                    cx, cy = int(lm.x * w), int(lm.y * h) #Las posiciones .x y .y son normalizadas, por eso se multiplica por el tamaño de anhura y altura de la pantalla
                    lista.append(cx)
                    lista.append(cy)
        print("Ya se ha guardado el valor")
        return lista