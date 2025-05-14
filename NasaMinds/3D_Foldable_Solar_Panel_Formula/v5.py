import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
import numpy as np

# Parameters for the foldable panel
N = 8  # Number of sides in the central polygon
A = 1.0  # Center-to-vertex radius
h = 0.1  # Separation between layers in stowed form
phi = np.radians(30)  # Angle between cone and flat plane in radians
beta = 2 * np.pi / N  # Angular separation between segments
d = h / np.cos(beta)  # Radial separation in stowed form

# Rotation matrix R for rotational symmetry
def rotation_matrix(beta):
    return np.array([
        [np.cos(beta), -np.sin(beta), 0],
        [np.sin(beta), np.cos(beta), 0],
        [0, 0, 1]
    ])

R = rotation_matrix(beta)

# Initialize the Z-layer and trapezoid progression
z_layer = 0  # Start at Z=0
z_increment = 0.1  # Increment for each layer (progressive height for rings)

# Generate the full foldable panel
all_trapezoids = []

for segment in range(N):  # Loop through each segment of the polygon
    rotation = np.linalg.matrix_power(R, segment)  # Rotate the segment using R
    fold_direction = 1 if segment % 2 == 0 else -1  # Alternate fold direction
    segment_trapezoids = []
    
    # Compute positions for each trapezoid in the segment
    for i in range(1, 5):  # Assume 4 rings, from inner to outer
        # Define the inner and outer radius for this trapezoid
        inner_radius = (i - 1) * (A / 4)
        outer_radius = i * (A / 4)
        
        # Define vertices with alternating fold directions and incremental Z-layers
        inner_left = [inner_radius * np.cos(segment * beta), inner_radius * np.sin(segment * beta), z_layer]
        outer_left = [outer_radius * np.cos(segment * beta), outer_radius * np.sin(segment * beta), z_layer + fold_direction * z_increment]
        inner_right = [inner_radius * np.cos((segment + 1) * beta), inner_radius * np.sin((segment + 1) * beta), z_layer]
        outer_right = [outer_radius * np.cos((segment + 1) * beta), outer_radius * np.sin((segment + 1) * beta), z_layer + fold_direction * z_increment]
        
        # Store the trapezoid vertices
        segment_trapezoids.append([inner_left, outer_left, outer_right, inner_right])
        
        # Increment Z-layer for the next trapezoid
        z_layer += z_increment
    
    # Add the segment's trapezoids to the panel
    all_trapezoids.append(segment_trapezoids)

# Visualization
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Draw all trapezoids in the panel
for segment in all_trapezoids:
    for trapezoid in segment:
        poly = Poly3DCollection([trapezoid], facecolor="blue", edgecolor="black", alpha=0.8)
        ax.add_collection3d(poly)

# Set limits for better visualization
ax.set_xlim([-1.5, 1.5])
ax.set_ylim([-1.5, 1.5])
ax.set_zlim([-1, 2])

# Set labels
ax.set_xlabel("X-axis")
ax.set_ylabel("Y-axis")
ax.set_zlabel("Z-axis")

# Title
ax.set_title("Fully Connected Foldable Panel with Alternating Folds")

# Display the plot
plt.show()