import numpy as np
import matplotlib.pyplot as plt

# Parameters for the uniform distribution
a = 0
b = 8
x = 3.25

# Generate data points for the x-axis
x_values = np.linspace(a, b, 1000)

# Calculate the probability density function (PDF)
pdf = [1 / (b - a) for _ in x_values]

# Create the plot
plt.plot(x_values, pdf, label='Uniform Distribution', color='blue')
plt.fill_between(x_values, 0, pdf, where=(x_values > x), color='red', alpha=0.5, label=f'P(X > {x}) = 0.594')

# Add titles and labels
plt.title('Uniform Distribution between 0 and 8 minutes')
plt.xlabel('Waiting Time (minutes)')
plt.ylabel('Probability Density')
plt.legend()

# Show the plot
plt.grid(True)
plt.show()
