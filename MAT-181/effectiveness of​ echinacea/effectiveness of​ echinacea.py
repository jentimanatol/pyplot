import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib.patches import Ellipse
from matplotlib.transforms import Affine2D

# Set style
sns.set(style="whitegrid", font_scale=1.2)
plt.rcParams['font.family'] = 'DejaVu Sans'
plt.rcParams['mathtext.fontset'] = 'cm'

# Data
groups = ['Echinacea', 'Placebo']
infected = [40, 91]
total = [47, 104]
rates = [i/t for i,t in zip(infected, total)]
ci_low, ci_high = -0.182, 0.134

# Create figure
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 8), gridspec_kw={'width_ratios': [1, 1.5]})

# ========== Left Plot: Infection Rates ==========
# Bar plot with error bars
bars = ax1.bar(groups, rates, width=0.6, 
               color=['#4c72b0', '#dd8452'], 
               edgecolor='black', linewidth=1.5)

# Add exact percentages on bars
for bar, rate in zip(bars, rates):
    height = bar.get_height()
    ax1.text(bar.get_x() + bar.get_width()/2., height-0.05,
             f'{rate*100:.1f}%', ha='center', va='top',
             color='white', fontweight='bold', fontsize=14)

# Add statistical details
ax1.text(0.5, 0.95, 
         f'z = -0.40\np = 0.689\nα = 0.01', 
         transform=ax1.transAxes, ha='center',
         bbox=dict(facecolor='white', edgecolor='gray', boxstyle='round'))

ax1.set_ylim(0, 1)
ax1.set_ylabel('Infection Rate', fontweight='bold')
ax1.set_title('Rhinovirus Infection Rates\nby Treatment Group', 
              fontsize=16, pad=20, fontweight='bold')

# ========== Right Plot: Confidence Interval ==========
# Draw the confidence interval
ax2.axhline(0, color='black', linestyle='--', alpha=0.5)
ci_line = ax2.hlines(0, ci_low, ci_high, 
                    colors='#55a868', linewidth=8, alpha=0.7)
ax2.scatter([0], [0], color='#55a868', s=200, zorder=5)

# Add interval markers
ax2.scatter([ci_low, ci_high], [0, 0], color='#55a868', s=100)
ax2.text(ci_low-0.02, 0.1, f'{ci_low:.3f}', ha='right', va='center')
ax2.text(ci_high+0.02, 0.1, f'{ci_high:.3f}', ha='left', va='center')

# Add interpretation
ax2.text(0.5, 0.8, '99% Confidence Interval\nfor Difference in Proportions',
         transform=ax2.transAxes, ha='center', fontsize=14)
ax2.text(0.5, 0.7, r'$(p_1 - p_2) \in (-0.182, 0.134)$',
         transform=ax2.transAxes, ha='center', fontsize=14)
ax2.text(0.5, 0.6, 'Includes zero → No significant effect',
         transform=ax2.transAxes, ha='center', fontstyle='italic')

ax2.set_xlim(-0.25, 0.25)
ax2.set_ylim(-0.5, 0.5)
ax2.set_yticks([])
ax2.set_xlabel('Difference in Infection Rates (Echinacea - Placebo)', 
               fontweight='bold')
ax2.set_title('Effect Size Estimation', fontsize=16, pad=20, fontweight='bold')

# ========== Common Elements ==========
# Add formula annotation
formula_text = r'$z = \frac{\hat{p}_1 - \hat{p}_2}{\sqrt{\hat{p}(1-\hat{p})(\frac{1}{n_1}+\frac{1}{n_2})}}$'
fig.text(0.25, 0.05, formula_text, ha='center', fontsize=14, 
         bbox=dict(facecolor='white', edgecolor='lightgray'))

# Add conclusion
conclusion = "Conclusion: Echinacea does not appear to have\n" + \
             "a significant effect on rhinovirus infection rates"
fig.text(0.75, 0.05, conclusion, ha='center', fontsize=14, 
         bbox=dict(facecolor='#ffd700', alpha=0.3, edgecolor='gold'))

# Add watermark
fig.text(0.5, 0.5, 'STATS\nVISUALIZATION', 
         fontsize=120, color='gray', alpha=0.1,
         ha='center', va='center', rotation=30)

# Add decorative elements
for ax in [ax1, ax2]:
    # Add light grid
    ax.grid(True, which='major', linestyle=':', linewidth=0.7, alpha=0.3)
    
    # Add bounding box
    for spine in ax.spines.values():
        spine.set_edgecolor('gray')
        spine.set_linewidth(1.5)

# Adjust layout
plt.tight_layout()
plt.subplots_adjust(bottom=0.2)

# Save and show
plt.savefig('echinacea_study.png', dpi=300, bbox_inches='tight')
plt.show()