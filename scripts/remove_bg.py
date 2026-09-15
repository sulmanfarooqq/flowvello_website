from PIL import Image
import math

src_img = r"C:\Users\my\.gemini\antigravity\brain\7bb54674-e008-4391-b404-f701fc0f504b\.user_uploaded\media_1789476325894.png"
img = Image.open(src_img).convert("RGBA")
pixels = img.load()

bg_color = (68, 68, 68)

for y in range(img.height):
    for x in range(img.width):
        r, g, b, a = pixels[x, y]
        
        # Calculate distance from background color
        dist = math.sqrt((r - bg_color[0])**2 + (g - bg_color[1])**2 + (b - bg_color[2])**2)
        
        # If it's exactly or very close to the background color, make it fully transparent
        if dist < 5:
            pixels[x, y] = (0, 0, 0, 0)
        elif dist < 60:
            # For anti-aliased edges, we calculate a partial transparency
            # The further from background, the more opaque it should be
            # This is a simple linear interpolation for the alpha channel
            alpha = int(((dist - 5) / 55.0) * 255)
            pixels[x, y] = (r, g, b, alpha)

# Save the full logo transparent
img.save(r"c:\Users\my\Desktop\chatgpt\img\logo.png")
img.save(r"c:\Users\my\Desktop\chatgpt\img\logo.webp")

# Crop and save the favicon transparent
favicon = img.crop((10, 0, 159, 149))
favicon.save(r"c:\Users\my\Desktop\chatgpt\img\favicon.png")
favicon.save(r"c:\Users\my\Desktop\chatgpt\img\favicon.ico", format="ICO", sizes=[(64, 64)])

print("Transparent assets generated successfully.")
