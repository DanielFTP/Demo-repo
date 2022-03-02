import numpy as np       # Import the numpy library.
import scipy.optimize    # Import the scipy library with fit routines.
import scipy.stats       # Import the scipy library with probability distributions and statistical tests.
import matplotlib.pyplot as plt    # Import the plotting library.

# Read both columns from the text file.
Outer_array = np.genfromtxt("decay.txt")
# inner array:
channel, count = Outer_array.transpose() # Return to the "inner array", each element is a channel and their corresponding event count

# Calculate the uncertainty (y_error bar sizes): Square root of the number of events per channel - Valid for poisson distribution
s_count = np.sqrt(count)

# Create and save a raw version of the plot with data points. The label will later be used to identify the curves in a legend.
plt.errorbar(channel, count, s_count, fmt='.k', elinewidth=0.2 , capsize=0.0, label="Data")

plt.xlabel("Channel (Energy units)") 
plt.ylabel("Count")

plt.savefig("decay_raw.eps")

#------------------------------------

# Number of events(counts) in channel c_i
def model(channel, m, s, A, y0, b): # <-- The model function as a function of the parameters ('x', m media 'mu', s - stdev 'sigma', A - ammplitude, y0, b)
  return  A * np.exp(-0.5 * (channel - m)**2 / s**2) + y0 + b * channel

p0 = (60, 10, 50, 20, 1) # Define initial values of the free parameters, with our model as n(c; m, s, A, y0, b)

# Perform the actual fit. 
popt, pcov = scipy.optimize.curve_fit(model, channel, count, p0, s_count) # Returns: popt: Optimal values for the parameters so that the sum of the squared residuals of f(xdata, *popt)-ydata (in our case model(channel, *popt)-count) is minimized.    And, pcov: The estimated covariance of popt. The diagonals provide the variance of the parameter estimate. 

# Where the parameters are:
#   (1) Model to fit  <-- The model function, f(x, …). It must take the independent variable as the first argument and the parameters to fit as separate remaining arguments.
#   (2) Array of x-values
#   (3) Array of y-values to which the model should be fitted
#   (4) Array with initial values for the free parameters
#   (5) Array with uncertainties on the y-values.

# To visualize the fitted model, we need to evaluate our model with the optimized parameters popt.
fit_count = model(channel, *popt) # Return best 'y <--> count' values due to the calling of the function 'model' with the optimized parameters popt

# Plot a curve representing the fitted model.
plt.plot(channel, fit_count, label="Linear + Gauss")

# Add a legend to identify data and our fit. This method uses values passed to
# the optional argument 'label' of plot() and errorbar().
plt.legend()

# Save the figure.
plt.savefig("decay.eps")

# Showing the fitted parameters 'popt', with their uncertainties correspoding to the square root of the covariance values given by the diagonals of the returned matrix 'pcov'
print("Optimal parameters:")
print("  m = %g +/- %g"  % (popt[0], np.sqrt(pcov[0][0])))  # media "mu" m
print("  s = %g +/- %g"  % (popt[1], np.sqrt(pcov[1][1])))  # stdev "sigma" s
print("  A = %g +/- %g"  % (popt[2], np.sqrt(pcov[2][2])))  # Amplitude A
print("  y0 = %g +/- %g" % (popt[3], np.sqrt(pcov[3][3])))  # 
print("  b = %g +/- %g"  % (popt[4], np.sqrt(pcov[4][4])))  #
print()  # print blank line

# ----------------------------  Testing with Chi^2  ----------------------------------------------

# Delta degrees of freedom
ddof = 5

#--------- chi^2 test "Mannually" -----------
 
print("Manual chi^2 test:")

# Calculate chi^2
uncertainty = np.sqrt(fit_count)
chi2 = ((count - fit_count)**2 / uncertainty**2).sum()

# Calculate p-value and print
p = scipy.stats.distributions.chi2.sf(chi2, len(count) - ddof)
print("  chi2 / dof = %g / %d" % (chi2, len(count) - ddof))
print("  p-value = %g" % p)

# --------- Chi^2 test using scipy -----------------
print("chi^2 from scipy:")

# Call chisquare and print.

#chi2, p = scipy.stats.chisquare(count, fit_count, ddof=ddof - 1)
#print("  chi2 / dof = %g / %d" % (chi2, len(count) - ddof))
#print("  p-value = %g" % p)

#print()  # print blank line
