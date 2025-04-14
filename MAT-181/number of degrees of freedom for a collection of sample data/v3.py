import matplotlib.pyplot as plt
import numpy as np

# Data from the question
speeds = [267, 198, 185, 169, 156, 151, 146, 146, 146, 141]
mean_speed = 17.598  # Sample mean from the provided data
std_dev_speed = 16.01712719  # Sample standard deviation from the provided data

# Number of samples
n = 50
# Degrees of freedom
df = n - 1
# Confidence Interval Limits
lower_limit = 13.046
upper_limit = 22.15

# Create the plot
plt.figure(figsize=(10, 6))

# Plot the data speeds
plt.plot(speeds, 'o-', label='Data Speeds', color='skyblue')

# Highlight the confidence interval
plt.axhspan(lower_limit, upper_limit, color='yellow', alpha=0.3, label=f'99% Confidence Interval: [{lower_limit}, {upper_limit}]')

# Add labels and title
plt.xlabel('Sample Index', fontsize=12)
plt.ylabel('Speed (Mbps)', fontsize=12)
plt.title('Airport Data Speeds with Confidence Interval', fontsize=14, fontweight='bold')

# Add legend
plt.legend(loc='upper right')

# Show the plot
plt.grid(True)
plt.tight_layout()
plt.show()
