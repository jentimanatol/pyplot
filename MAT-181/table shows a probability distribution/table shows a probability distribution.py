import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator

# Data
x = np.array([0, 1, 2, 3, 4, 5])
p = np.array([0.031, 0.146, 0.323, 0.323, 0.146, 0.031])

# Calculate statistics
mu = np.sum(x * p)
sigma = np.sqrt(np.sum(x**2 * p) - mu**2)

# Create figure
plt.figure(figsize=(10, 6), facecolor='#f5f5f5')
ax = plt.axes(facecolor='#f5f5f5')

# Custom styling
colors = ['#4e79a7', '#f28e2b', '#e15759', '#76b7b2', '#59a14f', '#edc948']
bar_width = 0.7
edge_color = '#333333'

# Plot bars with gradient effect
for i, (xi, pi) in enumerate(zip(x, p)):
    gradient = np.linspace(0.8, 1.2, 10)
    for g in gradient:
        alpha = 0.1 + 0.7 * (1 - abs(g-1))
        plt.bar(xi, pi, width=bar_width*g, color=colors[i], 
                alpha=alpha, edgecolor=edge_color, linewidth=0.5)

# Add mean and standard deviation lines
plt.axvline(mu, color='#d62728', linestyle='--', linewidth=2, alpha=0.7)
plt.axvspan(mu-sigma, mu+sigma, color='#d62728', alpha=0.1)

# Annotations
plt.text(mu, max(p)+0.03, f'μ = {mu:.1f}', ha='center', 
         color='#d62728', fontsize=12, weight='bold')
plt.text(mu+sigma+0.1, max(p)/2, f'σ = {sigma:.1f}', 
         color='#d62728', fontsize=12, rotation=90, va='center')

# Distribution formulas
formula_text = r'$P(X=k)$ - Probability Mass Function' + '\n' + \
               r'$\mu = \sum_{i} x_i P(x_i) = ' + f'{mu:.1f}$' + '\n' + \
               r'$\sigma = \sqrt{\sum_{i} x_i^2 P(x_i) - \mu^2} = ' + f'{sigma:.1f}$'

plt.text(5.3, 0.25, formula_text, fontsize=12, bbox=dict(facecolor='white', 
        alpha=0.8, edgecolor='gray', boxstyle='round,pad=0.5'))

# Customize plot
plt.title('X-linked Genetic Disorder Inheritance Probability\n', 
          fontsize=14, weight='bold', pad=20)
plt.xlabel('Number of Children Inheriting Disorder', fontsize=12, labelpad=10)
plt.ylabel('Probability', fontsize=12, labelpad=10)
plt.xticks(x)
plt.ylim(0, 0.35)
plt.grid(axis='y', linestyle='--', alpha=0.3)

# Remove spines
for spine in ['top', 'right']:
    ax.spines[spine].set_visible(False)

# Make x-axis integers only
ax.xaxis.set_major_locator(MaxNLocator(integer=True))

plt.tight_layout()
plt.show()