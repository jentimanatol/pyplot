import numpy as np
import matplotlib.pyplot as plt

# Define theta range from -π/2 to π/2
theta = np.linspace(-np.pi/2, np.pi/2, 500)

# Corresponding r values for the outer boundary
r = 9 * np.cos(theta)

# Convert to Cartesian coordinates for plotting
x = r * np.cos(theta)
y = r * np.sin(theta)

# Set up the plot
fig, ax = plt.subplots(subplot_kw={'aspect': 'equal'})

# Fill the region
ax.fill(x, y, color='lightblue', edgecolor='black', linewidth=1.5)
ax.plot(x, y, 'b', label=r'$r = 9\cos(\theta)$')

# Axes and settings
ax.set_title("Region Defined by $0 \\leq r \\leq 9\\cos(\\theta)$ and $-\\frac{\\pi}{2} \\leq \\theta \\leq \\frac{\\pi}{2}$")
ax.set_xlabel("x")
ax.set_ylabel("y")
ax.axhline(0, color='gray', linewidth=0.5)
ax.axvline(0, color='gray', linewidth=0.5)
ax.set_xlim(-1, 10)
ax.set_ylim(-10, 10)
ax.legend()
plt.grid(True)
plt.show()
