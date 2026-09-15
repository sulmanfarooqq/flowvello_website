from PIL import Image

src_img = r"C:\Users\my\.gemini\antigravity\brain\7bb54674-e008-4391-b404-f701fc0f504b\.user_uploaded\media_1789476325894.png"
img = Image.open(src_img)

# Crop the left square for the favicon (the monogram)
favicon = img.crop((10, 0, 159, 149))

# Save as PNG
favicon.save(r"c:\Users\my\Desktop\chatgpt\img\favicon.png")

# Save as ICO
favicon.save(r"c:\Users\my\Desktop\chatgpt\img\favicon.ico", format="ICO", sizes=[(64, 64)])

print("Favicon generated.")
