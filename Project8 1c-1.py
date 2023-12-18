# Dylan Johnson
# Import sympy
import sympy as sp

# Define the function
x = sp.symbols('x')
f = sp.log(x)

# Set a and b for the interval
a = 1
b = sp.E  # Use the sympy for e

# Set n and k variables and calculate delta_x
n, k = sp.symbols('n k')
delta_x = (b - a) / n

# Calculate c_k
c_k = a + (k * delta_x)

# Create the Riemann sum formula
riemann_sum = sp.summation(f.subs(x, c_k) * delta_x, (k, 1, n))

# Display the results
print(f"Riemann Sum Formula: {riemann_sum}")
