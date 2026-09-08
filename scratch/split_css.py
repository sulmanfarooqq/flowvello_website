import re

with open('css/global.css', 'r', encoding='utf-8') as f:
    css = f.read()

# We will extract blocks that match specific top-level IDs.
# A block is roughly #ID_NAME ... { ... }
# We can find all top-level selectors by splitting by } that are at the root level.
# Actually, since cssutils is installed, let's use it! It's much safer.
import cssutils
import logging

cssutils.log.setLevel(logging.CRITICAL)

sheet = cssutils.parseString(css)

out_files = {
    'global.css': [],
    'home.css': [],
    'services.css': [],
    'about.css': [],
    'contact.css': [],
    'portfolio.css': [],
    'pricing.css': []
}

def get_target(selectorText):
    if '#homeSection' in selectorText or '#featureSection' in selectorText or '#workSection' in selectorText or '#premiumHeroSection' in selectorText or '#specialFeature' in selectorText or '#featureDetails' in selectorText:
        return 'home.css'
    elif '#serviceSection' in selectorText:
        return 'services.css'
    elif '#portfolioSection' in selectorText:
        return 'portfolio.css'
    elif '#pricingSection' in selectorText:
        return 'pricing.css'
    elif '#testimonialSection' in selectorText or '#aboutSection' in selectorText:
        return 'about.css'
    elif '#contactSection' in selectorText or '#contactArea' in selectorText or '#googleMap' in selectorText:
        return 'contact.css'
    else:
        return 'global.css'

for rule in sheet:
    if rule.type == rule.STYLE_RULE:
        target = get_target(rule.selectorText)
        out_files[target].append(rule.cssText)
    elif rule.type == rule.MEDIA_RULE:
        # Check inside media rule if there are specific targets
        # For simplicity, put media rules in global.css
        out_files['global.css'].append(rule.cssText)
    elif rule.type == rule.FONT_FACE_RULE or rule.type == rule.IMPORT_RULE:
        out_files['global.css'].append(rule.cssText)
    else:
        out_files['global.css'].append(rule.cssText)

import os
for fname, rules in out_files.items():
    if rules:
        with open('css/' + fname + '.new', 'w', encoding='utf-8') as f:
            f.write('\n\n'.join(rules))
        print(f"Wrote {fname}.new with {len(rules)} rules")
