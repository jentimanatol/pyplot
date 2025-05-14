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

# Data for plotting
labels = ['P(B)', 'P(A ∩ B)', 'P(A|B)']
values = [P_B, len(A_and_B) / len(sample_space), P_A_given_B]

# Create the bar plot
plt.bar(labels, values, color=['blue', 'green', 'purple'])
plt.title('Visualization of Conditional Probability')
plt.ylim(0, 1)
plt.ylabel('Probability')
plt.show()