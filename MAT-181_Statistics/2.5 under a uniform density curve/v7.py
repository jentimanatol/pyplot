import numpy as np
import matplotlib.pyplot as plt

# Uniform distribution parameters
a = 6
b = 12
height = 1 / (b - a)

# X and Y values
x = np.linspace(4, 14, 1000)
y = np.where((x >= a) & (x <= b), height, 0)

# Plot
fig, ax = plt.subplots(figsize=(10, 5))
ax.plot(x, y, label='Uniform Distribution (6 to 12 lbs)', color='blue')
ax.fill_between(x, y, where=(x >= 0.2) & (x <= 0.8), 
                facecolor='red', alpha=0.3, hatch='//', edgecolor='red',
                label='P(0.2 ≤ X ≤ 0.8) = 0 (outside range)')

# Dashed lines to indicate boundaries
ax.axvline(0.2, color='red', linestyle='--')
ax.axvline(0.8, color='red', linestyle='--')

# Height label
ax.text(6.1, height + 0.005, 'Height = 1/6 ≈ 0.1667', fontsize=10, color='blue')

# Labels and formatting
ax.set_title('Uniform Distribution of Weight Loss (6 to 12 lbs)')
ax.set_xlabel('Pounds Lost')
ax.set_ylabel('Probability Density (P(x))')
ax.legend()
ax.grid(True)
ax.set_ylim(0, 0.2)

plt.show()

# This code visualizes the uniform distribution of weight loss between 6 and 12 pounds.
# The area under the curve represents the probability density function, and the shaded area indicates the probability of weight loss within a specific range.
# The dashed lines indicate the boundaries of the range, and the height of the distribution is labeled for clarity.
# The plot is designed to be clear and informative, with appropriate labels and a legend.
# The use of hatching in the shaded area helps to distinguish it visually from the rest of the plot.
# The code is structured to be easy to read and understand, with comments explaining each step.
# The final plot provides a clear representation of the uniform distribution and the specified probability range.
