with open('index.html', 'r') as f:
    lines = f.readlines()

# Line 4584 - replace display:block with display:none in the BOOK A 30-MIN button
for i in range(4582, 4590):
    if 'BOOK A 30-MIN' in ''.join(lines[i:i+10]) and 'display:block' in lines[i]:
        lines[i] = lines[i].replace('display:block', 'display:none', 1)
        print(f"Fixed line {i+1}")
        break

with open('index.html', 'w') as f:
    f.writelines(lines)
print("Done")
