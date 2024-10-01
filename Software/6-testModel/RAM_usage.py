import matplotlib.pyplot as plt
import numpy as np

# Read RAM usage data from file
ram_usage = []
with open('6-testModel/ram.txt', 'r') as file:
    for line in file:
        line = line.strip()
        if line:
            try:
                ram_usage.append(float(line))
            except ValueError:
                print(f"Ignoring non-numeric data: {line}")

# Plotting
plt.plot(ram_usage)
plt.title('RAM Usage Over Time')
plt.xlabel('Time')
plt.ylabel('RAM Usage')
plt.grid(True)
plt.show()

# Calculating mean, max, and min
mean_value = np.mean(ram_usage)
max_value = np.max(ram_usage)
min_value = np.min(ram_usage)

print(f"Mean RAM Usage: {mean_value}")
print(f"Max RAM Usage: {max_value}")
print(f"Min RAM Usage: {min_value}")
