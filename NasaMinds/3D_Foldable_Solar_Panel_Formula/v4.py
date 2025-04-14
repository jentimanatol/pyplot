'''folding mechanism where the first segment folds up (+Z), the next folds down (-Z), and so on. Additionally, with each subsequent ring of trapezoids, the Z positions increase or decrease progressively, creating a gradual rise or fall.'''
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
import numpy as np
from scipy.optimize import root

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

# Function to solve for the heights (mz_i+1 and vz_i+1)
def g_heights(heights, A, d, phi, i, fold_direction, z_offset):
    mz_next, vz_next = heights
    
    # Apply folding direction (+Z or -Z) and layer offset
    mz_next = mz_next * fold_direction + z_offset
    vz_next = vz_next * fold_direction + z_offset
    
    # Stowed positions
    m_prime_next = np.array([A + 2 * d * i - d, 0, mz_next])
    v_prime_next = np.array([A + 2 * d * i, 0, vz_next])
    
    # Deployed positions constrained to the cone
    m_next = np.array([A + 2 * d * i - d, 0, (A + 2 * d * i - d) * np.tan(phi)])
    v_next = np.array([A + 2 * d * i, 0, (A + 2 * d * i) * np.tan(phi)])
    
    # Residuals for constraints
    l5_stowed = np.linalg.norm(v_prime_next - m_prime_next)
    l5_deployed = np.linalg.norm(v_next - m_next)
    residual_5 = l5_stowed - l5_deployed
    
    l6_stowed = np.linalg.norm(m_prime_next - m_prime_next @ R)
    l6_deployed = np.linalg.norm(m_next - m_next @ R)
    residual_6 = l6_stowed - l6_deployed
    
    return [residual_5, residual_6]

# Initialize full panel
all_trapezoids = []

# Generate each segment and solve for all trapezoids
z_layer_offset = 0.0  # Starting Z offset for the first layer
z_increment = 0.1  # Increment for Z-layer with each outer ring

for segment in range(N):  # For each segment of the polygon
    rotation = np.linalg.matrix_power(R, segment)  # Rotate the segment using R
    fold_direction = 1 if segment % 2 == 0 else -1  # Alternate folding direction
    segment_trapezoids = []
    
    for i in range(2, 6):  # Assume we solve for vertices from 2 to n-1
        # Initial guess for heights mz_i+1 and vz_i+1
        initial_guess = [0.1, 0.1]
        result = root(g_heights, initial_guess, args=(A, d, phi, i, fold_direction, z_layer_offset))
        
        if result.success:
            mz_next, vz_next = result.x
            
            # Compute positions
            m_next = np.array([A + 2 * d * i - d, 0, (mz_next * fold_direction + z_layer_offset)])
            v_next = np.array([A + 2 * d * i, 0, (vz_next * fold_direction + z_layer_offset)])
            
            # Rotate to current segment
            m_rotated = rotation @ m_next
            v_rotated = rotation @ v_next
            
            # Store trapezoid vertices
            segment_trapezoids.append((m_rotated, v_rotated))
        else:
            print(f"Failed to solve for i={i} in segment {segment}")
    
    all_trapezoids.append(segment_trapezoids)
    z_layer_offset += z_increment  # Increment Z offset for the next ring

# Visualization
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

for segment in all_trapezoids:
    for m, v in segment:
        # Create the trapezoid
        trapezoid = Poly3DCollection([[m, v, v @ R, m @ R]], facecolor="blue", edgecolor="black", alpha=0.8)
        ax.add_collection3d(trapezoid)

# Set limits for better visualization
ax.set_xlim([-2, 2])
ax.set_ylim([-2, 2])
ax.set_zlim([-1, 2])

# Set labels
ax.set_xlabel("X-axis")
ax.set_ylabel("Y-axis")
ax.set_zlabel("Z-axis")

# Title
ax.set_title("Foldable Panel with Alternating Folding Directions and Layered Z")

# Display the plot
plt.show()