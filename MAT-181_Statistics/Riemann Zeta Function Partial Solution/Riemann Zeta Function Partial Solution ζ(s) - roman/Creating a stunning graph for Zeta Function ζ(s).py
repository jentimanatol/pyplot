import matplotlib.pyplot as plt
import numpy as np

# Define range for real part of s (0 < Re(s) < 10)
s_real = np.linspace(0.01, 10, 400)

# Calculate corresponding ζ(s) values
zeta_values = [1 + np.sum(1/np.arange(2,100)**x) for x in s_real]

# Create figure and axis
fig, ax = plt.subplots(figsize=(12,8))

# Plot ζ(s) values
ax.plot(s_real, zeta_values, label='ζ(s)', color='#00698f', linewidth=2)

# Add critical line Re(s)=1/2
ax.plot([0.5]*len(s_real), np.linspace(min(zeta_values),max(zeta_values),len(s_real)), 
        label='Critical Line Re(s)=1/2', color='#ff6347', linestyle='--')

# Add real axis
ax.plot(s_real, [0]*len(s_real), label='Real Axis', color='black')

# Mark zeros on critical line (first 5)
zeros = [0.5+14.1347j, 0.5+21.022j, 0.5+25.0109j, 0.5+30.4249j, 0.5+32.9351j]
ax.scatter([z.real for z in zeros], [zeta_values[np.argmin(abs(s_real-z.real))]
                                       for z in zeros], color='#00ff00', label='Zeros')

# Add title with OUR Riemann Zeta Function formula
ax.set_title(r'$\zeta(s) = 1 + \sum_{p=2}^{\infty} \frac{1}{p^s}$ pentru Re(s) > 1/2 + ε - Ipoteza lui Riemann', fontsize=18)

# Add labels
ax.set_xlabel('Partea reală a lui s (Re(s))', fontsize=14)
ax.set_ylabel('Valori ζ(s)', fontsize=14)

# Add grid and legend
ax.grid(True)
ax.legend()

# Show graph
plt.show()

