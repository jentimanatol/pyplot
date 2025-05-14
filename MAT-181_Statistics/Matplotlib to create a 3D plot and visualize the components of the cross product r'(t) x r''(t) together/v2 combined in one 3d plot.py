

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Define the vector functions r'(t) and r''(t)
def r_prime(t):
    return np.array([5, np.cos(t), -np.sin(t)])

def r_double_prime(t):
    return np.array([0, -np.sin(t), -np.cos(t)])

# Compute the cross product r'(t) x r''(t)
def cross_product(t):
    r1 = r_prime(t)
    r2 = r_double_prime(t)
    cross_prod = np.cross(r1, r2)
    return cross_prod

# Generate t values
t_values = np.linspace(0, 2*np.pi, 100)
cross_prod_values = np.array([cross_product(t) for t in t_values])

# Create a 3D plot
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')

# Plot the components of the cross product
ax.plot(t_values, cross_prod_values[:, 0], cross_prod_values[:, 1], label='Cross Product (x, y, z)')
ax.set_title('Cross Product Components in 3D')
ax.set_xlabel('t')
ax.set_ylabel('x-component')
ax.set_zlabel('y-component')

# Add a legend
ax.legend()

# Show the plot
plt.show()
