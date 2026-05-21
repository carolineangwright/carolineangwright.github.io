content = open('index.html').read()
content = content.replace(
    'src="skyline_cropped2.png" style="position:absolute;bottom:-120px;',
    'src="skyline_cropped2.png" style="position:absolute;bottom:-30px;'
)
open('index.html', 'w').write(content)
print("Done")
