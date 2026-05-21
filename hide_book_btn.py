with open('index.html', 'r') as f:
    lines = f.readlines()

# Line 4596 is index 4595 - find the opening <a tag by scanning backwards
for i in range(4595, 4580, -1):
    if '<a ' in lines[i]:
        start = i
        break

# Find closing </a> scanning forward
for i in range(4595, 4610):
    if '</a>' in lines[i]:
        end = i
        break

print(f"Hiding lines {start+1} to {end+1}")
for i in range(start, end+1):
    lines[i] = lines[i].replace('<a ', '<a hidden ', 1) if i == start else lines[i]

with open('index.html', 'w') as f:
    f.writelines(lines)
print("Done")
