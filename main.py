import machine
import time

LED1_PIN_NUM = 13
LED2_PIN_NUM = 14
LED3_PIN_NUM = 12
SWITCH_PIN_NUM = 2

led1 = machine.Pin(LED1_PIN_NUM, machine.Pin.OUT)
led2 = machine.Pin(LED2_PIN_NUM, machine.Pin.OUT)
led3 = machine.Pin(LED3_PIN_NUM, machine.Pin.OUT)


interruptor = machine.Pin(SWITCH_PIN_NUM, machine.Pin.IN)

count = 0

while True:
    estado_interruptor = interruptor.value()

    if estado_interruptor == 1:
        led1.off()
        led2.off()
        led3.off()
        count = 0
        while count == 0:
            led1.on()
            time.sleep(3)
            led1.off()
            count += 1
        count = 1
        if count == 1:
            while count == 1:
                led2.on()
                time.sleep(1)
                led2.off()
                count += 1
        count = 2
        if count == 2:
            while count == 2:
                led3.on()
                time.sleep(3)
                led3.off()
                count += 1
    else:
        count = 0

    time.sleep(0.1)
