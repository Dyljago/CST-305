# Dylan Johnson, used Numpy, Scipy, and MatPlotLib, used
# newtons law of cooling to model computer temperature

import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

# Defining ODE
def model(T,t,k,s):
    dTdt = -k*(T-s)
    return dTdt

# Parameters
k = 0.5 #Constant cooling rate
T = 80  # Initial temperature of computer cooling liquid
s = [50,60,70,80, 90]  # Temperature of surroundings

# Time span
t = np.linspace(0, 10)

# Going through array of s
for x in s:
    # Finding solution of ode
    solution = odeint(model, T, t, args=(k, x))
    # Plotting solution over time
    plt.plot(t, solution, label = "Temp: " + str(x))

# Labeling x and y axes
plt.xlabel('Time (s)')
plt.ylabel('Temperature')
# Giving title to graph
plt.title('Computer Cooling')
# Shows legend
plt.legend()
# Shows grid
plt.grid(True)
# Shows graph
plt.show()
