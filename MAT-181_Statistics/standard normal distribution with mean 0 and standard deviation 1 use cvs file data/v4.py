import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Read the first few lines of the CSV file to analyze its structure
file_path = 'data-3_6_2025-5_14 PM.csv'
with open(file_path, 'r') as file:
    for i in range(5):
        line = file.readline()
        print(f"Line {i+1}: {line.strip()}")

# Read the CSV file starting from the 6th line (actual data)
data = pd.read_csv(file_path, skiprows=5)

# Display the first few rows of the dataframe to verify column names and data
print(data.head())

# Extract z-scores and corresponding cumulative areas
z_scores = data.iloc[:, 0]  # Assuming the first column contains the z-scores
cumulative_areas = data.iloc[:, 1:]  # All other columns contain cumulative areas

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
