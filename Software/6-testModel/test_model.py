from mpu6050_v3 import Mpu6050
from randomForest import RandomForest
from statistics import Statistics
import time
from machine import SoftI2C, Pin

# Constants
BUTTON_GPIO = 18
LED_GPIO = 19

SDA_GPIO = 21
SCL_GPIO = 22

# Variables
gyr_set = []
acc_set = []

is_pressing = False

def analyze_sets(gyr_set, acc_set):
    # Calculate statistics
    # Extract values from dictionaries
    gyr_x = [entry['x'] for entry in gyr_set]
    gyr_y = [entry['y'] for entry in gyr_set]
    gyr_z = [entry['z'] for entry in gyr_set]

    acc_x = [entry['x'] for entry in acc_set]
    acc_y = [entry['y'] for entry in acc_set]
    acc_z = [entry['z'] for entry in acc_set]

    statistics = Statistics()

    # Calculate statistics
    n_samples = len(gyr_set)
    gyro_mean_x = statistics.mean(gyr_x)
    gyro_mean_y = statistics.mean(gyr_y)
    gyro_mean_z = statistics.mean(gyr_z)
    acce_mean_x = statistics.mean(acc_x)
    acce_mean_y = statistics.mean(acc_y)
    acce_mean_z = statistics.mean(acc_z)
    gyro_std_x = statistics.std(gyr_x)
    gyro_std_y = statistics.std(gyr_y)
    gyro_std_z = statistics.std(gyr_z)
    acce_std_x = statistics.std(acc_x)
    acce_std_y = statistics.std(acc_y)
    acce_std_z = statistics.std(acc_z)
    gyro_variance_x = statistics.variance(gyr_x)
    gyro_variance_y = statistics.variance(gyr_y)
    gyro_variance_z = statistics.variance(gyr_z)
    acce_variance_x = statistics.variance(acc_x)
    acce_variance_y = statistics.variance(acc_y)
    acce_variance_z = statistics.variance(acc_z)

    score = randomForest.score(n_samples,
                       gyro_mean_x,
                       gyro_mean_y,
                       gyro_mean_z,
                       acce_mean_x,
                       acce_mean_y,
                       acce_mean_z,
                       gyro_std_x,
                       gyro_std_y,
                       gyro_std_z,
                       acce_std_x,
                       acce_std_y,
                       acce_std_z,
                       gyro_variance_x,
                       gyro_variance_y,
                       gyro_variance_z,
                       acce_variance_x,
                       acce_variance_y,
                       acce_variance_z
                       )

    # Write the values to the file (Aixo es canviara per mostrar-ho al display)
    with open('test.txt', 'w') as file:
        file.write(str(score)) 

# def main():

i2c = SoftI2C(scl=Pin(SCL_GPIO), sda=Pin(SDA_GPIO))
mpu = Mpu6050(i2c)

but_pin = Pin(BUTTON_GPIO, Pin.IN)
led_pin = Pin(LED_GPIO, Pin.OUT)

randomForest = RandomForest()

while True:
    led_pin.value(but_pin.value())

    # If button is pressed
    if but_pin.value():

        # If was not pressing, clean sets
        if not is_pressing:
            gyr_set = []
            acc_set = []

        is_pressing = True

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
            analyze_sets(gyr_set, acc_set)
        
        is_pressing = False

# if __name__ == '__main__':
    # main()