import numpy as np
import matplotlib.pyplot as plt

# Given total energies
E_bulk = -1964.90316886  # Pristine cell
E_VBM = 9.7118  # Valence band maximum from bulk calculation
mu_N = 0

# Interstitial energies
E_defects_interstitial_010 = {
    +1: -1973.49125352,
    0: -1962.80392835,
    -1: -1949.99262910,
    -2: -1936.69816384,
    -3: -1922.93274672,
    -4: -1909.05878820
}

# Error corrections for interstitials (initially zero, will be updated later)
E_corr_interstitial_010 = {
    +1: 0.367166,
    0: 0.0,
    -1: 0.297166,
    -2: 1.28267,
    -3: 3.2145,
    -4: 5.23386
}

# Interstitial energies
E_defects_interstitial_100 = {
    +1: -1973.49166638,
    0: -1962.80294941,
    -1: -1949.99137394,
    -2: -1936.69845202,
    -3: -1922.93302104,
    -4: -1909.05909242
}

# Error corrections for interstitials (initially zero, will be updated later)
E_corr_interstitial_100 = {
    +1: 0.307166,
    0: 0.0,
    -1: 0.355166,
    -2: 1.40867,
    -3: 3.3645,
    -4: 6.19066
}

# Chemical potentials
mu_C = E_bulk / 216 

# Range of Fermi levels from VBM to CBM
fermi_levels = np.linspace(0, 10, 100)

# Calculate formation energies for different charge states
def formation_energy(E_defect, E_bulk, q, E_vbm, E_fermi, n_C, n_N, mu_C, mu_N, E_corr):
    return E_defect - E_bulk - (n_C * mu_C) - (n_N * mu_N) + q * (E_vbm + E_fermi) + E_corr


# Formation energies for Interstitial
E_f_interstitial_minus_four_100 = formation_energy(E_defects_interstitial_100[-4], E_bulk_interstitial, -4, E_VBM, fermi_levels, 1, 0, mu_C_interstitial, mu_N, E_corr_interstitial_100[-4])
E_f_interstitial_minus_three_100 = formation_energy(E_defects_interstitial_100[-3], E_bulk_interstitial, -3, E_VBM, fermi_levels, 1, 0, mu_C_interstitial, mu_N, E_corr_interstitial_100[-3])
E_f_interstitial_minus_two_100 = formation_energy(E_defects_interstitial_100[-2], E_bulk_interstitial, -2, E_VBM, fermi_levels, 1, 0, mu_C_interstitial, mu_N, E_corr_interstitial_100[-2])
E_f_interstitial_minus_one_100 = formation_energy(E_defects_interstitial_100[-1], E_bulk_interstitial, -1, E_VBM, fermi_levels, 1, 0, mu_C_interstitial, mu_N, E_corr_interstitial_100[-1])
E_f_interstitial_neutral_100 = formation_energy(E_defects_interstitial_100[0], E_bulk_interstitial, 0, E_VBM, fermi_levels, 1, 0, mu_C_interstitial, mu_N, E_corr_interstitial_100[0])
E_f_interstitial_plus_one_100 = formation_energy(E_defects_interstitial_100[1], E_bulk_interstitial, 1, E_VBM, fermi_levels, 1, 0, mu_C_interstitial, mu_N, E_corr_interstitial_100[1])

# Formation energies for Interstitial
E_f_interstitial_minus_four_010 = formation_energy(E_defects_interstitial_010[-4], E_bulk_interstitial, -4, E_VBM, fermi_levels, 1, 0, mu_C_interstitial, mu_N, E_corr_interstitial_010[-4])
E_f_interstitial_minus_three_010 = formation_energy(E_defects_interstitial_010[-3], E_bulk_interstitial, -3, E_VBM, fermi_levels, 1, 0, mu_C_interstitial, mu_N, E_corr_interstitial_010[-3])
E_f_interstitial_minus_two_010 = formation_energy(E_defects_interstitial_010[-2], E_bulk_interstitial, -2, E_VBM, fermi_levels, 1, 0, mu_C_interstitial, mu_N, E_corr_interstitial_010[-2])
E_f_interstitial_minus_one_010 = formation_energy(E_defects_interstitial_010[-1], E_bulk_interstitial, -1, E_VBM, fermi_levels, 1, 0, mu_C_interstitial, mu_N, E_corr_interstitial_010[-1])
E_f_interstitial_neutral_010 = formation_energy(E_defects_interstitial_010[0], E_bulk_interstitial, 0, E_VBM, fermi_levels, 1, 0, mu_C_interstitial, mu_N, E_corr_interstitial_010[0])
E_f_interstitial_plus_one_010 = formation_energy(E_defects_interstitial_010[1], E_bulk_interstitial, 1, E_VBM, fermi_levels, 1, 0, mu_C_interstitial, mu_N, E_corr_interstitial_010[1])

# Select the lowest energy charge state for each defect at each Fermi level
E_defects_interstitial_100 = np.minimum(np.minimum(np.minimum(np.minimum(np.minimum(E_f_interstitial_neutral_100, E_f_interstitial_plus_one_100), E_f_interstitial_minus_one_100), E_f_interstitial_minus_two_100), E_f_interstitial_minus_three_100),E_f_interstitial_minus_four_100)
E_defects_interstitial_010 = np.minimum(np.minimum(np.minimum(np.minimum(np.minimum(E_f_interstitial_neutral_010, E_f_interstitial_plus_one_010), E_f_interstitial_minus_one_010), E_f_interstitial_minus_two_010), E_f_interstitial_minus_three_010),E_f_interstitial_minus_four_010)

# Determine the Fermi level range for the stability region
#stability_region_start = 1.9 
#stability_region_end = 4.13   

#print(E_f_NV_neutral, E_f_NV_plus_one, E_f_NV_minus_one, E_f_NV_minus_two)

# Plotting the formation energies
plt.figure(figsize=(6, 8))  # Adjust the figure size to make it more vertical

# Plot for NV Center with only the most stable charge state at each Fermi level
plt.plot(fermi_levels, E_defects_interstitial_100, label='100', color='green', linewidth=3)

# Plot for Vacancy with only the most stable charge state at each Fermi level
plt.plot(fermi_levels, E_defects_interstitial_010, label='010', color='blue', linewidth=3)

# Highlight the stability region
#plt.fill_between(fermi_levels, 1.8, 7.2, 
                 #where=(fermi_levels >= stability_region_start) & (fermi_levels <= stability_region_end), 
                # color='green', alpha=0.2)

# Additional plot styling to match the reference plot
plt.xlabel('Fermi level (eV)', fontsize=14)
plt.ylabel('Formation energy (eV)', fontsize=14)
plt.xlim([0, 10])
plt.ylim([0, 10]) 
plt.xticks(fontsize=12)
plt.yticks(fontsize=12)

# Add grid lines
plt.grid(True, which='both', linestyle='--', linewidth=0.7)

# Minor ticks
plt.minorticks_on()

plt.legend(fontsize=12, loc='upper left')
plt.title('Formation Energy of self-interstitials in diamond', loc='left', fontsize=16, fontweight='bold')  # Title in the top-left corner

# Label the stability region for NV center
#plt.text(3.0, 6.5, 'Stability Region\nfor NV⁻1', fontsize=12, color='green', 
         #ha='center', bbox=dict(facecolor='white', alpha=0.5, edgecolor='green'))

# Tight layout for better spacing
plt.tight_layout()

plt.show()

