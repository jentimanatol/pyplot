import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator
import os

# Data
x = np.array([0, 1, 2, 3, 4, 5])
p = np.array([0.031, 0.146, 0.323, 0.323, 0.146, 0.031])

# Calculate statistics
mu = np.sum(x * p)
sigma = np.sqrt(np.sum(x**2 * p) - mu**2)

# Create figure with higher DPI for better quality
plt.figure(figsize=(10, 6), facecolor='#f5f5f5', dpi=120)
ax = plt.axes(facecolor='#f5f5f5')

# Custom styling with improved color palette
colors = plt.cm.viridis(np.linspace(0.2, 0.8, len(x)))
bar_width = 0.7
edge_color = '#333333'

# Plot bars with enhanced gradient effect
for i, (xi, pi) in enumerate(zip(x, p)):
    gradient = np.linspace(0.8, 1.2, 15)  # More gradient steps for smoother look
    for g in gradient:
        alpha = 0.1 + 0.7 * (1 - abs(g-1))
        plt.bar(xi, pi, width=bar_width*g, color=colors[i], 
                alpha=alpha, edgecolor=edge_color, linewidth=0.7, zorder=2)

# Add mean and standard deviation lines with better visibility
plt.axvline(mu, color='#d62728', linestyle='--', linewidth=2.5, alpha=0.8, zorder=1)
plt.axvspan(mu-sigma, mu+sigma, color='#d62728', alpha=0.15, zorder=0)

# Enhanced annotations with shadow effect
shadow_props = dict(boxstyle='round,pad=0.5', facecolor='white', alpha=0.85,
                   edgecolor='none')

plt.text(mu, max(p)+0.035, f'μ = {mu:.1f}', ha='center', 
         color='#d62728', fontsize=13, weight='bold', bbox=shadow_props)
plt.text(mu+sigma+0.12, max(p)/2, f'σ = {sigma:.1f}', 
         color='#d62728', fontsize=13, rotation=90, va='center', bbox=shadow_props)

# Distribution formulas with improved layout  used -$formula$ to visualise formula as in matlab
formula_text = r'$\text{PMF: } P(X=k)$' + '\n\n' + \
               r'$\mu = E[X] = \sum x_i P(x_i)$' + '\n' + \
               f'$\ \ = {mu:.1f}$' + '\n\n' + \
               r'$\sigma = \sqrt{E[X^2] - \mu^2}$' + '\n' + \
               r'$\ \ = \sqrt{\sum x_i^2 P(x_i) - \mu^2}$' + '\n' + \
               f'$\ \ = {sigma:.1f}$'

plt.text(5.5, 0.27, formula_text, fontsize=12, bbox=dict(facecolor='white', 
        alpha=0.9, edgecolor='#cccccc', boxstyle='round,pad=0.8'))

# Customize plot with professional touches
plt.title('Probability Distribution of X-linked Disorder Inheritance\n', 
          fontsize=15, weight='bold', pad=20, color='#333333')
plt.xlabel('Number of Affected Children', fontsize=13, labelpad=12, color='#333333')
plt.ylabel('Probability', fontsize=13, labelpad=12, color='#333333')
plt.xticks(x, fontsize=12)
plt.yticks(fontsize=11)
plt.ylim(0, 0.37)
plt.grid(axis='y', linestyle=':', alpha=0.4, color='gray')

# Remove spines and adjust layout
for spine in ['top', 'right']:
    ax.spines[spine].set_visible(False)
ax.spines['bottom'].set_color('#666666')
ax.spines['left'].set_color('#666666')

# Make x-axis integers only
ax.xaxis.set_major_locator(MaxNLocator(integer=True))

# Add subtle watermark
plt.text(0.95, 0.02, '© Anatolie Jentimir 2024', transform=ax.transAxes,
         fontsize=9, color='gray', alpha=0.5, ha='right')

plt.tight_layout()

# Save the figure (this is the new line)
output_path = os.path.join(os.getcwd(), 'genetic_disorder_probability_distribution.png')
plt.savefig(output_path, dpi=300, bbox_inches='tight', facecolor=ax.get_facecolor())
print(f"Graph saved successfully at: {output_path}")

plt.show()