import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Parameter t values
t = np.linspace(-10, 10, 100)

# Define r(t) components
x = t + 1
y = 3 * t - 1
z = 2 * t

# Create 3D plot
fig = plt.figure(figsize=(10, 7))
ax = fig.add_subplot(111, projection='3d')

# Plot the vector-valued curve
ax.plot(x, y, z, color='blue', label=r'$\vec{r}(t)$')

# Draw axes lines
ax.plot([-15, 15], [0, 0], [0, 0], color='black')  # x-axis
ax.plot([0, 0], [-30, 30], [0, 0], color='black')  # y-axis
ax.plot([0, 0], [0, 0], [-20, 20], color='black')  # z-axis

# Set limits
ax.set_xlim([-15, 15])
ax.set_ylim([-30, 30])
ax.set_zlim([-20, 20])

# Label axes
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')

# Add grid and legend
ax.grid(True)
ax.legend()
ax.set_title('3D Plot of Vector-Valued Function r(t)')

# Show plot
plt.show()
