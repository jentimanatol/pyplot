import matplotlib.pyplot as plt
import numpy as np

# Data for 3 countries
countries = ['Jamaica', 'Madagascar', 'Vietnam']
land_area_sqmi = [4244, 226597, 127882]  # square miles
co2_emissions_tons = [6865000, 20800000, 267000000]  # tons/year

# Bamboo CO2 absorption range (tons/year per acre)
bamboo_absorption_low = 25
bamboo_absorption_high = 60
acre_to_sqmi = 1 / 640  # 1 sq mi = 640 acres

# Absorption capacity per sqmi
absorb_low = bamboo_absorption_low * 640  # 16000 tons/year per sq mi
absorb_high = bamboo_absorption_high * 640  # 38400 tons/year per sq mi

# Required bamboo area to offset emissions
required_land_low = [emission / absorb_high for emission in co2_emissions_tons]
required_land_high = [emission / absorb_low for emission in co2_emissions_tons]

# Percentage of total land required
percent_land_low = [100 * req / land for req, land in zip(required_land_low, land_area_sqmi)]
percent_land_high = [100 * req / land for req, land in zip(required_land_high, land_area_sqmi)]

# Plotting
x = np.arange(len(countries))
width = 0.35

fig, ax = plt.subplots(figsize=(12, 7))
bars1 = ax.bar(x - width/2, percent_land_low, width, label='High Absorption (60 tons/acre)', color='green')
bars2 = ax.bar(x + width/2, percent_land_high, width, label='Low Absorption (25 tons/acre)', color='darkgreen')

# Add labels and titles
ax.set_ylabel('% of Land Area Required for Bamboo Plantations')
ax.set_title('Estimated Land % Required to Offset CO₂ Emissions via Bamboo Plantations')
ax.set_xticks(x)
ax.set_xticklabels(countries)
ax.legend()

# Annotate each bar with percentage value
for bars in [bars1, bars2]:
    for bar in bars:
        height = bar.get_height()
        ax.annotate(f'{height:.1f}%',
                    xy=(bar.get_x() + bar.get_width() / 2, height),
                    xytext=(0, 3),  # offset
                    textcoords="offset points",
                    ha='center', va='bottom')

# Add formula box
formula_text = (
    "Formulas Used:\n"
    "Required Area = CO₂ Emission / Bamboo Absorption Rate\n"
    "% Land Required = (Required Area / Total Land) * 100"
)
plt.gcf().text(0.15, 0.02, formula_text, fontsize=9, color='gray', style='italic')

# Watermark
plt.gcf().text(0.9, 0.01, 'Anatolie Jentimir 2025', fontsize=10, color='lightgray', ha='right', va='bottom', alpha=0.7)

plt.tight_layout()
plt.show()
