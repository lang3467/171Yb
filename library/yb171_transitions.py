# yb171_transitions.py

import numpy as np


# === Fundamental Constants (CODATA 2022) ===
c = 2.99792458e8        # m/s, speed of light
epsilon0 = 8.8541878188e-12  # F/m, vacuum permittivity
h = 6.62607015e-34      # J*s, Planck constant
hbar = 1.054571817e-34  # J*s, reduced Planck constant
e = 1.602176634e-19     # C, elementary charge
kB = 1.380649e-23       # J/K, Boltzmann constant
amu = 1.66053906660e-27 # kg
a0 = 5.29177210544e-11  # m, Bohr radius
me = 9.1093837139e-31   # kg, electron mass

# === Yb-171 Properties ===

# Yb-171 atomic mass
mass_u = 170.936331515
mass_kg = mass_u * amu

# Yb-171 atomic transitions & laser information
Transitions = {
    "399nm": {
        "name": "1S0 -> 1P1",
        "lambda_nm": 398.9108443,
        "tau_s": 5.464e-9,
        "gamma_Hz": 2*np.pi*29.13e6,
        "Isat_W_m2": 59.97e-3*1e4,   # mW/cm^2 → W/m^2
        "T_Doppler_K": 6.99e-4
    },
    "556nm": {
        "name": "1S0 -> 3P1",
        "lambda_nm": 555.8,
        "tau_s": 0.87e-6,
        "gamma_Hz": 2*np.pi*182e3,
        "Isat_W_m2": None,           # 문헌에서 보완 가능
        "T_Doppler_K": 4.4e-6
    },
    "578nm": {
        "name": "1S0 -> 3P0 (clock)",
        "lambda_nm": 578.0,
        "tau_s": None,               # 초장수명 (mHz linewidth)
        "gamma_Hz": None,
        "Isat_W_m2": None,
        "T_Doppler_K": None
    },
    "1389nm": {
        "name": "3P0 -> 3D1 (repump)",
        "lambda_nm": 1389.0,
        "tau_s": None,
        "gamma_Hz": None,
        "Isat_W_m2": None,
        "T_Doppler_K": None
    },
    "759nm": {
        "name": "3P0 -> 3S1 (repump)",
        "lambda_nm": 770.160,
        "tau_s": 13.8e-9,
        "gamma_Hz": 2*np.pi*11.5e6,
        "Isat_W_m2": None,
        "T_Doppler_K": 2.77e-4
    }
}
