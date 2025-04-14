# Data
weights = [144, 152, 142, 151, 160, 152, 131, 164, 141, 153, 140,
           144, 175, 156, 147, 133, 172, 159, 135, 159, 148, 171]

# Sort the data
weights_sorted = sorted(weights)

# Create a stem-and-leaf plot
stem_leaf = {}
for weight in weights_sorted:
    stem = weight // 10  # Extract the stem (first two digits)
    leaf = weight % 10   # Extract the leaf (last digit)
    if stem not in stem_leaf:
        stem_leaf[stem] = []
    stem_leaf[stem].append(leaf)

# Display the stem-and-leaf plot
print("Stem | Leaf")
print("-----------")
for stem in sorted(stem_leaf.keys()):
    leaves = " ".join(map(str, stem_leaf[stem]))  # Join leaves with spaces
    print(f"{stem:3} | {leaves}")