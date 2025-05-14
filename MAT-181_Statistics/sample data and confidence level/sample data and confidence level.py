import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

# Given data
n = 966
x = 585
confidence_level = 0.90
p_hat = x / n
z_critical = norm.ppf(1 - (1 - confidence_level)/2)
margin_error = z_critical * np.sqrt((p_hat * (1 - p_hat)) / n)
ci_lower = p_hat - margin_error
ci_upper = p_hat + margin_error

plt.figure(figsize=(12, 8))
plt.style.use('seaborn')

# Main plot
x_vals = np.linspace(0.5, 0.7, 500)
y_vals = norm.pdf(x_vals, loc=p_hat, scale=np.sqrt((p_hat * (1 - p_hat)) / n))
plt.plot(x_vals, y_vals, color='#3498db', linewidth=3)

# Confidence interval visualization
plt.axvline(x=ci_lower, color='#e74c3c', linestyle='--', linewidth=2)
plt.axvline(x=ci_upper, color='#e74c3c', linestyle='--', linewidth=2)
plt.axvspan(ci_lower, ci_upper, color='#e74c3c', alpha=0.1)

# Improved formula rendering
formula_text = (
    r'$\mathbf{Confidence\ Interval:}$' + '\n' +
    r'$\hat{p} \pm z_{\alpha/2}\sqrt{\frac{\hat{p}(1-\hat{p})}{n}}$' + '\n\n' +
    r'$\hat{p} = \frac{x}{n} = \frac{585}{966} \approx 0.606$' + '\n' +
    r'$z_{0.05} = 1.645$' + '\n' +
    r'$E = 1.645 \times \sqrt{\frac{0.606 \times 0.394}{966}} \approx 0.026$'
)

plt.text(0.02, 0.95, formula_text, fontsize=12, transform=plt.gca().transAxes,
         bbox=dict(facecolor='white', alpha=0.9, edgecolor='gray'))

# Legend with raw strings
plt.legend([
    r'Normal distribution $\mathcal{N}(\hat{p}, \sqrt{\hat{p}(1-\hat{p})/n})$',
    f'90% Confidence Bounds ({ci_lower:.3f}, {ci_upper:.3f})',
    f'Point estimate $\hat{{p}} = {p_hat:.3f}$'
], loc='upper right')

plt.title('Confidence Interval for Population Proportion')
plt.xlabel('Proportion (p)')
plt.ylabel('Probability Density')

# Watermark
plt.text(0.5, 0.5, 'Anatolie Jentimir 2023', fontsize=40, color='gray',
         alpha=0.1, ha='center', va='center', rotation=30,
         transform=plt.gca().transAxes)

plt.tight_layout()
plt.savefig('confidence_interval.png', dpi=300, bbox_inches='tight')
plt.show()

# instal:  pip install matplotlib seaborn 