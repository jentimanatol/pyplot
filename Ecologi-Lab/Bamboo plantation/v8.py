import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib.ticker import FuncFormatter

# Data
countries = ["Jamaica", "Madagascar", "Vietnam"]
land_area = [4244, 226597, 127882]  # sq mi
annual_emissions = [6_865_000, 20_800_000, 267_000_000]  # tons CO2/yr

# Bamboo sequestration rates (tons/sq mi/yr)
low_seq = 10
mid_seq = 20
high_seq = 40.7

# Calculate bamboo area needed to offset 100% emissions
bamboo_area_low = [emi / low_seq for emi in annual_emissions]
bamboo_area_mid = [emi / mid_seq for emi in annual_emissions]
bamboo_area_high = [emi / high_seq for emi in annual_emissions]

# Percentage of country's land required
percent_land_low = [area / land * 100 for area, land in zip(bamboo_area_low, land_area)]
percent_land_mid = [area / land * 100 for area, land in zip(bamboo_area_mid, land_area)]
percent_land_high = [area / land * 100 for area, land in zip(bamboo_area_high, land_area)]

# Plot setup
sns.set_style("whitegrid")
plt.figure(figsize=(12, 8))
colors = sns.color_palette("viridis", n_colors=3)

# Bar plot: Bamboo area needed
bar_width = 0.25
x = np.arange(len(countries))
plt.bar(x - bar_width, bamboo_area_low, width=bar_width, color=colors[0], label=f"Low Seq ({low_seq} t/sq mi/yr)")
plt.bar(x, bamboo_area_mid, width=bar_width, color=colors[1], label=f"Mid Seq ({mid_seq} t/sq mi/yr)")
plt.bar(x + bar_width, bamboo_area_high, width=bar_width, color=colors[2], label=f"High Seq ({high_seq} t/sq mi/yr)")

# Annotations
for i in range(len(countries)):
    plt.text(x[i] - bar_width, bamboo_area_low[i] * 1.02, f"{percent_land_low[i]:.0f}%", ha='center')
    plt.text(x[i], bamboo_area_mid[i] * 1.02, f"{percent_land_mid[i]:.0f}%", ha='center')
    plt.text(x[i] + bar_width, bamboo_area_high[i] * 1.02, f"{percent_land_high[i]:.0f}%", ha='center')

# Aesthetics
plt.title("Bamboo Area Needed to Offset National CO₂ Emissions", fontsize=14, pad=20)
plt.xlabel("Country", fontsize=12)
plt.ylabel("Bamboo Area Required (sq mi)", fontsize=12)
plt.xticks(x, countries)
plt.yscale("log")  # Log scale for better visualization
plt.gca().yaxis.set_major_formatter(FuncFormatter(lambda x, _: f"{x:,.0f}"))

# Legend and formula
formula_text = r"$\text{Bamboo Area} = \frac{\text{Annual CO}_2\text{ Emissions}}{\text{Sequestration Rate}}$"
plt.figtext(0.15, 0.85, formula_text, fontsize=11, bbox=dict(facecolor='white', alpha=0.5))
plt.legend(title="Sequestration Rate", bbox_to_anchor=(1.05, 1), loc='upper left')

plt.tight_layout()
plt.show()