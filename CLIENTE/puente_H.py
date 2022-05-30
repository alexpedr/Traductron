#!/usr/bin/env python

import RPi.GPIO as GPIO
import os
import time

class ruedas:
	def __init__(self):
		self.m2 = 2
		self.e2 = 3
		self.e1 = 4
		self.m1 = 17
		GPIO.setmode(GPIO.BCM)

		GPIO.setup(self.m2,GPIO.OUT)
		GPIO.setup(self.e2,GPIO.OUT)

		GPIO.setup(self.m1,GPIO.OUT)
		GPIO.setup(self.e1,GPIO.OUT)

		self.pwm_a = GPIO.PWM(self.e1,500)
		self.pwm_b = GPIO.PWM(self.e2,500)

		self.pwm_a.start(0)
		self.pwm_b.start(0)


	def giro_FavorRelojMotorA(self):
		GPIO.output(self.m1,False)
	def giro_ContraRelojMotorA(self):
		GPIO.output(self.m1,True)
	def giro_FavorRelojMotorB(self):
		GPIO.output(self.m2,False)
	def giro_ContraRelojMotorB(self):
		GPIO.output(self.m2,True)

  


