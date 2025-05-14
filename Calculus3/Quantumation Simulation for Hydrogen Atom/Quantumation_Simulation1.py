import numpy as np
from scipy.integrate import quad
import matplotlib.pyplot as plt

# Constants
a0 = 5.29e-11            # Bohr radius (m)
m = 9.11e-31             # Electron mass (kg)
hbar = 1.055e-34         # Reduced Planck's constant (J·s)
C = 1.5                  # Complexification factor
Delta = 1e-18            # Nexus interval (s)

# Wave function Ψ(x)
def psi(x):
    return (np.sqrt(2/np.pi)) * np.exp(-x/a0)

# Temporal flux operator Φ(x)
def phi(x):
    return (x**2) / (2 * m * hbar)

# Integrand function
def integrand(x):
    numerator = psi(x) * phi(x)
    denominator = np.sqrt(-1 + C * (x**Delta))
    return np.real_if_close(numerator / denominator)

# Perform numerical integration over [0, Delta]
result, error = quad(integrand, 0, Delta, limit=1000)

# Output result
print(f"Quantumation (℘) ≈ {result:.5e} ℘ units")


# Plotting the integrand across [0, Delta]
x_vals = np.linspace(1e-21, Delta, 500)
y_vals = [integrand(x) for x in x_vals]

plt.plot(x_vals, y_vals)
plt.title("Quantumation Integrand")
plt.xlabel("x (m)")
plt.ylabel("Integrand Value")
plt.grid(True)
plt.show()
