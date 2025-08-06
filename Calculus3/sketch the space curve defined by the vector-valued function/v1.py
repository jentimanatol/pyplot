import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

t = np.linspace(0, 1, 100)
x = -t
y = 4*t
z = 6*t

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot(x, y, z, label='r(t) = -t i + 4t j + 6t k')
ax.scatter([0], [0], [0], color='green', label='Start (0,0,0)')
ax.scatter([-1], [4], [6], color='red', label='End (-1,4,6)')
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')
ax.legend()
plt.title("Space Curve: r(t) = -t i + 4t j + 6t k")
plt.show()
