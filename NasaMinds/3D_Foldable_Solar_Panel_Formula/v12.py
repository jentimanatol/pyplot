import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
import numpy as np

# Parameters for the foldable panel
N = 8  # Number of sides in the central polygon
A = 1.0  # Center-to-vertex radius
phi = np.radians(30)  # Angle between cone and flat plane in radians
beta = 2 * np.pi / N  # Angular separation between segments
z_amplitude_parallel = 0.05  # Amplitude for parallel folds
z_amplitude_perpendicular = 0.1  # Amplitude for perpendicular folds

# Rotation matrix R for rotational symmetry
def rotation_matrix(beta):
    return np.array([
        [np.cos(beta), -np.sin(beta), 0],
        [np.sin(beta), np.cos(beta), 0],
        [0, 0, 1]
    ])

R = rotation_matrix(beta)

# Initialize all trapezoids
all_trapezoids = []

# Generate the trapezoids for the foldable panel
for segment in range(N):  # Loop through each segment
    rotation = np.linalg.matrix_power(R, segment)  # Rotate each segment
    segment_trapezoids = []
    last_top_vertices = None  # Track top vertices for continuity
    
    for i in range(1, 5):  # Loop through layers/rings (inner to outer)
        # Define the inner and outer radius for this trapezoid
        inner_radius = (i - 1) * (A / 4)
        outer_radius = i * (A / 4)
        
        # Define vertices dynamically to ensure parallel and perpendicular folding
        if last_top_vertices is None:
            # First trapezoid in the layer
            inner_left = [inner_radius * np.cos(segment * beta),
                          inner_radius * np.sin(segment * beta),
                          0]  # Z=0 for the base
            outer_left = [outer_radius * np.cos(segment * beta),
                          outer_radius * np.sin(segment * beta),
                          z_amplitude_parallel]  # Parallel fold upwards
            inner_right = [inner_radius * np.cos((segment + 1) * beta),
                           inner_radius * np.sin((segment + 1) * beta),
                           0]  # Z=0 for the base
            outer_right = [outer_radius * np.cos((segment + 1) * beta),
                           outer_radius * np.sin((segment + 1) * beta),
                           -z_amplitude_perpendicular]  # Perpendicular fold downwards
        else:
            # Use previous trapezoid's top vertices as the base
            inner_left, inner_right = last_top_vertices
            outer_left = [outer_radius * np.cos(segment * beta),
                          outer_radius * np.sin(segment * beta),
                          inner_left[2] + z_amplitude_parallel]  # Parallel fold upwards
            outer_right = [outer_radius * np.cos((segment + 1) * beta),
                           outer_radius * np.sin((segment + 1) * beta),
                           inner_right[2] - z_amplitude_perpendicular]  # Perpendicular fold downwards
        
        # Update last_top_vertices for the next trapezoid
        last_top_vertices = ([outer_left, outer_right])
        
        # Store the trapezoid's vertices
        segment_trapezoids.append([inner_left, outer_left, outer_right, inner_right])
    
    all_trapezoids.append(segment_trapezoids)

# Visualization
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Draw all trapezoids
for segment in all_trapezoids:
    for trapezoid in segment:
        poly = Poly3DCollection([trapezoid], facecolor="blue", edgecolor="black", alpha=0.8)
        ax.add_collection3d(poly)

# Set plot limits
ax.set_xlim([-1.5, 1.5])
ax.set_ylim([-1.5, 1.5])
ax.set_zlim([-0.5, 0.5])

# Set labels
ax.set_xlabel("X-axis")
ax.set_ylabel("Y-axis")
ax.set_zlabel("Z-axis")

# Title
ax.set_title("Foldable Panel with Parallel and Perpendicular Folds")

# Show the plot
plt.show()