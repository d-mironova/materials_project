import matplotlib.pyplot as plt

# Read data from file
energies = []
with open('energies.dat', 'r') as f:
    for line in f:
        energies.append(float(line.strip()))

# Generate the corresponding energy cutoffs
cutoffs = list(range(100, 650, 50))

# Plot the data
plt.plot(cutoffs, energies, marker='o')
plt.xlabel('Energy Cutoff (eV)')
plt.ylabel('Total Energy (eV)')
plt.title('Energy Cutoff Test for Carbon')
plt.grid(True)
plt.show()

