with open('index.html', 'r') as f:
    lines = f.readlines()

# Remove lines 3213-3214 (0-indexed: 3212-3213)
lines = lines[:3212] + lines[3214:]

with open('index.html', 'w') as f:
    f.writelines(lines)
print("Done")
