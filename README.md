# Flow Vello

A high-performance, production-ready static marketing website for an AI automation and software agency. 

## 🚀 Overview
Flow Vello is built with a strictly static, dependency-light architecture to ensure maximum speed, seamless SEO indexing, and zero-maintenance hosting. It serves as the primary digital storefront for the agency, showcasing AI transformation capabilities, workflow automation services, and client case studies.

## 🛠 Tech Stack
- **Architecture:** Pure HTML5, CSS3, Vanilla JS / jQuery
- **Framework:** Bootstrap (Responsive Grid System)
- **Animations:** WOW.js & Animate.css (Scroll reveal animations)
- **Components:** Owl Carousel (Sliders), Calendly Embed (Booking)
- **Assets:** 100% Next-Gen WebP imagery (Optimized for aggressive loading speeds)
- **Hosting:** Configured natively for **Netlify**

## ⚡ Performance & Optimizations
This project has been heavily optimized for Core Web Vitals and Lighthouse scores:
- **Zero Build System:** No Webpack, No Next.js, No React overhead. The browser parses exactly what is shipped.
- **FOUC Prevention:** Custom CSS logic completely prevents the "Flash of Unstyled Content" on animations.
- **Global Fade-In:** Implements a native, app-like 0.5s global page transition on navigation.
- **Asset Compression:** All images are downscaled and encoded in Method-6 WebP to reduce payload by over 15MB.
- **Netlify Edge Caching:** 
etlify.toml is configured with strict Cache-Control headers to leverage Edge CDNs instantly.

## 📂 Project Structure
\\\	ext
/
├── css/             # Global stylesheets, responsive fixes, and animations
├── js/              # Custom interactivity and plugin initialization
├── img/             # Highly compressed WebP imagery
├── services/        # Dedicated service detail pages
├── index.html       # Landing Page
├── about.html       # Company Principles & About
├── contact.html     # Custom 2-column Calendly booking page
├── faq.html         # Frequently Asked Questions
├── 404.html         # Custom branded error page
└── netlify.toml     # Production deployment headers and routing
\\\

## 🚀 Deployment Instructions
This project is configured out-of-the-box for **Netlify**. 

1. Push this repository to GitHub, GitLab, or Bitbucket.
2. Connect the repository to a new Netlify site.
3. **Leave the build command blank.** 
4. **Leave the publish directory as the root (/ or .).**
5. Deploy!

Netlify will automatically read the 
etlify.toml file to apply enterprise-grade security headers, aggressive caching protocols, and proper 404 routing.

## 🎨 Design System Constraints
When adding new pages or sections, adhere to the established visual identity:
- **Typography:** Teko for display headers, Rubik for body copy.
- **Colors:** Deep darks (#0b0f19, #1d1e22), crisp whites, and Flow Vello Red (#fb383b).
- **Pill Buttons:** Primary calls to action should utilize the .fv-dual-btn animated class or the .fv-pill-btn-white variant.
- **Animations:** Use .wow .fadeInUp generously, but maintain a .wow { visibility: hidden; } safety net to prevent text flashing.
