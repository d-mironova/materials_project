import numpy as np
import matplotlib.pyplot as plt

# Given total energies
E_bulk_interstitial = -1962.08822356  # Pristine cell for self-interstitial

E_VBM = 9.7118  # Valence band maximum from bulk calculation

# Interstitial energies
E_defects_interstitial = {
    +1: -1973.49166638,
    0: -1962.80294941,
    -1: -1949.99137394,
    -2: -1936.69845202,
    -3: -1922.93302104,
    -4: -1909.05909242
}

# Chemical potentials
mu_C_interstitial = E_bulk_interstitial / 216

# Error corrections for interstitials (initially zero, will be updated later)
E_corr_interstitial = {
    +1: 0.307166,
    0: 0.0,
    -1: 0.355166,
    -2: 1.40867,
    -3: 3.3645,
    -4: 6.19066
}

# Range of Fermi levels from VBM to CBM
fermi_levels = np.linspace(0, 10, 100)

def formation_energy(E_defect, E_bulk, q, E_vbm, E_fermi, n_C, n_N, mu_C, mu_N, E_corr):
    return E_defect - E_bulk - (n_C * mu_C) - (n_N * mu_N) + q * (E_vbm + E_fermi) + E_corr

# Formation energies for Interstitial
E_f_interstitial_minus_four = formation_energy(E_defects_interstitial[-4], E_bulk_interstitial, -4, E_VBM, fermi_levels, 1, 0, mu_C_interstitial, mu_N, E_corr_interstitial[-4])
E_f_interstitial_minus_three = formation_energy(E_defects_interstitial[-3], E_bulk_interstitial, -3, E_VBM, fermi_levels, 1, 0, mu_C_interstitial, mu_N, E_corr_interstitial[-3])
E_f_interstitial_minus_two = formation_energy(E_defects_interstitial[-2], E_bulk_interstitial, -2, E_VBM, fermi_levels, 1, 0, mu_C_interstitial, mu_N, E_corr_interstitial[-2])
E_f_interstitial_minus_one = formation_energy(E_defects_interstitial[-1], E_bulk_interstitial, -1, E_VBM, fermi_levels, 1, 0, mu_C_interstitial, mu_N, E_corr_interstitial[-1])
E_f_interstitial_neutral = formation_energy(E_defects_interstitial[0], E_bulk_interstitial, 0, E_VBM, fermi_levels, 1, 0, mu_C_interstitial, mu_N, E_corr_interstitial[0])
E_f_interstitial_plus_one = formation_energy(E_defects_interstitial[1], E_bulk_interstitial, 1, E_VBM, fermi_levels, 1, 0, mu_C_interstitial, mu_N, E_corr_interstitial[1])

# Plotting the formation energies
plt.figure(figsize=(10, 6))

# Plot for Interstitial
plt.plot(fermi_levels, E_f_interstitial_neutral, label='Interstitial (neutral)', color='brown')
plt.plot(fermi_levels, E_f_interstitial_plus_one, label='Interstitial (+1)', color='pink')
plt.plot(fermi_levels, E_f_interstitial_minus_one, label='Interstitial (-1)', color='blue')
plt.plot(fermi_levels, E_f_interstitial_minus_two, label='Interstitial (-2)', color='purple')
plt.plot(fermi_levels, E_f_interstitial_minus_three, label='Interstitial (-3)', color='red')
plt.plot(fermi_levels, E_f_interstitial_minus_four, label='Interstitial (-4)', color='green')


plt.xlabel('Fermi Level (eV)')
plt.ylabel('Formation Energy (eV)')
plt.title('Formation Energy of 100 Single Self-Interstitial in Diamond (217 atoms)')
plt.legend()
plt.grid(True)
plt.show()

