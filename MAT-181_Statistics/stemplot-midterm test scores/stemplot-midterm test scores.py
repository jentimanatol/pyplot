from collections import defaultdict
import matplotlib.pyplot as plt

# Data
scores = [85, 77, 93, 91, 74, 65, 68, 97, 88, 59, 74, 83, 85, 72, 63, 79]

# Sort the data
scores_sorted = sorted(scores)

# Create a stemplot
stemplot = defaultdict(list)
for score in scores_sorted:
    stem = score // 10  # Extract the tens digit
    leaf = score % 10   # Extract the units digit
    stemplot[stem].append(leaf)

# Print the stemplot
print("Stem | Leaves")
print("-------------")
for stem in sorted(stemplot.keys()):
    leaves = ' '.join(map(str, stemplot[stem]))
    print(f"{stem:4} | {leaves}")