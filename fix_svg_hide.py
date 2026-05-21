with open('index.html', 'r') as f:
    content = f.read()

content = content.replace(
    'top:420px;touch-action:auto;transform:none',
    'top:420px;display:none;touch-action:auto;transform:none',
    1
)

with open('index.html', 'w') as f:
    f.write(content)
print("Done")
