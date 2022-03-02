import numpy as np
import matplotlib.pyplot as plt

#Array with 200 equidistant x-values in the interval [−2.5,3] which functions as a grid for which we calculate the y values.
x = np.linspace(-2.5, 3, 200)
y = x**2

idx = (x >= 2) # Create index array
y[idx] = 4 # Set all y-values to 4, for which x >= 2.

plt.xlabel("$x$") # Set axis labels. Latex expression can be used.
plt.ylabel("Cropped Parabola")

plt.plot(x,y)
plt.savefig("cropped_parabola.eps")
#----------------------------------------------------------------------------------
# Create x-value grid for the "measured" data.
x_data = np.array([-2.5, -2, -1.5, -1, -.5, 0, .5, 1, 1.5, 2, 2.5, 3])
y_data = x_data**2

# Crop y_data points if x_data >= 2.
y_data[x_data >= 2] = 4

# Add random fluctuations to y_data.
#y_data += np.random.normal(0, 0.3, len(y_data)) # np.normal(mean, stdev, size) where size=number of samples, if size =(m,n,k) means m*n*k samples, or None(1 solo valor))

# Draw with error bars, including errors one-by-one
yerr = [0.6, 0.2, 0.4, 0.5, 0.7, 0.1, 0.2, 0.8, 0.7, 0.5, 0.1, 0.4]
xerr = [0.6, 0.2, 0.4, 0.5, 0.7, 0.1, 0.2, 0.8, 0.7, 0.5, 0.1, 0.4]
#x_data += xerr
#y_data += yerr

plt.errorbar(x_data, y_data, yerr, xerr, fmt="ko", capsize=0) # 3rd parameter=size of the error bar in $`y`$ direction.

# Save figure.
plt.savefig("measurement_ensayando_error_bars.eps")