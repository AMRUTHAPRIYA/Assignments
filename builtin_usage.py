import math
import random
import platform

# Generate a random integer between 1 and 100
random_num = random.randint(1, 100)

# Calculate the square root and round it down using math.floor
sqrt_floored = math.floor(math.sqrt(random_num))

# Retrieve system info using the platform module
os_name = platform.system()
python_version = platform.python_version()

# Print descriptive messages
print(f"Random Number: {random_num}")
print(f"Square Root (floored): {sqrt_floored}")
print(f"Operating System: {os_name}")
print(f"Python Version: {python_version}")