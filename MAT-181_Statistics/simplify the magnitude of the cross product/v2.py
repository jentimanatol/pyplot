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

# Calculate the magnitude of the cross product
magnitude = np.linalg.norm(cross_product, axis=1)

# Create a figure with a grid layout
fig = plt.figure(figsize=(14, 6))

# Add a 3D subplot
ax1 = fig.add_subplot(121, projection='3d')
ax1.quiver(np.zeros_like(t), np.zeros_like(t), np.zeros_like(t),
           cross_product[:, 0], cross_product[:, 1], cross_product[:, 2],
           length=0.1, normalize=True, color='b')
ax1.set_title("3D Cross Product Vectors")

# Add a 2D subplot
ax2 = fig.add_subplot(122)
ax2.plot(t, magnitude, 'r')
ax2.set_title("Magnitude of the Cross Product")
ax2.set_xlabel("t")
ax2.set_ylabel("Magnitude")

# Show the combined plot
plt.tight_layout()
plt.show()
