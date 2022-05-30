#                                    .';:cc;.
#                                .,',;lol::c.
#                                ;';lddddlclo
#                                lcloxxoddodxdool:,.
#                                cxdddxdodxdkOkkkkkkkd:.
#                         .ldxkkOOOOkkOO000Okkxkkkkx:.
#                    .lddxkkOkOOO0OOO0000Okxxxxkkkk:
#                 'ooddkkkxxkO0000KK00Okxdoodxkkkko
#                .ooodxkkxxxOO000kkkO0KOxolooxkkxxkl
#                lolodxkkxxkOx,.                .lkdolodkkxxxO.
#                doloodxkkkOk                            ....        .,cxO;
#                ddoodddxkkkk:                        ,oxxxkOdc'..o'
#                :kdddxxxxd,    ,lolccldxxxkkOOOkkkko,
#                 lOkxkkk;    :xkkkkkkkkOOO000OOkkOOk.
#                    ;00Ok' 'O000OO0000000000OOOO0Od.
#                        .l0l.;OOO000000OOOOOO000000x,
#                                .'OKKKK00000000000000kc.
#                                        .:ox0KKKKKKK0kdc,.
#                                                         ...
#
# Author: peppe8o
# Date: Feb 24th, 2020
# version: 1.2

# Import required libraries
import sys
import time
import RPi.GPIO as GPIO

# define variables
chan_list = [27,22,10,9] # GPIO ports to use
delay=.0015 # delay between each sequence step

# Use BCM GPIO references
# instead of physical pin numbers
GPIO.setmode(GPIO.BCM)

# Set all pins as output
for pin in chan_list:
    print("Setup pins")
    GPIO.setup(pin,GPIO.OUT)

#initialize array for sequence shift
arr1 = [1,1,0,0]
arr2 = [0,1,0,0]

def move():
    global arr1 # enables the edit of arr1 var inside a function
    global arr2 # enables the edit of arr2 var inside a function
    arrOUT = arr1[3:]+arr1[:3] # rotates array values of 1 digit
    arr1 = arr2
    arr2 = arrOUT
    GPIO.output(chan_list, arrOUT)
    time.sleep(delay)
# Start main loop
def bajar():
    global arr1 # enables the edit of arr1 var inside a function
    global arr2 # enables the edit of arr2 var inside a function
    arrOUT = arr1[1:]+arr1[:1] # rotates array values of 1 digit
    arr1 = arr2
    arr2 = arrOUT
    GPIO.output(chan_list, arrOUT)
    time.sleep(delay)
class stepper:
    def __init__(self):
        self.contador = 0
    def subirCamaraInicial(self):
        while(self.contador < 1000):
            move()
            self.contador += 1
    def bajarCamaraFinal(self):
        while(self.contador > 0):
            bajar()
            self.contador -= 1
    def subirXPuntos(self,cantidadPuntos):
        cantidad = 0
        while(self.contador < 1800 and cantidad < cantidadPuntos):
          self.contador += 1
          move()
          cantidad += 1
    def bajarXPuntos(self,cantidadPuntos):
        cantidad = 0
        while(self.contador > 100 and cantidad < cantidadPuntos):
          self.contador -= 1
          bajar()
          cantidad += 1