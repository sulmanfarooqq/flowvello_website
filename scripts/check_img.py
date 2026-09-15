from PIL import Image

src_img = r"C:\Users\my\.gemini\antigravity\brain\7bb54674-e008-4391-b404-f701fc0f504b\.user_uploaded\media_1789476325894.png"
img = Image.open(src_img)
print(f"Dimensions: {img.size}")
