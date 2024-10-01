"""
This script take samples of gestures to be trained on a next stage.

The gesture is recorded while the button is pushed and saved on the file "samples.json" 
"""

from mpu6050_v3 import Mpu6050
import time
from machine import SoftI2C, Pin
import json

# Constants
BUTTON_GPIO = 18
LED_GPIO = 19

SDA_GPIO = 21
SCL_GPIO = 22

# Variables
gyr_set = []
acc_set = []

is_pressing = False

label = "lineZ"

# Functions
def take_sample():
    pass

def save_sets(label, gyr_set, acc_set, filename):
    with open(filename, 'r') as f:
        existing_data = json.load(f)
    
    new_set = {
        "set_id": len(existing_data["data_sets"]) + 1,
        "label": label,
        "gyroscope": gyr_set,
        "accelerometer": acc_set
    }

    existing_data["data_sets"].append(new_set)

    with open(filename, 'w') as f:
        json.dump(existing_data, f)

# def main():

i2c = SoftI2C(scl=Pin(SCL_GPIO), sda=Pin(SDA_GPIO))
mpu = Mpu6050(i2c)

but_pin = Pin(BUTTON_GPIO, Pin.IN)
led_pin = Pin(LED_GPIO, Pin.OUT)

while True:
    led_pin.value(but_pin.value())

    # If button is pressed
    if but_pin.value():

        # If was not pressing, clean sets
        if not is_pressing:
            gyr_set = []
            acc_set = []

        is_pressing = True

        # Take sample (take_sample())
        # Get points
        gyr_point = mpu.get_gyro()
        acc_point = mpu.get_accel()

        # Append points to sets
        gyr_set.append(gyr_point)
        acc_set.append(acc_point)

        # Sleep for 100 ms
        time.sleep(0.1)
    
    # If is not pressed
    else:

        # If was pressing, save sets
        if is_pressing:
            save_sets(label, gyr_set, acc_set, 'samples.json')
        
        is_pressing = False

# if __name__ == '__main__':
    # main()