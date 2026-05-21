content = open('index.html').read()
# Find the div with the checkerboard SVG background and add display:none
content = content.replace(
    'background-image:url(&quot;data:image/svg+xml;utf8,%0A%20%20%20%20%3Csvg',
    'display:none;background-image:url(&quot;data:image/svg+xml;utf8,%0A%20%20%20%20%3Csvg',
    1
)
open('index.html', 'w').write(content)
print("Done")
