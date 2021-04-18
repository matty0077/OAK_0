from rgb_lcd import *
from Buzzer import *
import sys, time
from grovepi import *

dht_sensor_port = 3		# Connect the DHt sensor to port d2
dht_sensor_type = 0             # change this depending on your sensor type - see header commentwhile True:

######################################TEMPERATURE(Celsius and Farhenheit)              
def TEMP():
        try:
                #########sensor readings
                [ temp,hum ] = dht(dht_sensor_port,dht_sensor_type)
                #########calculate temperature for farenheight(Celsius is Default)
                tempF=temp*1.8+32
                tempF = round(tempF)
                tempF = int(tempF)
                DEW = temp-(14.55+0.114*temp)*(1-(0.01*hum))-((2.5+0.007*temp)*(1-(0.01*hum)))**3-(15.9+0.117*temp)*(1-(0.01*hum))**14
                DEW = round(DEW)
                DEW = int(DEW)
                
                #Display Temperature as F AND C
                setText("Temperature " + str(tempF) +"F" + "/" + str(temp) +"C")
                Set_Aqua()
                time.sleep(.75)
                
                ########info(customize Info for celsius if needed)
                if tempF<=32:
                    setText("Very Cold Near Freezing Point")
                    Set_Blue()
                elif tempF>32 and tempF<=50:
                    setText("Pretty Chilly")
                    Set_Aqua()
                elif tempF>50 and tempF<=60:
                    setText("Little Chilly")
                    Set_Teal()

                elif tempF>60 and tempF<=70:
                    setText("Ideal Temperature")
                    Set_Green()

                elif tempF>70 and tempF<=80:
                    setText("Warm")
                    Set_Yellow()
                elif tempF>80 and tempF<90:
                    setText("Hot")
                    Set_Orange()
                elif tempF>=90:
                    setText("Very Hot")
                    Set_Red()

                # Frost point warning-Uses dewpoint and temperature(celsius)
                if DEW <= 2 and temp <= 1:
                        setText("Frost Warning")
                        Set_Red()
                    
                time.sleep(.5) 
                Set_Clear()

        except KeyboardInterrupt:
                Set_Clear()
                sys.exit()
			
        except (IOError,TypeError) as e:
                setText("Temperature Error")
                Set_Red()
                time.sleep(1)
                Set_Clear()
                sys.exit()

###############################################HUMIDITY
def HUMID():
        try:
                #########sensor readings
                [ temp,hum ] = dht(dht_sensor_port,dht_sensor_type)
                #Display Humidity %
                setText("Humidity " + str(hum) + "%")
                Set_Aqua()
                time.sleep(.75)

                ########info
                if hum<30:
                    setText("Somewhat Dry")
                    Set_Yellow()

                elif hum>=30 and hum<=60:
                    setText("Ideal Humidity")
                    Set_Green()

                elif hum>60 and hum<80:
                    setText("Moderate Humidity")
                    Set_Green()

                else:
                    setText("High Humidity")
                    Set_Green()
                    
                time.sleep(1)
                Set_Clear()
			
        except (IOError,TypeError) as e:
                setText("Humidity Error")
                Set_Red()
                time.sleep(1)
                Set_Clear()
                sys.exit()
                
#########################################CBI-Chandler Burning Index
#Formula --> CBI = (((110 - 1.373 * RH) - 0.54 * (10.20 - T)) * (124 * 10(-0.0142 * RH)))/60
#T = Air temperature (Celsius)
#RH = Relative humidity	(%)
def CBI():
        #try:
        #########sensor readings
        [ temp,hum ] = dht(dht_sensor_port,dht_sensor_type)
        #CBI = (((110 - 1.373 * hum) - 0.54 * (10.20 - temp)) * (124 * 10*(-0.0142 * hum)))/60
        CBI = (((110 - 1.373 * hum) - 0.54 * (10.20 - temp)) * (124 * 10^(-0.0142 * hum)))/60
        #CBI = (((110 - 1.373 * hum) - 0.54 * (10.20 - temp)) * (124 * 10**(-0.0142 * hum)))/60
        print(str(CBI))

        time.sleep(.5)
                
        '''except KeyboardInterrupt:
                Set_Clear()
                sys.exit()
			
        except (IOError,TypeError) as e:
                setText("CBI Error")
                Set_Red()
                time.sleep(1)
                Set_Clear()
                sys.exit()'''


#while True:
        #TEMP()
        #HUMID()
        #CBI()
