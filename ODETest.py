import numpy as np
import matplotlib.pyplot as plt

from scipy.integrate import odeint

def model(x,t):
    k = 0.2
    dxdt = -k*x
    return dxdt

x0 = 5

t = np.linspace(0, 20)

x = odeint(model, x0, t)

plt.xlabel("Time")
plt.ylabel("x(t)")
plt.title("ODE Test")
plt.plot(t,x);
plt.show()
