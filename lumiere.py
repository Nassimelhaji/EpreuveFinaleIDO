import pigpio
import time


RED = 26
BLUE = 19
WHITE = 13


pi = pigpio.pi()
pi.set_mode(RED,pigpio.OUTPUT)
pi.set_mode(BLUE,pigpio.OUTPUT)
pi.set_mode(WHITE,pigpio.OUTPUT)


pi.write(RED,0)
pi.write(BLUE,0)
pi.write(WHITE,0)


