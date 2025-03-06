import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Read the CSV file (starting from line 5 for data extraction)
file_path = 'data-3_6_2025-5_14 PM.csv'
data = pd.read_csv(file_path, skiprows=5)

# Display the first few rows of the dataframe to verify column names and data
print(data.head())

# Extract z-scores and corresponding cumulative areas
# Skip non-numeric rows
z_scores = []
area_values = []

for idx, row in data.iterrows():
    try:
        z = float(row[0].strip())
        z_scores.append(z)
        area_values.append(list(map(float, row[1:])))
    except ValueError:
        print(f"Skipping non-numeric row at index {idx}")

# Flatten area_values list
area_list = [item for sublist in area_values for item in sublist]

# Ensure both lists have the same length by truncating the longer list
min_length = min(len(z_scores) * len(data.columns[1:]), len(area_list))
z_list = np.repeat(z_scores, len(data.columns[1:]))[:min_length]
area_list = area_list[:min_length]

# Check for consistency in the lengths of z_list and area_list
if len(z_list) != len(area_list):
    print(f"Error: Length mismatch between z-scores and cumulative areas. z_list length: {len(z_list)}, area_list length: {len(area_list)}")
else:
    print(f"Processed {len(z_list)} data points successfully.")

# Convert lists to numpy arrays for plotting
try:
    z_list = np.array(z_list, dtype=float)
    area_list = np.array(area_list, dtype=float)
except ValueError as e:
    print(f"Error in converting to numpy arrays: {e}")

# Plot the standard normal distribution with cumulative areas
plt.figure(figsize=(10, 6))
plt.plot(z_list, area_list, label='Standard Normal Distribution', color='blue')

# Highlight the area to the left of z = 0.76
z_value = 0.76
area_value = area_list[np.abs(z_list - z_value).argmin()]
#plt.fill_between(z_list, 0, area_list, where=(z_list <= z_value), color='red', alpha=0.5, label=f'Area to the left of z = {z_value} = {area_value:.4f}')
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
