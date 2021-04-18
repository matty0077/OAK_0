#!/usr/bin/env python
import time
import grovepi

# Connect the Grove Buzzer to digital port D8
buzzer = 4

grovepi.pinMode(buzzer,"OUTPUT")

def Buzz(tempo):
    try:
        # Buzz for 1 second
        grovepi.digitalWrite(buzzer,1)
        #print ('start')
        time.sleep(tempo)

        # Stop buzzing for 1 second and repeat
        grovepi.digitalWrite(buzzer,0)
        #print ('stop')
        time.sleep(tempo)

    except KeyboardInterrupt:
        grovepi.digitalWrite(buzzer,0)
    except IOError:
        print ("Error")

############################customizable alert system. tempo=time in between beeps, rounds is the total number of beeps
        
def Buzz_Alert(tempo,rounds):
    try:
        while True:
            if rounds>0:
                Buzz(tempo)
                rounds-=1
                time.sleep(tempo)
                #print(rounds)
                
            else:
                grovepi.digitalWrite(buzzer,0)
                break

    except KeyboardInterrupt:
        grovepi.digitalWrite(buzzer,0)
    except IOError:
        print ("Error")

#Buzz(.1)
#Buzz_Alert(.025,5)      
