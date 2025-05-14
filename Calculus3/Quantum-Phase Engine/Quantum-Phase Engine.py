import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm

# Define the function to approximate ℘(τ_QCD, γ)
def compute_P(tau, gamma):
    # Avoid division by zero and manage domain
    x = np.linspace(0.1, 10, 100)
    integrand = np.sin(x) * np.cos(x) / np.sqrt(
        -1 + (gamma + 0.01j) * x**tau + 1 / (tau**2) + (tau**3) / (10 * x**2)
    )
    return np.abs(np.trapz(integrand, x))

# Generate values for τ_QCD and γ
tau_vals = np.linspace(0.5, 3, 50)  # abstract scale range
gamma_vals = np.linspace(0.1, 5, 50)

# Meshgrid for surface plot
T, G = np.meshgrid(tau_vals, gamma_vals)
P = np.zeros_like(T)

# Calculate ℘ for each pair (τ_QCD, γ)
for i in range(T.shape[0]):
    for j in range(T.shape[1]):
        try:
            P[i, j] = compute_P(T[i, j], G[i, j])
        except Exception:
            P[i, j] = np.nan  # handle complex errors

# Plotting
fig = plt.figure(figsize=(12, 8))
ax = fig.add_subplot(111, projection='3d')
surf = ax.plot_surface(T, G, P, cmap=cm.viridis, edgecolor='none')
ax.set_title('Surface Plot of ℘(τ_QCD, γ)', fontsize=14)
ax.set_xlabel('τ_QCD')
ax.set_ylabel('γ')
ax.set_zlabel('℘')
fig.colorbar(surf, ax=ax, shrink=0.5, aspect=5)
plt.tight_layout()
plt.show()
