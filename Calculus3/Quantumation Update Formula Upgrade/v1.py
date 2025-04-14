import numpy as np
import matplotlib.pyplot as plt

# Define parameter ranges for sensitivity analysis
delta_values = np.linspace(0.8, 1.2, 100)   # Δ variation
C_real_values = np.linspace(0.8, 1.2, 100)  # ℂ real part variation
P_base = 3.721435e-9                        # Base ℘ result

# Dummy function to simulate ℘ based on Δ and ℂ changes
def compute_P(delta=1.0, C_real=1.0, P_base=P_base):
    # Simulate formula changes impact — this is a synthetic model
    correction_term = (P_base ** 2) / (delta ** 2)
    complex_factor = (C_real + 0.01j) * (1 ** delta)  # x=1 for simplification
    higher_order = delta ** 3 / (10 * (1 ** 2))
    denominator = np.sqrt(-1 + complex_factor + correction_term + higher_order)
    result = P_base * np.abs(1 / denominator)  # simplified form of integral behavior
    return np.real(result)

# Sensitivity analysis over Δ
P_vs_delta = [compute_P(delta=d) for d in delta_values]

# Sensitivity analysis over ℂ (real part)
P_vs_C_real = [compute_P(C_real=c) for c in C_real_values]

# Plotting
fig, axs = plt.subplots(1, 2, figsize=(14, 5))

# Δ sensitivity
axs[0].plot(delta_values, P_vs_delta, label='℘ vs Δ', color='teal')
axs[0].axhline(P_base, color='gray', linestyle='--', linewidth=1)
axs[0].set_title('Sensitivity of ℘ to Δ')
axs[0].set_xlabel('Δ')
axs[0].set_ylabel('℘')
axs[0].grid(True)

# ℂ sensitivity
axs[1].plot(C_real_values, P_vs_C_real, label='℘ vs ℂ (real)', color='purple')
axs[1].axhline(P_base, color='gray', linestyle='--', linewidth=1)
axs[1].set_title('Sensitivity of ℘ to ℂ (real part)')
axs[1].set_xlabel('ℂ (real)')
axs[1].set_ylabel('℘')
axs[1].grid(True)

plt.tight_layout()
plt.show()
