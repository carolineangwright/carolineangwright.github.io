with open('index.html', 'r') as f:
    content = f.read()

# Add a style tag before </head> to hide the black line
content = content.replace(
    '</head>',
    '<style>body{border:none;} section#contact{border-bottom:none;} footer{border-top:none;margin-top:0;}</style></head>',
    1
)

with open('index.html', 'w') as f:
    f.write(content)
print("Done")
