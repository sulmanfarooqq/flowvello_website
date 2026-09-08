import re
import cssutils
import logging
import os

cssutils.log.setLevel(logging.CRITICAL)

with open('css/global.css', 'r', encoding='utf-8') as f:
    css = f.read()

sheet = cssutils.parseString(css)

out_files = {
    'global.css.new': [],
    'home.css.new': [],
    'services-components.css.new': [],
    'about-components.css.new': [],
    'contact-components.css.new': [],
    'portfolio-components.css.new': [],
    'pricing-components.css.new': []
}

def get_target(selectorText):
    if '#homeSection' in selectorText or '#premiumHeroSection' in selectorText or '#featureSection' in selectorText or '#workSection' in selectorText:
        return 'home.css.new'
    elif '#serviceSection' in selectorText or '#specialFeature' in selectorText or '#featureDetails' in selectorText:
        return 'services-components.css.new'
    elif '#portfolioSection' in selectorText:
        return 'portfolio-components.css.new'
    elif '#pricingSection' in selectorText:
        return 'pricing-components.css.new'
    elif '#testimonialSection' in selectorText or '#aboutSection' in selectorText:
        return 'about-components.css.new'
    elif '#contactSection' in selectorText or '#googleMap' in selectorText:
        return 'contact-components.css.new'
    # Important: #contactArea is used globally across pages for the bottom CTA!
    elif '#contactArea' in selectorText:
        return 'global.css.new'
    else:
        return 'global.css.new'

for rule in sheet:
    if rule.type == rule.STYLE_RULE:
        target = get_target(rule.selectorText)
        out_files[target].append(rule.cssText)
    elif rule.type == rule.MEDIA_RULE:
        out_files['global.css.new'].append(rule.cssText)
    elif rule.type == rule.FONT_FACE_RULE or rule.type == rule.IMPORT_RULE:
        out_files['global.css.new'].append(rule.cssText)
    else:
        out_files['global.css.new'].append(rule.cssText)

for fname, rules in out_files.items():
    if rules:
        with open('css/' + fname, 'w', encoding='utf-8') as f:
            f.write('\n\n'.join(rules))
        print(f"{fname}: {len(rules)} rules written.")
