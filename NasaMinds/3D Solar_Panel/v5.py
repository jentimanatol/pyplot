import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection

# Create figure
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Mars robot base: Rectangle
base_vertices = [
    [-0.5, -0.5, 0],  # Bottom-left
    [-0.5, 0.5, 0],   # Top-left
    [0.5, 0.5, 0],    # Top-right
    [0.5, -0.5, 0]    # Bottom-right
]
base_faces = [base_vertices]
base = Poly3DCollection(base_faces, facecolor="brown", alpha=0.8)
ax.add_collection3d(base)

# Foldable solar panel segments
panel_segments = [
    [[0.5, -0.1, 0], [1, -0.3, 0.1], [1, 0.1, 0.1], [0.5, 0.1, 0]],  # Segment 1
    [[1, -0.3, 0.1], [1.5, -0.5, 0.2], [1.5, 0, 0.2], [1, -0.1, 0.1]]  # Segment 2
]

for segment in panel_segments:
    panel = Poly3DCollection([segment], edgecolor='black', facecolor="blue", alpha=0.8)
    ax.add_collection3d(panel)

# Add hinge points for realism
hinges = [[0.5, 0, 0], [1, -0.1, 0.1]]
for hinge in hinges:
    ax.scatter(hinge[0], hinge[1], hinge[2], color='red', s=40, label="Hinge")

# Set limits for a better view
ax.set_xlim([-1, 2])
ax.set_ylim([-1, 1])
ax.set_zlim([0, 0.5])

# Set labels
ax.set_xlabel('X-axis')
ax.set_ylabel('Y-axis')
ax.set_zlabel('Z-axis')

# Title
ax.set_title('Foldable Solar Panel for Mars Robot')

# Show plot
plt.show()