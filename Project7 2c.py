# Dylan Johnson
# Import Matplotlib and numpy
import matplotlib.pyplot as plt
import numpy as np

# Use a linespace at 1 (to avoid division by 0) to 1000
k = np.linspace(1, 1000)

# Set variables theta and mu
theta = 10
mu = 5

# Set p when theta and mu increased by k
p = (k * theta) / (k * mu)

# Calculate estimated wait and service times when mu and theta increased by k
estimated_wait = p * (1 / (k * mu)) / (1 - p)
estimated_service = (1 / (k * mu)) / (1 - p)

# Calculate estimated number
estimated_number = p / (1 - p)

# Calculate estimated time
estimated_time = estimated_service + estimated_wait

# Calculate throughput
X = estimated_number / estimated_time

# Generate plots
plt.figure(figsize=(10, 15))

# Plot utilization (p) as a function of k
# Create subplot with 2 cols, 2 rows, at place 1
plt.subplot(221)
plt.plot(k, p, label='Utilization (p)')
plt.title('Utilization vs. k')
plt.xlabel('k')
plt.ylabel('Utilization (p)')
plt.legend()

# Plot throughput (X) as a function of k
# Create subplot with 2 cols, 2 rows, at place 2
plt.subplot(222)
plt.plot(k, X, label='Throughput (X)')
plt.title('Throughput vs. k')
plt.xlabel('k')
plt.ylabel('Throughput (X)')
plt.legend()

# Plot mean number in the system (E[N]) as a function of k
# Create subplot with 2 cols, 2 rows, at place 3
plt.subplot(223)
plt.plot(k, estimated_number, label='Mean Number in the System (E[N])')
plt.title('Mean Number in the System vs. k')
plt.xlabel('k')
plt.ylabel('Mean Number in the System (E[N])')
plt.legend()

# Plot mean time in the system (E[T]) as a function of k
# Create subplot with 2 cols, 2 rows, at place 4
plt.subplot(224)
plt.plot(k, estimated_time, label='Mean Time in the System (E[T])')
plt.title('Mean Time in the System vs. k')
plt.xlabel('k')
plt.ylabel('Mean Time in the System (E[T])')
plt.legend()


# Adjust layout and show plots
plt.tight_layout()
plt.show()
