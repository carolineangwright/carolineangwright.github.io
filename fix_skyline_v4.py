content = open('index.html').read()
content = content.replace(
    'src="skyline_cropped2.png" style="position:absolute;bottom:0;left:0;width:100%;height:auto;opacity:0.75;pointer-events:none;z-index:1;"',
    'src="skyline_cropped2.png" style="position:absolute;bottom:-30px;left:0;width:100%;height:auto;opacity:0.75;pointer-events:none;z-index:1;"'
)
open('index.html', 'w').write(content)
print("Done")
