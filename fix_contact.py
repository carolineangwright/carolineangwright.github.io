with open('index.html', 'r') as f:
    content = f.read()

content = content.replace('src="skyline_cropped2.png"', 'src="skyline_combined.png"')

content = content.replace(
    'inset-block-start:420px;inset-inline-end:0px',
    'inset-block-start:420px;display:none;inset-inline-end:0px',
    1
)

with open('index.html', 'w') as f:
    f.write(content)
print("Done")
