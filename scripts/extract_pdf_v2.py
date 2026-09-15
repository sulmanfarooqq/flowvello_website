import pymupdf
import io
from PIL import Image
import os

pdf_path = r"c:\Users\my\Desktop\chatgpt\Brand Guidlines - Concept1[1] (1)-compressed.pdf"
doc = pymupdf.open(pdf_path)

images_found = []

for page_index in range(len(doc)):
    page = doc[page_index]
    image_list = page.get_images(full=True)
    
    if image_list:
        print(f"[+] Found {len(image_list)} images on page {page_index}")
    else:
        print(f"[!] No images found on page {page_index}")
        
    for image_index, img in enumerate(image_list, start=1):
        xref = img[0]
        base_image = doc.extract_image(xref)
        image_bytes = base_image["image"]
        image_ext = base_image["ext"]
        
        try:
            image = Image.open(io.BytesIO(image_bytes))
            print(f"    Image {image_index} - Size: {image.size}, Format: {image_ext}, Mode: {image.mode}")
            
            save_path = f"c:\\Users\\my\\Desktop\\chatgpt\\scripts\\extracted_{page_index}_{image_index}.{image_ext}"
            with open(save_path, "wb") as f:
                f.write(image_bytes)
                
        except Exception as e:
            print(f"    Error processing image {image_index}: {e}")

print("Extraction complete.")
