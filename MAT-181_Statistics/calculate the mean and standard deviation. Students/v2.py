import matplotlib.pyplot as plt
import numpy as np

# Data
friends = ['Friend A', 'Friend B', 'Friend C', 'Friend D', 'Friend E']
heights = [65, 68, 70, 62, 72]  # Heights in inches

# Calculate mean and standard deviation
mean_height = np.mean(heights)
std_dev = np.std(heights)

# Create the plot
plt.figure(figsize=(10, 6))

# Plot the heights of each friend
plt.bar(friends, heights, color='skyblue', label='Heights')

# Add a horizontal line for the mean
plt.axhline(mean_height, color='red', linestyle='--', label=f'Mean Height: {mean_height:.2f} inches')

# Add error bars for standard deviation
plt.errorbar(friends, heights, yerr=std_dev, fmt='o', color='black', capsize=5, label=f'Standard Deviation: {std_dev:.2f} inches')

# Add labels and title
plt.xlabel('Friends', fontsize=12)
plt.ylabel('Height (inches)', fontsize=12)
plt.title('Heights of 5 Friends with Mean and Standard Deviation', fontsize=14, fontweight='bold')

# Add informational text
info_text = (
    f"Mean Height: {mean_height:.2f} inches\n"
    f"Standard Deviation: {std_dev:.2f} inches\n"
    f"Friend A: 65 inches\n"
    f"Friend B: 68 inches\n"
    f"Friend C: 70 inches\n"
    f"Friend D: 62 inches\n"
    f"Friend E: 72 inches"
)
plt.text(0.5, 74, info_text, fontsize=10, bbox=dict(facecolor='lightyellow', alpha=0.8))

# Add legend
plt.legend(loc='upper right')

# Show the plot
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()