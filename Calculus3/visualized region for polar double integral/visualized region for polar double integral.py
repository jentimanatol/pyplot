# Fixing the math text in the plot title to avoid rendering issues with unsupported symbols

# Re-import necessary modules after kernel reset
import numpy as np
import matplotlib.pyplot as plt

# Polar limits
r_min, r_max = 0, 2
theta_min, theta_max = 0, np.pi / 6

# Create polar grid
r = np.linspace(r_min, r_max, 300)
theta = np.linspace(theta_min, theta_max, 300)
r, theta = np.meshgrid(r, theta)

# Convert to Cartesian coordinates for plotting
x = r * np.cos(theta)
y = r * np.sin(theta)




plt.figure(figsize=(6, 6))
plt.plot([0, 2*np.cos(theta_max)], [0, 2*np.sin(theta_max)], 'k--', lw=1)
plt.plot([0, 2*np.cos(theta_min)], [0, 2*np.sin(theta_min)], 'k--', lw=1)
plt.contourf(x, y, np.ones_like(r), alpha=0.5, cmap='Blues')

# Highlight circular arc
theta_arc = np.linspace(theta_min, theta_max, 300)
x_arc = r_max * np.cos(theta_arc)
y_arc = r_max * np.sin(theta_arc)
plt.plot(x_arc, y_arc, 'r', lw=2)

# Axes settings
plt.xlabel('x')
plt.ylabel('y')
plt.title('Region in Polar Coordinates: 0 <= r <= 2, 0 <= θ <= π/6')
plt.axis('equal')
plt.grid(True)

plt.show()
