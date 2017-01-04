import CHIP_IO.GPIO as GPIO
import sys
import time
import pygame


def btndown():
  global aold
  global bold
  global cold


  a = GPIO.input("U14_14")
  b = GPIO.input("U14_16")
  c = GPIO.input("U14_18")
  event = 0
  if aold==1 and a == 0:
    event = 1
  if bold==1 and b == 0:
    event = 2
  if cold==1 and c == 0:
    event = 3
  aold = a
  bold = b
  cold = c
  return event

def stopplay():
  print "stopplay"
  pygame.mixer.music.stop()

def startplay(song):
  path = "/home/chip/Music/"
  file = path + str(song) + ".mp3"
  pygame.mixer.music.load(file)
  pygame.mixer.music.play()
  print file

if __name__ == '__main__':
  GPIO.setup("U14_14", GPIO.IN)
  GPIO.setup("U14_16", GPIO.IN)
  GPIO.setup("U14_18", GPIO.IN)
  pygame.init()
  pygame.mixer.init()


  aold = 0
  bold = 0
  cold = 0
  playing = 0
  startplay(0)
  while 1:
    stat = btndown()
    if stat != 0:
      if playing == 0:
        startplay(stat)
        playing = stat
      elif playing == stat:
        stopplay()
        playing = 0
      else:
        startplay(stat)
        playing = stat
    time.sleep(0.1)
