import numpy as np
import matplotlib.pyplot as plt

# Parameters for the uniform distribution
a = 0  # Minimum value
b = 5  # Maximum value
x_value = 2.5  # Value to calculate probability for

# Probability calculation
probability = (x_value - a) / (b - a)

# Data for visualization
x = np.linspace(a - 1, b + 1, 500)  # Extended range for visualization
y = np.piecewise(x, [x < a, (x >= a) & (x <= b), x > b], [0, 1 / (b - a), 0])

# Plotting
plt.figure(figsize=(8, 5))
plt.plot(x, y, label='Uniform Density Curve', color='blue')
plt.fill_between(x, y, where=(x <= x_value) & (x >= a), color='lightblue', alpha=0.5,
                 label=f'P(X < {x_value}) = {probability:.2f}')
plt.axvline(x_value, color='red', linestyle='--', label=f'X = {x_value}')
plt.title('Uniform Distribution')
plt.xlabel('X')
plt.ylabel('Density')
plt.legend()
plt.grid(alpha=0.4)
plt.show()