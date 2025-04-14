import matplotlib.pyplot as plt

# Data for visualization
labels = ['Even & Red', 'Odd & Red', 'Black or Green']
sizes = [6, 12, 19]  # 6 even red, 12 odd red, 19 black or green
colors = ['red', 'darkred', 'black']
explode = (0.1, 0, 0)  # explode the even & red section for emphasis

# Create the pie chart
plt.figure(figsize=(8, 6))
plt.pie(sizes, labels=labels, autopct='%1.1f%%', colors=colors, explode=explode, startangle=140, shadow=True)
plt.title("Conditional Probability of Even Number Given Red Pocket")

# Add description and formula
description = ("Example of a standard roulette wheel (European version) with 37 pockets: "
               "18 red, 18 black, and 1 green. The numbers range from 1 to 36, "
               "with half being even and the other half odd. Among the red pockets, "
               "some contain even numbers and some contain odd numbers.\n\n"
               "The pie chart represents the probability distribution across all possible "
               "outcomes. The percentages in the chart show the overall probability of landing "
               "on a red even number, a red odd number, or a non-red number (black/green). "
               "However, when considering only the red pockets, we apply conditional probability.\n\n"
               "Conditional Probability Formula:\n"
               "P(A | B) = P(A ∩ B) / P(B) = 6/18 = 1/3 ≈ 33.3%\n\n"
               "This means that if we already know the ball landed on a red pocket, the chance "
               "that it is also an even number is 33.3%.")

# Display the chart
plt.figtext(0.5, -0.05, description, wrap=True, horizontalalignment='center', fontsize=10, bbox={"facecolor": "white", "alpha": 0.6, "pad": 5})
plt.show()
