import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Coordinates
points = {
    "A (3, 5, 4)": (3, 5, 4),
    "B (-7, 4, 3)": (-7, 4, 3)
}

# Plotting
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Plot each point
for label, (x, y, z) in points.items():
    ax.scatter(x, y, z, s=50)
    ax.text(x, y, z, f' {label}', fontsize=10)

# Set labels
ax.set_xlabel('X axis')
ax.set_ylabel('Y axis')
ax.set_zlabel('Z axis')

# Set limits for better visualization
ax.set_xlim(-10, 10)
ax.set_ylim(0, 10)
ax.set_zlim(0, 10)

plt.title("3D Plot of Points A and B")
plt.show()

