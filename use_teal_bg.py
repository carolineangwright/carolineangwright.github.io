with open('index.html', 'r') as f:
    content = f.read()
content = content.replace('src="skyline_combined.png"', 'src="Gemini_Generated_Image_8dyoqf8dyoqf8dyo.png"')
with open('index.html', 'w') as f:
    f.write(content)
print("Done")
