import numpy as np
import matplotlib.pyplot as plt

# Define the vector functions r'(t) and r''(t)
def r_prime(t):
    return np.array([5, np.cos(t), -np.sin(t)])

def r_double_prime(t):
    return np.array([0, -np.sin(t), -np.cos(t)])

# Compute the cross product r'(t) x r''(t)
def cross_product(t):
    r1 = r_prime(t)
    r2 = r_double_prime(t)
    cross_prod = np.cross(r1, r2)
    return cross_prod

# Generate t values
t_values = np.linspace(0, 2*np.pi, 100)
cross_prod_values = np.array([cross_product(t) for t in t_values])

# Plot the components of the cross product
fig = plt.figure(figsize=(12, 6))

ax1 = fig.add_subplot(131)
ax1.plot(t_values, cross_prod_values[:, 0], label='x-component')
ax1.set_title('x-component of Cross Product')
ax1.set_xlabel('t')
ax1.set_ylabel('Value')
ax1.grid(True)
ax1.legend()

ax2 = fig.add_subplot(132)
ax2.plot(t_values, cross_prod_values[:, 1], label='y-component', color='orange')
ax2.set_title('y-component of Cross Product')
ax2.set_xlabel('t')
ax2.set_ylabel('Value')
ax2.grid(True)
ax2.legend()

ax3 = fig.add_subplot(133)
ax3.plot(t_values, cross_prod_values[:, 2], label='z-component', color='green')
ax3.set_title('z-component of Cross Product')
ax3.set_xlabel('t')
ax3.set_ylabel('Value')
ax3.grid(True)
ax3.legend()

plt.tight_layout()
plt.show()
