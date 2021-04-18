#!/usr/bin/env python

import sys, time
from rgb_lcd import *
from Buzzer import *
import grovepi

# Connect the Grove Flame Sensor to digital port D2
flame_sensor = 7
grovepi.pinMode(flame_sensor,"INPUT")

def FLAME():
    try:
        FIRE=grovepi.digitalRead(flame_sensor)
        #print(grovepi.digitalRead(flame_sensor))
        if FIRE==0:
            Buzz_Alert(.025,5)
            setText("Fire Detected")
            Set_Red()

            
        else:
            setText("No Flame Detected")
            Set_Green()
            
        time.sleep(.5)
        Set_Clear()

    except KeyboardInterrupt:
        Set_Clear()
        sys.exit()
    except TypeError:
        Set_Red()
        setText("Flame Type Error")
        time.sleep(1)
        Set_Clear()
        sys.exit()
    except IOError:
        setText("Flame Connection Error")
        time.sleep(1)
        Set_Clear()
        sys.exit()


#while True:
    #FLAME()
