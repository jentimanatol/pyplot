import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib.ticker import FuncFormatter

# Data
countries = ["Jamaica", "Madagascar", "Vietnam"]
land_area = [4244, 226597, 127882]  # sq mi
annual_emissions = [6_865_000, 20_800_000, 267_000_000]  # tons CO2/yr
high_seq = 40.7  # Best-case sequestration (tons/sq mi/yr)

# Calculate bamboo area needed and % of land
bamboo_area = [emi / high_seq for emi in annual_emissions]
percent_land = [(area / land) * 100 for area, land in zip(bamboo_area, land_area)]

# Plot setup
plt.figure(figsize=(10, 6))
sns.set_style("whitegrid")
palette = sns.color_palette("rocket", len(countries))

# Bar plot (Bamboo area needed)
bars = plt.bar(countries, bamboo_area, color=palette, edgecolor='black', alpha=0.8)

# Annotate bars with area and % land
for bar, area, percent in zip(bars, bamboo_area, percent_land):
    height = bar.get_height()
    plt.text(bar.get_x() + bar.get_width() / 2, height * 1.02, 
             f"{area:,.0f} sq mi\n({percent:.0f}% of land)", 
             ha='center', va='bottom', fontsize=10)

# Horizontal line for land area reference
for i, land in enumerate(land_area):
    plt.axhline(y=land, color=palette[i], linestyle='--', alpha=0.3, 
                label=f"{countries[i]} Total Land Area")

# Aesthetics
plt.title("Bamboo Required to Offset 100% National CO₂ Emissions (Best-Case Scenario: 40.7 t/sq mi/yr)", 
          fontsize=12, pad=15)
plt.xlabel("Country", fontsize=11)
plt.ylabel("Bamboo Area Needed (sq mi)", fontsize=11)
plt.yscale("log")  # Log scale for readability
plt.gca().yaxis.set_major_formatter(FuncFormatter(lambda x, _: f"{x:,.0f}"))

# Legend and formula
formula_text = r"$\text{Bamboo Area} = \frac{\text{Annual CO}_2\text{ Emissions}}{40.7 \text{ t/sq mi/yr}}$"
plt.figtext(0.15, 0.82, formula_text, fontsize=11, bbox=dict(facecolor='white', alpha=0.5))
plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')

plt.tight_layout()
plt.show()