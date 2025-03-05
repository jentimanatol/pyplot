import matplotlib.pyplot as plt

# Given data
n1 = 197709
disease_1 = 37
n2 = 201132
disease_2 = 112

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
print(f"p_hat1 = {p1:.6f}")
print(f"q_hat1 = {q1:.6f}")
print(f"n2 = {n2}")
print(f"p_hat2 = {p2:.6f}")
print(f"q_hat2 = {q2:.6f}")
print(f"p_bar = {p_bar:.6f}")
print(f"q_bar = {q_bar:.6f}")

# Proportions for visualization
labels = ['Developed Disease', 'Did Not Develop Disease']
treatment_group = [p1, q1]
placebo_group = [p2, q2]

x = range(len(labels))

# Create subplots
fig, ax = plt.subplots()

# Plotting the bars
ax.bar(x, treatment_group, width=0.4, label='Treatment Group', align='center')
ax.bar(x, placebo_group, width=0.4, label='Placebo Group', align='edge')

# Adding labels
ax.set_xticks(x)
ax.set_xticklabels(labels)
ax.set_ylabel('Proportion')
ax.set_title('Proportion of Children Developing Disease in Treatment and Placebo Groups')
ax.legend()

# Display the plot
plt.show()
