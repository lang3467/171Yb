import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), "library"))

import numpy as np
import matplotlib.pyplot as plt
import yb171_transitions as yb 

def plot_maxwell_boltzmann(T_celsius=25):
    """
    Maxwell-Boltzmann 속도 분포를 그려주는 함수.
    T_celsius [°C] : 섭씨 온도 (기본값 25 °C)
    """
    # Convert to Kelvin
    T = T_celsius + 273.15  

    # Mass of Yb-171
    M = yb.mass_kg

    # Most probable speed (u)
    u = np.sqrt(2 * yb.kB * T / M)
    print(f"T = {T_celsius:.1f} °C  ({T:.2f} K)")
    print(f"Most probable speed u: {u:.3f} m/s")

    # Standard deviation for Maxwell-Boltzmann distribution
    sigma_mb = np.sqrt(yb.kB * T / M)
    print(f"Maxwell-Boltzmann Standard Deviation: {sigma_mb:.3f} m/s")

    # Velocity range
    v = np.linspace(0, 1000, 1000)

    # Maxwell-Boltzmann distribution function
    def f_v(v):
        prefactor = (M / (2 * np.pi * yb.kB * T))**1.5 * 4 * np.pi * v**2
        exponent = np.exp(-M * v**2 / (2 * yb.kB * T))
        return prefactor * exponent

    f_values = f_v(v)

    # 1-sigma, mean u
    sigma_points_mb = [u - sigma_mb, u, u + sigma_mb]

    # Plot
    plt.figure(figsize=(8, 5))
    plt.plot(v, f_values, label=f'MB Distribution (T={T_celsius:.1f} °C)', color='b')

    # Mark sigma points
    for point in sigma_points_mb:
        plt.axvline(x=point, color='r', linestyle='--', alpha=0.7,
                    label=f'{point:.2f} m/s')

    plt.xlabel('Velocity (m/s)')
    plt.ylabel('Probability Density')
    plt.title(f'Maxwell-Boltzmann Distribution for Yb at {T_celsius:.1f} °C')
    plt.legend()
    plt.grid()
    plt.show()

# Example usage
plot_maxwell_boltzmann(T_celsius=400)  # 예: 127 °C 입력 → 내부적으로 400 K 계산
