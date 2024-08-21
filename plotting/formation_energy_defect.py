import numpy as np
import matplotlib.pyplot as plt

# Given total energies
E_bulk = -1964.90316886  # Pristine cell
E_VBM = 9.7118  # Valence band maximum from bulk calculation

# NV Center energies
E_NV_neutral = -1948.96101285
E_NV_plus_one = -1959.72264966
E_NV_minus_one = -1937.77024285
E_NV_minus_two = -1925.00819253

# Vacancy energies
E_V_C_neutral = -1949.24408503
E_V_C_minus_one = -1938.29231440
E_V_C_minus_two = -1925.68738426
E_V_C_plus_one = -1959.85078867

# Chemical potentials
mu_C = E_bulk / 216
mu_N = -16.63311990 / 2 

# Error corrections for different charge states
E_corr_NV = {
    0: 0.0,   # Correction for neutral NV center
    1: 0.172166,   # Correction for +1 charge state
    -1: 0.427166, # Correction for -1 charge state
    -2: 1.48867  # Correction for -2 charge state
}

E_corr_V_C = {
    0: 0.0,   # Correction for neutral vacancy
    1: 0.177166,   # Correction for +1 charge state
    -1: 0.387166, # Correction for -1 charge state
    -2: 1.36667  # Correction for -2 charge state
}

# Range of Fermi levels from VBM to CBM
fermi_levels = np.linspace(0, 5, 100)

# Calculate formation energies for different charge states
def formation_energy(E_defect, E_bulk, q, E_vbm, E_fermi, n_C, n_N, mu_C, mu_N, E_corr):
    return E_defect - E_bulk - (n_C * mu_C) - (n_N * mu_N) + q * (E_vbm + E_fermi) + E_corr

# Define n_C and n_N for each defect
# For NV center: two C atoms removed, one N atom added (n_C = -2, n_N = 1)
# For Vacancy: one C atom removed (n_C = -1, n_N = 0)

# Formation energies for NV center
E_f_NV_neutral = formation_energy(E_NV_neutral, E_bulk, 0, E_VBM, fermi_levels, -2, 1, mu_C, mu_N, E_corr_NV[0])
E_f_NV_plus_one = formation_energy(E_NV_plus_one, E_bulk, 1, E_VBM, fermi_levels, -2, 1, mu_C, mu_N, E_corr_NV[1])
E_f_NV_minus_one = formation_energy(E_NV_minus_one, E_bulk, -1, E_VBM, fermi_levels, -2, 1, mu_C, mu_N, E_corr_NV[-1])
E_f_NV_minus_two = formation_energy(E_NV_minus_two, E_bulk, -2, E_VBM, fermi_levels, -2, 1, mu_C, mu_N, E_corr_NV[-2])

# Formation energies for Vacancy
E_f_V_C_neutral = formation_energy(E_V_C_neutral, E_bulk, 0, E_VBM, fermi_levels, -1, 0, mu_C, mu_N, E_corr_V_C[0])
E_f_V_C_plus_one = formation_energy(E_V_C_plus_one, E_bulk, 1, E_VBM, fermi_levels, -1, 0, mu_C, mu_N, E_corr_V_C[1])
E_f_V_C_minus_one = formation_energy(E_V_C_minus_one, E_bulk, -1, E_VBM, fermi_levels, -1, 0, mu_C, mu_N, E_corr_V_C[-1])
E_f_V_C_minus_two = formation_energy(E_V_C_minus_two, E_bulk, -2, E_VBM, fermi_levels, -1, 0, mu_C, mu_N, E_corr_V_C[-2])

# Select the lowest energy charge state for each defect at each Fermi level
E_f_NV = np.minimum(np.minimum(np.minimum(E_f_NV_neutral, E_f_NV_plus_one), E_f_NV_minus_one), E_f_NV_minus_two)
E_f_V_C = np.minimum(np.minimum(np.minimum(E_f_V_C_neutral, E_f_V_C_plus_one), E_f_V_C_minus_one), E_f_V_C_minus_two)

# Determine the Fermi level range for the stability region
stability_region_start = 1.9 
stability_region_end = 4.13   

#print(E_f_NV_neutral, E_f_NV_plus_one, E_f_NV_minus_one, E_f_NV_minus_two)

# Plotting the formation energies
plt.figure(figsize=(6, 8))  # Adjust the figure size to make it more vertical

# Plot for NV Center with only the most stable charge state at each Fermi level
plt.plot(fermi_levels, E_f_NV, label='NV', color='green', linewidth=3)

# Plot for Vacancy with only the most stable charge state at each Fermi level
plt.plot(fermi_levels, E_f_V_C, label='V$_C$', color='blue', linewidth=3)

# Highlight the stability region
plt.fill_between(fermi_levels, 1.8, 7.2, 
                 where=(fermi_levels >= stability_region_start) & (fermi_levels <= stability_region_end), 
                 color='green', alpha=0.2)

# Additional plot styling to match the reference plot
plt.xlabel('Fermi level (eV)', fontsize=14)
plt.ylabel('Formation energy (eV)', fontsize=14)
plt.xlim([0, 5])
plt.ylim([1.8, 7.2]) 
plt.xticks(fontsize=12)
plt.yticks(fontsize=12)

# Add grid lines
plt.grid(True, which='both', linestyle='--', linewidth=0.7)

# Minor ticks
plt.minorticks_on()

plt.legend(fontsize=12, loc='upper left')
plt.title('Formation Energy of defects in diamond', loc='left', fontsize=16, fontweight='bold')  # Title in the top-left corner

# Label the stability region for NV center
plt.text(3.0, 6.5, 'Stability Region\nfor NV⁻1', fontsize=12, color='green', 
         ha='center', bbox=dict(facecolor='white', alpha=0.5, edgecolor='green'))

# Tight layout for better spacing
plt.tight_layout()

plt.show()

