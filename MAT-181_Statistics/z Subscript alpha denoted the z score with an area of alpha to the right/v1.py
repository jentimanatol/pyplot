import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

# Function to plot z_alpha
def plot_z_alpha(alpha):
    x = np.linspace(-4, 4, 1000)
    y = norm.pdf(x, 0, 1)

    # Calculate z_alpha
    z_alpha = norm.ppf(1 - alpha)

    plt.plot(x, y, label='Standard Normal Distribution', color='blue')

    # Plot z_alpha line
    plt.axvline(z_alpha, color='red', linestyle='--', label=f'z_{alpha}={z_alpha:.2f}')

    plt.title(f'Standard Normal Distribution with z_{alpha}')
    plt.xlabel('Value')
    plt.ylabel('Probability Density')
    plt.legend()
    plt.grid(True)
    plt.show()

# Example: Plot z_alpha for alpha = 0.05
plot_z_alpha(0.05)
