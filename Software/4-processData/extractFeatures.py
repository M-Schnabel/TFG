import json
import numpy as np
import pandas as pd

"""
Using simple features:
    - n_samples
    - gyro_mean
    - acce_mean
    - gyro_std (standard deviation)
    - acce_std (standard deviation)
    - gyro_var (variation)
    - acce_var (variation)
"""

# Load the JSON data
with open('pc_samples.json', 'r') as f:
    data = json.load(f)

# Define lists to store extracted features
features = []

# Extract features from each sample
for sample in data['data_sets']:
    gyro_data = np.array([list(d.values()) for d in sample['gyroscope']])
    accel_data = np.array([list(d.values()) for d in sample['accelerometer']])
    
    # Calculate features
    n_samples = gyro_data.shape[0]
    gyro_mean = gyro_data.mean(axis=0)
    accel_mean = accel_data.mean(axis=0)
    gyro_std = gyro_data.std(axis=0)
    accel_std = accel_data.std(axis=0)
    gyro_variance = gyro_data.var(axis=0)
    accel_variance = accel_data.var(axis=0)
    
    # Append features to the list
    features.append({
        'n_samples': n_samples,
        'gyro_mean_x': gyro_mean[0],
        'gyro_mean_y': gyro_mean[1],
        'gyro_mean_z': gyro_mean[2],
        'acce_mean_x': accel_mean[0],
        'acce_mean_y': accel_mean[1],
        'acce_mean_z': accel_mean[2],
        'gyro_std_x': gyro_std[0],
        'gyro_std_y': gyro_std[1],
        'gyro_std_z': gyro_std[2],
        'acce_std_x': accel_std[0],
        'acce_std_y': accel_std[1],
        'acce_std_z': accel_std[2],
        'gyro_variance_x': gyro_variance[0],
        'gyro_variance_y': gyro_variance[1],
        'gyro_variance_z': gyro_variance[2],
        'acce_variance_x': accel_variance[0],
        'acce_variance_y': accel_variance[1],
        'acce_variance_z': accel_variance[2],
        'label': sample['label']
    })

# Convert the list of dictionaries to a Pandas DataFrame
df = pd.DataFrame(features)

# Display the DataFrame
print(df)

# Save the DataFrame
df.to_csv('features.csv', index=False)