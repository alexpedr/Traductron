# -*- coding: utf-8 -*-
"""
Created on Sun May 29 14:45:01 2022

@author: PC
"""

# -*- coding: utf-8 -*-
"""
Created on Sun May 29 09:40:47 2022

@author: PC
"""

# -*- coding: utf-8 -*-
"""
Created on Fri May 27 11:39:35 2022

@author: PC
"""

import random
import socket, select
from time import gmtime, strftime
from random import randint

from HandDetector import *
from altavoz import *
import cv2
import mediapipe as mp
import numpy as np
import os
mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles
mp_pose = mp.solutions.pose

# For static images:
IMAGE_FILES = []
BG_COLOR = (192, 192, 192) # gray
with mp_pose.Pose(
    static_image_mode=True,
    model_complexity=2,
    enable_segmentation=True,
    min_detection_confidence=0.5) as pose:
  for idx, file in enumerate(IMAGE_FILES):
    image = cv2.imread(file)
    image_height, image_width, _ = image.shape
    # Convert the BGR image to RGB before processing.
    results = pose.process(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))

    if not results.pose_landmarks:
      continue
    print(
        f'Nose coordinates: ('
        f'{results.pose_landmarks.landmark[mp_pose.PoseLandmark.NOSE].x * image_width}, '
        f'{results.pose_landmarks.landmark[mp_pose.PoseLandmark.NOSE].y * image_height})'
    )
    print(results.pose_landmarks)
    annotated_image = image.copy()
    # Draw segmentation on the image.
    # To improve segmentation around boundaries, consider applying a joint
    # bilateral filter to "results.segmentation_mask" with "image".
    condition = np.stack((results.segmentation_mask,) * 3, axis=-1) > 0.1
    bg_image = np.zeros(image.shape, dtype=np.uint8)
    bg_image[:] = BG_COLOR
    annotated_image = np.where(condition, annotated_image, bg_image)
    # Draw pose landmarks on the image.
    mp_drawing.draw_landmarks(
        annotated_image,
        results.pose_landmarks,
        mp_pose.POSE_CONNECTIONS,
        landmark_drawing_spec=mp_drawing_styles.get_default_pose_landmarks_style())
    cv2.imwrite('/tmp/annotated_image' + str(idx) + '.png', annotated_image)
    # Plot pose world landmarks.
    mp_drawing.plot_landmarks(
        results.pose_world_landmarks, mp_pose.POSE_CONNECTIONS)


imgcounter = 1
basename = "image%s.jpg"

HOST = '192.168.43.112'#'192.168.43.112'
PORT = 6666

connected_clients_sockets = []

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_socket.bind((HOST, PORT))
server_socket.listen(10)

connected_clients_sockets.append(server_socket)
buffer_size = 4096

