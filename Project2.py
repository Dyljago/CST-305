# Dylan Johnson
# Used math, time, numpy, matplotlib, and scipy libraries.
# Import libraries ---------------------------------------------------
import math
import time
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint
# --------------------------------------------------------------------


class Runge:

    # Computational Step counters-------------------------------------
    runge_steps = 0
    # ----------------------------------------------------------------

    # Differential Function ------------------------------------------
    def diffEq(y, x):
        return -y + math.log(x)
    # ----------------------------------------------------------------

    # Runge-Kutta Function -------------------------------------------
    def rungeKutta(x0, y0, h):
        k1 = Runge.diffEq(y0, x0)
        Runge.runge_steps += 1 # Increment by 1 because of the function evaluation
        k2 = Runge.diffEq(y0 + (h/2) * k1, x0 + (h/2))
        Runge.runge_steps += 2 # Increment by 2 because of the function evaluation and the multiplication
        k3 = Runge.diffEq(y0 + (h/2) * k2, x0 + (h/2))
        Runge.runge_steps += 2 # Increment by 2 because of the function evaluation and the multiplication
        k4 = Runge.diffEq(y0 + h * k3, x0 + h)
        Runge.runge_steps += 2 # Increment by 2 because of the function evaluation and the multiplication
        t4 = (1/6) * (k1 + 2*k2 + 2*k3 + k4)
        Runge.runge_steps += 5 # Increment by 5 because the multiplications and additions
        y1 = y0 + h * (t4)
        Runge.runge_steps += 2 # Increment by 2 because of the multiplication and addition
        x1 = x0 + h
        Runge.runge_steps += 1 # Increment by 1 because of the addition
        return (x1,y1)
    # ----------------------------------------------------------------

    # Function to run Runge Kutta for the desired runs ---------------
    def runCode(x_values, y_values, h, runs):
        for i in range(runs):
            x_values.append((Runge.rungeKutta(x_values[i], y_values[i], h)[0]))
            y_values.append((Runge.rungeKutta(x_values[i], y_values[i], h)[1]))
    # ----------------------------------------------------------------

    # Print Results From 0 to Amount of runs -------------------------
    def printResults(x_values, y_values, runs):
        for i in range(runs + 1):
            print("x" + str(i) + " = " + str(round(x_values[i], 4)) + ", \ty" + str(i) + " = " + str(round(y_values[i], 4)))
    # -----------------------------------------------------------------


class ODE:

    # Computational Step counters-------------------------------------
    ode_steps = 0
    # ----------------------------------------------------------------

    # Given Differential Equation -------------------------------------
    def diffEq(y, x):
        return -y + math.log(x)
    # -----------------------------------------------------------------

    # Funtion to run the code for the given number of runs ------------
    def runCode(x0, y0, h, runs):
        # Find the x_vals by multiplying the step size by the number of runs and adding it to the x for the number of runs + 1
        x_values = np.linspace(x0, x0 + h * runs, runs + 1)
        # Find the y_vals by using the odeint equation for the differential equation using y0, and the x_vals
        y_values = odeint(ODE.diffEq, y0, x_values)
        ODE.ode_steps += len(x_values) # Incremented by the length of the x_values list because that is how many times odeint runs
        return x_values, y_values
    # -----------------------------------------------------------------

    # -----------------------------------------------------------------
    def printResults(x_values, y_values):
        # For i in the size of the x and y values, x and y will enumerate through the x_vals and y_vals for the print statement
        for i, (x, y) in enumerate(zip(x_values, y_values)):
            print("x" + str(i) + " = " + str(round(x, 4)) + ", \ty" + str(i) + " = " + str(round(y[0], 4)))
    # -----------------------------------------------------------------


# Variables ----------------------------------------------------------
x0 = 2.0 # given initial x
y0 = 1.0 # given initial y
h = 0.3 # step size
runs = 1000 # number of runs
# --------------------------------------------------------------------

