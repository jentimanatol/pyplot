import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection

# Create figure
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Define vertices of the pyramid
vertices = [
    [0, 0, 0],  # Base corner 1
    [1, 0, 0],  # Base corner 2
    [1, 1, 0],  # Base corner 3
    [0, 1, 0],  # Base corner 4
    [0.5, 0.5, 1]  # Top vertex
]

# Define faces of the pyramid (each face is a list of vertices)
faces = [
    [vertices[0], vertices[1], vertices[4]],  # Side 1
    [vertices[1], vertices[2], vertices[4]],  # Side 2
    [vertices[2], vertices[3], vertices[4]],  # Side 3
    [vertices[3], vertices[0], vertices[4]],  # Side 4
    [vertices[0], vertices[1], vertices[2], vertices[3]]  # Base
]

# Create 3D polygon collection
pyramid = Poly3DCollection(faces, edgecolor='k', alpha=0.5)
pyramid.set_facecolor([(0.5, 0.7, 0.9, 0.9)])  # Add a light blue color

# Add the pyramid to the plot
ax.add_collection3d(pyramid)

# Set limits for better view
ax.set_xlim([0, 1])
ax.set_ylim([0, 1])
ax.set_zlim([0, 1])

# Set labels
ax.set_xlabel('X-axis')
ax.set_ylabel('Y-axis')
ax.set_zlabel('Z-axis')

# Show the plot
plt.show()