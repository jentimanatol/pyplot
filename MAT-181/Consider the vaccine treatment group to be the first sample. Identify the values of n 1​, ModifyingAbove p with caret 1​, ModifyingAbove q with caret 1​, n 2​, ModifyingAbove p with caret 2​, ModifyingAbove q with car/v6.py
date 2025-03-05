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
fig, ax1 = plt.subplots()

# Plotting the bars for the full range
bar_width = 0.3
ax1.bar(x - bar_width, treatment_group, width=bar_width, label='Treatment Group', color='lightblue', align='center')
ax1.bar(x, placebo_group, width=bar_width, label='Placebo Group', color='lightgreen', align='center')
ax1.bar(x + bar_width, pooled_group, width=bar_width, label='Pooled Group', color='lightcoral', align='center')

# Adding labels and title
ax1.set_xticks(x)
ax1.set_xticklabels(labels)
ax1.set_ylabel('Proportion (Full Range)', color='blue')
ax1.set_title('Proportion of Children Developing Disease\n(Dual Axes for Detailed View)')
ax1.legend(loc='upper right')

# Creating a secondary axis for zoomed-in view
ax2 = ax1.twinx()
ax2.set_ylim(0, 0.0002)
ax2.set_ylabel('Proportion (Zoomed)', color='red')

# Plotting the bars for the zoomed-in range
ax2.bar(x - bar_width, treatment_group, width=bar_width, alpha=0.3, color='blue', align='center')
ax2.bar(x, placebo_group, width=bar_width, alpha=0.3, color='green', align='center')
ax2.bar(x + bar_width, pooled_group, width=bar_width, alpha=0.3, color='red', align='center')

# Adding detailed annotations
for i, v in enumerate(treatment_group):
    ax2.text(i - bar_width, v + 0.00001, f"{v:.8f}", ha='center', fontweight='bold', fontsize=10)
for i, v in enumerate(placebo_group):
    ax2.text(i, v + 0.00001, f"{v:.8f}", ha='center', fontweight='bold', fontsize=10)
for i, v in enumerate(pooled_group):
    ax2.text(i + bar_width, v + 0.00001, f"{v:.8f}", ha='center', fontweight='bold', fontsize=10)

# Adding imaginary lines for separation
ax2.axhline(y=0.0001, color='gray', linestyle='--')
ax2.axhline(y=0.0002, color='gray', linestyle='--')

# Display the plot
plt.tight_layout()
plt.show()
