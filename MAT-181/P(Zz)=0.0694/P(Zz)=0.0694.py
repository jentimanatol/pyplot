import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

# Right-tail area
right_area = 0.0694
left_area = 1 - right_area

# Compute the z-score
z_cutoff = norm.ppf(left_area)

# Define the range for the x-axis
x = np.linspace(-4, 4, 1000)
y = norm.pdf(x, 0, 1)

# Fill the area from z_cutoff to +infinity
x_fill = np.linspace(z_cutoff, 4, 1000)
y_fill = norm.pdf(x_fill, 0, 1)

# Plotting
plt.figure(figsize=(10, 6))
plt.plot(x, y, color='black', label='Standard Normal Distribution')
plt.fill_between(x_fill, y_fill, color='orange', alpha=0.6, label=r'Shaded Area: $P(Z > z)$')

# Add vertical line at z = z_cutoff
plt.axvline(x=z_cutoff, color='red', linestyle='--', label=fr'$z = {z_cutoff:.2f}$')

# Annotations
plt.text(-3.5, 0.1, r"$\mu = 0,\ \sigma = 1$", fontsize=12)
plt.text(z_cutoff + 0.2, 0.02, rf"$P(Z > {z_cutoff:.2f}) = 0.0694$", fontsize=12)

# Formatting
plt.title('Standard Normal Distribution: Area to the Right of a Z-Score', fontsize=14)
plt.xlabel('z', fontsize=12)
plt.ylabel('Probability Density', fontsize=12)
plt.grid(True)
plt.legend()
plt.tight_layout()

# Save and show
plt.savefig("normal_distribution_right_tail_0.0694.png", dpi=300)
plt.show()
