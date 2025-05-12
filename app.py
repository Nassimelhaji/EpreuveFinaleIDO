import paho.mqtt.client as pmc
from pigpio_dht import DHT11
import time
import pigpio
import threading


# Constantes
GPIO_DHT = 4 
BTN = 3
BROKER = "10.10.1.151"
PORT = 1883
TOPICT = "final/yanninassim/T"
TOPICH = "final/yanninassim/H"
TOPIC_RECEVOIR = "final/#"

# Fonctions
def connexion(client, userdata, flags, code, properties):
    if code == 0:
        print("Connecté")
        client.publish(TOPICT)
        client.publish(TOPICH)
    else:
        print("Erreur code %d\n", code)

def reception_msg(cl,userdata,msg):
    print("\t\t",msg.payload.decode())


def envoi_msg():
    while True:
        result = sensor.read()
        temperature = result["temp_c"]
        humidity = result["humidity"]
        client.publish(TOPICT, "yanninassim : temp : " + str(temperature) + " °C")
        client.publish(TOPICH, "yanninassim : humidity : " + str(humidity) + " %")
        time.sleep(30)




# Lecture du module dht11
pi = pigpio.pi()
pi.set_mode(GPIO_DHT,pigpio.INPUT)
pi.set_mode(3,pigpio.INPUT)
sensor = DHT11(GPIO_DHT)
pressTick = pi.get_current_tick()

def bouton():
    etat_bouton = 1
    while True:
        diff = pigpio.tickDiff(pressTick, tick)
        value = pi.read(BTN)
        if value != etat_bouton:
            etat_bouton = value
            if etat_bouton == 0:
                result = sensor.read()
                temperature = result["temp_c"]
                humidity = result["humidity"]
                client.publish(TOPICT, "yanninassimButton : temp : " + str(temperature) + " °C")
                client.publish(TOPICH, "yanninassimButton : humidity : " + str(humidity) + " %")



client = pmc.Client(pmc.CallbackAPIVersion.VERSION2)
client.on_connect = connexion
client.on_message = reception_msg
thread_entree_message1 = threading.Thread(target=envoi_msg, daemon=True)
thread_entree_message2 = threading.Thread(target=bouton, daemon=True)

# Connexion au broker
try:
    client.connect(BROKER,PORT)
    client.subscribe(TOPIC_RECEVOIR)
    thread_entree_message1.start()
    thread_entree_message2.start()
    client.loop_forever()

except KeyboardInterrupt:
    client.disconnect()
    pi.stop()