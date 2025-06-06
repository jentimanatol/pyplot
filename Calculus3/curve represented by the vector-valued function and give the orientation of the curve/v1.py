import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D

# Define the parameter t
t = np.linspace(-10, 10, 400)

# Define the vector-valued function r(t)
x = t + 1
y = 3*t - 1
z = 2*t

# Create the 3D plot
fig = plt.figure(figsize=(10, 6))
ax = fig.add_subplot(111, projection='3d')
ax.plot(x, y, z, label='r(t) = (t+1)i + (3t−1)j + 2tk', color='blue')
ax.quiver(x[::40], y[::40], z[::40], 
          np.gradient(x)[::40], np.gradient(y)[::40], np.gradient(z)[::40],
          length=1, normalize=True, color='red', label='Orientation')

# Labels and title
ax.set_title("Sketch of r(t) = (t + 1)i + (3t − 1)j + 2tk")
ax.set_xlabel("x (t+1)")
ax.set_ylabel("y (3t−1)")
ax.set_zlabel("z (2t)")
ax.legend()
plt.tight_layout()
plt.show()
