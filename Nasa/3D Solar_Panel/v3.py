import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Line3DCollection

# Create figure
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Rover base: Rectangle
base_vertices = [
    [-0.5, -0.5, 0],  # Bottom-left
    [-0.5, 0.5, 0],   # Top-left
    [0.5, 0.5, 0],    # Top-right
    [0.5, -0.5, 0]    # Bottom-right
]
base_faces = [base_vertices]
base = Line3DCollection(base_faces, colors='brown', linewidths=5)
ax.add_collection3d(base)

# Foldable antenna segments
antenna_segments = [
    [[0, 0, 0], [0, 0, 0.5]],  # Segment 1 (fixed base)
    [[0, 0, 0.5], [0.2, 0, 1]],  # Segment 2 (foldable part 1)
    [[0.2, 0, 1], [0.4, 0, 1.5]]  # Segment 3 (foldable part 2)
]

for segment in antenna_segments:
    x_line, y_line, z_line = zip(*segment)
    ax.plot(x_line, y_line, z_line, color='black', linewidth=2)

# Set limits for a better view
ax.set_xlim([-1, 1])
ax.set_ylim([-1, 1])
ax.set_zlim([0, 2])

# Set labels
ax.set_xlabel('X-axis')
ax.set_ylabel('Y-axis')
ax.set_zlabel('Z-axis')

# Title
ax.set_title('Foldable Antenna for Mars Rover')

# Show plot
plt.show()