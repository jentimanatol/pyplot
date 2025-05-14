import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

# Define the range for the x-axis
x = np.linspace(-4, 4, 1000)
y = norm.pdf(x, 0, 1)

# Define the z-score cutoff
z_cutoff = 1.13

# Fill the area from -infinity to z = 1.13
x_fill = np.linspace(-4, z_cutoff, 1000)
y_fill = norm.pdf(x_fill, 0, 1)

# Plotting
plt.figure(figsize=(10, 6))
plt.plot(x, y, color='black', label='Standard Normal Distribution')
plt.fill_between(x_fill, y_fill, color='skyblue', alpha=0.6, label=r'Shaded Area: $P(Z < 1.13)$')

# Add annotation
plt.text(-3.5, 0.1, r"$\mu = 0,\ \sigma = 1$", fontsize=12)
plt.text(-0.5, 0.02, r"$P(Z < 1.13) = 0.8708$", fontsize=12, color='black')

# Add vertical line at z = 1.13
plt.axvline(x=z_cutoff, color='red', linestyle='--', label=r'$z = 1.13$')

# Formatting
plt.title('Standard Normal Distribution: Area to the Left of $z = 1.13$', fontsize=14)
plt.xlabel('z', fontsize=12)
plt.ylabel('Probability Density', fontsize=12)
plt.grid(True)
plt.legend()
plt.tight_layout()


plt.savefig("normal_distribution_z_less_than_1.13.png", dpi=300)






plt.show()
