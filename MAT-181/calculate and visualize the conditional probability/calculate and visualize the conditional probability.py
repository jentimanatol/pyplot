# Python program to calculate and visualize the conditional probability

import matplotlib.pyplot as plt

# Define the total cards in the deck and the subsets
total_cards = 52
total_red_cards = 26  # 13 hearts + 13 diamonds
total_hearts = 13
hearts_given_red = 13  # All hearts are red

# Calculate probabilities
P_red = total_red_cards / total_cards  # Probability of drawing a red card
P_heart_given_red = hearts_given_red / total_red_cards  # Conditional probability P(Heart | Red)

# Print the results
print("Probability of drawing a red card (P(Red)):", P_red)
print("Conditional probability of drawing a heart given the card is red (P(Heart | Red)):", P_heart_given_red)

# Visualization of the probabilities
labels = ['P(Red)', 'P(Heart | Red)']
values = [P_red, P_heart_given_red]
colors = ['red', 'pink']

# Create the bar plot
plt.bar(labels, values, color=colors, alpha=0.7, edgecolor='black')
plt.ylim(0, 1)
plt.title('Conditional Probability Visualization: P(Heart | Red)', fontsize=14)
plt.ylabel('Probability', fontsize=12)

# Annotate bars with values
for i, v in enumerate(values):
    plt.text(i, v + 0.02, f'{v:.2f}', ha='center', fontsize=10)

# Display the plot
plt.show()