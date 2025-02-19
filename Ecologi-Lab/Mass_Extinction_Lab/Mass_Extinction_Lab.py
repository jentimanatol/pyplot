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
    'O2 (%)': [19, 25.4, 31.0, 20.4, 22.7, 21.0],
    'CO2 (ppm)': [4689, 3105, 324, 13.49, 856, 392],
    'Day Length (h)': [21.8, 22.1, 22.6, 23, 23.7, 24],
    'Luminosity (in Charts)': [96.16, 69.63, 97.58, 98.24, 99.86, 100],
    'Biodiversity (# of genera)': [869, 1488, 1026, 620, 1357, 2470]
}

# Create DataFrame
df = pd.DataFrame(data)

# Plotting
fig, ax1 = plt.subplots(figsize=(12, 6))

# Plot Avg. Surface Temp
ax1.set_xlabel('Millions of Years Ago')
ax1.set_ylabel('Avg. Surface Temp (°C)', color='tab:red')
ax1.plot(df['Millions of Years Ago'], df['Avg. Surface Temp (°C)'], color='tab:red', marker='o')
ax1.tick_params(axis='y', labelcolor='tab:red')

# Extend x-axis for more detail
ax1.set_xticks(df['Millions of Years Ago'])
ax1.set_xticklabels(df['Millions of Years Ago'])

# Create twin Axes sharing the x-axis
ax2 = ax1.twinx()
ax2.set_ylabel('CO2 (ppm)', color='tab:blue')
ax2.plot(df['Millions of Years Ago'], df['CO2 (ppm)'], color='tab:blue', marker='o')
ax2.tick_params(axis='y', labelcolor='tab:blue')

# Plot O2 (%)
ax3 = ax1.twinx()
ax3.spines['right'].set_position(('outward', 60))
ax3.set_ylabel('O2 (%)', color='tab:green')
ax3.plot(df['Millions of Years Ago'], df['O2 (%)'], color='tab:green', marker='o')
ax3.tick_params(axis='y', labelcolor='tab:green')

# Plot Day Length (h)
ax4 = ax1.twinx()
ax4.spines['right'].set_position(('outward', 120))
ax4.set_ylabel('Day Length (h)', color='tab:orange')
ax4.plot(df['Millions of Years Ago'], df['Day Length (h)'], color='tab:orange', marker='o')
ax4.tick_params(axis='y', labelcolor='tab:orange')

# Plot Luminosity (in Charts)
ax5 = ax1.twinx()
ax5.spines['right'].set_position(('outward', 180))
ax5.set_ylabel('Luminosity (in Charts)', color='tab:purple')
ax5.plot(df['Millions of Years Ago'], df['Luminosity (in Charts)'], color='tab:purple', marker='o')
ax5.tick_params(axis='y', labelcolor='tab:purple')

# Plot Biodiversity (# of genera)
ax6 = ax1.twinx()
ax6.spines['right'].set_position(('outward', 240))
ax6.set_ylabel('Biodiversity (# of genera)', color='tab:brown')
ax6.plot(df['Millions of Years Ago'], df['Biodiversity (# of genera)'], color='tab:brown', marker='o')
ax6.tick_params(axis='y', labelcolor='tab:brown')

# Title and Show plot
plt.title('Earth Parameters Over Time')
fig.tight_layout()
plt.gca().invert_xaxis()
plt.show()
