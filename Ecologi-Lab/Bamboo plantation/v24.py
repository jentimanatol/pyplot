import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib.ticker import FuncFormatter
from matplotlib.patches import Patch

# ======================
# DATA & CALCULATIONS
# ======================
countries = ["Jamaica", "Madagascar", "Vietnam"]
land_area = np.array([4244, 228531, 127932])  # sq mi

#data from https://www.worldometers.info/co2-emissions/
# Jamaica: 6,083,040 tons CO2/yr
# Madagascar: 4,099,000 tons CO2/yr
# Vietnam: 327,905,620 tons CO2/yr
annual_emissions = np.array([6_083_040, 4_099_000, 327_905_620])  # tons CO2/yr 

# Updated sequestration rate: 25 tons CO2 per acre per year
# Convert to per square mile: 25 * 640 = 16,000 tons CO2/sq mi/yr
high_seq = 16000  # tons CO2/sq mi/yr

# Calculations
bamboo_area_needed = annual_emissions / high_seq
percent_land = (bamboo_area_needed / land_area) * 100

# ======================
# PLOT SETUP
# ======================
plt.figure(figsize=(15, 8))
sns.set_style("whitegrid")
plt.rcParams['mathtext.fontset'] = 'cm'  # Professional math fonts
palette = sns.color_palette("rocket", n_colors=2)

# ======================
# GROUPED BAR PLOT
# ======================
bar_width = 0.4
x = np.arange(len(countries))

# Plot bars
bars_land = plt.bar(x - bar_width/2, land_area, width=bar_width,
                   color=palette[0], alpha=0.9, edgecolor='black',
                   label='Actual Land Area')
bars_bamboo = plt.bar(x + bar_width/2, bamboo_area_needed, width=bar_width,
                     color=palette[1], alpha=0.9, edgecolor='black',
                     label='Bamboo Area Needed')

# ======================
# ANNOTATIONS
# ======================
def format_large_num(x):
    """Convert large numbers to readable format (e.g., 1M, 1K)"""
    if x >= 1e6:
        return f"{x/1e6:,.1f}M"
    elif x >= 1e3:
        return f"{x/1e3:,.0f}K"
    return f"{x:,.0f}"

for i, (land, bamboo, percent) in enumerate(zip(land_area, bamboo_area_needed, percent_land)):
    # Land area labels
    plt.text(x[i] - bar_width/2, land * 1.05, 
             f"{format_large_num(land)} sq mi", 
             ha='center', va='bottom', fontsize=10, fontweight='bold')
    
    # Bamboo area labels
    plt.text(x[i] + bar_width/2, bamboo * 1.05, 
             f"{format_large_num(bamboo)} sq mi\n({percent:,.0f}% of land)", 
             ha='center', va='bottom', fontsize=10, fontweight='bold',
             bbox=dict(facecolor='white', alpha=0.8, edgecolor='none'))

# ======================
# AESTHETICS
# ======================
plt.title("National Land vs. Bamboo Needed for 100% CO₂ Offset\n(Best-Case: 16,000 t/sq mi/yr)", 
          fontsize=16, pad=20, fontweight='bold')
plt.xlabel("Country", fontsize=14, labelpad=10)
plt.ylabel("Area (sq mi) [Log Scale]", fontsize=14, labelpad=10)
plt.xticks(x, countries, fontsize=12)
plt.yscale("log")
plt.gca().yaxis.set_major_formatter(FuncFormatter(lambda x, _: format_large_num(x)))
plt.grid(True, which="both", ls="--", alpha=0.2)










# ======================





# ======================
# PROFESSIONAL LEGEND WITH FORMULAS & CALCULATIONS
# ======================
legend_elements = [
    Patch(facecolor=palette[0], label='Actual Land Area', edgecolor='black'),
    Patch(facecolor=palette[1], label='Bamboo Area Needed', edgecolor='black'),
    
    # Initial Data Section (CO2 Emissions per Country)
    plt.Line2D([0], [0], color='none', label=r"$\mathbf{Initial\ Data:}$"),
    plt.Line2D([0], [0], color='none', label=r"$\text{Jamaica:}\ 6,083,040\ \text{tons\ CO}_2\text{/yr}$"),
    plt.Line2D([0], [0], color='none', label=r"$\text{Madagascar:}\ 4,099,000\ \text{tons\ CO}_2\text{/yr}$"),
    plt.Line2D([0], [0], color='none', label=r"$\text{Vietnam:}\ 327,905,620\ \text{tons\ CO}_2\text{/yr}$"),
    plt.Line2D([0], [0], color='none', label=r"$\mathbf{Formulas}$"),
    
    # General Formulas Section
    plt.Line2D([0], [0], color='none', label=
        r"$\text{Bamboo Area} = \frac{\text{CO}_2\text{ Emissions}}{16,000\ \text{t/sq mi/yr}}$"),
    plt.Line2D([0], [0], color='none', label=
        r"$\text{Land \%} = \frac{\text{Bamboo Area}}{\text{Land Area}} \times 100$")
]

# Append country-specific calculations
for i, country in enumerate(countries):
    bamboo_area_formula = rf"$\text{{Bamboo Area}} = \frac{{{annual_emissions[i]:,.0f}}}{{16,000}} = {bamboo_area_needed[i]:,.1f}\ \text{{sq mi}}$"
    land_percent_formula = rf"$\text{{Land \%}} = \frac{{{bamboo_area_needed[i]:,.1f}}}{{{land_area[i]:,.0f}}} \times 100 = {percent_land[i]:.2f}\%$"
    legend_elements.append(
        plt.Line2D(
            [0], [0], color='none',
            label=f"{country}: \n    {bamboo_area_formula},\n    {land_percent_formula}"
        )
    )

plt.legend(handles=legend_elements, loc='upper right', 
           bbox_to_anchor=(1.35, 1), frameon=True, fontsize=11,
           title="Key Formulas & Country Calculations:", title_fontsize=12)









# ======================






# ======================
# FINAL TOUCHES
# ======================
plt.tight_layout()
plt.savefig('bamboo_co2_offset_corrected.png', dpi=300, bbox_inches='tight')  # Save high-res
plt.show()
