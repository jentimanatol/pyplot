import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Define the parameter t
t = np.linspace(-5, 5, 100)

# Define the components of the vector function r(t)
x = t + 1
y = 3*t - 1
z = 2*t

# Create a 3D plot
fig = plt.figure(figsize=(10, 7))
ax = fig.add_subplot(111, projection='3d')

# Plot the vector-valued function
ax.plot(x, y, z, label=r'$\vec{r}(t) = (t+1)\hat{i} + (3t - 1)\hat{j} + 2t\hat{k}$', color='blue')
ax.quiver(x[::10], y[::10], z[::10], 1, 3, 2, length=0.5, color='red', normalize=True)

# Enhance axis visibility
ax.set_xlabel('x-axis', labelpad=15)
ax.set_ylabel('y-axis', labelpad=15)
ax.set_zlabel('z-axis', labelpad=15)
ax.set_title('3D Plot of the Vector-Valued Function with Orientation')
ax.legend()
ax.grid(True)

# Add coordinate axes for clarity
ax.plot([min(x), max(x)], [0, 0], [0, 0], color='black', linestyle='--')  # x-axis
ax.plot([0, 0], [min(y), max(y)], [0, 0], color='black', linestyle='--')  # y-axis
ax.plot([0, 0], [0, 0], [min(z), max(z)], color='black', linestyle='--')  # z-axis

plt.show()
