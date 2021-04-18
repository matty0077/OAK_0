from rgb_lcd import *
from Buzzer import *
import sys, time, random
import grovepi

'''def Type(word):
    # typewriter
    str = word
    for i in range(0,12):
        setText(str[:i])
        time.sleep(.01)'''
#A0 Socket
air_sensor = 0
   
def AIR():
    grovepi.pinMode(air_sensor,"INPUT")
    try:
        sensor_value = grovepi.analogRead(air_sensor)

        if sensor_value > 700:
            Buzz_Alert(.025,5)
            setText("High pollution " + str(sensor_value))#red
            Set_Red()
            
        elif sensor_value > 300:
            Buzz_Alert(.1,3)
            setText("Mild pollution " + str(sensor_value))#orange
            Set_Orange()
            
        elif sensor_value > 100 and sensor_value < 300:
            setText("Air fresh " + str(sensor_value))#green
            Set_Green()
            
        else:
            setText("Air Pristine " + str(sensor_value))#random colors
            Rando()
                
        time.sleep(.5)
        Set_Clear()
        #print("sensor_value =", sensor_value)

    except KeyboardInterrupt:
        Set_Clear()
        sys.exit()
    except TypeError:
        Set_Red()
        setText("Air Type Error")
        time.sleep(1)
        Set_Clear()
        sys.exit()
    except IOError:
        setText("Air Connection Error")
        time.sleep(1)
        Set_Clear()
        sys.exit()

#while True:
    #AIR()
