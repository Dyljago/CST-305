# Dylan Johnson
# Using libraries numpy, matplotlib, scipy, and fractions
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint
from fractions import Fraction


# Define the function for part 1a
def part1a(x):
    return 1 - x - (1/3) * x**3 - (1/12) * x**4


# Define the range of x values
x_values = np.linspace(0, 5, 100)

# Calculate the corresponding y values at each x value
y_values = part1a(x_values)

# Plot the function
plt.plot(x_values, y_values, label='y\" - 2xy\' + x^2y')
plt.title('Part 1a')
# Add a dotted line from the x-axis to x = 3.5
plt.plot([3.5, 3.5], [-100, part1a(3.5)], 'r--', label='x = 3.5')

# Add a dotted line from the y-axis to y=-29.975
plt.plot([0, 3.5], [part1a(3.5), part1a(3.5)], 'g--', label='y = -29.297')

# Label x and y axes
plt.xlabel('x')
plt.ylabel('y')

# Set x and y limits for visual
plt.xlim(0, 5)
plt.ylim(-100, 10)
# Show plot
plt.grid(True)
plt.legend()
plt.show()


# Define the function for part 1b
def part1b(x):
    return 6 + (x - 3) - 11/2 * ((x-3)**2)


# Define the range of x values
x_values = np.linspace(0, 5, 100)

# Calculate the corresponding y values for each x value
y_values = part1b(x_values)

# Plot the function
plt.plot(x_values, y_values, label='y\" - (x - 2)y\' + 2y')
plt.title('Part 1b')

# Add a dotted line at x = 3 since we know y(3) = 6
plt.plot([3, 3], [-50, part1b(3)], 'r--', label='x = 3')

# Add a dotted line at y = 6 since we know y(3) = 6
plt.plot([0, 3], [part1b(3), part1b(3)], 'g--', label='y = 6')

# Label x and y axes
plt.xlabel('x')
plt.ylabel('y')

# Set x and y limits for visuals
plt.xlim(0, 5)
plt.ylim(-50, 10)
# Show plot
plt.grid(True)
plt.legend()
plt.show()


# Define function for part 2
def part2(n):
    # Create a_values array of n+2 fractions
    a_values = [Fraction(0) for _ in range(n + 2)]
    # Set a_value at 0
    a_values[0] = Fraction(1)
    # Set a_value at 1
    a_values[1] = Fraction(1)

    # From 2 until n+2 set a_value
    for i in range(2, n + 2):
        # a_value at i is equivalent to this result
        a_values[i] = -((i - 2) * (i - 3) + 1) * Fraction(1, 4 * i * (i - 1)) * a_values[i - 2]

    # Return a_values from 2 onward
    return a_values[2:]


# Call the function to get the values of a for n=8
a_values = part2(8)


# Function to print all a_values in the array
def printAVals():
    # For each i from 2 onward, for each a in a_values
    for i, a in enumerate(a_values, start=2):
        # Check if a is divisible by 2
        if i % 2 == 0:
            # If so it is an a0
            print(f'a_{i} = {a} a0')
        else:
            # Otherwise it is an a1
            print(f'a_{i} = {a} a1')


# Print a_values to check the ones I got for the assignment
printAVals()

# Plot the resulting values of a against n
# Converted to float to avoid warning in code for a-values
plt.plot(range(0, len(a_values)), [float(a) for a in a_values], marker='o')

# Set title
plt.title('A(n+2) results at n')
# Set labels
plt.xlabel('n')
plt.ylabel('a(n+2)')
# Show grid
plt.grid(True)
plt.show()


# Defining ODE
def part3(T,t,k,s):
    # Newton's Law of Cooling
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
    solution = odeint(part3, T, t, args=(k, x))
    # Plotting solution over time
    plt.plot(t, solution, label = "Temp: " + str(x))

# Labeling x and y axes
plt.xlabel('Time (Seconds)')
plt.ylabel('Temperature (Celsius)')
# Giving title to graph
plt.title('Computer Cooling')
# Shows legend
plt.legend()
# Shows grid
plt.grid(True)
# Shows graph
plt.show()


