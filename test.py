from datetime import datetime
# Test bouton
import pigpio
import time


BTN = 3
pi = pigpio.pi()
pi.set_mode(BTN,pigpio.INPUT)


while True:
    etat_bouton = 1
    value = pi.read(BTN)
    if value != etat_bouton:
        start_time = datetime.now().second
        start_time2 = str(start_time)
        print(start_time)
        if(value == etat_bouton):
            end_time = datetime.now().second
            print("End tme : " + str(end_time))
            buttonTime = end_time - start_time
            print("button time : " + str(buttonTime))

            if buttonTime >= 2:
                print("Long button")
                print(buttonTime)
            elif buttonTime >= 1:
                print("Court button")
            



