
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
        start_time = time.time()
        
        value = pi.read(BTN)
        if(value == etat_bouton):
            buttonTime = time.time() - start_time
            print(buttonTime)

            if buttonTime >= 2:
                print("Plus grand que 2")

