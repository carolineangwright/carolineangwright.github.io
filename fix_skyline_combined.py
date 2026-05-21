content = open('index.html').read()
content = content.replace('src="skyline_cropped2.png"', 'src="skyline_combined.png"')
open('index.html', 'w').write(content)
print("Done")
