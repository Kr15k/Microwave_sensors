from machine import Pin, Timer
import time

# Define the pin connected to the sensor
sensor_pin = Pin(15, Pin.IN)

# Define a variable to store the start time
start_time = None

# Define a callback for the pin interrupt
def pin_callback(pin):
    global start_time
    # If the pin is high, then store the current time
    if pin.value():
        start_time = time.ticks_us()
    # If the pin is low, then calculate the time difference
    else:
        if start_time:
            time_diff = time.ticks_diff(time.ticks_us(), start_time)
            # Calculate the frequency shift (Hz)
            freq_shift = 1 / (time_diff * 1e-6)
            # Calculate the speed (m/s)
            speed = (freq_shift * 3e8) / (2 * 10.525e9)
            # Round the speed to 2 decimal places
            speed = round(speed, 2)
            print('Speed: ', speed, 'm/s')

# Set the callback for the pin interrupt
sensor_pin.irq(trigger=Pin.IRQ_RISING | Pin.IRQ_FALLING, handler=pin_callback)

# Start a loop to keep the program running
while True:
    pass
