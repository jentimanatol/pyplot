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
bamboo_area = annual_emissions / high_seq
percent_land = (bamboo_area / land_area) * 100

# Plot setup
plt.figure(figsize=(12, 7))
sns.set_style("whitegrid")
palette = sns.color_palette("mako_r", len(countries))

# Bar plot
bars = plt.bar(countries, bamboo_area, color=palette, edgecolor='black', alpha=0.9)

# Annotations
for bar, area, percent in zip(bars, bamboo_area, percent_land):
    height = bar.get_height()
    plt.text(bar.get_x() + bar.get_width() / 2, height * 1.02, 
             f"{area:,.0f} sq mi\n({percent:,.0f}% of land)", 
             ha='center', va='bottom', fontsize=10)

# Horizontal reference lines
for i, land in enumerate(land_area):
    plt.axhline(y=land, color=palette[i], linestyle=':', alpha=0.4, lw=1.5)

# Legend with LaTeX formulas (simplified to avoid f-string issues)
legend_text = [
    r"$\text{Bamboo Area} = \frac{\text{CO}_2\text{ Emissions}}{40.7\ \text{t/sq mi/yr}}$",
    r"$\text{Land \%} = \left(\frac{\text{Bamboo Area}}{\text{Country Area}}\right) \times 100$",
    "",
    r"$\text{Jamaica:}\ \frac{6.86\text{M}}{40.7} = 168,\!700\ \text{sq mi}$",
    r"$\text{Madagascar:}\ \frac{20.8\text{M}}{40.7} = 511,\!000\ \text{sq mi}$",
    r"$\text{Vietnam:}\ \frac{267\text{M}}{40.7} = 6.56\text{M}\ \text{sq mi}$"
]

plt.legend(
    handles=[plt.Line2D([0], [0], color='white', label=text) for text in legend_text],
    title="Calculations:",
    loc='upper right',
    bbox_to_anchor=(1.35, 1),
    frameon=True,
    edgecolor='black',
    title_fontsize=12,
    fontsize=10,
    handlelength=0
)

# Aesthetics
plt.title(
    "Bamboo Required for 100% CO₂ Offset (Best-Case: 40.7 t/sq mi/yr)\n",
    fontsize=14,
    pad=20
)
plt.xlabel("Country", fontsize=12)
plt.ylabel("Bamboo Area Needed (sq mi)", fontsize=12)
plt.yscale("log")
plt.gca().yaxis.set_major_formatter(FuncFormatter(lambda x, _: f"{x:,.0f}"))

plt.tight_layout()
plt.show()