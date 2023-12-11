# Dylan Johnson
# Import matplotlib
import matplotlib.pyplot as plt

# Given data
arrival_times = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
service_durations = [2.22,1.76,2.13,0.14,0.76,0.7,0.47,0.22,0.18,2.41,0.41,0.46,1.37,0.27,0.27]

# Initialize empty arrays
exit_times = []
service_start_times = []
time_in_queue = []
# Customers in system (including in the service system)
system_customers = [0, 1, 2, 2, 2, 3, 4, 3, 2, 0, 1, 2, 1, 1, 0]
# Calculated queue customers
queue_customers = [0, 0, 1, 1, 1, 2, 3, 2, 1, 0, 0, 1, 0, 0, 0]

# Current time
current_time = 0

# Simulate the queue
for arrival, service in zip(arrival_times, service_durations):
    
    # Calculate service start time based off of either the
    #           arrival time or the current time
    service_start = max(current_time, arrival)
    service_start_times.append(service_start)
    
    # Calculate exit time by adding service time to service start
    exit_time = service_start + service
    exit_times.append(exit_time)
    
    # Calculate time in queue by subtracting service start from arrival time
    time_in_queue.append(service_start - arrival)
    
    # Update current time
    current_time = exit_time

# Calculate L_q and L_q^(A) to check with paper calculations
L_q = sum(time_in_queue) / current_time
L_q_A = sum(queue_customers) / 15

# Print results for L_q and L_q^(A)
print("L_q: " + str(L_q))
print("L_q^((A)): " + str(L_q_A))

# Generate plots
plt.figure(figsize=(10, 5))

# Plot customer arrival time as a function of service start time
# Use a subplot of 3 rows, 2 cols, and spot 1
plt.subplot(321)
plt.plot(arrival_times, service_start_times)
plt.title('Customer Arrival Time vs. Service Start Time')

# Plot customer arrival time as a function of exit time
# Use a subplot of 3 rows, 2 cols, and spot 2
plt.subplot(322)
plt.plot(arrival_times, exit_times)
plt.title('Customer Arrival Time vs. Exit Time')

# Plot customer arrival time as a function of time in queue
# Use a subplot of 3 rows, 2 cols, and spot 3
plt.subplot(323)
plt.plot(arrival_times, time_in_queue)
plt.title('Customer Arrival Time vs. Time in Queue')

# Plot customer arrival time as a function of the number of customers in the system
# Use a subplot of 3 rows, 2 cols, and spot 4
plt.subplot(324)
plt.plot(arrival_times, system_customers)
plt.title('Customer Arrival Time vs. Number of Customers in System')

# Plot customer arrival time as a function of the number of customers in the queue
# Use a subplot of 3 rows, 2 cols, and spot 5
plt.subplot(325)
plt.plot(arrival_times, queue_customers)
plt.title('Customer Arrival Time vs. Number of Customers in Queue')

# Adjust layout and show plots
plt.tight_layout()
plt.show()
