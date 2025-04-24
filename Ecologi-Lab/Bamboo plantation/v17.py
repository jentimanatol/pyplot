import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib.ticker import FuncFormatter

# Data from table
countries = ["Jamaica", "Madagascar", "Vietnam"]
bamboo_area = np.array([883, 2678, 34377])
forest_area = np.array([1766, 5356, 68754])
land_area = np.array([4244, 226597, 127882])

# Visualization setup
plt.figure(figsize=(14, 8))
sns.set_style("whitegrid")
colors = sns.color_palette("husl", 3)

# Create grouped bars
bar_width = 0.25
x = np.arange(len(countries))
bars_bamboo = plt.bar(x - bar_width, bamboo_area, width=bar_width, 
                     color=colors[0], edgecolor='black', label='Bamboo Needed')
bars_forest = plt.bar(x, forest_area, width=bar_width,
                     color=colors[1], edgecolor='black', label='Forest Needed')
bars_land = plt.bar(x + bar_width, land_area, width=bar_width,
                   color=colors[2], edgecolor='black', label='Actual Land')

# Annotate bars with values
def annotate_bars(bars):
    for bar in bars:
        height = bar.get_height()
        plt.text(bar.get_x() + bar.get_width()/2., height*1.02,
                f'{height:,.0f}', ha='center', va='bottom', fontsize=9)

annotate_bars(bars_bamboo)
annotate_bars(bars_forest)
annotate_bars(bars_land)

# Aesthetics
plt.title('Land Area Requirements for 100% CO₂ Offset', fontsize=16, pad=20)
plt.xlabel('Country', fontsize=14)
plt.ylabel('Area (square miles) - Log Scale', fontsize=14)
plt.xticks(x, countries)
plt.yscale('log')
plt.gca().yaxis.set_major_formatter(FuncFormatter(lambda x, _: f'{x:,.0f}'))

# Professional legend with formulas
legend_elements = [
    plt.Line2D([0], [0], color=colors[0], lw=4, label='Bamboo (30 t/ha/yr)'),
    plt.Line2D([0], [0], color=colors[1], lw=4, label='Forest (15 t/ha/yr)'),
    plt.Line2D([0], [0], color=colors[2], lw=4, label='Actual Land Area'),
    plt.Line2D([0], [0], color='white', label=
        r'$\text{Area} = \frac{\text{CO}_2\text{ Emissions}}{\text{Seq. Rate} \times 259}$')
]

plt.legend(handles=legend_elements, loc='upper right', 
          bbox_to_anchor=(1.35, 1), title='Calculation Parameters:')

# Add key insight
plt.figtext(0.5, 0.93, 
           "Key Insight: Bamboo requires 50% less land than forests for equivalent CO₂ offset",
           ha='center', fontsize=12, bbox=dict(facecolor='white', alpha=0.7))

plt.tight_layout()
plt.savefig('carbon_offset_comparison.png', dpi=300, bbox_inches='tight')
plt.show()