import numpy as np
import matplotlib.pyplot as plt

# Constants
P_base = 3.721435e-9  # Base ℘ result

# Create ranges for τ_QCD and γ
tau_qcd_values = np.linspace(0.8e-18, 1.2e-18, 100)  # τ_QCD in seconds
gamma_imag_values = np.linspace(1.4, 2.2, 100)       # Imaginary coefficient for γ = i√3 ~ i*1.732

# Dummy function to simulate ℘ based on τ_QCD and γ imaginary part
def compute_P_transparent(tau_qcd=1e-18, gamma_imag=1.732, P_base=P_base):
    gamma = 1j * gamma_imag
    correction_term = (P_base ** 2) / (tau_qcd ** 2)
    complex_factor = (gamma + 0.01j) * (1 ** tau_qcd)  # x=1 for simplification
    higher_order = tau_qcd ** 3 / (10 * (1 ** 2))
    denominator = np.sqrt(-1 + complex_factor + correction_term + higher_order)
    result = P_base * np.abs(1 / denominator)  # simplified form of integral behavior
    return np.real(result)

# Sensitivity over τ_QCD
P_vs_tau = [compute_P_transparent(tau_qcd=tau) for tau in tau_qcd_values]

# Sensitivity over γ (imaginary part)
P_vs_gamma = [compute_P_transparent(gamma_imag=gamma) for gamma in gamma_imag_values]

# Plotting
fig, axs = plt.subplots(1, 2, figsize=(14, 5))

# τ_QCD sensitivity
axs[0].plot(tau_qcd_values * 1e18, P_vs_tau, color='darkorange')
axs[0].axhline(P_base, color='gray', linestyle='--', linewidth=1)
axs[0].set_title('Sensitivity of ℘ to τ_QCD')
axs[0].set_xlabel('τ_QCD (×10⁻¹⁸ s)')
axs[0].set_ylabel('℘')
axs[0].grid(True)

# γ (imaginary part) sensitivity
axs[1].plot(gamma_imag_values, P_vs_gamma, color='seagreen')
axs[1].axhline(P_base, color='gray', linestyle='--', linewidth=1)
axs[1].set_title('Sensitivity of ℘ to γ (imaginary part)')
axs[1].set_xlabel('γ (imaginary component)')
axs[1].set_ylabel('℘')
axs[1].grid(True)

plt.tight_layout()
plt.show()

