
import numpy as np
import matplotlib.pyplot as plt

from mpl_toolkits.mplot3d import Axes3D

# Create a grid of x and y values
x = np.linspace(-2, 2, 400)
y = np.linspace(-10, 10, 400)
X, Y = np.meshgrid(x, y)

# Denominator
denominator = Y - X**3

# Avoid division by zero (discontinuity along y = x^3)
with np.errstate(divide='ignore', invalid='ignore'):
    Z = 8 / denominator
    Z[np.abs(denominator) < 1e-2] = np.nan  # Mask near-discontinuity

# Plotting
fig = plt.figure(figsize=(10, 7))
ax = fig.add_subplot(111, projection='3d')

# Surface plot with discontinuity masked
surf = ax.plot_surface(X, Y, Z, cmap='coolwarm', edgecolor='none', alpha=0.9)

# Highlight the curve y = x^3 where the function is undefined
x_curve = np.linspace(-2, 2, 400)
y_curve = x_curve**3
z_curve = np.full_like(x_curve, 0)
ax.plot(x_curve, y_curve, z_curve, 'k--', linewidth=2, label="Discontinuity: $y = x^3$")

# Labels
ax.set_title(r"$f(x, y) = \frac{8}{y - x^3}$", fontsize=14)
ax.set_xlabel("x")
ax.set_ylabel("y")
ax.set_zlabel("f(x, y)")
ax.view_init(elev=30, azim=135)
ax.legend()

plt.tight_layout()
plt.show()
