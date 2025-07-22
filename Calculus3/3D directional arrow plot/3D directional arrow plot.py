import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Define the function f(x, y)
def f(x, y):
    return (1/4)*x**2*y + x + y + y**2

# Define the gradient of f
def grad_f(x, y):
    df_dx = 0.5 * x * y + 1
    df_dy = 0.25 * x**2 + 1 + 2 * y
    return np.array([df_dx, df_dy])

# Direction vector (unit)
u = np.array([np.sqrt(2)/2, np.sqrt(2)/2])

# Grid for surface
x = np.linspace(-4, 4, 30)
y = np.linspace(-4, 4, 30)
X, Y = np.meshgrid(x, y)
Z = f(X, Y)

# Pick a point to compute the directional derivative
x0, y0 = 1, 1
z0 = f(x0, y0)
grad = grad_f(x0, y0)

# Compute the directional derivative
D_uf = np.dot(grad, u)
arrow = D_uf * u  # directional vector scaled by the derivative

# Start a 3D plot
fig = plt.figure(figsize=(10, 7))
ax = fig.add_subplot(111, projection='3d')

# Plot surface
ax.plot_surface(X, Y, Z, cmap='viridis', alpha=0.6, edgecolor='none')

# Plot the point and gradient direction
ax.quiver(x0, y0, z0, arrow[0], arrow[1], 0, color='r', linewidth=2, label='Directional Derivative')
ax.scatter(x0, y0, z0, color='black', s=50, label=f'Point ({x0}, {y0})')

# Labels and titles
ax.set_title('Directional Derivative of $f(x, y)$ at (1, 1) in direction $\\vec{u}$')
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('f(x, y)')
ax.legend()

plt.tight_layout()
plt.show()
