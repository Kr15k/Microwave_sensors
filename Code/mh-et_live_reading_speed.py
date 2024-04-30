# Code made by Kr15k with help of ChatGPT
from machine import Pin
import time

# Define the pins connected to sensors
sensor_pin1 = Pin(15, Pin.IN)
sensor_pin2 = Pin(16, Pin.IN)

# Define variables to store the start times and speeds
start_time1 = None
start_time2 = None
speed1 = None
speed2 = None

# Define a callback for the pin interrupt
def pin_callback1(pin):
    global start_time1, speed1
    # If the pin is high, then store the current time
    if pin.value():
        start_time1 = time.ticks_us()
    # If the pin is low, then calculate the time difference
    else:
        if start_time1:
            time_diff = time.ticks_diff(time.ticks_us(), start_time1)
            # Calculate the frequency shift (Hz)
            freq_shift = 1 / (time_diff * 1e-6)
            # Calculate the speed (m/s)
            speed1 = (freq_shift * 3e8) / (2 * 10.525e9)
            # Round the speed to 2 decimal places
            speed1 = round(speed1, 2)
            if speed1 > 1:
                print('Speed from Sensor 1: ', speed1, 'm/s')

def pin_callback2(pin):
    global start_time2, speed2
    # If the pin is high, then store the current time
    if pin.value():
        start_time2 = time.ticks_us()
    # If the pin is low, then calculate the time difference
    else:
        if start_time2:
            time_diff = time.ticks_diff(time.ticks_us(), start_time2)
            # Calculate the frequency shift (Hz)
            freq_shift = 1 / (time_diff * 1e-6)
            # Calculate the speed (m/s)
            speed2 = (freq_shift * 3e8) / (2 * 10.525e9)
            # Round the speed to 2 decimal places
            speed2 = round(speed2, 2)
            if speed2 > 1:
                print('Speed from Sensor 2: ', speed2, 'm/s')

# Set the callbacks for the pin interrupts
sensor_pin1.irq(trigger=Pin.IRQ_RISING | Pin.IRQ_FALLING, handler=pin_callback1)
sensor_pin2.irq(trigger=Pin.IRQ_RISING | Pin.IRQ_FALLING, handler=pin_callback2)

# Start a loop to keep the program running
while True:
    pass
