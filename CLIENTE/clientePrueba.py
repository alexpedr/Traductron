#!/usr/bin/env python

import sys
import time
import RPi.GPIO as GPIO
from  stepper import *
from  puente_H import *

from picamera import PiCamera
from time import sleep
import os

camera = PiCamera()
camera.start_preview()

Stepper = stepper()
Ruedas = ruedas()
Ruedas.pwm_a.ChangeDutyCycle(int(0))
Ruedas.pwm_b.ChangeDutyCycle(int(0))

Stepper.subirCamaraInicial()

#Stepper.contador = 0

#Stepper.contador = 1700;
#Stepper.bajarCamaraFinal()


movimiento = 'S'

import random
import socket, select
from time import gmtime, strftime
from random import randint
import os
import time
image = "mano.jpg"

HOST = '192.168.43.112'
PORT = 6666

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = (HOST, PORT)
sock.connect(server_address)

def giro_derecha():
  contador = 0
  while(contador < 14000):
    Ruedas.giro_FavorRelojMotorA()
    Ruedas.giro_ContraRelojMotorB()
    contador += 1
def giro_izquierda():
  contador = 0
  while(contador < 14000):
    Ruedas.giro_ContraRelojMotorA()
    Ruedas.giro_FavorRelojMotorB()
    contador += 1
inicial = time.time()
while(True):
    try:
        time.sleep(1.3)
        #os.remove('/home/pi/Documents/mano.jpg')
        camera.capture('/home/pi/Documents/mano.jpg')
        
        myfile = open('mano.jpg', 'rb')
        bytes = myfile.read()
        size = len(bytes)
        sock.sendto(("SIZE %s" % size).encode(),(HOST,PORT))
        answer = sock.recv(4096)
        answer = answer.decode()
        print ('answer = %s' % answer)
        if answer == 'GOT SIZE':
            sock.sendto(bytes,(HOST,PORT))
            answer = sock.recv(4096)
            answer = answer.decode()
            print ('answer = %s' % answer)
            if answer == 'GOT IMAGE' :
                #sock.sendto(("BYE BYE ").encode(),(HOST,PORT))
                print ('SE HA PODIDO ENVIAR LA IMAGEN CORRECTAMENTE')
            
            movimientoData = sock.recv(4096)
            with open('movimiento.txt', 'wb') as f:
                f.write(movimientoData)
            with open('movimiento.txt', 'r') as f:
                letra = f.read()
                print(letra)
                if letra == 'S':
                  pass
                elif letra == 'U':
                  Stepper.subirXPuntos(500)
                elif letra == 'D':
                  Stepper.bajarXPuntos(500)
                elif letra == 'RD':
                  Stepper.bajarXPuntos(200)
                  Ruedas.pwm_a.ChangeDutyCycle(int(30))
                  Ruedas.pwm_b.ChangeDutyCycle(int(30))
                  
                  giro_derecha()
                  Ruedas.pwm_a.ChangeDutyCycle(int(0))
                  Ruedas.pwm_b.ChangeDutyCycle(int(0))
                elif letra == 'LD':
                  Stepper.bajarXPuntos(200)
                  Ruedas.pwm_a.ChangeDutyCycle(int(30))
                  Ruedas.pwm_b.ChangeDutyCycle(int(30))
                  
                  giro_izquierda()
                  Ruedas.pwm_a.ChangeDutyCycle(int(0))
                  Ruedas.pwm_b.ChangeDutyCycle(int(0))
                elif letra == 'RU':
                  Stepper.subirXPuntos(400)
                  Ruedas.pwm_a.ChangeDutyCycle(int(30))
                  Ruedas.pwm_b.ChangeDutyCycle(int(30))
                  
                  giro_derecha()
                  Ruedas.pwm_a.ChangeDutyCycle(int(0))
                  Ruedas.pwm_b.ChangeDutyCycle(int(0))
                elif letra == 'LU':
                  Stepper.subirXPuntos(400)
                  Ruedas.pwm_a.ChangeDutyCycle(int(30))
                  Ruedas.pwm_b.ChangeDutyCycle(int(30))
                  
                  giro_izquierda()
                  Ruedas.pwm_a.ChangeDutyCycle(int(0))
                  Ruedas.pwm_b.ChangeDutyCycle(int(0))
                elif letra == 'L':
                  Ruedas.pwm_a.ChangeDutyCycle(int(30))
                  Ruedas.pwm_b.ChangeDutyCycle(int(30))
                  
                  giro_izquierda()
                  Ruedas.pwm_a.ChangeDutyCycle(int(0))
                  Ruedas.pwm_b.ChangeDutyCycle(int(0))
                elif letra == 'R':
                  Ruedas.pwm_a.ChangeDutyCycle(int(30))
                  Ruedas.pwm_b.ChangeDutyCycle(int(30))
                  
                  giro_derecha()
                  Ruedas.pwm_a.ChangeDutyCycle(int(0))
                  Ruedas.pwm_b.ChangeDutyCycle(int(0))
            print("Se ha modificado el archivo de movimiento")
        myfile.close()
        print(time.time() - inicial)
    except KeyboardInterrupt:
        
        Stepper.bajarCamaraFinal()
        GPIO.output(chan_list, (0,0,0,0))
        camera.stop_preview()
        GPIO.cleanup()
        sock.close()
        sys.exit()
