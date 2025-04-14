import matplotlib.pyplot as plt
import pandas as pd

# Data from the user
data = {
    'Event': [
        'Ordovician', 'Devonian', 'Permian', 'Triassic', 
        'Cretaceous', 'Present Day'
    ],
    'Millions of Years Ago': [440, 380, 280, 200, 65, 0],
    'Avg. Surface Temp (°C)': [15, 19, 12, 16, 16, 13],
    'CO2 (ppm)': [4689, 3105, 324, 13.49, 856, 392]
}

# Create DataFrame
df = pd.DataFrame(data)

# Plotting
fig, ax1 = plt.subplots()

# Plot Avg. Surface Temp
ax1.set_xlabel('Millions of Years Ago')
ax1.set_ylabel('Avg. Surface Temp (°C)', color='tab:red')
ax1.plot(df['Millions of Years Ago'], df['Avg. Surface Temp (°C)'], color='tab:red', marker='o')
ax1.tick_params(axis='y', labelcolor='tab:red')

# Create a twin Axes sharing the xaxis
ax2 = ax1.twinx()
ax2.set_ylabel('CO2 (ppm)', color='tab:blue')
ax2.plot(df['Millions of Years Ago'], df['CO2 (ppm)'], color='tab:blue', marker='o')
ax2.tick_params(axis='y', labelcolor='tab:blue')

# Title and Show plot
plt.title('Average Surface Temperature and CO2 Levels Over Time')
fig.tight_layout()
plt.gca().invert_xaxis()
plt.show()
