
# NOTE:
# 	There are also 2x potentiometers on the board for adjusting measuring distance and hold time
# 	Rotate the pot labelled "Delay time" clockwise to decrease the hold time (0.3s - 25s)
# 	Rotate the pot labelled "Distance" clockwise to decrease the measuring distance (10cm - 6m)
# Connect the Grove PIR Motion Sensor to digital port D8
# NOTE: Some PIR sensors come with the SIG line connected to the yellow wire and some with the SIG line connected to the white wire.
# If the example does not work on the first run, try changing the pin number
# For example, for port D8, if pin 8 does not work below, change it to pin 7, since each port has 2 digital pins.
# For port 4, this would pin 3 and 4
import sys, time
sys.path.append("/home/pi/Desktop/GROVE_2.0/OAK/LOGIKA/")
from META import *
from rgb_lcd import *
from Buzzer import *
import grovepi

#D8 Slot
pir_sensor = 8

motion=0
def MOTION():
        grovepi.pinMode(pir_sensor,"INPUT")

        try:
                # Sense motion, usually human, within the target range
                motion=grovepi.digitalRead(pir_sensor)
                if motion==1:
                        setText('Motion Detected!')
                        Buzz_Alert(.025,5)
                        Threader(Flash_Red())
                else:
                        setText('No Lifeforms Detected')
                        Threader(Flash_Aqua())

                time.sleep(.5)#timer is releative to your version but typically without the lcd, anything less than ".2" would give less accurate readings.
                Set_Clear()

        except KeyboardInterrupt:
                Set_Clear()
                sys.exit()
        except TypeError:
                Set_Red()
                setText("Motion Type Error")
                time.sleep(1)
                Set_Clear()
                sys.exit()
        except IOError:
                setText("Motion Connection Error")
                time.sleep(1)
                Set_Clear()
                sys.exit()

#while True:
        #MOTION()
