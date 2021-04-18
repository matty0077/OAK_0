#For Gas Leaks--Detects...
#carbon monixide
#coal gas
#liquefied gas
import sys, time
from rgb_lcd import *
from Buzzer import *
import os
import math
import decimal
import grovepi

#A2 Socket
MQ9_gas_sensor = 2

def GAS():
    grovepi.pinMode(MQ9_gas_sensor,"INPUT")
    
    try:
        # Get sensor value
        gas_value = grovepi.analogRead(MQ9_gas_sensor)

        if gas_value>=350 and gas_value<650:
            Buzz_Alert(.1,3)
            setText("Medium Gas " + str(gas_value))#orange
            Set_Orange()

        elif gas_value>=650:
            Buzz_Alert(.025,5)
            setText("Gas Levels Dangerous " + str(gas_value))#red
            Set_Red()

        else:
            setText("Gas Nominal " + str(gas_value))#green
            Set_Green()

        time.sleep(.5)
        Set_Clear()
        #print("gas_value=",gas_value)

    except KeyboardInterrupt:
        Set_Clear()
        sys.exit()
    except TypeError:
        Set_Red()
        setText("Gas Type Error")
        time.sleep(1)
        Set_Clear()
        sys.exit()
    except IOError:
        setText("Gas Connection Error")
        time.sleep(1)
        Set_Clear()
        sys.exit()

#while True:
    #GAS()

