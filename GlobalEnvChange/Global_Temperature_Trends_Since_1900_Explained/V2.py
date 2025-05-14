import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import pandas as pd

# Data from the Land-Ocean Temperature Index (C)
years = np.array([
    1880, 1881, 1882, 1883, 1884, 1885, 1886, 1887, 1888, 1889,
    1900, 1940, 1941, 1945, 1980, 1998, 2016, 2023, 2024
])
temperature_anomalies = np.array([
    -0.18, -0.10, -0.12, -0.18, -0.29, -0.34, -0.32, -0.37, -0.18, -0.11,
    -0.09, 0.12, 0.18, 0.09, 0.26, 0.61, 1.01, 1.17, 1.28
])

# Create a DataFrame for easier plotting
data = pd.DataFrame({'Year': years, 'Temperature Anomaly (°C)': temperature_anomalies})

# Set style
sns.set_theme(style="darkgrid")
plt.figure(figsize=(12, 6))

# Plot the main trend
sns.lineplot(data=data, x='Year', y='Temperature Anomaly (°C)', marker='o', label='Temperature Anomalies', linewidth=2, color='b')

# Highlight key events
highlight_points = {
    1940: "WWII Peak - Increased industrial activity before war          \n ",
    1945: "WWII Dip - Decreased emissions due to war disruption",
    1980: "Rapid Rise Starts - Industrialization & greenhouse gas emissions",
    1998: "Major Increase - Global warming intensifies",
    2016: "Crossed 1°C - Significant warming milestone",
    2023: "Recent High - Ongoing climate change impact"
}

for year, label in highlight_points.items():
    temp = data[data['Year'] == year]['Temperature Anomaly (°C)'].values[0]
    plt.scatter(year, temp, color='red', s=100, zorder=3)
    plt.text(year, temp + 0.05, label, fontsize=10, ha='right', color='red', bbox=dict(facecolor='white', alpha=0.7, edgecolor='red'))

# Additional explanation text
plt.text(1885, 1.1, "Significant Rise in Global Temperature Since 1900", fontsize=12, color='black', bbox=dict(facecolor='white', alpha=0.6))
plt.text(1890, 1.0, "Post-WWII dip before rapid industrialization", fontsize=10, color='black', bbox=dict(facecolor='white', alpha=0.6))
plt.text(1985, -0.2, "Pre-1980s - Temperatures relatively stable", fontsize=10, color='black', bbox=dict(facecolor='white', alpha=0.6))

# Labels and title
plt.xlabel('Year\n by Anatolie Jentimir ENV')
plt.ylabel('Temperature Anomaly (°C)')
plt.title('Global Temperature Anomalies (1880-2024) with Key Events by Anatolie Jentimir ENV')
plt.legend()
plt.show()
