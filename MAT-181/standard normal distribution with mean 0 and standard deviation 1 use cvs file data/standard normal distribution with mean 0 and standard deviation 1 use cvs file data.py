import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Read the CSV file (starting from line 5 for data extraction)
data = pd.read_csv('data-3_6_2025-5_14 PM.csv', skiprows=5)

# Extract z-scores and corresponding cumulative areas
z_scores = data['z']
cumulative_areas = data.drop('z', axis=1)

# Create a flat list of z-scores and their corresponding cumulative areas
z_list = []
area_list = []
for col in cumulative_areas.columns:
    z_list.extend(z_scores)
    area_list.extend(cumulative_areas[col])

# Convert lists to numpy arrays for plotting
z_list = np.array(z_list)
area_list = np.array(area_list)

# Plot the standard normal distribution with cumulative areas
plt.figure(figsize=(10, 6))
plt.plot(z_list, area_list, label='Standard Normal Distribution', color='blue')

# Highlight the area to the left of z = 0.76
z_value = 0.76
area_value = area_list[np.abs(z_list - z_value).argmin()]
plt.fill_between(z_list, 0, area_list, where=(z_list <= z_value), color='red', alpha=0.5, label=f'Area to the left of z = {z_value} = {area_value:.4f}')

# Add titles, labels, and legend
plt.title('Standard Normal Distribution with Shaded Area', fontsize=16)
plt.xlabel('z-score', fontsize=14)
plt.ylabel('Cumulative Area', fontsize=14)
plt.legend(fontsize=12)

# Add grid for better visualization
plt.grid(True)

# Show the plot
plt.show()
