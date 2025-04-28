import numpy as np
import matplotlib.pyplot as plt

# Parameters for the uniform density curve
a = 0       # Minimum value of X
b = 8       # Maximum value of X
x_value = 2.5  # The value for which probability is calculated

# Probability calculation
probability = (x_value - a) * 0.125  # Area under the curve
print(f"Probability that X < {x_value}: {probability:.3f}")

# Data for visualization
x = np.linspace(a - 1, b + 1, 500)  # Extended range for visualization
y = np.piecewise(x, [x < a, (x >= a) & (x <= b), x > b], [0, 0.125, 0])

# Plotting
plt.figure(figsize=(8, 5))
plt.plot(x, y, label='Uniform Density Curve', color='blue')
plt.fill_between(x, y, where=(x <= x_value) & (x >= a), color='lightblue', alpha=0.5,
                 label=f'P(X < {x_value}) = {probability:.3f}')
plt.axvline(x_value, color='red', linestyle='--', label=f'X = {x_value}')
plt.title('Uniform Distribution Curve')
plt.xlabel('X')
plt.ylabel('Probability Density P(x)')
plt.legend()
plt.grid(alpha=0.4)
plt.show()