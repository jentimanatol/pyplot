import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Rectangle

# -----------------------------
# COUNTRY DATA & CALCULATIONS
# -----------------------------
countries = ['Jamaica', 'Madagascar', 'Vietnam']
land_area_sqmi = [4244, 226597, 127882]  # in square miles
co2_emissions_tons = [6865000, 20800000, 267000000]  # tons/year

# Bamboo CO2 absorption rates (per acre per year)
bamboo_absorption_low = 25  # tons/year
bamboo_absorption_high = 60  # tons/year
acre_to_sqmi = 1 / 640

# Absorption capacity per square mile
absorb_low = bamboo_absorption_low * 640  # = 16000 tons/year per sq mi
absorb_high = bamboo_absorption_high * 640  # = 38400 tons/year per sq mi

# Land required for each scenario
required_land_high_abs = [emission / absorb_high for emission in co2_emissions_tons]
required_land_low_abs = [emission / absorb_low for emission in co2_emissions_tons]

# Percentage of land required
percent_land_high_abs = [100 * r / t for r, t in zip(required_land_high_abs, land_area_sqmi)]
percent_land_low_abs = [100 * r / t for r, t in zip(required_land_low_abs, land_area_sqmi)]

# -----------------------------
# PLOTTING
# -----------------------------
x = np.arange(len(countries))
width = 0.35
fig, ax = plt.subplots(figsize=(16, 9))

# Bars
bars_high = ax.bar(x - width/2, percent_land_high_abs, width, label='Bamboo Absorption: 60 tons/acre', color='#4CAF50')
bars_low = ax.bar(x + width/2, percent_land_low_abs, width, label='Bamboo Absorption: 25 tons/acre', color='#2E7D32')

# Title and labels
ax.set_title('🌿 Bamboo Plantation Land Required to Offset National CO₂ Emissions', fontsize=18, weight='bold', pad=20)
ax.set_ylabel('% of Total Land Area Needed', fontsize=13)
ax.set_xticks(x)
ax.set_xticklabels(countries, fontsize=12)
ax.legend(loc='upper left', fontsize=11)
ax.grid(True, linestyle='--', alpha=0.3)

# Add value annotations
for bars in [bars_high, bars_low]:
    for bar in bars:
        height = bar.get_height()
        ax.annotate(f'{height:.2f}%',
                    xy=(bar.get_x() + bar.get_width() / 2, height),
                    xytext=(0, 3),
                    textcoords="offset points",
                    ha='center', va='bottom', fontsize=9)

# Background context panel with formulas
formula_text = (
    r"$\text{CO}_2\ \text{Offset Area} = \frac{\text{CO}_2\ \text{Emissions}}{\text{Bamboo Absorption per sq mi}}$" + "\n" +
    r"$\%\ \text{Land Needed} = \left( \frac{\text{CO}_2\ \text{Offset Area}}{\text{Total Land Area}} \right) \times 100$" + "\n\n" +
    "Assumptions:\n" +
    "- 1 sq mile = 640 acres\n" +
    "- Bamboo absorbs between 25–60 tons of CO₂ per acre annually"
)
props = dict(boxstyle='round', facecolor='whitesmoke', alpha=0.8)
ax.text(1.02, 0.5, formula_text, transform=ax.transAxes, fontsize=10,
        verticalalignment='center', bbox=props, family='monospace')

# Additional details text
details_text = "\n".join([
    f"{countries[i]}: {land_area_sqmi[i]:,} sq mi, {co2_emissions_tons[i]:,} tons CO₂/year"
    for i in range(len(countries))
])
props2 = dict(boxstyle='round', facecolor='mintcream', alpha=0.8)
ax.text(1.02, 0.85, details_text, transform=ax.transAxes, fontsize=10,
        verticalalignment='top', bbox=props2, family='monospace', color='darkblue')

# Decorative footer
fig.text(0.5, 0.02, 'Visualization by Anatolie Jentimir 2025', fontsize=10,
         color='gray', ha='center', style='italic')

# Watermark overlay
fig.text(0.95, 0.95, 'Anatolie Jentimir', fontsize=28, color='lightgray',
         ha='right', va='top', alpha=0.15, rotation=30)

plt.tight_layout(rect=[0, 0.05, 0.92, 1])
plt.show()
