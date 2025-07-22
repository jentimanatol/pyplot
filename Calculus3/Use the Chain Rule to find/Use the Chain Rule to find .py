import numpy as np
import matplotlib.pyplot as plt

# Create a grid of s and t values (avoid s = 0 to prevent division by zero)
s = np.linspace(-3, 3, 400)
t = np.linspace(-3, 3, 400)
S, T = np.meshgrid(s, t)

# Avoid division by zero for S
epsilon = 1e-6
S = np.where(np.abs(S) < epsilon, epsilon, S)

# Partial derivatives
dw_ds = 3 * T * (1 - (3 * T**2) / (S**2))
dw_dt = 3 * (S**2 + 9 * T**2) / S

# Plot setup
fig = plt.figure(figsize=(14, 6))

# ∂w/∂s plot
ax1 = fig.add_subplot(121, projection='3d')
surf1 = ax1.plot_surface(S, T, dw_ds, cmap='coolwarm', edgecolor='none')
ax1.set_title(r'$\frac{\partial w}{\partial s} = 3t(1 - \frac{3t^2}{s^2})$')
ax1.set_xlabel('s')
ax1.set_ylabel('t')
ax1.set_zlabel(r'$\frac{\partial w}{\partial s}$')
fig.colorbar(surf1, ax=ax1, shrink=0.5, aspect=10)

# ∂w/∂t plot
ax2 = fig.add_subplot(122, projection='3d')
surf2 = ax2.plot_surface(S, T, dw_dt, cmap='viridis', edgecolor='none')
ax2.set_title(r'$\frac{\partial w}{\partial t} = \frac{3(s^2 + 9t^2)}{s}$')
ax2.set_xlabel('s')
ax2.set_ylabel('t')
ax2.set_zlabel(r'$\frac{\partial w}{\partial t}$')
fig.colorbar(surf2, ax=ax2, shrink=0.5, aspect=10)

plt.tight_layout()
plt.show()
