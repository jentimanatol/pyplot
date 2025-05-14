import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

# Data from the problem
n = 1180
p_hat = 0.88
p_null = 0.94
z_score = -8.70
alpha = 0.05  # typical significance level

# Calculate standard error and CI
se = np.sqrt(p_null * (1 - p_null) / n)
ci_lower = p_hat - norm.ppf(1 - alpha/2) * se
ci_upper = p_hat + norm.ppf(1 - alpha/2) * se

# Create figure with artistic style
plt.figure(figsize=(12, 8))

# Use available style - first check what's available
print("Available styles:", plt.style.available)
plt.style.use('ggplot')  # Using a commonly available style

# Main plot - normal distribution
x = np.linspace(0.85, 0.99, 500)
y = norm.pdf(x, loc=p_null, scale=se)
plt.plot(x, y, color='#3498db', linewidth=3, 
         label=f'Null Distribution\n$p_0 = {p_null:.2f}$\n$SE = {se:.4f}$')

# Add test statistic marker (fixed escape sequence)
plt.axvline(x=p_hat, color='#e74c3c', linestyle='--', linewidth=2,
           label=fr'Sample Proportion\n$\hat{{p}} = {p_hat:.2f}$\n$z = {z_score:.2f}$')

# Add confidence interval
plt.axvspan(ci_lower, ci_upper, color='#2ecc71', alpha=0.2,
           label=f'95% Confidence Interval\n({ci_lower:.3f}, {ci_upper:.3f})')

# Add critical region (one-tailed)
critical_value = norm.ppf(alpha)
critical_x = np.linspace(0.85, p_null + critical_value * se, 100)
critical_y = norm.pdf(critical_x, loc=p_null, scale=se)
plt.fill_between(critical_x, critical_y, color='#e74c3c', alpha=0.3,
               label=f'Rejection Region\n(α = {alpha:.2f})')

# Add formulas and explanations
formula_text = (
    r'$\bf{Hypothesis\ Test:}$' + '\n' +
    r'$H_0: p = 0.94$' + '\n' +
    r'$H_1: p < 0.94$' + '\n\n' +
    r'$\bf{Test\ Statistic:}$' + '\n' +
    r'$z = \frac{\hat{p} - p_0}{\sqrt{\frac{p_0(1-p_0)}{n}}} = \frac{0.88-0.94}{\sqrt{\frac{0.94 \times 0.06}{1180}}} \approx -8.70$'
)

plt.text(0.02, 0.7, formula_text, fontsize=12, transform=plt.gca().transAxes,
         bbox=dict(facecolor='white', alpha=0.9, edgecolor='gray'))

# Styling
plt.title('Hypothesis Test for Cell Phone Ownership\n'
          'Claim: Fewer than 94% of adults have a cell phone',
          fontsize=14, pad=20)
plt.xlabel('Proportion of Adults with Cell Phones', fontsize=12)
plt.ylabel('Probability Density', fontsize=12)
plt.legend(loc='upper left', framealpha=1)
plt.grid(True, alpha=0.3)

# Add watermark
plt.text(0.5, 0.5, 'Statistical Analysis\nby Python', fontsize=40, 
         color='gray', alpha=0.1, ha='center', va='center', 
         rotation=30, transform=plt.gca().transAxes)

# Add z-score annotation
plt.annotate(f'Extremely low z-score ({z_score:.2f})\nStrong evidence against H0',
             xy=(p_hat, 0), xytext=(0.87, 10),
             arrowprops=dict(arrowstyle="->", color='#34495e'),
             bbox=dict(boxstyle="round", fc="w"))

plt.tight_layout()
plt.savefig('cell_phone_hypothesis_test.png', dpi=300, bbox_inches='tight')
plt.show()