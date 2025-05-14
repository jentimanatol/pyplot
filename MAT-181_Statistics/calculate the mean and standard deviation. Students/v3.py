
import matplotlib.pyplot as plt
import numpy as np

# Data
friends = ['Ashley', 'Ayaan', 'Miryan', 'Anatolie', 'Mahbuba']
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


# Add informational text in the top-right corner
info_text = (
    "squared differences  each height  \n"
    "Ashley: (65−67.4)²=(−2.4)²=5.76   \n"
    "Ayaan: (68−67.4)²=(0.6)²=0.36     \n"
    "Miryan: (70−67.4)²=(2.6)²=6.76    \n"
    "Anatolie: (62−67.4)²=(−5.4)²=29.16\n"
    "Mahbuba: (72−67.4)²=(4.6)²=21.16  \n"
)


plt.text(0.95, 0.05, info_text, fontsize=10, bbox=dict(facecolor='lightyellow', alpha=0.8),
         transform=plt.gca().transAxes, verticalalignment='bottom', horizontalalignment='right')

# Add legend
plt.legend(loc='upper left')

# Show the plot
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()