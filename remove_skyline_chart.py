with open('index.html', 'r') as f:
    lines = f.readlines()

# Remove lines 3210-3245 (0-indexed: 3209-3244)
lines = lines[:3209] + lines[3245:]

with open('index.html', 'w') as f:
    f.writelines(lines)
print("Done")
