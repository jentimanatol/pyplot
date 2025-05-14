import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import matplotlib.colors as mcolors

# Data based on the sample proportions and their probabilities
proportions = [0, 0.5, 1]
probabilities = [4/9, 4/9, 1/9]

# Set the style
sns.set(style="whitegrid")
plt.rcParams['font.family'] = 'DejaVu Serif'  # Modern serif font for elegance

# Create the plot
fig, ax = plt.subplots(figsize=(10, 6))

# Create bars (initial color will be replaced by gradient)
bars = ax.bar(proportions, probabilities, color='gray', width=0.1, edgecolor='black')

# Apply gradient colors to bars
gradient_colors = sns.color_palette("viridis", n_colors=3)
for bar, color in zip(bars, gradient_colors):
    bar.set_color(color)
    bar.set_linewidth(1)
    bar.set_linestyle('-')
    bar.set_capstyle('round')
    bar.set_joinstyle('round')

# Annotate bars with probability values
for bar, prob in zip(bars, probabilities):
    yval = bar.get_height()
    ax.text(bar.get_x() + bar.get_width()/2.0, yval + 0.01, f"{prob:.2f}", ha='center', va='bottom', fontsize=12)

# Titles and labels
plt.title("Sampling Distribution of Proportion of Even Numbers\nPopulation = {3, 4, 7}", fontsize=16, pad=20)
plt.xlabel(r"Proportion of Even Numbers in Sample ($x$)", fontsize=14)
plt.ylabel(r"Probability $P(x)$", fontsize=14)

# Formulas on the plot
formulas = (
    r"Population\ Proportion = \frac{1}{3} \approx 0.333",
    r"Mean\ of\ Sample\ Proportion = \sum (x \times P(x))",
    r"= (0)(\frac{4}{9}) + (0.5)(\frac{4}{9}) + (1)(\frac{1}{9})",
    r"= \frac{3}{9} = 0.333",
    r"Since\ \bar{p} = p,\ \text{the\ estimator\ is\ unbiased.}"
)

# Place formulas as text box
props = dict(boxstyle='round', facecolor='white', alpha=0.9)
textstr = '\n'.join(formulas)
ax.text(1.05, 0.8, textstr, transform=ax.transAxes, fontsize=12,
        verticalalignment='top', bbox=props)

# Add legend manually
labels = ["Proportion = 0", "Proportion = 0.5", "Proportion = 1"]
handles = [plt.Rectangle((0,0),1,1, color=color) for color in gradient_colors]
ax.legend(handles, labels, title="Sample Proportions", bbox_to_anchor=(1.05, 0.5), loc='center left')

# Tidy layout
plt.tight_layout()

# Save high-resolution version with transparent background
plt.savefig("sampling_distribution_proportion.png", dpi=600, transparent=True)

# Show plot
plt.show()
