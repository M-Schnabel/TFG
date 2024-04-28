import json
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from collections import Counter

filename = 'pc_samples.json'

# Load JSON data from file
with open(filename, 'r') as f:
    data = json.load(f)

# Separate data by label
gyroscope_sets_by_label = {}
accelerometer_sets_by_label = {}

for set_data in data['data_sets']:
    label = set_data['label']
    gyroscope_sets_by_label.setdefault(label, []).append(set_data['gyroscope'])
    accelerometer_sets_by_label.setdefault(label, []).append(set_data['accelerometer'])

# Count the number of sets for each label
gyroscope_sets_count = {label: len(sets) for label, sets in gyroscope_sets_by_label.items()}
accelerometer_sets_count = {label: len(sets) for label, sets in accelerometer_sets_by_label.items()}

# Create a new figure for all subplots
fig = plt.figure(figsize=(18, 12))

# Add gyroscope subplots
for i, (label, gyroscope_sets) in enumerate(gyroscope_sets_by_label.items(), 1):
    ax = fig.add_subplot(2, 3, i, projection='3d')
    for gyroscope_set in gyroscope_sets:
        x = [point['x'] for point in gyroscope_set]
        y = [point['y'] for point in gyroscope_set]
        z = [point['z'] for point in gyroscope_set]
        ax.scatter(x, y, z)
    ax.set_title(f'Gyroscope - {label}: {gyroscope_sets_count[label]} sets')
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')

# Add accelerometer subplots
for i, (label, accelerometer_sets) in enumerate(accelerometer_sets_by_label.items(), 4):
    ax = fig.add_subplot(2, 3, i, projection='3d')
    for accelerometer_set in accelerometer_sets:
        x = [point['x'] for point in accelerometer_set]
        y = [point['y'] for point in accelerometer_set]
        z = [point['z'] for point in accelerometer_set]
        ax.scatter(x, y, z)
    ax.set_title(f'Accelerometer - {label}: {accelerometer_sets_count[label]} sets')
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')

# Adjust layout
plt.tight_layout()

# Show plots
plt.show()
