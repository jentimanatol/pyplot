import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
import numpy as np

# Function to calculate area of a triangle given its vertices
def calculate_triangle_area(v1, v2, v3):
    # Convert vertices to numpy arrays
    v1, v2, v3 = np.array(v1), np.array(v2), np.array(v3)
    # Use the cross product to calculate area
    return 0.5 * np.linalg.norm(np.cross(v2 - v1, v3 - v1))

# Create figure
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Parameters for the octagonal solar panel
radius = 1.0  # Radius of the octagonal panel
num_segments = 8  # Number of segments (lips)
angles = np.linspace(0, 2 * np.pi, num_segments + 1)  # Divide the circle into segments
concave_depth = 0.2  # Depth of concavity (how much it curves inward)

# Generate each segment with concave shape
for i in range(num_segments):
    # Define the vertices of the curved segment
    vertices = [
        [0, 0, 0],  # Center of the solar panel
        [radius * np.cos(angles[i]), radius * np.sin(angles[i]), -concave_depth],  # Edge point 1 (curved inward)
        [radius * np.cos(angles[i + 1]), radius * np.sin(angles[i + 1]), -concave_depth],  # Edge point 2 (curved inward)
    ]
    # Add the filled curved segment
    segment = Poly3DCollection([vertices], facecolor="blue", edgecolor="black", alpha=0.8)
    ax.add_collection3d(segment)

    # Calculate and print the area of the segment
    area = calculate_triangle_area(vertices[0], vertices[1], vertices[2])
    print(f"Segment {i + 1}: Area = {area:.2f}")

# Set view limits for better visualization
ax.set_xlim([-1.5, 1.5])
ax.set_ylim([-1.5, 1.5])
ax.set_zlim([-1, 0.5])

# Set labels
ax.set_xlabel("X-axis")
ax.set_ylabel("Y-axis")
ax.set_zlabel("Z-axis")

# Title
ax.set_title("Concave Octagonal Foldable Solar Panel for Mars Walker")

# Display the plot
plt.show()