from mpu6050_v3 import Mpu6050
# from randomForest import RandomForest
from RandomForestOptimized import RandomForestOptimized
from statistics import Statistics
import time
from machine import SoftI2C, Pin

import gc

# Constants
BUTTON_GPIO = 18
LED_GPIO = 19

SDA_GPIO = 21
SCL_GPIO = 22

# Variables
gyr_set = []
acc_set = []

is_pressing = False

def free(full=False):
    F = gc.mem_free()
    A = gc.mem_alloc()
    T = F+A
    P = '{0:.2f}'.format(F/T*100)
    if not full:
        return P
    else :
        return ('Total:{0} Free:{1} ({2})'.format(T,F,P))

def analyze_sets(gyr_set, acc_set):
    # Calculate statistics
    # Extract values from dictionaries
    gyro_x = [entry['x'] for entry in gyr_set]
    gyro_y = [entry['y'] for entry in gyr_set]
    gyro_z = [entry['z'] for entry in gyr_set]

    acce_x = [entry['x'] for entry in acc_set]
    acce_y = [entry['y'] for entry in acc_set]
    acce_z = [entry['z'] for entry in acc_set]

    statistics = Statistics()

    n_samples = len(gyr_set)
    gyro_std_y = statistics.std(gyro_y)
    gyro_energy_y = statistics.energy(gyro_y)
    gyro_kurt_y = statistics.kurt(gyro_y)
    gyro_variance_y = statistics.variance(gyro_y)
    acce_min_z = statistics.min(acce_z)
    gyro_kurt_z = statistics.kurt(gyro_z)
    gyro_rms_y = statistics.rms(gyro_y)
    gyro_std_x = statistics.std(gyro_x)
    gyro_skew_y = statistics.skew(gyro_y)
    gyro_kurt_x = statistics.kurt(gyro_x)
    gyro_skew_z = statistics.skew(gyro_z)
    gyro_mean_z = statistics.mean(gyro_z)
    gyro_rms_z = statistics.rms(gyro_z)
    gyro_variance_z = statistics.variance(gyro_z)
    acce_energy_x = statistics.energy(acce_x)
    gyro_mean_y = statistics.mean(gyro_y)
    acce_range_x = statistics.range(acce_x)
    acce_mean_z = statistics.mean(acce_z)
    acce_rms_x = statistics.rms(acce_x)
    acce_std_z = statistics.std(acce_z)
    gyro_energy_x = statistics.energy(gyro_x)
    acce_corr_xz = statistics.corr(acce_x, acce_z)
    gyro_corr_xy = statistics.corr(gyro_x, gyro_y)
    gyro_variance_x = statistics.variance(gyro_x)
    acce_variance_x = statistics.variance(acce_x)
    acce_skew_x = statistics.skew(acce_x)
    acce_rms_y = statistics.rms(acce_y)
    acce_std_x = statistics.std(acce_x)
    acce_max_x = statistics.max(acce_x)
    acce_energy_z = statistics.energy(acce_z)
    gyro_std_z = statistics.std(gyro_z)
    gyro_energy_z = statistics.energy(gyro_z)
    acce_variance_z = statistics.variance(acce_z)
    acce_min_x = statistics.min(acce_x)
    acce_rms_z = statistics.rms(acce_z)
    acce_kurt_x = statistics.kurt(acce_x)
    acce_mean_y = statistics.mean(acce_y)
    gyro_rms_x = statistics.rms(gyro_x)
    acce_energy_y = statistics.energy(acce_y)
    acce_skew_z = statistics.skew(acce_z)
    
    score = randomForestOptimized.score(n_samples, gyro_std_y, gyro_energy_y, gyro_kurt_y, gyro_variance_y, acce_min_z, gyro_kurt_z, gyro_rms_y, gyro_std_x, gyro_skew_y, gyro_kurt_x, gyro_skew_z, gyro_mean_z, gyro_rms_z, gyro_variance_z, acce_energy_x, gyro_mean_y, acce_range_x, acce_mean_z, acce_rms_x, acce_std_z, gyro_energy_x, acce_corr_xz, gyro_corr_xy, gyro_variance_x, acce_variance_x, acce_skew_x, acce_rms_y, acce_std_x, acce_max_x, acce_energy_z, gyro_std_z, gyro_energy_z, acce_variance_z, acce_min_x, acce_rms_z, acce_kurt_x, acce_mean_y, gyro_rms_x, acce_energy_y, acce_skew_z)



# ####################################################
#     total = sum(score)
#     prob_circle = score[0] / total * 100
#     prob_line = score[1] / total * 100
#     prob_lineZ = score[2] / total * 100
#     probs = [prob_circle, prob_line, prob_lineZ]

#     max_pos = probs.index(max(probs))

#     # Write the values to the file (Aixo es canviara per mostrar-ho al display)
#     with open('test.txt', 'w') as file:
#         file.write(f"{str(probs)} -->")
#         if max_pos == 0:
#             file.write(str("Circle"))
#         elif max_pos == 1:
#             file.write(str("Line"))
#         elif max_pos == 2:
#             file.write(str("LineZ"))
####################################################

# def main():

i2c = SoftI2C(scl=Pin(SCL_GPIO), sda=Pin(SDA_GPIO))
mpu = Mpu6050(i2c)

but_pin = Pin(BUTTON_GPIO, Pin.IN)
led_pin = Pin(LED_GPIO, Pin.OUT)

# randomForest = RandomForest()
randomForestOptimized = RandomForestOptimized()

while True:
    led_pin.value(but_pin.value())

    with open('ram.txt', 'a') as file:
            file.write(f'{free()}\n')

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