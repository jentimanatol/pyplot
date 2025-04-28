import numpy as np
import matplotlib.pyplot as plt

# Uniform distribution parameters
a = 6   # Minimum
b = 12  # Maximum
height = 1 / (b - a)  # Height of the uniform PDF

# X values for plotting
x = np.linspace(4, 14, 1000)
y = np.where((x >= a) & (x <= b), height, 0)

# Plot the uniform PDF
plt.figure(figsize=(10, 5))
plt.plot(x, y, label='Uniform Distribution (6 to 12 lbs)', color='blue')
plt.fill_between(x, y, where=(x >= 0.2) & (x <= 0.8), color='red', alpha=0.3, label='P(0.2 ≤ X ≤ 0.8) = 0')

# Dashed lines to mark 0.2 and 0.8
plt.axvline(0.2, color='red', linestyle='--')
plt.axvline(0.8, color='red', linestyle='--')

# Label the height
plt.text(6.1, height + 0.005, 'Height = 1/6 ≈ 0.1667', fontsize=10, color='blue')

# Labels and styling
plt.title('Uniform Distribution of Weight Loss (6 to 12 lbs)')
plt.xlabel('Pounds Lost')
plt.ylabel('Probability Density (P(x))')
plt.legend()
plt.grid(True)
plt.ylim(0, 0.2)
plt.show()