print("Se comienza el server")
detector = handDetector()
clasificador = pickle.load(open("redNeuronal.sav","rb"))
contador = 0
while True:

    read_sockets, write_sockets, error_sockets = select.select(connected_clients_sockets, [], [])
    for sock in read_sockets:

        if sock == server_socket:

            sockfd, client_address = server_socket.accept()
            connected_clients_sockets.append(sockfd)

        else:
            try:
                print (' Buffer size is %s' % buffer_size)
                if buffer_size > 4096:
                    data = sock.recv(buffer_size,socket.MSG_WAITALL)
                else:
                    data = sock.recv(buffer_size)
                print("HE RECIBDIDO EL SIZE")
                txt = str(data)
                txt = txt[2:-1]
                tmp = txt.split()
                if tmp[0] == 'SIZE':
                    #tmp = txt.split()
                    size = int(tmp[1])

                    print ('got size')
                    print ('size is %s' % size)

                    sock.sendto("GOT SIZE".encode(),("192.168.43.16",22))
                    # Now set the buffer size for the image 
                    buffer_size = size

                elif txt.startswith('BYE'):
                    sock.shutdown()

                elif data:
                    
                    #print(txt)
                    
                    myfile = open("./fotoMano.jpg", 'wb')
                    if not data:
                        myfile.close()
                        print("Ha fallado algo")
                        break
                    print("VOY A ESCRIBIR LOS DATOS")
                    myfile.write(data)
                    myfile.close()
                    
                    
                    print("HE RECIBIDO LA IMAGEN")
                    
                    sock.sendto("GOT IMAGE".encode(),("192.168.43.16",22))
                    buffer_size = 4096
                    
                    print("HE ENVIADO EL GOT IMAGE")
                    img = cv2.imread("fotoMano.jpg")
                    
                    with mp_pose.Pose(
                        min_detection_confidence=0.5,
                        min_tracking_confidence=0.5) as pose:
                        # To improve performance, optionally mark the image as not writeable to
                        # pass by reference.
                            
                            img.flags.writeable = False
                            try:
                                img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
                            except:
                                print("HA habido un error")
                            print("ESTOY AQUI")
                            results = pose.process(img)
                            
                            lm = results.pose_landmarks
                            
                            lmPose = mp_pose.PoseLandmark
                            
                            
                            h, w = img.shape[:2]
                            
                            if lm is not None:
                                l_shldr_x = int(lm.landmark[lmPose.LEFT_SHOULDER].x * w)
                                l_shldr_y = int(lm.landmark[lmPose.LEFT_SHOULDER].y * h)
                                
                                r_shldr_x = int(lm.landmark[lmPose.RIGHT_SHOULDER].x * w)
                                r_shldr_y = int(lm.landmark[lmPose.RIGHT_SHOULDER].y * h)
                            
                                r_hand_x =  int(lm.landmark[lmPose.RIGHT_WRIST].x * w)
                                r_hand_y =  int(lm.landmark[lmPose.RIGHT_WRIST].y * h)
                                
                                l_hand_x =  int(lm.landmark[lmPose.LEFT_WRIST].x * w)
                                l_hand_y =  int(lm.landmark[lmPose.LEFT_WRIST].y * h)
                            else:
                                l_shldr_x = w/2
                                l_shldr_y = 0
                                
                                r_shldr_x = w/2
                                r_shldr_y = 0
                            
                                r_hand_x =  w/2
                                r_hand_y =  0
                                
                                l_hand_x =  w/2
                                l_hand_y =  0
                            print("HOLA HOLA HOLA")
                            results = pose.process(img)
                            print("TENGO LOS RESULTADOS")
                            lm = results.pose_landmarks
                            lmPose = mp_pose.PoseLandmark
                            print("Se tienen los results")
                            img = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)
                            img = detector.findHands(img)
                            
                            #print(r_hand_y)
                            
                            cv2.imwrite("fotoPuntos.jpg",img)
                            cv2.imshow("fotoMano.jpg",img)
                            lista = cp.deepcopy(detector.guardarValores(img))
                            listaVacia = np.zeros(42)
                            listaFinal = []
                            
                            listaFinal.append(lista)
                            
                            listaFinal.append(listaVacia)
                            prediccion = 0
                            if(len(listaFinal[0]) !=0):
                                prediccion = clasificador.predict(listaFinal)
                                prediccion = prediccion[0]
                                with open('movimiento.txt', 'w') as f:
                                    f.write("S")
                                    print("HE PREDECIDO")
                                generarSonido(prediccion)
                            else:
                                with open('movimiento.txt', 'w') as f:
                                    if(r_hand_y > h and r_hand_x < w/5):
                                        print("Bajar camara a la derecha")
                                        f.write("RD")
                                    elif(r_hand_y > h and r_hand_x > 4*w/5):
                                        print("Bajar camara a la izquierda")
                                        f.write("LD")
                                    elif(r_hand_y < h/3 and r_hand_x < w/5): #Estaba a 5
                                        print("Subir camara a la derecha")
                                        f.write("RU")
                                    elif(r_hand_x > 4*w/5 and r_hand_y < h/3):
                                        print("Subir camara a la izquierda")
                                        f.write("IU")
                                    elif(r_hand_y < h/3):
                                        print("Subir camara")
                                        f.write("U")
                                    elif(r_hand_y > h):
                                        print("Bajar camara")
                                        f.write("D")
                                    elif(r_hand_x < w/5):
                                        print("Girar camara a la derecha")
                                        f.write("R")
                                    elif(r_hand_x > 4*w/5):
                                        print("Girar camara a la izquierda")
                                        f.write("L")
                                    elif(r_hand_x > w/5 and r_hand_x < 4*w/5 and r_hand_y < h and r_hand_y > h/3):
                                        print("Quieto")
                                        f.write('S')
                                    else:
                                        f.write('U')
                            print("Se ha escrito el pdf")
                            archivoMovimiento = open('movimiento.txt', 'rb')
                            archivoMovimientoBytes = archivoMovimiento.read()
                            print(archivoMovimientoBytes)
                            sock.sendto(archivoMovimientoBytes,("192.168.43.16",22))
                            buffer_size = 4096
                            print("HE ENVIADO EL TXT")
                            contador += 1
                            print(contador)
                            if prediccion == 0:
                                print("NO SE PUEDE LEER")
                            else:
                                print(chr(65+prediccion))
                            print("LLEGO HASTA AQUI")
                            #altavoz.generarSonido(65+prediccion)
                            #prediccion = chr(65+prediccion)
                            
            except:
                #sock.close()
                #print("SE CIERRA LA CONEXION")
                #connected_clients_sockets.remove(sock)
                continue
        imgcounter += 1
server_socket.close()