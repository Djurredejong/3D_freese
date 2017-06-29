#!/usr/bin/env python

import os, sys#, pygame 
#from pygame import locals
import time
import RPi.GPIO as GPIO

stepDelay = 0.002

# Define GPIO pins where the in1-in4 pins of 
# the ULN2003 board are connected to
p1 = 11 #17
p2 = 12 #18
p3 = 15 #22
p4 = 16 #23
q1 = 31
q2 = 32 
q3 = 35
q4 = 36

def setup_motor(p1,p2,p3,p4):
  GPIO.setmode(GPIO.BOARD)

  # set up motor 
  GPIO.setup(p1, GPIO.OUT)
  GPIO.setup(p2, GPIO.OUT)
  GPIO.setup(p3, GPIO.OUT)
  GPIO.setup(p4, GPIO.OUT)

  GPIO.output(p1, GPIO.LOW)
  GPIO.output(p2, GPIO.LOW)
  GPIO.output(p3, GPIO.LOW)
  GPIO.output(p4, GPIO.LOW)

# a 0.18 degree (counter)clockwise rotation
def cw(sequence):
  sequence = sequence[1:]+sequence[:1]
  step(sequence)
  return sequence  

def ccw(sequence):
  sequence = sequence[3:]+sequence[:3]
  step(sequence)
  return sequence  
  
def step(a):
  GPIO.output(a[0], GPIO.LOW)
  GPIO.output(a[1], GPIO.LOW)
  GPIO.output(a[2], GPIO.HIGH)
  GPIO.output(a[3], GPIO.HIGH)

setup_motor(p1,p2,p3,p4)
setup_motor(q1,q2,q3,q4)
seq1 = [p1,p2,p3,p4]
seq2 = [q1,q2,q3,q4]
for i in range(2000):
  seq1 = cw(seq1)
  seq2 = ccw(seq2)
  time.sleep(stepDelay)

#for i in range(2000):
#  sequence = ccw(sequence)
#  time.sleep(stepDelay)

GPIO.cleanup()
