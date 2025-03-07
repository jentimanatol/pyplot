import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Define the parameter t
t = np.linspace(0, 2 * np.pi, 100)

# Define the vectors r'(t) and r''(t)
r_prime = np.array([-np.ones_like(t), 5 * np.cos(t), -5 * np.sin(t)])
r_double_prime = np.array([np.zeros_like(t), -5 * np.sin(t), -5 * np.cos(t)])

# Calculate the cross product r'(t) x r''(t)
cross_product = np.cross(r_prime.T, r_double_prime.T)

# Create a 3D plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Plot the cross product vectors with adjusted size
ax.quiver(np.zeros_like(t), np.zeros_like(t), np.zeros_like(t),
          cross_product[:, 0], cross_product[:, 1], cross_product[:, 2],
          length=0.1, normalize=True, color='b')

# Set the limits for the grid
ax.set_xlim([-1, 1])
ax.set_ylim([-5, 5])
ax.set_zlim([-5, 5])

ax.set_title("3D Cross Product Vectors")
ax.set_xlabel("X")
ax.set_ylabel("Y")
ax.set_zlabel("Z")

# Show the plot
plt.show()
