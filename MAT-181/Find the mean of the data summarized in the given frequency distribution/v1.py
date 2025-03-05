'''
Find the mean of the data summarized in the given frequency distribution.
 
 The test scores of 40 students are summarized in the frequency distribution below. Find the mean score.
 Score :
 50-59
 60-69
 70-79
 80-89
 90-99

Students:
 5
 15
 6
 5
 9

'''

import matplotlib.pyplot as plt

# Data
scores = ['50-59', '60-69', '70-79', '80-89', '90-99']
students = [5, 15, 6, 5, 9]

# Calculate the midpoints for each score range
midpoints = [(50 + 59) / 2, (60 + 69) / 2, (70 + 79) / 2, (80 + 89) / 2, (90 + 99) / 2]
# Calculate total sum and mean score
total_sum = sum(mid * num for mid, num in zip(midpoints, students))
mean_score = total_sum / sum(students)

# Plotting
plt.bar(scores, students, color='skyblue')
plt.xlabel('Score Range')
plt.ylabel('Number of Students')
plt.title('Frequency Distribution of Test Scores')

# Adding labels for the calculations
for i, (score, student) in enumerate(zip(scores, students)):
    plt.text(i, student + 0.5, f'Mid: {midpoints[i]:.1f}\nNum: {student}', ha='center', va='bottom')

plt.text(2, max(students) + 2, f'Mean Score: {mean_score:.1f}', ha='center', va='bottom', fontsize=12, color='red')

plt.show()
