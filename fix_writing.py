import re
content = open('index.html').read()
content = re.sub(r'<a[^>]*>(?:(?!</a>).)*WRITING(?:(?!</a>).)*</a>', '', content, flags=re.DOTALL)
open('index.html', 'w').write(content)
print("Done")
