#!/usr/bin/env python
#MOSFET is also a kind of switch, but its switching frequency can reach up to 5MHz, much faster than normal mechanical relay.
#There are two screw terminals on opposite sides of the board.
#One side for power source and the other side for the device you want to control.

import sys, time
import grovepi
from rgb_lcd import *

#D6 Slot
mosfet = 6
grovepi.pinMode(mosfet,"OUTPUT")

###################### Full speed
def Mos_Max():
    try:
        grovepi.analogWrite(mosfet,255)
        #print ("full speed")
    except KeyboardInterrupt:
        grovepi.analogWrite(mosfet,0)
        Set_Clear()
        sys.exit()
    except TypeError:
        grovepi.analogWrite(mosfet,0)
        Set_Red()
        setText("Mosfet Type Error")
        time.sleep(1)
        Set_Clear()
        sys.exit()
    except IOError:
        grovepi.analogWrite(mosfet,0)
        setText("Mosfet Connection Error")
        time.sleep(1)
        Set_Clear()
        sys.exit()

##################### Half speed
def Mos_Half():
    try:
        grovepi.analogWrite(mosfet,128)
        #print ("half speed")
    except KeyboardInterrupt:
        grovepi.analogWrite(mosfet,0)
        Set_Clear()
        sys.exit()
    except TypeError:
        grovepi.analogWrite(mosfet,0)
        Set_Red()
        setText("Mosfet Type Error")
        time.sleep(1)
        Set_Clear()
        sys.exit()
    except IOError:
        grovepi.analogWrite(mosfet,0)
        setText("Mosfet Connection Error")
        time.sleep(1)
        Set_Clear()
        sys.exit()

####################### Off
def Mos_Off():
    try:
        grovepi.analogWrite(mosfet,0)
        #print ("Off")
    except TypeError:
        grovepi.analogWrite(mosfet,0)
        Set_Red()
        setText("Mosfet Type Error")
        time.sleep(1)
        Set_Clear()
        sys.exit()
    except IOError:
        grovepi.analogWrite(mosfet,0)
        setText("Mosfet Connection Error")
        time.sleep(1)
        Set_Clear()
        sys.exit()

#Mos_Max()
#time.sleep(1)
#Mos_Half()
#time.sleep(1)
#Mos_Off()
