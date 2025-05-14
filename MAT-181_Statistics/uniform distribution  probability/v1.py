import matplotlib.pyplot as plt
import numpy as np

# Parameters for the uniform distribution
a, b = 6, 12
pdf_value = 1 / (b - a)

# Define the range for the x-axis
x = np.linspace(5, 13, 1000)
y = np.where((x >= a) & (x <= b), pdf_value, 0)

# Highlight the region between 8.5 and 10
x_fill = np.linspace(8.5, 10, 1000)
y_fill = np.full_like(x_fill, pdf_value)

# Plotting
plt.figure(figsize=(10, 6))
plt.plot(x, y, label='PDF of Uniform($a=6$, $b=12$)', color='blue')
plt.fill_between(x_fill, y_fill, alpha=0.5, color='orange', label='Area: $P(8.5 \\leq X \\leq 10)$')

# Add annotations
plt.text(8.7, 0.18, '$f(x) = \\frac{1}{b - a} = \\frac{1}{12 - 6} = \\frac{1}{6}$', fontsize=12)
plt.text(8.7, 0.15, '$P(8.5 \\leq X \\leq 10) = \\frac{10 - 8.5}{12 - 6} = \\frac{1.5}{6} = 0.25$', fontsize=12)

# Formatting the plot
plt.title('Uniform Distribution: $X \\sim U(6, 12)$', fontsize=14)
plt.xlabel('Weight Loss (pounds)', fontsize=12)
plt.ylabel('Probability Density', fontsize=12)
plt.ylim(0, 0.25)
plt.legend()
plt.grid(True)
plt.tight_layout()

plt.show()
