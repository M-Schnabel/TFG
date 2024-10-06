from machine import SoftI2C, Pin
from mpu6050_v3 import Mpu6050
from RandomForestOptimized import RandomForestOptimized
from statistics import Statistics
import time
import ujson

# Pin definitions
BUTTON_GPIO = 18
LED_GPIO = 19
SDA_GPIO = 21
SCL_GPIO = 22

# Setup I2C for MPU6050
i2c = SoftI2C(sda=Pin(SDA_GPIO), scl=Pin(SCL_GPIO))
mpu = Mpu6050(i2c)

# Setup button and LED
button = Pin(BUTTON_GPIO, Pin.IN, Pin.PULL_DOWN)
led = Pin(LED_GPIO, Pin.OUT)

# Initialize Random Forest Classifier and Statistics
randomForestOptimized = RandomForestOptimized()
statistics = Statistics()

def record_gesture():
    gyr_set = []
    acc_set = []
    
    # Record data as long as the button is pressed
    while button.value():  # Button is pressed
        # Turn on the LED during recording
        led.on()

        # Get gyroscope and accelerometer data
        gyr_point = mpu.get_gyro()
        acc_point = mpu.get_accel()

        # Append to datasets
        gyr_set.append(gyr_point)
        acc_set.append(acc_point)

        # Sleep for 100 ms
        time.sleep(0.1)

    # Turn off the LED after recording
    led.off()

    return gyr_set, acc_set

def calculate_features(gyr_set, acc_set):
    # Extract data from sets
    gyro_x = [entry['x'] for entry in gyr_set]
    gyro_y = [entry['y'] for entry in gyr_set]
    gyro_z = [entry['z'] for entry in gyr_set]

    acce_x = [entry['x'] for entry in acc_set]
    acce_y = [entry['y'] for entry in acc_set]
    acce_z = [entry['z'] for entry in acc_set]

    # Calculate features
    n_samples = len(gyr_set)
    features = {
        'gyro_std_y': statistics.std(gyro_y),
        'gyro_energy_y': statistics.energy(gyro_y),
        'gyro_kurt_y': statistics.kurt(gyro_y),
        'gyro_variance_y': statistics.variance(gyro_y),
        'acce_min_z': statistics.min(acce_z),
        'gyro_kurt_z': statistics.kurt(gyro_z),
        'gyro_rms_y': statistics.rms(gyro_y),
        'gyro_std_x': statistics.std(gyro_x),
        'gyro_skew_y': statistics.skew(gyro_y),
        'gyro_kurt_x': statistics.kurt(gyro_x),
        'gyro_skew_z': statistics.skew(gyro_z),
        'gyro_mean_z': statistics.mean(gyro_z),
        'gyro_rms_z': statistics.rms(gyro_z),
        'gyro_variance_z': statistics.variance(gyro_z),
        'acce_energy_x': statistics.energy(acce_x),
        'gyro_mean_y': statistics.mean(gyro_y),
        'acce_range_x': statistics.range(acce_x),
        'acce_mean_z': statistics.mean(acce_z),
        'acce_rms_x': statistics.rms(acce_x),
        'acce_std_z': statistics.std(acce_z),
        'gyro_energy_x': statistics.energy(gyro_x),
        'acce_corr_xz': statistics.corr(acce_x, acce_z),
        'gyro_corr_xy': statistics.corr(gyro_x, gyro_y),
        'gyro_variance_x': statistics.variance(gyro_x),
        'acce_variance_x': statistics.variance(acce_x),
        'acce_skew_x': statistics.skew(acce_x),
        'acce_rms_y': statistics.rms(acce_y),
        'acce_std_x': statistics.std(acce_x),
        'acce_max_x': statistics.max(acce_x),
        'acce_energy_z': statistics.energy(acce_z),
        'gyro_std_z': statistics.std(gyro_z),
        'gyro_energy_z': statistics.energy(gyro_z),
        'acce_variance_z': statistics.variance(acce_z),
        'acce_min_x': statistics.min(acce_x),
        'acce_rms_z': statistics.rms(acce_z),
        'acce_kurt_x': statistics.kurt(acce_x),
        'acce_mean_y': statistics.mean(acce_y),
        'gyro_rms_x': statistics.rms(gyro_x),
        'acce_energy_y': statistics.energy(acce_y),
        'acce_skew_z': statistics.skew(acce_z),
    }

    return features, n_samples

def predict_gesture(features, n_samples):
    # Use the Random Forest model to predict gesture
    score = randomForestOptimized.score(
        n_samples,
        features['gyro_std_y'], features['gyro_energy_y'], features['gyro_kurt_y'], features['gyro_variance_y'],
        features['acce_min_z'], features['gyro_kurt_z'], features['gyro_rms_y'], features['gyro_std_x'],
        features['gyro_skew_y'], features['gyro_kurt_x'], features['gyro_skew_z'], features['gyro_mean_z'],
        features['gyro_rms_z'], features['gyro_variance_z'], features['acce_energy_x'], features['gyro_mean_y'],
        features['acce_range_x'], features['acce_mean_z'], features['acce_rms_x'], features['acce_std_z'],
        features['gyro_energy_x'], features['acce_corr_xz'], features['gyro_corr_xy'], features['gyro_variance_x'],
        features['acce_variance_x'], features['acce_skew_x'], features['acce_rms_y'], features['acce_std_x'],
        features['acce_max_x'], features['acce_energy_z'], features['gyro_std_z'], features['gyro_energy_z'],
        features['acce_variance_z'], features['acce_min_x'], features['acce_rms_z'], features['acce_kurt_x'],
        features['acce_mean_y'], features['gyro_rms_x'], features['acce_energy_y'], features['acce_skew_z']
    )

    return score

def save_result_to_json(gesture_score):
    # Load existing results if the file exists, otherwise create a new structure
    try:
        with open("resultats.json", "r") as f:
            data = ujson.load(f)
    except OSError:
        data = {"resultats": []}

    # Mapping indices to gestures
    gesture_map = ["Cercle", "Línia XY", "Línia Z"]

    # Find the gesture with the highest score
    max_score_index = gesture_score.index(max(gesture_score))
    gesture_name = gesture_map[max_score_index]
    confidence = max(gesture_score)

    # Create a new entry
    new_entry = {
        "id": len(data["resultats"]) + 1,
        "gest": gesture_name,
        "confiança": confidence
    }

    # Append new entry to the list
    data["resultats"].append(new_entry)

    # Write updated data back to the JSON file
    with open("resultats.json", "w") as f:
        ujson.dump(data, f)

# Main loop
while True:
    # Check if the button is pressed to start recording gesture
    if button.value():
        # Record gesture
        gyr_set, acc_set = record_gesture()

        # Calculate features
        features, n_samples = calculate_features(gyr_set, acc_set)

        # Predict gesture
        gesture_score = predict_gesture(features, n_samples)
        
        # Save the result to JSON file
        save_result_to_json(gesture_score)

    time.sleep(0.1)  # Debounce delay
