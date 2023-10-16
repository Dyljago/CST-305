# Dylan Johnson
# Using NumPy and MatPlotLib libraries

import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

# Create an array of values for t
t = np.linspace(0, 10, 100)

# Set the c1 and c2 for both equations (Notes on why both are zero in documentation)
a = b = c = d = 0

# Create the homogeneous solutions of part 1 (which are always zero)
def a1(x, t):
    return a * np.cos(2*t) + b * np.sin(2*t)
def a2(x, t):
    return c * np.cos(t) + d * np.sin(t)

# Calculate the values for the two green's function results of part 1
def b1(t):
    return t / 4 - np.sin(2 * t) / 8
def b2(t):
    return 4 * (1 - np.cos(t))


# Create the axs to place each subplot on
fig, axs = plt.subplots(2, 2, figsize = (12, 6))

# Set the value of each ode at t to h1, h2, g1, and g2 respectively
h1 = odeint(a1, 0, t)
h2 = odeint(a2, 0, t)
g1 = b1(t)
g2 = b2(t)

# Homogeneous Solution for 1a
axs[0][0].plot(t, h1, label="c1*cos(2t) + c2*sin(2t)", color='b')
axs[0][0].set_title("Homogeneous Solution for First ODE")
axs[0][0].set_xlabel("t")
axs[0][0].set_ylabel("y(t)")
axs[0][0].grid(True)
axs[0][0].legend()

# Homogeneous Solution for 1b
axs[0][1].plot(t, h2, label="c1*cos(t) + c2*sin(t)", color='m')
axs[0][1].set_title("Homogeneous Solution for Second ODE")
axs[0][1].set_xlabel("t")
axs[0][1].set_ylabel("y(t)")
axs[0][1].grid(True)
axs[0][1].legend()

# Plot of t/4 - sin(2t)/8
axs[1][0].plot(t, g1, label="t/4 - sin(2t)/8", color='r')
axs[1][0].set_xlabel("t")
axs[1][0].set_ylabel("y(t)")
axs[1][0].set_title("Plot of t/4 - sin(2t)/8")
axs[1][0].grid(True)
axs[1][0].legend()

# Plot of 4(1 - cos(t))
axs[1][1].plot(t, g2, label="4(1 - cos(t))", color='g')
axs[1][1].set_xlabel("t")
axs[1][1].set_ylabel("y(t)")
axs[1][1].set_title("Plot of 4(1 - cos(t))")
axs[1][1].grid(True)
axs[1][1].legend()

# Set the graphs to be placed together
plt.tight_layout()

# Display the plots
plt.show()
