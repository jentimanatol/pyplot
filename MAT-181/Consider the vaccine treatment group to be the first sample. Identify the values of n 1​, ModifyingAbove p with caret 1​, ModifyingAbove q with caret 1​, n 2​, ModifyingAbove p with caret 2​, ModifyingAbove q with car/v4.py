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
labels = ['Developed Disease']
treatment_group = [p1]
placebo_group = [p2]
pooled_group = [p_bar]

x = np.arange(len(labels))

# Create subplots
fig, ax1 = plt.subplots()

# Plotting the main bars for developed disease
bar_width = 0.3
bar1 = ax1.bar(x, treatment_group, width=bar_width, label='Treatment Group', align='center')
bar2 = ax1.bar(x + bar_width, placebo_group, width=bar_width, label='Placebo Group', align='center')
bar3 = ax1.bar(x + 2 * bar_width, pooled_group, width=bar_width, label='Pooled Group', align='center')

# Adding labels to primary y-axis
ax1.set_xticks(x + bar_width)
ax1.set_xticklabels(labels)
ax1.set_ylabel('Proportion')
ax1.set_title('Proportion of Children Developing Disease (Zoomed In and Full View)')
ax1.legend()

# Adding detailed annotations with larger text
for bar in [bar1, bar2, bar3]:
    for rect in bar:
        height = rect.get_height()
        ax1.text(rect.get_x() + rect.get_width() / 2., 1.05 * height,
                 f'{height:.8f}', ha='center', va='bottom', fontweight='bold', fontsize=10)

# Create a secondary y-axis that zooms in on the lower range (0 to 0.0002)
ax2 = ax1.twinx()
ax2.set_ylim(0, 0.0002)
ax2.set_ylabel('Zoomed Proportion')
ax2.grid(False)

# Adding imaginary lines for the zoomed range
ax1.axhline(y=0.0001, color='gray', linestyle='--')
ax1.axhline(y=0.0002, color='gray', linestyle='--')

# Display the plot
plt.show()
