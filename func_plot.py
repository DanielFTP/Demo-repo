import numpy as np
import matplotlib.pyplot as plt

#Array with 200 equidistant x-values in the interval [−2.5,3] which functions as a grid for which we calculate the y values.
x = np.linspace(-2.5, 3, 10)

# Calculate the regular parabola
y = x**2

# Create index array
idx = (x >= 2)

# Set all y-values to 4, for which x >= 2.
y[idx] = 4

plt.plot(x,y)

#plt.savefig("cropped_parabola.eps")
plt.savefig("cropped_parabola_mod.eps")

