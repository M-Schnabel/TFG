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
fig = plt.figure(figsize=(12, 18))  # Adjust the figure size to make plots larger

# Add gyroscope and accelerometer subplots in rows
for row_index, (label, gyroscope_sets) in enumerate(gyroscope_sets_by_label.items()):
    # Gyroscope subplot
    ax = fig.add_subplot(3, 2, 2*row_index + 1, projection='3d')
    for gyroscope_set in gyroscope_sets:
        x = [point['x'] for point in gyroscope_set]
        y = [point['y'] for point in gyroscope_set]
        z = [point['z'] for point in gyroscope_set]
        ax.scatter(x, y, z)
    ax.set_title(f'Gyroscope - {label}: {gyroscope_sets_count[label]} sets')
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')

    # Accelerometer subplot
    accelerometer_sets = accelerometer_sets_by_label[label]
    ax = fig.add_subplot(3, 2, 2*row_index + 2, projection='3d')
    for accelerometer_set in accelerometer_sets:
        x = [point['x'] for point in accelerometer_set]
        y = [point['y'] for point in accelerometer_set]
        z = [point['z'] for point in accelerometer_set]
        ax.scatter(x, y, z)
    ax.set_title(f'Accelerometer - {label}: {accelerometer_sets_count[label]} sets')
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')

# Adjust layout and add spacing between rows
# plt.subplots_adjust(hspace=0.5)

# Save the figure as a vertically oriented image with good size on the plots
plt.savefig('plots_vertical.png', bbox_inches='tight', pad_inches=0.1, dpi=300)  # Adjust the DPI as needed
