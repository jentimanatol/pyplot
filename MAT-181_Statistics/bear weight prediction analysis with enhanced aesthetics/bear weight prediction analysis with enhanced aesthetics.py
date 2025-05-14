import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats
from matplotlib.patches import Ellipse
from matplotlib.transforms import Affine2D
import seaborn as sns


# Set professional style
#plt.style.use('seaborn-darkgrid')
plt.style.use('seaborn-v0_8-darkgrid')  # For seaborn styles in matplotlib 3.6+
plt.rcParams['font.family'] = 'DejaVu Sans'
plt.rcParams['mathtext.fontset'] = 'cm'
plt.rcParams['axes.titlepad'] = 20



# Data
chest = np.array([58, 50, 65, 59, 59, 48])
weight = np.array([414, 312, 499, 450, 456, 260])

# Calculate regression
slope, intercept, r_value, p_value, std_err = stats.linregress(chest, weight)
regression_line = intercept + slope * chest

# Prediction for 63 inches
pred_x = 63
pred_y = intercept + slope * pred_x

# Create figure
fig, ax = plt.subplots(figsize=(12, 8), dpi=120)

# Scatter plot with enhanced aesthetics
scatter = ax.scatter(chest, weight, c=weight, cmap='viridis', 
                    s=200, edgecolor='black', linewidth=1.5, 
                    zorder=5, label='Actual Data')

# Regression line with confidence interval
sns.regplot(x=chest, y=weight, scatter=False, 
           line_kws={'color':'#E74C3C', 'lw':3, 'ls':'--', 
                    'label':f'Regression: y = {intercept:.1f} + {slope:.1f}x'})

# Prediction point
ax.scatter(pred_x, pred_y, s=300, marker='*', color='gold', 
          edgecolor='black', linewidth=1, 
          label=f'Prediction (63"): {pred_y:.1f} lbs')

# Actual weight point
ax.scatter(pred_x, 552, s=300, marker='X', color='#3498DB', 
          edgecolor='black', linewidth=1, 
          label=f'Actual Weight: 552 lbs')

# Add equation and stats
eq_text = (f'$\\hat{{y}} = {intercept:.1f} + {slope:.1f}x$\n'
          f'$r = {r_value:.3f}$\n'
          f'$p = {p_value:.4f}$\n'
          f'$R^2 = {r_value**2:.3f}$')
ax.text(0.02, 0.98, eq_text, transform=ax.transAxes,
       ha='left', va='top', fontsize=12,
       bbox=dict(facecolor='white', alpha=0.8, edgecolor='gray'))

# Add residual lines
for xi, yi, yi_pred in zip(chest, weight, regression_line):
    ax.plot([xi, xi], [yi, yi_pred], 'k-', alpha=0.3, lw=1)

# Customize axes and title
ax.set_xlabel('Chest Size (inches)', fontsize=12, fontweight='bold')
ax.set_ylabel('Weight (pounds)', fontsize=12, fontweight='bold')
ax.set_title('Bear Weight Prediction from Chest Size\n'
            'Linear Regression Analysis', 
            fontsize=14, fontweight='bold', pad=20)

# Add grid and legend
ax.grid(True, alpha=0.3)
ax.legend(loc='lower right', framealpha=1)

# Add watermark
fig.text(0.5, 0.5, 'Anatolie Jentimir 2024', fontsize=20, 
        color='gray', alpha=0.1, ha='center', va='center', rotation=30)

# Add correlation interpretation
corr_strength = "Very Strong" if abs(r_value) > 0.8 else "Strong"
fig.text(0.7, 0.15, 
        f"Correlation Interpretation:\n"
        f"r = {r_value:.3f} ({corr_strength} {'Positive' if r_value > 0 else 'Negative'})",
        ha='center', va='center', fontsize=10,
        bbox=dict(facecolor='white', alpha=0.7))

# Add prediction error annotation
error = abs(pred_y - 552)
ax.annotate(f'Prediction Error: {error:.1f} lbs', 
           xy=(pred_x, (pred_y+552)/2), xytext=(10, 30),
           textcoords='offset points', ha='center',
           arrowprops=dict(arrowstyle='->', color='black'))

# Adjust layout
plt.tight_layout()
plt.savefig('bear_weight_regression.png', dpi=300, bbox_inches='tight')
plt.show()