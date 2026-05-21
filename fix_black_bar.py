with open('index.html', 'r') as f:
    content = f.read()

content = content.replace(
    '<html style="scroll-behavior:smooth">',
    '<html style="scroll-behavior:smooth;background-color:#ffffff;">'
)

with open('index.html', 'w') as f:
    f.write(content)
print("Done")
