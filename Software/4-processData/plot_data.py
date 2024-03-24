import json
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

filename = 'pc_samples.json'

# Load JSON data from file
with open(filename, 'r') as f:
    data = json.load(f)

# Calculate the total number of sets
total_sets = len(data['data_sets'])

# Create a new figure for gyroscope data
fig1 = plt.figure()
ax1 = fig1.add_subplot(111, projection='3d')

# Plot gyroscope data
for set_data in data['data_sets']:
    gyroscope = set_data['gyroscope']
    x = [point['x'] for point in gyroscope]
    y = [point['y'] for point in gyroscope]
    z = [point['z'] for point in gyroscope]
    ax1.scatter(x, y, z, label='Gyroscope')

# Set labels and legend for gyroscope plot
ax1.set_title('Gyroscope Data')
ax1.set_xlabel('X')
ax1.set_ylabel('Y')
ax1.set_zlabel('Z')
ax1.legend([f'Total Sets: {total_sets}'])

# Create a new figure for accelerometer data
fig2 = plt.figure()
ax2 = fig2.add_subplot(111, projection='3d')

# Plot accelerometer data
for set_data in data['data_sets']:
    accelerometer = set_data['accelerometer']
    x = [point['x'] for point in accelerometer]
    y = [point['y'] for point in accelerometer]
    z = [point['z'] for point in accelerometer]
    ax2.scatter(x, y, z, label='Accelerometer')

# Set labels and legend for accelerometer plot
ax2.set_title('Accelerometer Data')
ax2.set_xlabel('X')
ax2.set_ylabel('Y')
ax2.set_zlabel('Z')
ax2.legend([f'Total Sets: {total_sets}'])

# Show plots
plt.show()
