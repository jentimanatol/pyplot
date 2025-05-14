import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

# Function to plot the standard normal distribution with shaded area
def plot_z_shaded(z_value):
    x = np.linspace(-4, 4, 1000)
    y = norm.pdf(x, 0, 1)

    # Create the plot
    plt.plot(x, y, label='Standard Normal Distribution', color='blue')

    # Plot the z_value line
    plt.axvline(z_value, color='red', linestyle='--', label=f'z = {z_value}')

    # Shade the area to the left of z_value
    plt.fill_between(x, 0, y, where=(x <= z_value), color='red', alpha=0.5, label=f'Area to the left of z = {z_value} = 0.7764')

    # Add titles and labels
    plt.title('Standard Normal Distribution with Shaded Area')
    plt.xlabel('Value')
    plt.ylabel('Probability Density')
    plt.legend()
    plt.grid(True)
    plt.show()

# Plot for z = 0.76
plot_z_shaded(0.76)
