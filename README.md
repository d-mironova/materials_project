# Computational materials with VASP

## Overview
This is a repository for the code base of my computational materials projects related to the NV-centers and interstitials. This project contains scripts for Density of States (DOS) calculations, plotting various physical properties, and charge analysis related to carbon self-interstitials in diamond.

## Directory Structure

- `dos_calculation/` - Scripts for DOS calculations and plotting DOS related to interstitial and neighboring atoms.
- `plotting/` - Scripts for plotting formation energies, stability regions, and other related physical properties.
- `charge_analysis/` - Scripts for charge density analysis.

## Installation

To run these scripts, you will need:
- Python 3.x
- Gnuplot
- VASP (for generating necessary data)
- Perl (for running the `.pl` scripts)

## Usage

### DOS Calculation

1. **Split DOS**: 
    ```bash
    ./dos_calculation/split_dos
    ```
2. **Sum DOS for Interstitials**:
    ```bash
    ./dos_calculation/sum_dos_interstitials.sh
    ```
3. **Sum DOS for Neighbors**:
    ```bash
    ./dos_calculation/sum_dos_neighbours.sh
    ```

### Plotting

1. **Formation Energy Plot**:
    ```bash
    python plotting/formation_energy_defect.py
    ```

### Charge Analysis

1. **Split Charge Density**:
    ```bash
    ./charge_analysis/splitchg.pl PARCHG_file_name
    ```
