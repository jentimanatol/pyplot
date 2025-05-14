import matplotlib.pyplot as plt
import numpy as np

# Data from the question
speeds = [267, 198, 185, 169, 156, 151, 146, 146, 146, 141]

# Calculate mean and standard deviation
mean_speed = np.mean(speeds)
std_dev_speed = np.std(speeds)

# Create the plot
plt.figure(figsize=(10, 6))

# Plot the speeds of each celebrity
plt.bar(range(len(speeds)), speeds, color='skyblue', label='Data Speeds')

# Add a horizontal line for the mean
plt.axhline(mean_speed, color='red', linestyle='--', label=f'Mean Speed: {mean_speed:.2f} Mbps')

# Add error bars for standard deviation
plt.errorbar(range(len(speeds)), speeds, yerr=std_dev_speed, fmt='o', color='black', capsize=5, label=f'Standard Deviation: {std_dev_speed:.2f} Mbps')

# Add labels and title
plt.xlabel('Data Point Index', fontsize=12)
plt.ylabel('Speed (Mbps)', fontsize=12)
plt.title('Airport Data Speeds with Mean and Standard Deviation', fontsize=14, fontweight='bold')

# Add informational text in the top-right corner
info_text = (
    "Squared differences for each speed:  \n"
    "1: (267−162.1)²=11035.21   \n"
    "2: (198−162.1)²=1296.01    \n"
    "3: (185−162.1)²=524.41     \n"
    "4: (169−162.1)²=47.61      \n"
    "5: (156−162.1)²=37.21      \n"
    "6: (151−162.1)²=122.41     \n"
    "7: (146−162.1)²=259.21     \n"
    "8: (146−162.1)²=259.21     \n"
    "9: (146−162.1)²=259.21     \n"
    "10: (141−162.1)²=448.41    \n"
)

plt.text(0.95, 0.05, info_text, fontsize=10, bbox=dict(facecolor='lightyellow', alpha=0.8),
         transform=plt.gca().transAxes, verticalalignment='bottom', horizontalalignment='right')

# Add legend
plt.legend(loc='upper left')

# Show the plot
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()
