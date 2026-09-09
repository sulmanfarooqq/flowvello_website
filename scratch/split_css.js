const fs = require('fs');

const cssPath = 'css/global.css';
const cssContent = fs.readFileSync(cssPath, 'utf8');

const lines = cssContent.split('\n');

const outFiles = {
    'global.css': [],
    'home.css': [],
    'services.css': [],
    'about.css': [],
    'contact.css': [],
    'portfolio.css': [],
    'pricing.css': []
};

// We will scan each line. If a line or block belongs to a section, put it there.
// A CSS block starts with a selector and ends with }

// Since the CSS is formatted with } on the same line or next line, we can just track if we are inside a rule.
// But actually, in the view_file, CSS rules look like:
// #homeSection .slider-box {
//     background: url(../img/home-bg.webp); ... }
//
// So each rule is clearly prefixed. We don't even need to track blocks perfectly if we just look at the prefix.
// If the line starts with or contains #homeSection, it's home.css. But what about properties inside the block?
// We need to track the CURRENT active block.

let currentTarget = 'global.css';
let insideBlock = false;
let braceCount = 0;

for (let i = 0; i < lines.length; i++) {
    let line = lines[i];
    
    // Count braces to know if we are inside a rule or media query
    let openBraces = (line.match(/\{/g) || []).length;
    let closeBraces = (line.match(/\}/g) || []).length;
    
    if (braceCount === 0 && line.trim().length > 0) {
        // We are at the root level, evaluating the selector
        if (line.includes('#homeSection') || line.includes('#featureSection') || line.includes('#workSection') || line.includes('#premiumHeroSection')) {
            currentTarget = 'home.css';
        } else if (line.includes('#serviceSection')) {
            currentTarget = 'services.css';
        } else if (line.includes('#portfolioSection')) {
            currentTarget = 'portfolio.css';
        } else if (line.includes('#pricingSection')) {
            currentTarget = 'pricing.css';
        } else if (line.includes('#testimonialSection') || line.includes('#aboutSection')) {
            currentTarget = 'about.css';
        } else if (line.includes('#contactSection')) {
            currentTarget = 'contact.css';
        } else if (line.includes('@media')) {
            // media queries go to global for now
            currentTarget = 'global.css';
        } else if (line.startsWith('/*')) {
            // keep currentTarget or go to global? Let's keep it.
        } else if (line.includes('#footerSection') || line.includes('#navigration')) {
            currentTarget = 'global.css';
        } else {
            currentTarget = 'global.css';
        }
    }
    
    outFiles[currentTarget].push(line);
    
    braceCount += openBraces;
    braceCount -= closeBraces;
    
    // Reset target when exiting block, but what about media queries?
    // Media queries have nested blocks. So braceCount > 0 inside media query.
    // This logic works! When braceCount hits 0, the next line is a new root selector.
}

for (const [file, content] of Object.entries(outFiles)) {
    if (content.length > 0) {
        fs.writeFileSync('css/' + file + '.new', content.join('\n'));
        console.log('Wrote', file + '.new', content.length, 'lines');
    }
}
