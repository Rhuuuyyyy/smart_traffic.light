import machine
import time

# Matematic's var
basic_time = 15

# Set the LED's input 
LED1_PIN_NUM = 13
LED2_PIN_NUM = 14
LED3_PIN_NUM = 12
SWITCH_PIN_NUM = 2

# Set the LED's output
led1 = machine.Pin(LED1_PIN_NUM, machine.Pin.OUT)
led2 = machine.Pin(LED2_PIN_NUM, machine.Pin.OUT)
led3 = machine.Pin(LED3_PIN_NUM, machine.Pin.OUT)

# Set the interruptor's function
interruptor = machine.Pin(SWITCH_PIN_NUM, machine.Pin.IN)

# Traffic light's mechanic 
count = 0
status_interruptor = interruptor.value()

while True:
    if status_interruptor == 1:
        led1.off()
        led2.off()
        led3.off()
        count = 0
        while count == 0:
            while basic_time != 0:
            led1.on()
            time.sleep(basic_time)
            led1.off()
            count += 1
        count = 1
        if count == 1:
            while count == 1:
                while basic_time != 0:
                led2.on()
                time.sleep(4)
                led2.off()
                count += 1
        count = 2
        if count == 2:
            while count == 2:
                while basic_time != 0:
                led3.on()
                time.sleep(basic_time)
                led3.off()
                count += 1
    else:
        count = 0
    time.sleep(0.1)
