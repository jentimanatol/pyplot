import matplotlib.pyplot as plt
import numpy as np

# Example data
x = np.array([58, 50, 65, 59, 59, 48])  # Chest size (inches)
y = np.array([414, 312, 499, 450, 456, 260])  # Weight (lbs)

# Regression line
b1, b0 = 14.1, -398.2  # Slope and intercept
regression_line = b0 + b1 * x

# Plot
plt.figure(figsize=(10, 6))
plt.scatter(x, y, color='#3498DB', label='Actual Data')
plt.plot(x, regression_line, '--', color='#E74C3C', label='Regression Line: $\hat{y} = -398.2 + 14.1x$')
plt.xlabel('Chest Size (inches)')
plt.ylabel('Weight (lbs)')
plt.legend()
plt.grid(True, alpha=0.3)
plt.title('Bear Weight vs. Chest Size Regression')
plt.show()