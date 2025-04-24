import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

# Configure seaborn aesthetics
sns.set(style="whitegrid", font_scale=1.2)

# Data for each problem
problem_labels = [
    "P1: Defect Rate",
    "P2: Voter %",
    "P3: Incumbent Support",
    "P4: GP Students",
    "P5: Asthma in Kids",
    "P6: Fax Defects",
    "P7: Female Weight (High s)",
    "P8: Salary",
    "P9: Female Weight (Low s)"
]
z_or_t_stats = [2.35, -1.23, -1.60, 1.02, -0.567, -0.415, 0.157, -2.238, 1.574]
p_values = [0.0094, 0.1093, 0.1096, 0.1539, 0.5686, 0.3409, 0.8764, 0.0412, 0.1312]

# Set color palette for visual distinction
colors = sns.color_palette("husl", len(problem_labels))

fig, ax = plt.subplots(figsize=(14, 8))

# Plot z/t-statistics as bars
bars = ax.barh(problem_labels, z_or_t_stats, color=colors, edgecolor='black')

# Add P-value annotations
for i, (bar, pval) in enumerate(zip(bars, p_values)):
    width = bar.get_width()
    ax.text(width + 0.1 if width > 0 else width - 0.8,
            bar.get_y() + bar.get_height() / 2,
            f"P = {pval:.4f}",
            va='center',
            color='black',
            fontweight='bold')

# Customize axis labels and title
ax.set_xlabel("Z / T Statistic Value")
ax.set_title("Hypothesis Test Statistics and P-values for Chapter 8 Problems")

# Add vertical reference line at 0
ax.axvline(0, color='gray', linestyle='--')

# Add watermark
fig.text(0.95, 0.02, 'MAT 181 Chapter 8', fontsize=12,
         color='gray', ha='right', va='bottom', alpha=0.5, rotation=0)

# Add formula display (manual visual)
plt.figtext(0.5, -0.08, "Z = (\u0302p - p0) / sqrt(p0(1-p0)/n),  T = (x̄ - \u03bc0) / (s / sqrt(n))",
            wrap=True, horizontalalignment='center', fontsize=10, color='darkblue')

plt.tight_layout()
plt.show()
