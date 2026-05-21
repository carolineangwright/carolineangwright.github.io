with open('index.html', 'r') as f:
    lines = f.readlines()

# Find the line near 4591 that has display:none and LINKEDIN context
for i in range(4585, 4598):
    if 'display:none' in lines[i] and i < 4595:
        lines[i] = lines[i].replace('display:none', 'display:block', 1)
        print(f"Restored display:block at line {i+1}")
        break

with open('index.html', 'w') as f:
    f.writelines(lines)
print("Done")
