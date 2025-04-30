import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

# Define the range for the x-axis
x = np.linspace(-4, 4, 1000)
y = norm.pdf(x, 0, 1)

# Z-scores for the interval
z_left = -0.92
z_right = 0.92

# Fill the area between -0.92 and 0.92
x_fill = np.linspace(z_left, z_right, 1000)
y_fill = norm.pdf(x_fill, 0, 1)

# Plotting
plt.figure(figsize=(10, 6))
plt.plot(x, y, color='black', label='Standard Normal Distribution')
plt.fill_between(x_fill, y_fill, color='lightgreen', alpha=0.6, label=r'Shaded Area: $P(-0.92 < Z < 0.92)$')

# Add vertical lines
plt.axvline(x=z_left, color='red', linestyle='--', label=r'$z = -0.92$')
plt.axvline(x=z_right, color='red', linestyle='--', label=r'$z = 0.92$')

# Annotations
plt.text(-2.5, 0.1, r"$\mu = 0,\ \sigma = 1$", fontsize=12)
plt.text(-0.7, 0.02, r"$P(-0.92 < Z < 0.92) = 0.6424$", fontsize=12)

# Formatting
plt.title('Standard Normal Distribution: Area Between $z = -0.92$ and $z = 0.92$', fontsize=14)
plt.xlabel('z', fontsize=12)
plt.ylabel('Probability Density', fontsize=12)
plt.grid(True)
plt.legend()
plt.tight_layout()

# Save and show
plt.savefig("normal_distribution_between_-0.92_and_0.92.png", dpi=300)
plt.show()
