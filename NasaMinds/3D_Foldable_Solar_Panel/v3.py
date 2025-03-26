import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
import numpy as np

# Create figure
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Parameters for the octagonal solar panel
radius = 1.0  # Radius of the panel
num_segments = 8  # Number of lips (segments)
angles = np.linspace(0, 2 * np.pi, num_segments + 1)  # Divide the circle into segments
num_trapezoids = 5  # Number of trapezoids per lip
rotation_angle = np.radians(10)  # Rotation angle around the Z-axis (10 degrees)
bend_angle = np.radians(5)  # Bend angle for folding each trapezoid

# Generate each segment with rotated and bent trapezoidal panels
for i in range(num_segments):
    # Rotation direction: alternate between +10° and -10°
    rotation = rotation_angle if i % 2 == 0 else -rotation_angle

    # Define the base angles for the segment
    angle_start = angles[i]
    angle_end = angles[i + 1]

    # Create trapezoids along the lip
    for j in range(num_trapezoids):
        inner_radius = j * (radius / num_trapezoids)  # Inner radius of the trapezoid
        outer_radius = (j + 1) * (radius / num_trapezoids)  # Outer radius of the trapezoid

        # Z-offset for the bending
        inner_z = j * np.tan(bend_angle)
        outer_z = (j + 1) * np.tan(bend_angle)

        # Vertices of the trapezoid before rotation
        vertices = [
            [inner_radius * np.cos(angle_start), inner_radius * np.sin(angle_start), inner_z],  # Bottom-left
            [outer_radius * np.cos(angle_start), outer_radius * np.sin(angle_start), outer_z],  # Top-left
            [outer_radius * np.cos(angle_end), outer_radius * np.sin(angle_end), outer_z],  # Top-right
            [inner_radius * np.cos(angle_end), inner_radius * np.sin(angle_end), inner_z],  # Bottom-right
        ]

        # Apply rotation around the Z-axis
        rotated_vertices = []
        for vertex in vertices:
            x, y, z = vertex
            x_rot = x * np.cos(rotation) - y * np.sin(rotation)
            y_rot = x * np.sin(rotation) + y * np.cos(rotation)
            rotated_vertices.append([x_rot, y_rot, z])

        # Add the filled trapezoid
        trapezoid = Poly3DCollection([rotated_vertices], facecolor="blue", edgecolor="black", alpha=0.8)
        ax.add_collection3d(trapezoid)

# Set limits for better visualization
ax.set_xlim([-1.5, 1.5])
ax.set_ylim([-1.5, 1.5])
ax.set_zlim([-1, 1])

# Set labels
ax.set_xlabel("X-axis")
ax.set_ylabel("Y-axis")
ax.set_zlabel("Z-axis")

# Title
ax.set_title("Continuous Solar Panel with Alternating Z-Axis Rotations")

# Display the plot
plt.show()