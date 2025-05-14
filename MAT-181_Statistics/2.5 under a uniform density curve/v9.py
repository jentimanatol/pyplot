import numpy as np
import matplotlib.pyplot as plt

# Uniform distribution parameters
a = 6
b = 12
height = 1 / (b - a)  # 1 / (12 - 6) = 1/6

# X and Y values
x = np.linspace(4, 14, 1000)
y = np.where((x >= a) & (x <= b), height, 0)

# Plotting
fig, ax = plt.subplots(figsize=(10, 5))

# Plot uniform PDF
ax.plot(x, y, label='Uniform Distribution (6 to 12 lbs)', color='blue')

# Hashurated area: P(0.2 ≤ X ≤ 0.8) = 0
x_fill = np.linspace(0.2, 0.8, 500)
y_fill = np.zeros_like(x_fill)
ax.fill_between(x_fill, y_fill, height, 
                facecolor='none', hatch='///', edgecolor='red', linewidth=0.0,
                label='P(0.2 ≤ X ≤ 0.8) = 0 (Outside Range)')

# Dashed boundary lines
ax.axvline(0.2, color='red', linestyle='--')
ax.axvline(0.8, color='red', linestyle='--')

# Label the height
ax.text(6.1, height + 0.005, 'Height = 1/6 ≈ 0.1667', fontsize=10, color='blue')

# Styling
ax.set_title('Uniform Distribution of Weight Loss (6 to 12 lbs)')
ax.set_xlabel('Pounds Lost')
ax.set_ylabel('Probability Density (P(x))')
ax.set_ylim(0, 0.2)
ax.legend()
ax.grid(True)

plt.show()
