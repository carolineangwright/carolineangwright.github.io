content = open('index.html').read()
content = content.replace(
    'src="skyline_cropped.png"',
    'src="skyline_cropped2.png"'
)
open('index.html', 'w').write(content)
print("Done")
