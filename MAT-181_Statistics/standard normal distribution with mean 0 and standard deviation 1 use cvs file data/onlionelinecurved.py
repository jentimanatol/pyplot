import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

# Generate data points for the x-axis
x = np.linspace(-4, 4, 1000)

# Calculate the corresponding y values for a standard normal distribution
y = norm.pdf(x, 0, 1)

# Create the plot
plt.plot(x, y, label='Normal Distribution', color='blue')

# Add titles and labels
plt.title('Normal Distribution Curve')
plt.xlabel('Value')
plt.ylabel('Probability Density')
plt.legend()

# Show the plot
plt.grid(True)
plt.show()
