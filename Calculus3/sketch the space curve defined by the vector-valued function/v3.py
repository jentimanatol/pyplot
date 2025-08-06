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

# Annotate axis lines with names and numbers
ax.text(1.2, 0, 0, 'x', color='black')
ax.text(0, 5.5, 0, 'y', color='black')
ax.text(0, 0, 6.8, 'z', color='black')

# Add numerical labels on axes near the ends
ax.text(-1, 0.2, 0.2, '-1', color='black')
ax.text(0.5, 0.2, 0.2, '0.5', color='black')
ax.text(0, 4, 0.2, '4', color='black')
ax.text(0, 0.2, 6, '6', color='black')

# Remove grid and axis ticks
ax.grid(False)
ax.set_xticks([])
ax.set_yticks([])
ax.set_zticks([])

# Set limits
ax.set_xlim([-1.5, 1])
ax.set_ylim([-1, 5])
ax.set_zlim([-1, 7])

# Title and legend
ax.set_title("Space Curve: r(t) = -t i + 4t j + 6t k")
ax.legend()

plt.show()
