import matplotlib.pyplot as plt
import numpy as np

# Define range for real part of s (0 < Re(s) < 10)
s_real = np.linspace(0.01, 10, 400)

# Calculate corresponding values
original_values = [np.sum(1/np.arange(1,100)**x) for x in s_real]
our_values = [1 + np.sum(1/np.arange(2,100)**x) for x in s_real]

# Create figure and axis
fig, axs = plt.subplots(2, figsize=(12,10), sharex=True)

# Top subplot: difference
axs[0].plot(s_real, np.abs(np.array(original_values) - np.array(our_values)), color='#666666')
axs[0].set_title('Difference: Original - Our Method')
axs[0].set_ylabel('Absolute Difference')

# Bottom subplot: original and our values
axs[1].plot(s_real, original_values, label='Original Riemann Zeta Function', color='#00698f', linewidth=2)
axs[1].plot(s_real, our_values, label='Our Method: 1 + Σ[1/p^s]', color='#ff6347', linewidth=2)
axs[1].set_title('Original vs Our Method')
axs[1].set_xlabel('Real part of s (Re(s))')
axs[1].set_ylabel('Zeta Function values')
axs[1].legend()

# Layout so plots do not overlap
fig.tight_layout()

# Show graph
plt.show()
