import matplotlib.pyplot as plt

# Define the sample space of a six-sided die
sample_space = [1, 2, 3, 4, 5, 6]

# Define events
A = {2, 4, 6}  # Even numbers
B = {3, 4, 5, 6}  # Numbers greater than 2
A_and_B = A & B  # Intersection of A and B

# Probabilities
P_B = len(B) / len(sample_space)  # Probability of B
P_A_given_B = len(A_and_B) / len(B)  # Conditional probability P(A|B)
P_A_and_B = len(A_and_B) / len(sample_space)  # Probability of A ∩ B

# Data for plotting
labels = ['P(B): Event B', 'P(A ∩ B): Intersection', 'P(A|B): Conditional Probability']
values = [P_B, P_A_and_B, P_A_given_B]
colors = ['blue', 'green', 'purple']

# Create the bar plot
plt.bar(labels, values, color=colors, alpha=0.7, edgecolor='black')

# Add title and labels
plt.title('Visualization of Conditional Probability', fontsize=14)
plt.ylim(0, 1)
plt.ylabel('Probability', fontsize=12)

# Add legend
plt.legend(['Probabilities based on die rolls'], loc='upper left', fontsize=10)

# Annotate each bar with its value
for i, v in enumerate(values):
    plt.text(i, v + 0.02, f'{v:.2f}', ha='center', fontsize=10)

# Display the plot
plt.show()