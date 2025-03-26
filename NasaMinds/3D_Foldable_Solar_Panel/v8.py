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
num_subdivisions = 5  # Number of radial subdivisions from center to periphery

# Generate each lip starting from the second trapezoid
for i in range(num_segments):
    # Define the angles for the segment
    angle_start = angles[i]
    angle_end = angles[i + 1]

    # Assign Z-values for this lip
    if i % 2 == 0:  # Even lips
        left_small_z, left_big_z = 5, 6
        right_small_z, right_big_z = -5, -6
    else:  # Odd lips (reversed Z-values)
        left_small_z, left_big_z = -5, -6
        right_small_z, right_big_z = 5, 6

    # Define the vertices of the lip as a single cohesive panel
    vertices = []
    for j in range(2, num_subdivisions + 1):  # Start at j=2 to skip the first trapezoid
        inner_radius = (j - 1) * (radius / num_subdivisions)
        outer_radius = j * (radius / num_subdivisions)

        # Inner edge vertices
        inner_left_x = inner_radius * np.cos(angle_start)
        inner_left_y = inner_radius * np.sin(angle_start)
        inner_right_x = inner_radius * np.cos(angle_end)
        inner_right_y = inner_radius * np.sin(angle_end)
        inner_left_z = left_small_z
        inner_right_z = right_small_z

        # Outer edge vertices
        outer_left_x = outer_radius * np.cos(angle_start)
        outer_left_y = outer_radius * np.sin(angle_start)
        outer_right_x = outer_radius * np.cos(angle_end)
        outer_right_y = outer_radius * np.sin(angle_end)
        outer_left_z = left_big_z
        outer_right_z = right_big_z

        # Add all four points for the current radial step
        vertices.append([
            [inner_left_x, inner_left_y, inner_left_z],
            [outer_left_x, outer_left_y, outer_left_z],
            [outer_right_x, outer_right_y, outer_right_z],
            [inner_right_x, inner_right_y, inner_right_z],
        ])

    # Create the cohesive trapezoidal panel
    for v in vertices:
        trapezoid = Poly3DCollection([v], facecolor="blue", edgecolor="black", alpha=0.8)
        ax.add_collection3d(trapezoid)

# Set limits for better visualization
ax.set_xlim([-1.5, 1.5])
ax.set_ylim([-1.5, 1.5])
ax.set_zlim([-10, 10])

# Set labels
ax.set_xlabel("X-axis")
ax.set_ylabel("Y-axis")
ax.set_zlabel("Z-axis")

# Title
ax.set_title("Solar Panel with First Trapezoid Removed from Each Lip")

# Display the plot
plt.show()