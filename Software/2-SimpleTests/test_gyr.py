import time
from machine import Pin, SoftI2C
from mpu6050 import Mpu6050

i2c = SoftI2C(scl=Pin(22), sda=Pin(21))
mpu = Mpu6050(i2c)

# gpio_pin_number = 2
# gpio_pin = Pin(gpio_pin_number, Pin.OUT)

while True:
    # print(mpu.get_gy_values())
    # print(mpu.get_ac_values())
    # print(mpu.get_values())

    values = mpu.get_values()

    print(f"Giroscopi -> X: {values['GyX']}, Y: {values['GyY']}, Z: {values['GyZ']}")
    # print(f"Accelerometre -> X: {values['AcX']}, Y: {values['AcY']}, Z: {values['AcZ']}")

    # gpio_pin.value(not gpio_pin.value())
    
    time.sleep(1)