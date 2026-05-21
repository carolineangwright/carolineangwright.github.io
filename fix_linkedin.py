with open('index.html', 'r') as f:
    lines = f.readlines()

# Fix line 4591 - restore display:block for LinkedIn
lines[4590] = lines[4590].replace('display:none', 'display:block', 1)

# Hide line 4596 - BOOK A 30-MIN - find its <a tag
for i in range(4593, 4600):
    if 'display:block' in lines[i]:
        lines[i] = lines[i].replace('display:block', 'display:none', 1)
        print(f"Hid BOOK A 30-MIN at line {i+1}")
        break

with open('index.html', 'w') as f:
    f.writelines(lines)
print("Done")
