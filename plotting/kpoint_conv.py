import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

# Define the parabolic function
def parabola(x, a, b, c):
    return a * x**2 + b * x + c

# Read data from file
kpoints = []
energies = []
with open('kpoints_energies.dat', 'r') as f:
    for line in f:
        kpoint, energy = map(float, line.split())
        kpoints.append(kpoint)
        energies.append(energy)

kpoints = np.array(kpoints)
energies = np.array(energies)

# Fit a parabola to the data
popt, _ = curve_fit(parabola, kpoints, energies)

# Generate points for the fitted parabola
kpoints_fit = np.linspace(min(kpoints), max(kpoints), 100)
energies_fit = parabola(kpoints_fit, *popt)

# Plot the data and the fitted parabola
plt.plot(kpoints, energies, 'o', label='Data')
plt.plot(kpoints_fit, energies_fit, '-', label='Fit: a=%.3f, b=%.3f, c=%.3f' % tuple(popt))
plt.xlabel('K-point Grid Density (n)')
plt.ylabel('Total Energy (eV)')
plt.title('K-point Convergence Test for Carbon')
plt.legend()
plt.grid(True)
plt.show()

