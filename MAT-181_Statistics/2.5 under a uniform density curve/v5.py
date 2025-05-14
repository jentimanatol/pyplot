import numpy as np
import matplotlib.pyplot as plt

# Parameters of the uniform distribution
a = 6   # Minimum weight loss
b = 12  # Maximum weight loss

# Values for the x-axis
x = np.linspace(4, 14, 1000)  # Extend beyond the range for visual clarity
y = np.where((x >= a) & (x <= b), 1/(b - a), 0)  # Uniform distribution PDF

# Plot the uniform distribution
plt.figure(figsize=(10, 5))
plt.plot(x, y, label='Uniform Distribution (6 to 12 lbs)', color='blue')
plt.fill_between(x, y, where=(x >= 0.2) & (x <= 0.8), color='red', alpha=0.3, label='P(0.2 ≤ X ≤ 0.8) = 0')

# Add lines to indicate the interval boundaries
plt.axvline(0.2, color='red', linestyle='--', linewidth=1)
plt.axvline(0.8, color='red', linestyle='--', linewidth=1)

# Labels and title
plt.title('Uniform Distribution of Weight Loss (6 to 12 lbs)')
plt.xlabel('Pounds Lost')
plt.ylabel('Probability Density')
plt.legend()
plt.grid(True)
plt.show()
