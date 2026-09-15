from PIL import Image

src_img = r"c:\Users\my\Desktop\chatgpt\img\logo.png"
img = Image.open(src_img).convert("RGBA")
pixels = img.load()

# The dark brand color
dark_r, dark_g, dark_b = 34, 36, 41

for y in range(img.height):
    for x in range(img.width):
        r, g, b, a = pixels[x, y]
        
        if a > 0:
            # If it's mostly white/gray (not red)
            # The red logo has high red, low green/blue. White text has high all three.
            if r > 150 and g > 150 and b > 150:
                # Calculate luminance
                # Simple inversion or mapping to dark brand color
                # Since we want it dark, we just map it. To keep anti-aliasing soft, we blend it
                pixels[x, y] = (dark_r, dark_g, dark_b, a)

img.save(r"c:\Users\my\Desktop\chatgpt\img\logo-dark.png")
img.save(r"c:\Users\my\Desktop\chatgpt\img\logo-dark.webp")
print("logo-dark generated.")
