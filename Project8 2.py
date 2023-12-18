# Dylan Johnson
# Import numpy and scipy.interpolate
import numpy as np
from scipy.interpolate import interp1d

# Set time array from 1-30
time_data = np.array([ 1,  2,  3,  4,  5,
                       6,  7,  8,  9, 10,
                      11, 12, 13, 14, 15,
                      16, 17, 18, 19, 20,
                      21, 22, 23, 24, 25,
                      26, 27, 28, 29, 30])
# Set Download rate array
download_rate_data = np.array([0.509, 0.324, 0.745, 0.420, 0.419,
                               0.420, 0.420, 0.419, 0.420, 0.419,
                               0.420, 0.417, 0.694, 0.833, 0.405,
                               0.416, 0.420, 0.710, 0.870, 0.418,
                               0.452, 0.372, 0.822, 0.806, 0.670,
                               0.840, 0.694, 0.773, 0.758, 0.747])

# Define the interpolation function of the two data sets
interpolation_function = interp1d(time_data, download_rate_data, kind='linear', fill_value='extrapolate')

# Generate values for the interpolated function for a timespace of 0-30
time_values = np.linspace(0, 30, 1000)
download_rate_values = interpolation_function(time_values)

# Calculate Riemann Sum using trapezoidal rule
riemann_sum = np.trapz(download_rate_values, time_values)
print(f'Riemann Sum: {riemann_sum}')

