import os
import glob

# Files to update
html_files = glob.glob('*.html') + glob.glob('services/*.html') + glob.glob('industries/*.html')

print(f"Checking {len(html_files)} HTML files for web-based-games...")

count = 0
for fpath in html_files:
    if not os.path.exists(fpath):
        continue
    with open(fpath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    modified = False
    
    # Check for web-based-games in navigation dropdown
    # Pattern 1: root level href="services/web-based-games.html"
    old_item_root = '<li><a class="dropdown-item nested-subitem" href="services/web-based-games.html"><i class="fal fa-gamepad" style="width:20px; color:#FF2E3E; margin-right:8px; display:inline-block; text-align:center;"></i> Web-Based Games</a></li>'
    new_item_root = '<li><a class="dropdown-item nested-subitem" href="services/api-software-integration.html"><i class="fal fa-plug" style="width:20px; color:#FF2E3E; margin-right:8px; display:inline-block; text-align:center;"></i> API & Integrations</a></li>'
    
    # Pattern 2: nested level href="../services/web-based-games.html"
    old_item_sub = '<li><a class="dropdown-item nested-subitem" href="../services/web-based-games.html"><i class="fal fa-gamepad" style="width:20px; color:#FF2E3E; margin-right:8px; display:inline-block; text-align:center;"></i> Web-Based Games</a></li>'
    new_item_sub = '<li><a class="dropdown-item nested-subitem" href="../services/api-software-integration.html"><i class="fal fa-plug" style="width:20px; color:#FF2E3E; margin-right:8px; display:inline-block; text-align:center;"></i> API & Integrations</a></li>'

    if old_item_root in content:
        content = content.replace(old_item_root, new_item_root)
        modified = True
    if old_item_sub in content:
        content = content.replace(old_item_sub, new_item_sub)
        modified = True
        
    if modified:
        with open(fpath, 'w', encoding='utf-8') as f:
            f.write(content)
        count += 1
        print(f"Updated nav in: {fpath}")

print(f"Done. Updated navigation in {count} files.")
