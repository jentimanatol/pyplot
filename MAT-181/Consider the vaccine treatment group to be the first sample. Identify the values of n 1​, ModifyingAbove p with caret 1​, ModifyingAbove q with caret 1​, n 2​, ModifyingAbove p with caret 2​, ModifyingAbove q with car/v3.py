import matplotlib.pyplot as plt

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

# Print the calculated values
print(f"n1 = {n1}")
print(f"p_hat1 = {p1:.8f}")
print(f"q_hat1 = {q1:.8f}")
print(f"n2 = {n2}")
print(f"p_hat2 = {p2:.8f}")
print(f"q_hat2 = {q2:.8f}")
print(f"p_bar = {p_bar:.8f}")
print(f"q_bar = {q_bar:.8f}")

# Proportions for visualization
labels = ['Developed Disease', 'Did Not Develop Disease']
treatment_group = [p1, q1]
placebo_group = [p2, q2]
pooled_group = [p_bar, q_bar]

x = range(len(labels))

# Create subplots
fig, ax = plt.subplots()

# Plotting the bars
bar_width = 0.3
ax.bar(x, treatment_group, width=bar_width, label='Treatment Group', align='center')
ax.bar([i + bar_width for i in x], placebo_group, width=bar_width, label='Placebo Group', align='center')
ax.bar([i + 2 * bar_width for i in x], pooled_group, width=bar_width, label='Pooled Group', align='center')

# Adding labels
ax.set_xticks([i + bar_width for i in x])
ax.set_xticklabels(labels)
ax.set_ylabel('Proportion')
ax.set_title('Proportion of Children Developing Disease in Treatment, Placebo, and Pooled Groups')
ax.legend()

# Adding detailed annotations
for i, v in enumerate(treatment_group):
    ax.text(i - bar_width / 2, v + 0.00002, f"{v:.8f}", ha='center', fontweight='bold')
for i, v in enumerate(placebo_group):
    ax.text(i + bar_width / 2, v + 0.00002, f"{v:.8f}", ha='center', fontweight='bold')
for i, v in enumerate(pooled_group):
    ax.text(i + 1.5 * bar_width, v + 0.00002, f"{v:.8f}", ha='center', fontweight='bold')

# Display the plot
plt.show()

