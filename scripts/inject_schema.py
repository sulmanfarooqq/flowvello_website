import glob
import re

files = glob.glob('c:/Users/my/Desktop/chatgpt/*.html') + glob.glob('c:/Users/my/Desktop/chatgpt/services/*.html') + glob.glob('c:/Users/my/Desktop/chatgpt/industries/*.html')

schema_code = """
<!-- FLOW VELLO ENTITY SCHEMA -->
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": ["Organization", "LocalBusiness"],
  "name": "Flow Vello",
  "alternateName": "Proto IT Consultants",
  "url": "https://flowvello.com",
  "logo": "https://flowvello.com/img/logo.webp",
  "description": "An elite AI, workflow automation, and custom software development agency.",
  "address": {
    "@type": "PostalAddress",
    "addressLocality": "Islamabad",
    "addressCountry": "PK"
  },
  "sameAs": [
    "https://www.linkedin.com/company/flowvello"
  ],
  "knowsAbout": ["Workflow Automation", "Artificial Intelligence", "Software Engineering"]
}
</script>
"""

count = 0
for filepath in files:
    with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
        html = f.read()

    if "FLOW VELLO ENTITY SCHEMA" in html:
        continue

    # insert before </head>
    new_html = re.sub(r'(</head>)', f"{schema_code}\\1", html, flags=re.IGNORECASE)
    
    if new_html != html:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_html)
        count += 1

print(f"Injected JSON-LD Schema into {count} files.")
