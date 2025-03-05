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
