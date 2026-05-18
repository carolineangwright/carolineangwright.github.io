import re

content = open('index.html').read()

img_tag = '<img src="skyline_fixed2.png" style="position:absolute;bottom:0;right:0;width:65%;height:auto;opacity:0.7;pointer-events:none;z-index:1;" />'

# Insert after the opening tag of the contact section
content = content.replace(
    '<div class="skyline-chart"',
    img_tag + '\n<div class="skyline-chart"',
    1
)

open('index.html', 'w').write(content)
print("Done")
