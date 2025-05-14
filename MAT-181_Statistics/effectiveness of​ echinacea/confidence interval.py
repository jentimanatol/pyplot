import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Ellipse
from matplotlib.offsetbox import AnchoredText
from scipy.stats import norm

# Data from the problem
p1 = 40/47  # Echinacea group
p2 = 91/104  # Placebo group
n1, n2 = 47, 104
diff = p1 - p2
se = np.sqrt(p1*(1-p1)/n1 + p2*(1-p2)/n2)
z_critical = norm.ppf(0.995)  # 99% CI
ci_lower = diff - z_critical * se
ci_upper = diff + z_critical * se

# Create figure with enhanced aesthetics
plt.figure(figsize=(12, 6), dpi=120)
ax = plt.gca()

# Set background color
ax.set_facecolor('#f5f5f5')
plt.grid(True, linestyle='--', alpha=0.7)

# Confidence interval visualization
plt.errorbar(diff, 0, xerr=[[diff - ci_lower], [ci_upper - diff]], 
             fmt='o', markersize=10, color='#e63946', 
             ecolor='#457b9d', elinewidth=3, capsize=10, capthick=3,
             label='Difference with 99% CI')

# Reference line at zero
plt.axvline(x=0, color='#2a9d8f', linestyle='--', linewidth=2, alpha=0.7)

# Add distribution curve
x = np.linspace(ci_lower - 0.1, ci_upper + 0.1, 500)
y = norm.pdf(x, loc=diff, scale=se) * 0.5
plt.plot(x, y, color='#1d3557', linewidth=2.5, alpha=0.7)

# Fill the confidence area
plt.fill_between(x, y, where=((x >= ci_lower) & (x <= ci_upper)), 
                color='#a8dadc', alpha=0.4, label='99% Confidence Region')

# # Add formula annotations
# formula_text = r'$\hat{p}_1 - \hat{p}_2 = %.3f$' % diff + '\n' + \
#                r'$SE = \sqrt{\frac{\hat{p}_1(1-\hat{p}_1)}{n_1} + \frac{\hat{p}_2(1-\hat{p}_2)}{n_2}} = %.3f$' % se + '\n' + \
#                r'$CI_{99\%} = %.3f \pm %.3f$' % (diff, z_critical*se)

formula_text = (fr'$\hat{{p}}_1 - \hat{{p}}_2 = {diff:.3f}$' + '\n' + 
               fr'$SE = \sqrt{{\frac{{\hat{{p}}_1(1-\hat{{p}}_1)}}{{n_1}} + \frac{{\hat{{p}}_2(1-\hat{{p}}_2)}}{{n_2}}}} = {se:.3f}$' + '\n' + 
               fr'$CI_{{99\%}} = {diff:.3f} \pm {z_critical*se:.3f}$')



plt.annotate(formula_text, xy=(0.02, 0.85), xycoords='axes fraction', 
             bbox=dict(boxstyle='round', facecolor='white', alpha=0.8),
             fontsize=10, fontfamily='monospace')

# Add statistical conclusion
conclusion_text = f'CI includes 0 ({ci_lower:.3f}, {ci_upper:.3f})\n' + \
                  'Fail to reject null hypothesis\n' + \
                  'No significant effect found'
anchored_text = AnchoredText(conclusion_text, loc='upper right', 
                            frameon=True, prop=dict(size=10))
ax.add_artist(anchored_text)

# Add watermark
plt.text(0.95, 0.05, 'STATS VISUALIZATION', transform=ax.transAxes,
         fontsize=30, color='gray', alpha=0.2, ha='right', va='bottom',
         rotation=15, fontweight='bold')

# Customize axes and title
plt.title('Effect of Echinacea on Rhinovirus Infections\n99% Confidence Interval Analysis', 
          pad=20, fontsize=14, fontweight='bold')
plt.xlabel('Difference in Infection Rates (Echinacea - Placebo)', labelpad=10)
plt.yticks([])
plt.xlim(ci_lower - 0.1, ci_upper + 0.1)
plt.ylim(-0.05, max(y) + 0.05)

# Add legend with custom location
plt.legend(loc='upper center', bbox_to_anchor=(0.5, -0.15), 
           ncol=2, framealpha=0.9)

# Add decorative elements
ellipse = Ellipse((diff, max(y)/2), width=ci_upper-ci_lower, height=max(y)/3, 
                 angle=0, color='#457b9d', alpha=0.1)
ax.add_patch(ellipse)

plt.tight_layout()
plt.show()