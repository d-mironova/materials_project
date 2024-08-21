import matplotlib.pyplot as plt
import numpy as np

# Define energy levels (example values)
E_ground_relaxed = -1948.96101285  # Ground state relaxed energy (reference)
E_excited_relaxed = 2.02  # Excited state relaxed energy
E_ground_excited_geom = 1.80  # Ground state energy at excited state geometry
E_excited_ground_geom = 2.27  # Excited state energy at ground state geometry

# Generate the coordinate values
coords = np.linspace(-1, 1, 100)

# Quadratic potential energy surfaces (PES) as a function of coordinate
# Assume some arbitrary curvature (a for ground state, b for excited state)
a, b = 1.0, 1.0

ground_state_pes = a * (coords ** 2) + E_ground_relaxed
excited_state_pes = b * (coords ** 2) + E_excited_relaxed

# Plotting the potential energy surfaces
plt.plot(coords, ground_state_pes, label="Ground State PES", color='black')
plt.plot(coords, excited_state_pes, label="Excited State PES", color='black')

# Mark the energy points
plt.hlines(E_excited_ground_geom, xmin=-1, xmax=0, color='red', linestyle='--', label="Absorption")
plt.hlines(E_ground_excited_geom, xmin=0, xmax=1, color='blue', linestyle='--', label="Emission")
plt.hlines(E_excited_relaxed, xmin=-0.2, xmax=0.2, color='green', linestyle='--', label="ZPL")

# Annotate the points
plt.annotate("Absorption 2.27 eV", xy=(0, E_excited_ground_geom), xytext=(-0.5, E_excited_ground_geom + 0.2),
             arrowprops=dict(facecolor='red', shrink=0.05))
plt.annotate("Emission 1.80 eV", xy=(0, E_ground_excited_geom), xytext=(0.5, E_ground_excited_geom + 0.2),
             arrowprops=dict(facecolor='blue', shrink=0.05))
plt.annotate("ZPL 2.02 eV", xy=(0, E_excited_relaxed), xytext=(0.2, E_excited_relaxed + 0.2),
             arrowprops=dict(facecolor='green', shrink=0.05))

# Set labels and title
plt.xlabel("Generalized Coordinate")
plt.ylabel("Energy (eV)")
plt.legend()
plt.title("Configuration-Coordinate Diagram")
plt.grid(True)

# Display the plot
plt.show()

