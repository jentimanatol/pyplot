import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib.ticker import FuncFormatter

# Data
countries = ["Jamaica", "Madagascar", "Vietnam"]
land_area = np.array([4244, 226597, 127882])  # sq mi
annual_emissions = np.array([6_865_000, 20_800_000, 267_000_000])  # tons CO2/yr
high_seq = 40.7  # Best-case sequestration (tons/sq mi/yr)

# Calculations
bamboo_area_needed = annual_emissions / high_seq
percent_land = (bamboo_area_needed / land_area) * 100

# Plot setup
plt.figure(figsize=(14, 8))
sns.set_style("whitegrid")
palette = sns.color_palette("viridis", n_colors=2)  # Colors for grouped bars

# Grouped bar plot
bar_width = 0.35
x = np.arange(len(countries))

# Bars for land area and bamboo area needed
bars_land = plt.bar(x - bar_width/2, land_area, width=bar_width, 
                    color=palette[0], edgecolor='black', label='Total Land Area')
bars_bamboo = plt.bar(x + bar_width/2, bamboo_area_needed, width=bar_width, 
                      color=palette[1], edgecolor='black', label='Bamboo Area Needed')

# Annotations
for i in range(len(countries)):
    # Land area annotation
    plt.text(x[i] - bar_width/2, land_area[i] * 1.05, f"{land_area[i]:,.0f} sq mi", 
             ha='center', va='bottom', fontsize=10)
    # Bamboo area annotation
    plt.text(x[i] + bar_width/2, bamboo_area_needed[i] * 1.05, 
             f"{bamboo_area_needed[i]:,.0f} sq mi\n({percent_land[i]:,.0f}% of land)", 
             ha='center', va='bottom', fontsize=10)

# Aesthetics
plt.title("Land Area vs. Bamboo Needed for 100% CO2₂ Offset (40.7 t/sq mi/yr)", fontsize=14, pad=20)
plt.xlabel("Country", fontsize=12)
plt.ylabel("Area (sq mi)", fontsize=12)
plt.xticks(x, countries)
plt.yscale("log")  # Log scale for readability
plt.gca().yaxis.set_major_formatter(FuncFormatter(lambda x, _: f"{x:,.0f}"))

# Custom legend with formulas
formula_text = [
    r"$\text{Bamboo Area} = \frac{\text{Annual CO}_2\text{ Emissions}}{40.7\ \text{t/sq mi/yr}}$",
    r"$\text{Land \%} = \left(\frac{\text{Bamboo Area}}{\text{Total Land Area}}\right) \times 100$"
]

# Create legend handles
legend_handles = [
    bars_land,
    bars_bamboo,
    plt.Line2D([0], [0], color='white', label=formula_text[0]),
    plt.Line2D([0], [0], color='white', label=formula_text[1])
]

plt.legend(
    handles=[bars_land, bars_bamboo] + legend_handles[2:],
    title="Calculations:",
    loc='upper right',
    bbox_to_anchor=(1.35, 1),
    frameon=True
)

#plt.figtext(0.5, 0.10, "Bamboo area needed exceeds national land by 40–5000%", 
 #           ha='center', fontsize=12, style='italic', bbox=dict(facecolor='white', alpha=0.7))


plt.tight_layout()
plt.show()