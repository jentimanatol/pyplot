import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Grid setup
x = np.linspace(-4, 4, 400)
y = np.linspace(-2, 2, 400)
X, Y = np.meshgrid(x, y)

# Define expression inside square root
expr = 36 - 9*X**2 + 144*Y**2

# Domain mask: valid only where (x^2 / 4 - y^2 / 0.25 <= 1)
domain_mask = (X**2 / 4 - Y**2 / 0.25) <= 1

# Apply mask to remove values outside domain
Z = np.sqrt(expr)
Z[~domain_mask] = np.nan  # Set outside-domain values to NaN for clean plot

# 3D Plotting
fig = plt.figure(figsize=(10, 7))
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(X, Y, Z, cmap='viridis', edgecolor='k', alpha=0.9)

# Labels and titles
ax.set_title(r"$f(x, y) = \sqrt{36 - 9x^2 + 144y^2}$", fontsize=14)
ax.set_xlabel("x")
ax.set_ylabel("y")
ax.set_zlabel("f(x, y)")
ax.view_init(elev=30, azim=135)

plt.tight_layout()
plt.show()
