#!/usr/bin/env python
import sys, time
from rgb_lcd import *
import grovepi

#A1 Slot
potentiometer = 1
#Rot = grovepi.analogRead(potentiometer)


def ANGLE():
    grovepi.pinMode(potentiometer,"INPUT")
    
    try:
        # Read sensor value from potentiometer
        Rot = grovepi.analogRead(potentiometer)
        #print(Rot)

    except KeyboardInterrupt:
        Set_Clear()
        sys.exit()
    except TypeError:
        Set_Red()
        setText("Rotary Type Error")
        time.sleep(1)
        Set_Clear()
        sys.exit()
    except IOError:
        setText("Rotary Connection Error")
        time.sleep(1)
        Set_Clear()
        sys.exit()


#while True:
    #ANGLE()
