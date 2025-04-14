import numpy as np
import matplotlib.pyplot as plt

# Define the symbolic range
x_values = np.linspace(0.1, 10, 1000)  # avoid zero in denominator

# Constants
P_base = 3.721435e-9
tau_qcd = 1e-18
gamma_imag = np.sqrt(3)
gamma = 1j * gamma_imag

# Define Ψ(x) and Φ(x) as sample waveforms
def psi(x): return np.sin(x)
def phi(x): return np.cos(x)

# Compute ℘ integrand
def compute_integrand(x, P_value, tau_qcd, gamma):
    numerator = psi(x) * phi(x)
    correction_term = (P_value ** 2) / (tau_qcd ** 2)
    higher_order_term = (tau_qcd ** 3) / (10 * x ** 2)
    complex_factor = (gamma + 0.01j) * x ** tau_qcd
    denominator = np.sqrt(-1 + complex_factor + correction_term + higher_order_term)
    return np.real(numerator / denominator)

# Evaluate integrand over range
integrand_values = compute_integrand(x_values, P_base, tau_qcd, gamma)

# Plotting
plt.figure(figsize=(10, 5))
plt.plot(x_values, integrand_values, label=r"$\frac{\Psi(x) \otimes \Phi(x)}{\sqrt{-1 + (\gamma + 0.01i)x^{\tau_{QCD}} + \frac{\mathcal{P}^2}{\tau_{QCD}^2} + \frac{\tau_{QCD}^3}{10x^2}}}$")
plt.title("Visualization of Quantumation Integrand")
plt.xlabel("x")
plt.ylabel("Integrand Value")
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()

