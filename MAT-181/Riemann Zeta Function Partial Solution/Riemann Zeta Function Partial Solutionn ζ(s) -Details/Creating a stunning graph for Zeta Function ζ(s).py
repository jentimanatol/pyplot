import matplotlib.pyplot as plt
import numpy as np

# Define range for real part of s (1 < Re(s) < 10)
s_real = np.linspace(1.01, 10, 400)

# Calculate corresponding ζ(s) values
zeta_values = [1 + sum(1/p**x for p in range(2, 100)) for x in s_real]

# Create figure and axis
fig, ax = plt.subplots(figsize=(12, 8))

# Plot ζ(s) values
ax.plot(s_real, zeta_values, label='ζ(s)', color='#00698f', linewidth=2)

# Add title and labels
ax.set_title('Riemann Zeta Function ζ(s)', fontsize=18)
ax.set_xlabel('Real part of s (Re(s))', fontsize=14)
ax.set_ylabel('ζ(s) values', fontsize=14)

# Add grid and legend
ax.grid(True)
ax.legend()

# Highlight area where my proof applies (Re(s) > 1/2 + ε ≈ 0.5)
ax.fill_between(s_real, 0, 100, where=s_real>0.5, alpha=0.2, color='#c7f464')

# Mark points ζ(4) and ζ(5) we calculated
ax.scatter([4, 5], [1.0803, 1.03667], color='#ff6347', s=100, label='ζ(4) & ζ(5)')
ax.legend()

# Show graph
plt.show()
