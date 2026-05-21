with open('index.html', 'r') as f:
    lines = f.readlines()

# Line 3205 is index 3204 - add display:none to its style
lines[3204] = lines[3204].replace(
    'perspective-origin:720px 18px;pointer-events:auto;position:static',
    'display:none;perspective-origin:720px 18px;pointer-events:auto;position:static',
    1
)

with open('index.html', 'w') as f:
    f.writelines(lines)
print("Done")
