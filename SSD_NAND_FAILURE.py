import numpy as np
import matplotlib.pyplot as plt
import random

# Constants
total_blocks = 1000  # Number of NAND blocks
total_cycles = 5000  # Total program-erase cycles
failure_threshold = 3000  # Threshold for failure (number of cycles after which blocks can fail)

# Generate random initial block wear levels
block_wear = np.random.randint(0, failure_threshold // 2, size=total_blocks)

# Lists to store the data for analysis
failures_per_cycle = []
average_wear = []

# Function to simulate the wear and tear of NAND blocks
def simulate_wear(cycles):
    failures = 0
    for i in range(total_blocks):
        # Increment wear per cycle
        block_wear[i] += random.randint(1, 5)
        
        # Check if block has failed
        if block_wear[i] >= failure_threshold:
            failures += 1
            
    return failures

# Run simulation for all cycles
for cycle in range(total_cycles):
    failures = simulate_wear(cycle)
    failures_per_cycle.append(failures)
    average_wear.append(np.mean(block_wear))

# Plot failure rate over time
plt.figure(figsize=(10, 5))
plt.plot(failures_per_cycle, label='Failures per Cycle')
plt.xlabel('Program/Erase Cycles')
plt.ylabel('Number of Failures')
plt.title('NAND Block Failures Over Time')
plt.legend()
plt.show()

# Plot average block wear
plt.figure(figsize=(10, 5))
plt.plot(average_wear, label='Average Block Wear', color='orange')
plt.xlabel('Program/Erase Cycles')
plt.ylabel('Average Wear Level')
plt.title('Average NAND Block Wear Over Time')
plt.legend()
plt.show()
