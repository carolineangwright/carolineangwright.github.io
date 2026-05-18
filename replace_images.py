import base64
from bs4 import BeautifulSoup

# Image files - put these in the same folder as this script
image_map = {
    ('Before', 0): 'aidkit_before_cropped.png',
    ('After', 0):  'aidkit_after_cropped.png',
    ('Before', 1): 'exodigo_before_cropped.png',
    ('After', 1):  'exodigo_after_cropped.png',
}

with open('index.html', 'r') as f:
    soup = BeautifulSoup(f, 'html.parser')

befores = soup.find_all('img', alt='Before')
afters  = soup.find_all('img', alt='After')

print(f'Found {len(befores)} Before images, {len(afters)} After images')

for i, img in enumerate(befores):
    fname = image_map[('Before', i)]
    with open(fname, 'rb') as imgf:
        b64 = base64.b64encode(imgf.read()).decode('utf-8')
    img['src'] = f'data:image/png;base64,{b64}'
    print(f'Replaced Before #{i} with {fname}')

for i, img in enumerate(afters):
    fname = image_map[('After', i)]
    with open(fname, 'rb') as imgf:
        b64 = base64.b64encode(imgf.read()).decode('utf-8')
    img['src'] = f'data:image/png;base64,{b64}'
    print(f'Replaced After #{i} with {fname}')

with open('index.html', 'w') as f:
    f.write(str(soup))

print('Done! index.html updated.')
