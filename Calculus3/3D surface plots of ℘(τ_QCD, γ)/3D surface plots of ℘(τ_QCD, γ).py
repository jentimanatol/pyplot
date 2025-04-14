import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Define Ψ(x) and Φ(x)
def psi(x): return np.sin(x)
def phi(x): return np.cos(x)

# Define integration range
x_vals = np.linspace(0.1, 10, 500)  # avoid x=0

# Define parameter grids
tau_qcd_vals = np.logspace(-20, -16, 30)
gamma_imag_vals = np.linspace(0.1, 5.0, 30)

# Initialize result matrix
P_surface = np.zeros((len(tau_qcd_vals), len(gamma_imag_vals)))

# Calculate P for each (tau_qcd, gamma)
for i, tau_qcd in enumerate(tau_qcd_vals):
    for j, gamma_imag in enumerate(gamma_imag_vals):
        gamma = 1j * gamma_imag
        def integrand(x):
            numerator = psi(x) * phi(x)
            correction = (3.721435e-9 ** 2) / (tau_qcd ** 2)
            higher_order = (tau_qcd ** 3) / (10 * x**2)
            denominator = np.sqrt(-1 + (gamma + 0.01j) * x**tau_qcd + correction + higher_order)
            return np.real(numerator / denominator)
        y_vals = np.array([integrand(x) for x in x_vals])
        P_surface[i, j] = np.trapz(y_vals, x_vals)

# Create 3D surface plot
Tau, Gamma = np.meshgrid(gamma_imag_vals, tau_qcd_vals)
fig = plt.figure(figsize=(12, 7))
ax = fig.add_subplot(111, projection='3d')
surf = ax.plot_surface(Gamma, Tau, P_surface, cmap='viridis')

ax.set_title("3D Surface Plot of ℘(τ_QCD, γ)")
ax.set_xlabel("γ (imaginary component)")
ax.set_ylabel("τ_QCD (s)")
ax.set_zlabel("℘ value")
fig.colorbar(surf, shrink=0.5, aspect=10)
plt.tight_layout()
plt.show()

