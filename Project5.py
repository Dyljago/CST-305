# Import numpy and matplotlib libraries
import numpy as np
import matplotlib.pyplot as plt


# Method to calculate and return the xdot, ydot, and zdot for a given x, y, z, and r
def lorenz(x, y, z, r, s=10, b=2.667):
    x_dot = s * (y - x)
    y_dot = r*x - y - x*z
    z_dot = x * y - b * z
    return x_dot, y_dot, z_dot


# Method to calculate the data and create the graphs for a given r
def runCode(r):
    # Time step is 0.01 seconds
    dt = 0.01
    # Number of steps for graphs
    num_steps = 10000
    # Create arrays for x's, y's, and z's
    xs = np.empty(num_steps + 1)
    ys = np.empty(num_steps + 1)
    zs = np.empty(num_steps + 1)
    # Set initial x, y, and z values to 7.5, 22.5, and 35 kilobytes for txt, rtf, and docx files
    xs[0], ys[0], zs[0] = (7.5, 22.5, 35)
    # For loop to move through the number of steps
    for i in range(num_steps):
        # Use lorenz method to calculate xdot, ydot, and zdot
        x_dot, y_dot, z_dot = lorenz(xs[i], ys[i], zs[i], r)
        # Set the next x, y, and z to the result of x,y,z + x,y,zdot * time step
        xs[i + 1] = xs[i] + (x_dot * dt)
        ys[i + 1] = ys[i] + (y_dot * dt)
        zs[i + 1] = zs[i] + (z_dot * dt)

    # Plot
    fig = plt.figure()
    # Plot the 3D result
    ax = fig.add_subplot(111, projection='3d')
    # Plot these three arrays with a line width of 0.5
    ax.plot(xs, ys, zs, lw=0.5)
    # Label each axis appropriately
    ax.set_xlabel("X Axis")
    ax.set_ylabel("Y Axis")
    ax.set_zlabel("Z Axis")
    # Set title for this r value
    ax.set_title("Lorenz Attractor: r = " + str(r))

    # Create a figure with a subplot with 3 rows
    fig, (ax_x, ax_y, ax_z) = plt.subplots(3, 1, figsize=(8, 12))

    # Plot X, Y, and Z axes on separate subplots
    ax_x.plot(np.arange(0, num_steps + 1) * dt, xs)
    # Set y label and title
    ax_x.set_ylabel("X: txt")
    ax_x.set_title("Lorenz Attractor: r = " + str(r))
    # Set max x limit to 100 on graph and min x limit to -1
    ax_x.set_xlim(auto=False, left=-1, right=100)

    ax_y.plot(np.arange(0, num_steps + 1) * dt, ys)
    # Set y label
    ax_y.set_ylabel("Y: rtf")
    # Set max x limit to 100 on graph and min x limit to -1
    ax_y.set_xlim(auto=False, left=-1, right=100)

    ax_z.plot(np.arange(0, num_steps + 1) * dt, zs)
    # Set x and y labels
    ax_z.set_xlabel("t - Time")
    ax_z.set_ylabel("Z: docx")
    # Set max x limit to 100 on graph and min x limit to -1
    ax_z.set_xlim(auto=False, left=-1, right=100)

    # Show the graphs
    plt.tight_layout()
    plt.show()


# Method to start the code
def start():
    # Try block to get an input for r
    try:
        # Ask for an input for r and convert it into an integer
        r = int(input("What value would you like for 'r', enter '0' to stop: "))
    except ValueError:
        # If it cannot be converted into an integer then print this
        print("Not valid response")
        # And restart the input code
        start()
    except KeyboardInterrupt:
        # If someone terminates the code before an input is entered then print nothing and exit
        # Before adding this I would receive a keyboard interrupt error when stopping the code
        print()
    else:
        # Otherwise if r is converted to an integer successfully then check if r is 0
        if r != 0:
            # If not use the runCode method for r
            runCode(r)
            # Then restart the input code
            start()
        # Otherwise exit the code


# Initial start call
start()
