import RPi.GPIO as GPIO
from math import floor
from time import sleep

class Motor:
  def __init__(self,p1,p2,p3,p4):
    self.p1=p1
    self.p2=p2
    self.p3=p3
    self.p4=p4
    self.seq = [self.p1,self.p2,self.p3,self.p4]
    self.stepDelay = 0.002

    self.setup()

  def __exit__(self):
    GPIO.cleanup()

  def off(self):
    self.__exit__()

  def setup(self):
    GPIO.setmode(GPIO.BOARD)
    for pin in self.seq:
      GPIO.setup(pin, GPIO.OUT)
      GPIO.output(pin, GPIO.LOW)

  def cw(self,steps=1):
    for i in range(steps):
      self.seq = self.seq[1:]+self.seq[:1]
      self.step()
      if steps>1:
        sleep(self.stepDelay)

  def ccw(self,steps=1):
    for i in range(steps):
      self.seq = self.seq[3:]+self.seq[:3]
      self.step()
      if steps>1:
        sleep(self.stepDelay)
  
  def step(self):
    GPIO.output(self.seq[0], GPIO.LOW)
    GPIO.output(self.seq[1], GPIO.LOW)
    GPIO.output(self.seq[2], GPIO.HIGH)
    GPIO.output(self.seq[3], GPIO.HIGH)

  def degrees_cw(self,degrees=1.8):
    self.cw(int(floor(degrees/0.18)))

  def degrees_ccw(self,degrees=1.8):
    self.ccw(int(floor(degrees/0.18)))

  def rotate(self, degrees=1.8):
    if degrees > 0:
      self.degrees_cw(degrees) 
    else:
      self.degrees_ccw(-degrees) 

