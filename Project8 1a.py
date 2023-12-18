# Dylan Johnson
# Using libraries numpy, matplotlib
import numpy as np
import matplotlib.pyplot as plt

# Define the function
def function(x):
    return np.sin(x)+1

# Generate t values
t = np.linspace(-5, 5, 1000)

# Generate y values for the function
y = function(t)

# Define the boundaries for rectangles
x_start = -np.pi
x_end = np.pi
# Define the desired number of rectangles
n_rectangles = 4  

# Calculate the width of each rectangle
rectangle_width = (x_end - x_start) / n_rectangles

# Plot the function
plt.plot(t, y, label='1/5 * x^2')

# Add lines going up from x-axis at x=2 and x=6
plt.axvline(x=x_start, color='r', linestyle='--', label=f'x={x_start}')
plt.axvline(x=x_end, color='r', linestyle='--', label=f'x={x_end}')

# Add rectangles along the boundary for left side
for i in range(n_rectangles):
    x_rect = x_start + i * rectangle_width
    y_rect = function(x_rect)
    plt.fill_between([x_rect, x_rect + rectangle_width], 0, [y_rect, y_rect], alpha=0.2, color='purple')

plt.xlim(-5, 5)
plt.ylim(-2.5, 2.5)

# Add labels and title
plt.xlabel('x')
plt.ylabel('f(x)')
plt.title(f'Left Function Plot with {n_rectangles} Rectangles along the Boundary')
plt.legend()

# Show the plot
plt.show()


# Plot the function
plt.plot(t, y, label='1/5 * x^2')

# Add lines going up from x-axis at x=2 and x=6
plt.axvline(x=x_start, color='r', linestyle='--', label=f'x={x_start}')
plt.axvline(x=x_end, color='r', linestyle='--', label=f'x={x_end}')

# Add rectangles along the boundary for middle side
for i in range(n_rectangles):
    x_rect = x_start + i * rectangle_width
    y_rect = function(x_rect+0.5)
    plt.fill_between([x_rect, x_rect + rectangle_width], 0, [y_rect, y_rect], alpha=0.2, color='purple')

plt.xlim(-5, 5)
plt.ylim(-2.5, 2.5)

# Add labels and title
plt.xlabel('x')
plt.ylabel('f(x)')
plt.title(f'Middle Function Plot with {n_rectangles} Rectangles along the Boundary')
plt.legend()

# Show the plot
plt.show()


# Plot the function
plt.plot(t, y, label='1/5 * x^2')

# Add lines going up from x-axis at x=2 and x=6
plt.axvline(x=x_start, color='r', linestyle='--', label=f'x={x_start}')
plt.axvline(x=x_end, color='r', linestyle='--', label=f'x={x_end}')

# Add rectangles along the boundary for right side
for i in range(n_rectangles):
    x_rect = x_start + i * rectangle_width
    y_rect = function(x_rect+1)
    plt.fill_between([x_rect, x_rect + rectangle_width], 0, [y_rect, y_rect], alpha=0.2, color='purple')

plt.xlim(-5, 5)
plt.ylim(-2.5, 2.5)

# Add labels and title
plt.xlabel('x')
plt.ylabel('f(x)')
plt.title(f'Right Function Plot with {n_rectangles} Rectangles along the Boundary')
plt.legend()

# Show the plot
plt.show()
