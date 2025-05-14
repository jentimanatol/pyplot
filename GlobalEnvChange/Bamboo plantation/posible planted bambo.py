import matplotlib.pyplot as plt
import numpy as np

# Country data
countries = ['Jamaica', 'Madagascar', 'Vietnam']
land_area_sqmi = np.array([4244, 226597, 127882])
co2_emissions = np.array([6865000, 20800000, 267000000])

# Bamboo absorption rate per sq mi
bamboo_absorption_per_sqmi = 80 * 640  # 80 tons/acre/year * 640 acres/sq mi

# Potential reduction with 10% land area planted with bamboo
bamboo_area = 0.1 * land_area_sqmi
potential_reduction = bamboo_area * bamboo_absorption_per_sqmi

# Plotting
x = np.arange(len(countries))
width = 0.35

fig, ax = plt.subplots(figsize=(10, 6))
bars1 = ax.bar(x - width/2, co2_emissions / 1e6, width, label='Total CO₂ Emissions')
bars2 = ax.bar(x + width/2, potential_reduction / 1e6, width, label='Potential Reduction (1% Bamboo)')

# Labels and title
ax.set_ylabel('CO₂ (Million Tons)')
ax.set_title('CO₂ Emissions and Potential Reductions via Bamboo Plantations')
ax.set_xticks(x)
ax.set_xticklabels(countries)
ax.legend()

# Annotate bars with values
for bar in bars1:
    height = bar.get_height()
    ax.annotate(f'{height:.1f}',
                xy=(bar.get_x() + bar.get_width() / 2, height),
                xytext=(0, 3),  # 3 points vertical offset
                textcoords="offset points",
                ha='center', va='bottom')
for bar in bars2:
    height = bar.get_height()
    ax.annotate(f'{height:.1f}',
                xy=(bar.get_x() + bar.get_width() / 2, height),
                xytext=(0, 3),
                textcoords="offset points",
                ha='center', va='bottom')

plt.tight_layout()
plt.show()
