import numpy as np

# Create a numpy array by passing a list to np.array.
numbers = np.array([4, 9, 16, 36, 49])

# Calculate the square root for each item in the array numbers.
roots = np.sqrt(numbers)

# Execute other computations for each element separately.
another_opp = 1.5 * roots - 4

print(another_opp)
