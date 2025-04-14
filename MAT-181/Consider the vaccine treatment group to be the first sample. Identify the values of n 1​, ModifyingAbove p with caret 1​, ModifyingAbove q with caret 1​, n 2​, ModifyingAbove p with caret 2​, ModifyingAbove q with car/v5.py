import matplotlib.pyplot as plt
import numpy as np

# Given data
n1 = 196249
disease_1 = 38
n2 = 193976
disease_2 = 146

# Calculating proportions
p1 = disease_1 / n1
q1 = 1 - p1
p2 = disease_2 / n2
q2 = 1 - p2

# Calculating pooled proportions
total_children = n1 + n2
total_disease = disease_1 + disease_2
p_bar = total_disease / total_children
q_bar = 1 - p_bar

# Proportions for visualization
labels = ['Developed Disease', 'Did Not Develop Disease']
treatment_group = [p1, q1]
placebo_group = [p2, q2]
pooled_group = [p_bar, q_bar]

x = np.arange(len(labels))

# Create subplots
fig, (ax1, ax2) = plt.subplots(2, 1, gridspec_kw={'height_ratios': [1, 3]}, sharex=True)

# Plotting the main bars for developed disease
bar_width = 0.3
ax1.bar(x - bar_width, treatment_group, width=bar_width, label='Treatment Group', align='center')
ax1.bar(x, placebo_group, width=bar_width, label='Placebo Group', align='center')
ax1.bar(x + bar_width, pooled_group, width=bar_width, label='Pooled Group', align='center')

# Adding labels and title
ax1.set_xticks(x)
ax1.set_xticklabels(labels)
ax1.set_ylabel('Proportion (Zoomed)')
ax1.set_title('Proportion of Children Developing Disease\n(Split Graph: 0.0001-0.0002 and 0.9-1)')
ax1.legend()

# Zoom in on the lower range
ax1.set_ylim(0, 0.0002)

# Plotting the main bars for did not develop disease
ax2.bar(x - bar_width, treatment_group, width=bar_width, align='center')
ax2.bar(x, placebo_group, width=bar_width, align='center')
ax2.bar(x + bar_width, pooled_group, width=bar_width, align='center')

# Adding labels and title
ax2.set_xticks(x)
ax2.set_xticklabels(labels)
ax2.set_ylabel('Proportion (Full Range)')
ax2.legend()

# Focus on the higher range
ax2.set_ylim(0.9, 1)

# Adding detailed annotations with larger text
for i, v in enumerate(treatment_group):
    ax1.text(i - bar_width, v + 0.00001, f"{v:.8f}", ha='center', fontweight='bold', fontsize=10)
    ax2.text(i - bar_width, v + 0.005, f"{v:.8f}", ha='center', fontweight='bold', fontsize=10)
for i, v in enumerate(placebo_group):
    ax1.text(i, v + 0.00001, f"{v:.8f}", ha='center', fontweight='bold', fontsize=10)
    ax2.text(i, v + 0.005, f"{v:.8f}", ha='center', fontweight='bold', fontsize=10)
for i, v in enumerate(pooled_group):
    ax1.text(i + bar_width, v + 0.00001, f"{v:.8f}", ha='center', fontweight='bold', fontsize=10)
    ax2.text(i + bar_width, v + 0.005, f"{v:.8f}", ha='center', fontweight='bold', fontsize=10)

# Adding imaginary lines for separation
ax1.axhline(y=0.0001, color='gray', linestyle='--')
ax1.axhline(y=0.0002, color='gray', linestyle='--')
ax2.axhline(y=0.9, color='gray', linestyle='--')
ax2.axhline(y=1, color='gray', linestyle='--')

# Display the plot
plt.tight_layout()
plt.show()
