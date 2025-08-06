import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

# Parameter t
t = np.linspace(0, 1, 100)
x = -t
y = 4 * t
z = 6 * t

# Create 3D plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Plot the space curve
ax.plot(x, y, z, label='r(t) = -t i + 4t j + 6t k', color='blue')

# Highlight start and end points
ax.scatter([0], [0], [0], color='green', label='Start (0,0,0)', s=50)
ax.scatter([-1], [4], [6], color='red', label='End (-1,4,6)', s=50)

# Add coordinate axes (lines)
axis_length = 7
ax.plot([-axis_length, axis_length], [0, 0], [0, 0], 'k')  # x-axis
ax.plot([0, 0], [-axis_length, axis_length], [0, 0], 'k')  # y-axis
ax.plot([0, 0], [0, 0], [-axis_length, axis_length], 'k')  # z-axis

# Set axis labels
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')

# Add ticks and remove grid
ax.grid(False)
ax.set_xticks(np.arange(-1, 1.1, 0.5))
ax.set_yticks(np.arange(0, 5, 1))
ax.set_zticks(np.arange(0, 7, 1))

# Set limits
ax.set_xlim([-1.5, 1])
ax.set_ylim([-1, 5])
ax.set_zlim([-1, 7])

# Title and legend
ax.set_title("Space Curve: r(t) = -t i + 4t j + 6t k")
ax.legend()

plt.show()
