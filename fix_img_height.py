with open('index.html', 'r') as f:
    content = f.read()
content = content.replace(
    'src="Gemini_Generated_Image_8dyoqf8dyoqf8dyo.png" style="position:absolute;bottom:-30px;left:0;width:100%;height:auto;opacity:0.75;pointer-events:none;z-index:1;"',
    'src="Gemini_Generated_Image_8dyoqf8dyoqf8dyo.png" style="position:absolute;bottom:0;left:0;width:100%;height:100%;object-fit:cover;object-position:bottom;opacity:0.9;pointer-events:none;z-index:1;"'
)
with open('index.html', 'w') as f:
    f.write(content)
print("Done")
