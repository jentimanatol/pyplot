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

# Add title and labels
plt.title('Conditional Probability: P(Heart | Red)', fontsize=14)
plt.ylim(0, 1)
plt.ylabel('Probability', fontsize=12)

# Add legend
plt.legend(['P(Red) = Total Red Cards / Total Cards\nP(Heart | Red) = Number of Hearts / Total Red Cards'], loc='upper left', fontsize=10)

# Annotate bars with values
for i, v in enumerate(values):
    plt.text(i, v + 0.02, f'{v:.2f}', ha='center', fontsize=10)

# Add description
plt.text(-0.5, -0.2, 
         "The plot visualizes:\n1. P(Red): Probability of drawing a red card from the deck.\n"
         "2. P(Heart | Red): Conditional probability of drawing a heart, given the card is red.\n"
         "Formulas:\nP(Red) = Total Red Cards / Total Cards\nP(Heart | Red) = Number of Hearts / Total Red Cards", 
         fontsize=10, ha='left', va='top')

# Display the plot
plt.show()