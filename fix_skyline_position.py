content = open('index.html').read()
content = content.replace(
    'src="skyline_fixed2.png" style="position:absolute;bottom:0;right:0;width:65%;height:auto;opacity:0.7;pointer-events:none;z-index:1;"',
    'src="skyline_fixed2.png" style="position:absolute;bottom:0;left:0;width:100%;height:50%;object-fit:cover;object-position:bottom;opacity:0.75;pointer-events:none;z-index:1;"'
)
open('index.html', 'w').write(content)
print("Done")
