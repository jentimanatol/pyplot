import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Define the function f(x, y)
def f(x, y):
    return 3 * x * (y - 9) + np.exp(x) + np.exp(y)

# Define the gradient of f
def grad_f(x, y):
    df_dx = 3 * (y - 9) + np.exp(x)
    df_dy = 3 * x + np.exp(y)
    return np.array([df_dx, df_dy])

# Direction vector from point A to B
A = np.array([0, -8])
B = np.array([-1, -4])
v = B - A
v_unit = v / np.linalg.norm(v)

# Evaluate gradient at (0, 0)
x0, y0 = 0, 0
z0 = f(x0, y0)
grad = grad_f(x0, y0)

# Directional derivative
directional_derivative = np.dot(grad, v_unit)
arrow = directional_derivative * v_unit  # Scale unit vector by directional derivative magnitude

# Surface grid
x = np.linspace(-2, 2, 100)
y = np.linspace(-10, 2, 100)
X, Y = np.meshgrid(x, y)
Z = f(X, Y)

# Plotting
fig = plt.figure(figsize=(12, 8))
ax = fig.add_subplot(111, projection='3d')

# Surface plot
ax.plot_surface(X, Y, Z, cmap='plasma', alpha=0.6, edgecolor='none')

# Directional arrow
ax.quiver(x0, y0, z0, arrow[0], arrow[1], 0, color='red', linewidth=2,
          label=rf"$D_{{\vec{{u}}}}f(0,0) = \frac{{30}}{{\sqrt{{17}}}} \approx {directional_derivative:.2f}$")

# Mark the point (0, 0)
ax.scatter(x0, y0, z0, color='black', s=60, label="Point (0, 0)")

# Annotation of gradient vector
ax.quiver(x0, y0, z0, grad[0], grad[1], 0, color='green', linestyle='dashed', linewidth=2,
          label=rf"$\nabla f(0, 0) = ({grad[0]}, {grad[1]})$")

# Labels and legend
ax.set_title("Directional Derivative Visualization with Gradient and Unit Direction Vector", fontsize=14)
ax.set_xlabel("x")
ax.set_ylabel("y")
ax.set_zlabel("f(x, y)")
ax.view_init(elev=30, azim=135)
ax.legend()

plt.tight_layout()
plt.show()
