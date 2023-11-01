import numpy as np
import matplotlib.pyplot as plt

# Define the range of values for t
t = np.linspace(-0.5, 1.5, 1000)

# Calculate e^(-5t) and -e^(-5t)
ans1 = np.exp(-5 * t)
ans2 = -ans1

# Create the plot
plt.figure(figsize=(10, 6))
plt.plot(t, ans1, label='e^(-5t)', color='blue')
plt.plot(t, ans2, label='-e^(-5t)', color='orange')

# Set plot labels and legend
plt.xlabel('t')
plt.ylabel('Function Value')
plt.title('x(t) = e^(At)*C')
plt.legend()

# Set the y-axis limits to -150 to 150
plt.ylim(-3, 3)

# Display the plot
plt.grid()
plt.show()
