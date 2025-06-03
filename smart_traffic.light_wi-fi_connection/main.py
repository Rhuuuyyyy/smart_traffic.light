import machine
import time
import network
from umqtt.simple import MQTTClient

# Wi-fi Config
WIFI_SSID = 'meuwifi123'
WIFI_PASS = 'minhasenha123'
MQTT_BROKER = 'broker.hivemq.com'
MQTT_TOPIC_PIR1 = b'sensor/pir1'

# Wi-fi Connect
def conecta_wifi():
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    wlan.connect(WIFI_SSID, WIFI_PASS)
    print("Conectando-se ao Wi-Fi...", end="")
    while not wlan.isconnected():
        time.sleep(1)
        print(".", end="")
    print("\nConectado:", wlan.ifconfig())

# Callback MQTT
pir1_simulado = 0

def sub_cb(topic, msg):
    global pir1_simulado
    if topic == MQTT_TOPIC_PIR1:
        if msg == b'1':
            pir1_simulado = 1
        else:
            pir1_simulado = 0

# Hardware Config
basic_time = 15

LED1_PIN_NUM = 13
LED2_PIN_NUM = 14
LED3_PIN_NUM = 12
PIR2_PIN_NUM = 26
SWITCH_PIN_NUM = 2

led1 = machine.Pin(LED1_PIN_NUM, machine.Pin.OUT)
led2 = machine.Pin(LED2_PIN_NUM, machine.Pin.OUT)
led3 = machine.Pin(LED3_PIN_NUM, machine.Pin.OUT)
pir2 = machine.Pin(PIR2_PIN_NUM, machine.Pin.IN)
interruptor = machine.Pin(SWITCH_PIN_NUM, machine.Pin.IN)

def int_status():
    if interruptor.value() == 0:
        led1.off()
        led2.off()
        led3.off()

# Wi-Fi & MQTT 
conecta_wifi()
client = MQTTClient("esp32_pir_trafficlight", MQTT_BROKER)
client.set_callback(sub_cb)
client.connect()
client.subscribe(MQTT_TOPIC_PIR1)
print("Conectado ao broker MQTT e inscrito no tópico:", MQTT_TOPIC_PIR1)

# Traffic Light
red_time = 15
green_time = 15
count = 0

while True:
    client.check_msg()  # Check MQTT Message

    if interruptor.value() == 1:
        if count == 0:
            red_time_atual = red_time
            while red_time_atual > 0:
                client.check_msg()
                if interruptor.value() == 0:
                    count = 4
                    break
                led1.on()
                time.sleep(1)
                red_time_atual -= 1

                if pir1_simulado == 1 and pir2.value() == 0:
                    red_time_atual += 5
                elif pir1_simulado == 0 and pir2.value() == 1:
                    red_time_atual -= 5
                elif pir1_simulado == 0 and pir2.value() == 0:
                    red_time_atual -= 1
                elif pir1_simulado == 1 and pir2.value() == 1:
                    red_time_atual -= 1

            led1.off()
            count += 1

        elif count == 1:
            if interruptor.value() == 0:
                count = 4
            else:
                led2.on()
                time.sleep(3)
                led2.off()
                count += 1

        elif count == 2:
            green_time_atual = green_time
            while green_time_atual > 0:
                client.check_msg()
                if interruptor.value() == 0:
                    count = 4
                    break
                led3.on()
                time.sleep(1)
                green_time_atual -= 1

                if pir1_simulado == 1 and pir2.value() == 0:
                    green_time_atual -= 5
                elif pir1_simulado == 0 and pir2.value() == 1:
                    green_time_atual += 2.5
                elif pir1_simulado == 0 and pir2.value() == 0:
                    green_time_atual -= 1
                elif pir1_simulado == 1 and pir2.value() == 1:
                    green_time_atual -= 1 

            led3.off()
            count += 1

        elif count == 3:
            if interruptor.value() == 0:
                count = 4
            else:
                led2.on()
                time.sleep(3)
                led2.off()
                count = 0

        elif count == 4:
            int_status()
            if interruptor.value() == 1:
                count = 0 
    else:
        int_status()
