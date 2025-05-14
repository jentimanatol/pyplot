import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib.ticker import FuncFormatter

# Scientific Constants
SQMI_TO_HECTARES = 259  # 1 square mile = 259 hectares
BAMBOO_SEQ_RATE = 30    # Bamboo: 30 t CO2/ha/yr (IPCC average)
FOREST_SEQ_RATE = 15    # Tropical forest: 15 t CO2/ha/yr (Nature 2021)

# Country Data
countries = ["Jamaica", "Madagascar", "Vietnam"]
land_area = np.array([4244, 226597, 127882])  # in sq mi
annual_emissions = np.array([6_865_000, 20_800_000, 267_000_000])  # t CO2/yr

# Calculate required areas
def calculate_area(emissions, seq_rate):
    """Returns area in sq mi needed to offset emissions"""
    return emissions / (seq_rate * SQMI_TO_HECTARES)

bamboo_area = calculate_area(annual_emissions, BAMBOO_SEQ_RATE)
forest_area = calculate_area(annual_emissions, FOREST_SEQ_RATE)

# Visualization Setup
plt.figure(figsize=(14, 8))
sns.set_style("whitegrid")
plt.rcParams['font.family'] = 'DejaVu Sans'  # Better LaTeX rendering
colors = sns.color_palette("husl", 3)

# Create Grouped Bar Plot
bar_width = 0.25
x = np.arange(len(countries))

fig, ax = plt.subplots(figsize=(14, 8))
rects1 = ax.bar(x - bar_width, bamboo_area, bar_width, 
                color=colors[0], label='Bamboo Area Needed')
rects2 = ax.bar(x, forest_area, bar_width, 
                color=colors[1], label='Forest Area Needed')
rects3 = ax.bar(x + bar_width, land_area, bar_width, 
                color=colors[2], label='Actual Land Area')

# Add Value Labels
def autolabel(rects):
    for rect in rects:
        height = rect.get_height()
        ax.annotate(f'{height:,.0f}',
                    xy=(rect.get_x() + rect.get_width() / 2, height),
                    xytext=(0, 3),  # 3 points vertical offset
                    textcoords="offset points",
                    ha='center', va='bottom', fontsize=9)

autolabel(rects1)
autolabel(rects2)
autolabel(rects3)

# Plot Aesthetics
ax.set_title('Land Area Required for 100% CO₂ Offset\n(Bamboo vs. Tropical Forests)',
             fontsize=16, pad=20, fontweight='bold')
ax.set_xlabel('Country', fontsize=14)
ax.set_ylabel('Area (square miles) - Log Scale', fontsize=14)
ax.set_xticks(x)
ax.set_xticklabels(countries, fontsize=12)
ax.set_yscale('log')
ax.yaxis.set_major_formatter(FuncFormatter(lambda x, _: f'{x:,.0f}'))
ax.grid(True, which="both", ls="--", alpha=0.3)

# Professional Legend with Formulas
from matplotlib.lines import Line2D
legend_elements = [
    Line2D([0], [0], color=colors[0], lw=4, label='Bamboo (30 t/ha/yr)'),
    Line2D([0], [0], color=colors[1], lw=4, label='Forest (15 t/ha/yr)'),
    Line2D([0], [0], color=colors[2], lw=4, label='Actual Land Area'),
    Line2D([0], [0], color='white', label=
        r'$\text{Area} = \frac{\text{CO}_2\text{ Emissions}}{\text{Seq. Rate} \times 259}$'),
    Line2D([0], [0], color='white', label=
        r'$\text{Seq. Rate: Bamboo}=30\ \text{t/ha/yr},\ \text{Forest}=15\ \text{t/ha/yr}$')
]

ax.legend(handles=legend_elements, loc='upper right', 
          bbox_to_anchor=(1.35, 1), frameon=True,
          title='Carbon Sequestration Parameters:', title_fontsize=12)

# Add Key Insight
plt.figtext(0.5, 0.93, 
           "Key Insight: Bamboo requires 50% less land than forests for equivalent CO₂ offset",
           ha='center', fontsize=12, style='italic', 
           bbox=dict(facecolor='white', alpha=0.7))

plt.tight_layout()

# Save High-Resolution Image
plt.savefig('carbon_offset_comparison.png', dpi=300, bbox_inches='tight')
plt.show()