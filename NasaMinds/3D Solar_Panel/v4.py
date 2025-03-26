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
    [[0.5, 0, 0], [1, -0.2, 0.1], [1, 0.2, 0.1], [0.5, 0, 0]],  # Folded segment 1
    [[1, -0.2, 0.1], [1.5, -0.4, 0.2], [1.5, 0, 0.2], [1, -0.2, 0.1]],  # Folded segment 2
]

for segment in panel_segments:
    panel = Poly3DCollection([segment], edgecolor='black', facecolor="blue", alpha=0.8)
    ax.add_collection3d(panel)

# Add folding hinges for style (visualization purpose)
hinges = [[0.5, 0, 0], [1, -0.01-edge convention'] visual way.

Like specific enhancements structure