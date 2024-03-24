from mpu6050_v3 import Mpu6050
import time
from machine import SoftI2C, Pin
import json

i2c = SoftI2C(scl=Pin(22), sda=Pin(21))
mpu = Mpu6050(i2c)

time.sleep(1)
print("3")
time.sleep(1)
print("2")
time.sleep(1)
print("1")
time.sleep(1)
print("Go")

gyr_set = []
acc_set = []

initial_time = time.time()
while initial_time > time.time() - 3:
    gyr_point = mpu.get_gyro()
    acc_point = mpu.get_accel()

    gyr_set.append(gyr_point)
    acc_set.append(acc_point)

    time.sleep(0.05)

with open("input_data.json", 'r') as f:
    existing_data = json.load(f)

new_set = {
    "set_id": len(existing_data["data_sets"]) + 1,
    "gyroscope": gyr_set,
    "accelerometer": acc_set
}

existing_data["data_sets"].append(new_set)

with open("input_data.json", 'w') as f:
    json.dump(existing_data, f)