import matplotlib.pyplot as plt

# Data for visualization
labels = ['Even & Red', 'Odd & Red', 'Black or Green']
sizes = [6, 12, 19]  # 6 even red, 12 odd red, 19 black or green
colors = ['red', 'darkred', 'black']
explode = (0.1, 0, 0)  # explode the even & red section for emphasis

# Create the pie chart
plt.figure(figsize=(8, 6))
plt.pie(sizes, labels=labels, autopct='%1.1f%%', colors=colors, explode=explode, startangle=140, shadow=True)
plt.title("Conditional Probability of Even Number Given Red Pocket By Anatolie Jentimir")

# Add description and formula
description = ("Exemple of standard roulette wheel (European version) has 37 pockets:"
               "18 red, 18 black, and 1 green. The numbers are 1-36, with half "
                "of them being even and the other half being odd. "
                "This pie chart visualizes the probability distribution of landing on "
               "an even number given that the ball has landed on a red pocket.\n"
               "Conditional Probability Formula:\n"
               "P(A | B) = P(A ∩ B) / P(B) = 6/18 = 1/3 ≈ 33.3%")

# Display the chart
plt.figtext(0.5, 0.02, description, wrap=True, horizontalalignment='center', fontsize=10, bbox={"facecolor": "white", "alpha": 0.6, "pad": 5})
plt.show()