# List of Values -----------------------------------------------------
x_values = [x0]
y_values = [y0]
# --------------------------------------------------------------------

# # Run And Print Code -----------------------------------------------
# Runge start time
runge_start_time = time.time()
Runge.runCode(x_values, y_values, h, runs)
# Runge end time
runge_end_time = time.time()
runge_elapsed_time = runge_end_time - runge_start_time
# ODE start time
ode_start_time = time.time()
x_valuesODE, y_valuesODE = ODE.runCode(x0, y0, h, runs)
# ODE end time
ode_end_time = time.time()
ode_elapsed_time = ode_end_time - ode_start_time

# Print Runge and ODE elapsed times
print("\nRunge-Kutta Elapsed Time: \t" + str(runge_elapsed_time) + " seconds")
print("\nODE Elapsed Time: \t\t\t" + str(ode_elapsed_time) + " seconds")
if ode_elapsed_time > runge_elapsed_time:
    difference = ode_elapsed_time - runge_elapsed_time
    print("\nThe Runge-Kutta program runs \t" + str(difference) + " seconds faster than the ODE program")
elif ode_elapsed_time < runge_elapsed_time:
    difference = runge_elapsed_time - ode_elapsed_time
    print("\nThe ODE program runs \t" + str(difference) + " seconds faster than the Runge-Kutta program")
else:
    print("\nThe two programs run for the same elapsed time")

# Print runge and ode step counts
print("\nRunge-Kutta Computational Step Count: \t" + str(Runge.runge_steps) + " steps")
print("\nODE Computational Step Count: \t\t\t" + str(ODE.ode_steps) + " steps")

# --------------------------------------------------------------------

# Print Results If Desired -------------------------------------------
# print("Runge-Kutta Method")
# Runge.printResults(x_values, y_values, runs)
# print("ODE Method")
# ODE.printResults(x_valuesODE, y_valuesODE)
# --------------------------------------------------------------------

# Set multiple graphs within one of a specific size ------------------
fig, axs = plt.subplots(1, 3, figsize = (15, 5))
# --------------------------------------------------------------------

# Plot Runge-Kutta values on graph 1 ---------------------------------
axs[0].plot(x_values, y_values, linestyle = "-", color = "darkorange", label = "Runge-Kutta")
# --------------------------------------------------------------------

# Plot ODE values on graph 2 -----------------------------------------
axs[1].plot(x_valuesODE, y_valuesODE, linestyle = (0, (10, 15)), color = "blue", label = "ODE")
# --------------------------------------------------------------------

# Plot both sets of values on graph 3 --------------------------------
axs[2].plot(x_values, y_values, linestyle = "-", color = "darkorange", label = "Runge-Kutta")
axs[2].plot(x_valuesODE, y_valuesODE, linestyle = (0, (10, 15)), color = "blue", label = "ODE")
# --------------------------------------------------------------------

# Labeling x and y axes on graphs ------------------------------------
axs[0].set_xlabel('X Vals')
axs[0].set_ylabel('Y Vals')
axs[1].set_xlabel('X Vals')
axs[1].set_ylabel('Y Vals')
axs[2].set_xlabel('X Vals')
axs[2].set_ylabel('Y Vals')
# --------------------------------------------------------------------

# Giving title to graphs ---------------------------------------------
axs[0].set_title('Runge-Kutta')
axs[1].set_title('ODE')
axs[2].set_title('Runge-Kutta vs ODE')
# --------------------------------------------------------------------

# Show legends -------------------------------------------------------
axs[0].legend()
axs[1].legend()
axs[2].legend()
# --------------------------------------------------------------------

# Shows grids --------------------------------------------------------
axs[0].grid(True)
axs[1].grid(True)
axs[2].grid(True)
# --------------------------------------------------------------------

# Makes graphs fit closer --------------------------------------------
plt.tight_layout()
# --------------------------------------------------------------------

# Shows graphs -------------------------------------------------------
plt.show()
# --------------------------------------------------------------------

