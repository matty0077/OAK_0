#!/usr/bin/env python
###OAK SYSTEM- Management directed for indoor safety and security
#TEMPerature/HUMIDity-calculate temp/humid, frost
#rgblcd- show you data uses color for more info
#button- for switching modes
##########################IMPROVEMENTS
#hold button for shut off
#cbi

import sys
sys.path.append("/home/pi/Desktop/GROVE_2.0/OAK/LOGIKA/")
sys.path.append('/home/pi/Desktop/GROVE_2.0/OAK/LOGIKA/SENSORS/')

import threading
import time
import subprocess
import math
import logging
from datetime import datetime

from META import *
from rgb_lcd import *
from Buzzer import *
from Air import *
from Flame import *
from Gas import *
from Mosfet import *
from Motion import *
from Rotary import *
from Temp_Humid import *

#Button-D2 Slot
button = 2
grovepi.pinMode(button,"INPUT")

######Erika class manages these specific sensors for the purposes of plantingg
class OAK:
        MODE=0
        TIME= "%a %-d %b %-I:%M"
########################DATE TIME
        def Date_Time(self):
                try:
                        msg = "%s" % (datetime.now().strftime(self.TIME))
                        setText(msg)
                        Set_Yellow()
                        time.sleep(1)
                        Set_Clear()

                except KeyboardInterrupt:
                        Set_Clear()
                        sys.exit()

################################button. cycles through programs
        def Button(self):
                try:
                        press=grovepi.digitalRead(button)
                        #print(press)
                        if press==1:
                                self.MODE+=1
                                if self.MODE>9:
                                        self.MODE=0
                                        
                except IOError:
                        print("ButtonError")
                        setText("ButtonError")
                        Set_Red()

########################aNGLE cHECK
        def Fan_Check(self):
                try:
                        ROTT=grovepi.analogRead(potentiometer)
                        if ROTT<150:
                                Mos_Off()
                        elif ROTT>=150 and ROTT<600:
                                Mos_Half()
                        elif ROTT>=600:
                                Mos_Max()
                        
                except KeyboardInterrupt:
                        Set_Clear()
                        sys.exit()
                             
##############simple scan of environment
        def Quik_Scan(self):
                try:
                        setText("Quick Scan...")
                        Set_Teal()
                        time.sleep(.25)
                        TEMP()
                        HUMID()
                        AIR()
                        GAS()
                        
                except KeyboardInterrupt:
                        Set_Clear()
                        sys.exit()
##########################SLEEP
        def Watch_Dog(self):
                try:
                        setText("Watch Dog Scan")
                        Set_Teal()
                        time.sleep(.25)
                        FLAME()
                        GAS()
                        MOTION()
                        #SOUND()
                        
                except KeyboardInterrupt:
                        Set_Clear()
                        sys.exit()
                
##########################BEACON
        def Beacon(self):
                try:
                        setText("S.O.S.")
                        Threader(Buzz(.1))
                        Set_Red()
                        Threader(Buzz(.1))
                        Set_Blue()
                        
                except KeyboardInterrupt:
                        Set_Clear()
                        sys.exit()

#############abbreviate class                
O=OAK()

###########MAIN PROGRAM(FOR SWITCHING MODESc)
def Main():
        while True:
            try:
                if  O.MODE==0:#date/time
                        O.Date_Time()
                elif  O.MODE==1:#temperature
                        TEMP()
                elif  O.MODE==2:#humidity
                        HUMID()
                elif  O.MODE==3:#air pressure
                        AIR()
                elif  O.MODE==4:#Altitude
                        GAS()
                elif  O.MODE==5:#
                        FLAME()
                elif  O.MODE==6:#
                        MOTION()
                #################MODES
                elif  O.MODE==7:#
                        O.Quik_Scan()
                elif  O.MODE==8:#
                        O.Watch_Dog()
                elif  O.MODE==9:#
                        O.Beacon()
                        
                ##Runs Fan check and Cycle Button Simultaneously       
                Threader(O.Button)
                Threader(O.Fan_Check)

            except KeyboardInterrupt:
                Set_Clear()
                break
                sys.exit()
            except TypeError:
                print ("Error")
            except IOError:
                print ("Error")

##############TESTING
while True:
        Main()
        #O.Fan_Check()
        #O.Beacon()
        #O.Watch_Dog()
        #O.Quik_Scan()
        
