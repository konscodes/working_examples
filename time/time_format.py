import time

# Get the current time in seconds since the Epoch
current_time = time.time()

# Convert the time to a formatted string
current_time_string = time.strftime('%Y-%m-%d %H:%M:%S',
                                    time.localtime(current_time))

print("The current time is:", current_time_string)
