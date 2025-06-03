import machine
import time

# Matematic's var

basic_time = 15

# Set the LED's input 
LED1_PIN_NUM = 13
LED2_PIN_NUM = 14
LED3_PIN_NUM = 12
PIR1_PIN_NUM = 27
PIR2_PIN_NUM = 26
SWITCH_PIN_NUM = 2

# Set the LED's output
led1 = machine.Pin(LED1_PIN_NUM, machine.Pin.OUT)
led2 = machine.Pin(LED2_PIN_NUM, machine.Pin.OUT)
led3 = machine.Pin(LED3_PIN_NUM, machine.Pin.OUT)
pir1 = machine.Pin(PIR1_PIN_NUM, machine.Pin.IN)
pir2 = machine.Pin(PIR2_PIN_NUM, machine.Pin.IN)

# Set the interruptor's function
interruptor = machine.Pin(SWITCH_PIN_NUM, machine.Pin.IN)

# Traffic light's mechanic 

def int_status():
    if status_interruptor == 1:
        led1.off()
        led2.off()
        led3.off()

status_interruptor = interruptor.value()

red_time = 15
green_time = 15
count = 0

def int_status():

    if interruptor.value() == 0:
        led1.off()
        led2.off()
        led3.off()

while True:

    if interruptor.value() == 1:
        if count == 0:
            red_time_atual = red_time
            while red_time_atual > 0:
                if interruptor.value() == 0:
                    count = 4
                    break
                led1.on()
                time.sleep(1)
                red_time_atual -= 1

                if pir1.value() == 1 and pir2.value() == 0:
                    red_time_atual += 5
                elif pir1.value() == 0 and pir2.value() == 1:
                    red_time_atual -= 5
                elif pir1.value() == 0 and pir2.value() == 0:
                    red_time_atual -= 1
                elif pir1.value() == 1 and pir2.value() == 1:
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
                if interruptor.value() == 0:
                    count = 4
                    break
                led3.on()
                time.sleep(1)
                green_time_atual -= 1

                if pir1.value() == 1 and pir2.value() == 0:
                    green_time_atual -= 5
                elif pir1.value() == 0 and pir2.value() == 1:
                    green_time_atual += 2.5
                elif pir1.value() == 0 and pir2.value() == 0:
                    green_time_atual -= 1
                elif pir1.value() == 1 and pir2.value() == 1:
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
