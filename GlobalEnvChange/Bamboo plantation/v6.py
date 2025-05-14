import matplotlib.pyplot as plt
import numpy as np

# Country data
countries = ['Jamaica', 'Madagascar', 'Vietnam']
land_area_sqmi = np.array([4244, 226597, 127882])
co2_emissions = np.array([6865000, 20800000, 267000000])

# Bamboo absorption rate per sq mi
bamboo_absorption_per_sqmi = 80 * 640  # 80 tons/acre/year * 640 acres/sq mi

# Potential reduction with 5% land area planted with bamboo
bamboo_area = 0.05 * land_area_sqmi
potential_reduction = bamboo_area * bamboo_absorption_per_sqmi

# Plotting
x = np.arange(len(countries))
width = 0.35

fig, ax = plt.subplots(figsize=(12, 7))
bars1 = ax.bar(x - width/2, co2_emissions / 1e6, width, label='Total CO₂ Emissions', color='skyblue')
bars2 = ax.bar(x + width/2, potential_reduction / 1e6, width, label='Potential Reduction (5% Bamboo)', color='lightgreen')

# Labels and title
ax.set_ylabel('CO₂ (Million Tons)', fontsize=12)
ax.set_title('CO₂ Emissions and Potential Reductions via Bamboo Plantations (5% Land Area)', fontsize=14, fontweight='bold')
ax.set_xticks(x)
ax.set_xticklabels(countries, fontsize=12)
ax.legend()

# Annotate bars with values
for bar in bars1:
    height = bar.get_height()
    ax.annotate(f'{height:.2f}',
                xy=(bar.get_x() + bar.get_width() / 2, height),
                xytext=(0, 3),
                textcoords="offset points",
                ha='center', va='bottom', fontsize=10)
for bar in bars2:
    height = bar.get_height()
    ax.annotate(f'{height:.2f}',
                xy=(bar.get_x() + bar.get_width() / 2, height),
                xytext=(0, 3),
                textcoords="offset points",
                ha='center', va='bottom', fontsize=10)

# Additional annotations
for i in range(len(countries)):
    ax.text(x[i], max(co2_emissions[i], potential_reduction[i]) / 1e6 + 5,
            f"Land Area: {land_area_sqmi[i]:,} sq mi\nEmissions: {co2_emissions[i]:,} tons",
            ha='center', va='bottom', fontsize=9, bbox=dict(boxstyle="round,pad=0.3", facecolor='white', alpha=0.5))

# Watermark
fig.text(0.95, 0.05, 'Anatolie Jentimir 2025', fontsize=12, color='gray',
         ha='right', va='bottom', alpha=0.5)

plt.tight_layout()
plt.show()
