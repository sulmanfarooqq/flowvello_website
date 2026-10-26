import os
import re

# ==============================================================================
# 1. DEVELOPMENT SERVICE DETAIL PAGES DATA (EXACT 13-SECTION BLUEPRINT)
# ==============================================================================

DEV_SERVICES_DATA = [
    # -------------------------------------------------------------
    # 1. Custom Web Applications
    # -------------------------------------------------------------
    {
        "filename": "web-applications.html",
        "title": "Custom Web Applications | Techtox",
        "meta_desc": "Architect and develop bespoke web applications, business portals, and admin dashboards engineered for scalability, security, and intuitive workflows.",
        "eyebrow": "CUSTOM SOFTWARE ARCHITECTURE",
        "h1": "Custom Web Applications",
        "hero_desc": "We architect and engineer scalable, secure, and intuitive web applications tailored precisely to your operational workflows, user roles, and business logic.",
        "hero_img": "https://images.unsplash.com/photo-1498050108023-c5249f4df085?auto=format&fit=crop&w=1920&q=80",
        "demo_video_url": "https://www.youtube.com/watch?v=LXb3EKWsInQ",
        
        "problems": [
            ("Off-the-Shelf SaaS Inflexibility", "Generic SaaS tools force your team to bend operational processes around software limitations, leading to clunky workarounds, fragmented spreadsheets, and recurring seat license bloat."),
            ("Disconnected Internal Systems", "Critical customer, order, and inventory data is scattered across incompatible third-party tools, creating manual duplicate entry and reporting inaccuracies."),
            ("Scalability Bottlenecks & Crashes", "As user volume and transaction records grow, unoptimized web platforms slow down, experience database locks, and crash during peak business operations."),
            ("Poor User Adoption & Cluttered UX", "Complex, outdated user interfaces confuse staff and clients, causing excessive onboarding costs, administrative errors, and heavy reliance on manual support.")
        ],
        
        "solution": {
            "title": "Purpose-Built Web Applications Engineered for High-Volume Operations",
            "desc": "We architect and develop bespoke web applications using modern, maintainable stacks (React, Vue, Node.js, Python FastAPI, and PostgreSQL). Every database schema, role-based permission set, and user journey is engineered around your exact business requirements, delivering blistering performance, rock-solid security, and effortless user adoption."
        },
        
        "outcomes": [
            ("10x", "Operational Speed", "Streamlined workflows, automated calculations, and instant search replace hours of manual administrative work."),
            ("100%", "Data Integrity & IP Ownership", "You own 100% of the custom codebase, database schema, and intellectual property with zero vendor lock-in."),
            ("99.9%", "Production Uptime", "Built on resilient cloud architectures with automated health checks, connection pooling, and optimized queries.")
        ],
        
        "workflow": [
            ("01", "Architecture & Data Modeling", "Map entity relationships, role-based access models, API endpoints, and technical requirements before writing code."),
            ("02", "Interactive UX/UI Prototyping", "Design user journeys, component design systems, and responsive wireframes with stakeholder sign-off."),
            ("03", "Full-Stack Development", "Implement responsive frontend views, robust REST/GraphQL APIs, business logic services, and database migrations."),
            ("04", "Security & Load Testing", "Execute automated unit tests, integration suites, role permission penetration audits, and high-concurrency load checks."),
            ("05", "Cloud Deployment & CI/CD", "Deploy to AWS, Azure, or DigitalOcean with automated deployment pipelines, SSL provisioning, and live telemetry monitoring.")
        ],
        
        "capabilities": [
            ("fa fa-tachometer-alt", "Centralized Admin Dashboards", "Comprehensive operational dashboards with real-time analytics, filtering, metric calculation, and report export."),
            ("fa fa-user-shield", "Multi-Tier Role & Permission Control", "Granular user permission matrices, organization multi-tenancy, audit logging, and enterprise SSO/OAuth authentication."),
            ("fa fa-database", "High-Performance Database Architectures", "Optimized PostgreSQL and MySQL schemas with Redis caching layers built to handle millions of transactions."),
            ("fa fa-plug", "RESTful & GraphQL API Endpoints", "Clean, well-documented API backends ready for seamless integration with mobile apps, client portals, and external SaaS."),
            ("fa fa-mobile-alt", "Responsive Modern User Interfaces", "Blistering fast React and Vue user interfaces built with responsive design systems that work seamlessly across desktop, tablet, and mobile."),
            ("fa fa-cloud-upload-alt", "Automated Cloud CI/CD & Backups", "Continuous integration pipelines with automated daily database snapshots, disaster recovery protocols, and zero-downtime deploys.")
        ],
        
        "tools": {
            "native": ["React.js", "Next.js", "Vue.js", "Node.js", "Python / FastAPI", "TypeScript", "PostgreSQL", "MySQL", "Tailwind CSS"],
            "custom": ["Docker & Containers", "AWS Cloud", "Azure", "DigitalOcean", "Redis Cache", "GraphQL", "GitHub Actions CI/CD", "RESTful APIs"]
        },
        
        "portfolio": [
            {
                "title": "Enterprise Inventory & Order Management Portal",
                "img": "https://images.unsplash.com/photo-1460925895917-afdab827c52f?auto=format&fit=crop&w=800&q=80",
                "problem": "Wholesale distributor lost 15+ hours weekly synchronizing multi-warehouse orders in fragmented Excel sheets.",
                "built": "Custom React + Node.js portal tracking 45,000+ SKUs with live stock alerts and automated supplier PO dispatch.",
                "tools": "React, Node.js, PostgreSQL, Docker, Redis"
            },
            {
                "title": "Healthcare Clinic Patient & Telehealth Portal",
                "img": "https://images.unsplash.com/photo-1576091160399-112ba8d25d1d?auto=format&fit=crop&w=800&q=80",
                "problem": "Clunky legacy EHR system caused long patient wait times and lacked self-service intake and document signing.",
                "built": "HIPAA-compliant web app with secure patient onboarding, digital consent forms, and live appointment booking.",
                "tools": "Next.js, Python FastAPI, PostgreSQL, AWS S3"
            },
            {
                "title": "B2B Client Collaboration & Milestone Engine",
                "img": "https://images.unsplash.com/photo-1551288049-bebda4e38f71?auto=format&fit=crop&w=800&q=80",
                "problem": "Consulting firm struggled with client communication, deliverable sign-offs, and disjointed invoicing.",
                "built": "Bespoke client portal with real-time milestone tracking, Stripe invoicing, and role-based permissions.",
                "tools": "React, TypeScript, Node.js, Stripe API, PostgreSQL"
            }
        ],
        
        "faqs": [
            ("How long does it take to develop a custom web application?", "Timelines depend on scope. A focused operational MVP or internal portal typically takes 4 to 8 weeks, while complex enterprise platforms take 10 to 16 weeks delivered in iterative two-week milestones."),
            ("Who owns the source code and intellectual property?", "You own 100% of the custom code, architecture diagrams, database schemas, and assets upon project completion. There are zero licensing fees or vendor lock-ins."),
            ("Can the web application integrate with our existing databases and tools?", "Yes. We regularly build applications that connect to existing SQL Server, MySQL, ERP, CRM, or accounting systems via secure APIs and automated background sync pipelines."),
            ("How do you ensure data security and user privacy?", "We implement industry best practices: HTTPS encryption, OWASP top 10 vulnerability hardening, parameterized database queries, JWT/OAuth2 authentication, and encrypted data at rest."),
            ("What post-launch support and maintenance do you offer?", "Every build includes a 14-day warranty period. We also provide ongoing maintenance agreements covering feature additions, dependency updates, uptime monitoring, and SLA-backed support.")
        ]
    },

    # -------------------------------------------------------------
    # 2. WordPress Solutions
    # -------------------------------------------------------------
    {
        "filename": "wordpress-solutions.html",
        "title": "WordPress Solutions | Techtox",
        "meta_desc": "High-performance corporate WordPress websites and custom Gutenberg theme architectures built for speed, security, and content control.",
        "eyebrow": "ENTERPRISE CMS ARCHITECTURE",
        "h1": "WordPress Solutions",
        "hero_desc": "High-performance, secure, and custom-engineered WordPress websites built for blistering speed, intuitive content editing, and zero plugin bloat.",
        "hero_img": "https://images.unsplash.com/photo-1616469829581-73993eb86b02?auto=format&fit=crop&w=1920&q=80",
        "demo_video_url": "https://www.youtube.com/watch?v=LXb3EKWsInQ",
        
        "problems": [
            ("Bloated Themes & Slow Page Load Speeds", "Off-the-shelf page builders with 50+ third-party plugins cause 5+ second load times, destroying search rankings and ad conversion rates."),
            ("Security Vulnerabilities & Malware Attacks", "Outdated plugins and unmaintained theme architectures leave corporate sites exposed to SQL injections, brute-force attacks, and blacklist penalties."),
            ("Cluttered, Fragile Admin Editing", "Marketing teams struggle with fragile layouts that break whenever non-technical staff attempt to publish a blog post or update copy."),
            ("Plugin Conflicts & Broken Updates", "WordPress and plugin core updates frequently break forms, checkouts, or site styling due to conflicting, unmaintained spaghetti code.")
        ],
        
        "solution": {
            "title": "Custom WordPress Engineering: Fast, Secure, and Built to Scale",
            "desc": "We build custom WordPress websites using lightweight custom themes, Gutenberg block architectures, and enterprise-grade security hardening. Your site loads in under 1.5 seconds, scores 90+ on Google PageSpeed, and gives your editorial team an intuitive, bulletproof editing experience without plugin bloat."
        },
        
        "outcomes": [
            ("<1.5s", "Page Load Time", "Clean code, asset minification, and advanced Redis/Varnish caching ensure sub-1.5 second loading."),
            ("95+", "Core Web Vitals Score", "Google PageSpeed optimization for higher organic search visibility and lower ad acquisition costs."),
            ("Zero", "Plugin Bloat & Conflicts", "Custom modular blocks and custom post types replace 30+ unnecessary external plugins.")
        ],
        
        "workflow": [
            ("01", "Audit & Information Architecture", "Analyze content hierarchy, target keywords, custom post types, and speed bottlenecks."),
            ("02", "Bespoke UI/UX & Block Design", "Craft modular layouts and interactive components tailored strictly to your brand guidelines."),
            ("03", "Clean Theme & Block Development", "Develop lightweight PHP/React Gutenberg blocks with zero bloated third-party page builders."),
            ("04", "Speed, SEO & Security Hardening", "Implement object caching, WebP compression, schema markup, and firewall configuration."),
            ("05", "Seamless Migration & Live Launch", "Execute zero-downtime database migration, DNS switch, SSL provisioning, and editor training.")
        ],
        
        "capabilities": [
            ("fab fa-wordpress", "Custom Gutenberg Modular Blocks", "Flexible, brand-consistent drag-and-drop blocks tailored specifically for your marketing team."),
            ("fa fa-layer-group", "Custom Post Types & Taxonomies", "Structured content management for portfolios, case studies, team directories, and resource libraries."),
            ("fa fa-bolt", "Core Web Vitals & Speed Optimization", "CSS/JS minification, critical path rendering, image WebP conversion, and Redis object caching."),
            ("fa fa-shield-check", "Enterprise Security Hardening", "WAF firewall configuration, custom login endpoints, two-factor authentication, and brute-force prevention."),
            ("fa fa-shopping-cart", "WooCommerce Customization & Checkout", "Bespoke e-commerce extensions, multi-currency support, custom payment gateways, and optimized one-page checkouts."),
            ("fa fa-sync-alt", "CRM & Webhook Integrations", "Connect form submissions and customer inquiries directly to HubSpot, Salesforce, ActiveCampaign, or Slack.")
        ],
        
        "tools": {
            "native": ["WordPress Core", "WooCommerce", "Gutenberg Block Editor", "Advanced Custom Fields (ACF Pro)", "MySQL", "PHP 8.2+", "WP REST API"],
            "custom": ["Redis Object Cache", "Cloudflare CDN", "Wordfence Security", "WP Rocket", "Nginx", "WP-CLI", "GitHub Actions"]
        },
        
        "portfolio": [
            {
                "title": "Corporate SaaS Marketing Website & Resource Center",
                "img": "https://images.unsplash.com/photo-1460925895917-afdab827c52f?auto=format&fit=crop&w=800&q=80",
                "problem": "Previous Elementor site took 6.2s to load, dragging down ad conversion rates and Google SEO rankings.",
                "built": "Custom Gutenberg theme with custom post types, instant search, and sub-1.2s loading speeds.",
                "tools": "WordPress, Gutenberg, ACF Pro, Redis, Cloudflare"
            },
            {
                "title": "High-Traffic Editorial Publication & Magazine",
                "img": "https://images.unsplash.com/photo-1504711434969-e33886168f5c?auto=format&fit=crop&w=800&q=80",
                "problem": "100,000+ monthly readers experienced frequent server 504 gateway timeouts during traffic surges.",
                "built": "High-concurrency Nginx architecture with Cloudflare edge caching, schema markup, and lazy-loading media.",
                "tools": "WordPress, Nginx, Cloudflare CDN, MariaDB, Redis"
            },
            {
                "title": "B2B Industrial Manufacturer Product Catalog",
                "img": "https://images.unsplash.com/photo-1581091226825-a6a2a5aee158?auto=format&fit=crop&w=800&q=80",
                "problem": "Outdated catalog site lacked responsive mobile layouts, CAD spec sheet downloads, and RFQ forms.",
                "built": "Modernized product catalog with custom attribute filtering and automated sales lead routing to HubSpot.",
                "tools": "WordPress, WooCommerce (Catalog Mode), ACF, HubSpot API"
            }
        ],
        
        "faqs": [
            ("Why build a custom WordPress theme instead of using a commercial theme?", "Commercial themes are packed with hundreds of features you will never use, causing heavy CSS/JS bloat and slow speeds. A custom theme is coded with only what your business requires, ensuring sub-1.5s load times, rock-solid security, and effortless editing."),
            ("Can our non-technical team easily update pages and add blog posts?", "Yes. We build native Gutenberg blocks tailored to your exact layouts. Your team can easily rearrange sections, change images, and update copy without touching any code or risking broken styling."),
            ("How do you handle site migration from an existing host or CMS?", "We handle complete end-to-end migrations including database transfer, image asset migration, 301 SEO redirects to preserve rankings, and zero-downtime DNS cutover."),
            ("What security measures are implemented to protect against hacking?", "We implement server-level WAF firewalls, disable XML-RPC, rename admin login endpoints, enforce two-factor authentication, and configure automated hourly backups."),
            ("Do you provide ongoing WordPress maintenance and plugin updates?", "Yes. We offer monthly maintenance packages that include managed updates tested on staging first, security monitoring, daily backups, and dedicated development hours.")
        ]
    },

    # -------------------------------------------------------------
    # 3. Shopify Stores
    # -------------------------------------------------------------
    {
        "filename": "shopify-stores.html",
        "title": "Shopify Stores | Techtox",
        "meta_desc": "High-converting, brand-first Shopify and Shopify Plus storefronts engineered to maximize average order value, accelerate load speed, and streamline fulfillment.",
        "eyebrow": "E-COMMERCE CONVERSION ARCHITECTURE",
        "h1": "Shopify Stores",
        "hero_desc": "High-converting, brand-first Shopify & Shopify Plus storefronts engineered to maximize average order value, accelerate load speed, and streamline fulfillment.",
        "hero_img": "https://images.unsplash.com/photo-1556742049-0cfed4f6a45d?auto=format&fit=crop&w=1920&q=80",
        "demo_video_url": "https://www.youtube.com/watch?v=LXb3EKWsInQ",
        
        "problems": [
            ("High Cart Abandonment & Checkout Friction", "Confusing navigation, slow mobile checkout steps, and hidden fees cause 70%+ of interested shoppers to leave without purchasing."),
            ("Slow Mobile Storefronts Costing Revenue", "Bloated third-party app scripts slow down mobile rendering, driving up paid ad bounce rates and slashing return on ad spend (ROAS)."),
            ("Fragmented Inventory & Multi-Channel Errors", "Managing stock across Shopify, marketplaces, and physical retail manually causes overselling, backorders, and angry customer reviews."),
            ("Generic Look & Limited Customization", "Cookie-cutter theme templates fail to convey brand authority or support custom product bundles, tier pricing, and subscriptions.")
        ],
        
        "solution": {
            "title": "Custom Shopify Storefronts Built for Scale, Speed, and Conversions",
            "desc": "We design and develop custom Shopify Liquid themes and headless e-commerce solutions that captivate shoppers and remove buying friction. From frictionless 1-click upsells and custom product configurators to real-time ERP and fulfillment integrations, we turn your store into an automated selling engine."
        },
        
        "outcomes": [
            ("+28%", "Average Conversion Rate", "Frictionless mobile navigation, trust badges, and streamlined one-page checkout flows."),
            ("<1.8s", "Mobile Page Load Speed", "Clean Liquid code, asset lazy loading, and elimination of redundant tracking scripts."),
            ("100%", "Automated Inventory & Order Sync", "Bi-directional integration between Shopify, warehouses, 3PLs, and accounting software.")
        ],
        
        "workflow": [
            ("01", "E-Commerce Strategy & Audit", "Analyze customer buying paths, average order value opportunities, and catalog structure."),
            ("02", "Conversion-Focused UI/UX Design", "Create mobile-first wireframes and high-fidelity prototypes prioritizing visual product storytelling."),
            ("03", "Custom Liquid & Storefront Engineering", "Build responsive themes, custom section schemas, dynamic drawers, and cart logic."),
            ("04", "Payment, App & 3PL Integration", "Configure payment gateways, tax zones, email marketing flows, and fulfillment connectors."),
            ("05", "Launch, QA & Conversion Tracking", "Execute test transactions, verify analytics event tracking, and launch without downtime.")
        ],
        
        "capabilities": [
            ("fab fa-shopify", "Bespoke Liquid Theme Development", "Clean, modular Shopify Online Store 2.0 theme engineering tailored strictly to your brand identity."),
            ("fa fa-boxes", "Custom Product Bundles & Subscriptions", "Increase AOV with intelligent cross-sells, dynamic bundles, and recurring recharge subscription setups."),
            ("fa fa-shopping-bag", "High-Converting Slide-Out Ajax Cart", "Dynamic free shipping progress bars, 1-click upsells, and promo code inputs directly inside the cart drawer."),
            ("fa fa-globe", "Multi-Currency & Internationalization", "Shopify Markets setup with automatic geolocation currency conversion and localized shipping rates."),
            ("fa fa-truck-loading", "ERP, 3PL & Warehouse Automation", "Seamless bi-directional synchronization with ShipStation, Katana ERP, QuickBooks, and Klaviyo."),
            ("fa fa-tachometer-alt", "Speed Optimization & App Audit", "Eliminate bloated third-party scripts and optimize image rendering for lightning-fast mobile browsing.")
        ],
        
        "tools": {
            "native": ["Shopify", "Shopify Plus", "Liquid", "Online Store 2.0", "Storefront API", "Shopify Checkout Extensibility"],
            "custom": ["Klaviyo", "Recharge Subscriptions", "ShipStation", "Gorgias", "Shopify Payments / Stripe", "Google Tag Manager"]
        },
        
        "portfolio": [
            {
                "title": "Direct-to-Consumer Apparel Brand Storefront",
                "img": "https://images.unsplash.com/photo-1441986300917-64674bd600d8?auto=format&fit=crop&w=800&q=80",
                "problem": "Mobile conversion rate was stalled at 1.4% due to a sluggish, cluttered theme and slow product pages.",
                "built": "Custom Shopify OS 2.0 theme with sticky add-to-cart, size guides, and instant slide cart; conversion rose to 2.9%.",
                "tools": "Shopify Plus, Liquid, Klaviyo, Gorgias"
            },
            {
                "title": "Nutritional Supplement Brand Subscription Engine",
                "img": "https://images.unsplash.com/photo-1584308666744-24d5c474f2ae?auto=format&fit=crop&w=800&q=80",
                "problem": "High customer churn and manual fulfillment processing for monthly supplement refills.",
                "built": "Automated Recharge subscription setup with custom bundle configurator and automated customer portal.",
                "tools": "Shopify, Recharge Subscriptions, ShipStation, Klaviyo"
            },
            {
                "title": "Luxury Home Decor Multi-Currency Flagship",
                "img": "https://images.unsplash.com/photo-1618221195710-dd6b41faaea6?auto=format&fit=crop&w=800&q=80",
                "problem": "US-only store struggled to convert European and Canadian traffic due to currency barriers.",
                "built": "Shopify Markets multi-currency deployment with localized shipping rates and automated duty calculation.",
                "tools": "Shopify Plus, Shopify Markets, Liquid, Stripe"
            }
        ],
        
        "faqs": [
            ("Can you migrate our existing store from WooCommerce, Magento, or BigCommerce to Shopify?", "Yes. We execute complete store migrations including customer accounts, order history, product catalogs, collections, SEO redirects, and payment gateways with zero loss of data or rankings."),
            ("What is the difference between standard Shopify and Shopify Plus?", "Shopify Plus is built for high-volume enterprise brands ($1M+ annual revenue) offering customizable checkout code, dedicated API rate limits, wholesale B2B portals, and automated workflow scripts. We build on both."),
            ("How do you ensure apps do not slow down our storefront?", "We avoid unnecessary third-party apps by custom coding features (such as mega menus, size guides, FAQ accordions, and slide-out carts) directly into the Liquid theme."),
            ("Can we offer recurring subscriptions and product bundles?", "Yes. We integrate industry-standard subscription platforms (such as Recharge or native Shopify Subscriptions) and build custom bundle builders that boost your average order value."),
            ("Do you handle post-launch Shopify support and marketing integrations?", "Yes. We offer continuous e-commerce maintenance, A/B testing, speed audits, and full integration with Klaviyo email flows and Google Analytics 4.")
        ]
    },

    # -------------------------------------------------------------
    # 4. Desktop Applications
    # -------------------------------------------------------------
    {
        "filename": "desktop-applications.html",
        "title": "Desktop Applications | Techtox",
        "meta_desc": "High-performance, offline-resilient desktop applications engineered for high-volume data processing, hardware integration, and internal operational workflows.",
        "eyebrow": "DEDICATED DESKTOP SOFTWARE",
        "h1": "Desktop Applications",
        "hero_desc": "High-performance, offline-resilient desktop applications engineered for high-volume data processing, hardware integration, and internal operational workflows.",
        "hero_img": "https://images.unsplash.com/photo-1517694712202-14dd9538aa97?auto=format&fit=crop&w=1920&q=80",
        "demo_video_url": "https://www.youtube.com/watch?v=LXb3EKWsInQ",
        
        "problems": [
            ("Web Browser Overhead & Memory Limits", "Browser-based applications choke, freeze, or crash when processing massive spreadsheets, image archives, or real-time sensor streams."),
            ("Hardware & Local Peripheral Disconnection", "Web apps cannot reliably communicate with local industrial equipment, thermal barcode printers, weighing scales, or USB scanners."),
            ("Internet Dependency & Costly Downtime", "When internet connectivity drops, web-only business operations grind to a halt, stopping warehouse shipping and point-of-sale desks."),
            ("Sluggish Manual Data Entry Workflows", "Employees lose hours waiting on browser page reloads, tab navigation lag, and caching delays during high-speed repetitive data entry.")
        ],
        
        "solution": {
            "title": "Purpose-Built Desktop Software Engineered for Performance & Control",
            "desc": "We engineer native and cross-platform desktop applications (C# .NET WPF, MAUI, Electron, and Python) designed for raw execution speed, offline autonomy, and direct hardware communication. Whether you need a high-speed warehouse dispatch station, an offline data processing utility, or a local hardware monitoring tool, we build software that never slows down."
        },
        
        "outcomes": [
            ("100%", "Offline Autonomy", "Execute critical business operations locally with background synchronization once connectivity resumes."),
            ("<10ms", "UI Response Times", "Native multi-threaded desktop architectures that process thousands of records without interface lag."),
            ("Direct", "Hardware Integration", "Seamless communication with thermal printers, barcode scanners, RS-232 serial ports, and industrial scales.")
        ],
        
        "workflow": [
            ("01", "Operational Workflow Analysis", "Map hardware requirements, operator workflows, memory footprints, and security constraints."),
            ("02", "Architecture & Driver Prototyping", "Design local database schema, asynchronous worker threads, and communication drivers."),
            ("03", "Native UI & Business Logic", "Engineer ergonomic keyboard-first interfaces, background sync tasks, and robust business logic."),
            ("04", "On-Site Hardware & Stress QA", "Test under extreme data loads, edge-case network drops, and diverse operating system environments."),
            ("05", "Installer Packaging & Updates", "Deploy MSI/EXE packages with automated background update mechanisms and diagnostic logging.")
        ],
        
        "capabilities": [
            ("fa fa-cogs", "High-Throughput Batch Processing", "Process tens of thousands of records, CSV imports, or image batches using multi-threaded CPU cores without freezing."),
            ("fa fa-print", "Direct Peripheral & Hardware Drivers", "Communicate natively with USB barcode scanners, RFID readers, receipt printers, and serial scales via COM ports."),
            ("fa fa-database", "Offline-First Embedded Databases", "Store operational records locally in SQLite or LiteDB with intelligent two-way synchronization to central cloud servers."),
            ("fa fa-keyboard", "Keyboard-Driven Ergonomic Interfaces", "Optimized for ultra-fast data entry with custom hotkeys, tab stops, and zero browser latency."),
            ("fab fa-windows", "Native Windows & Cross-Platform Builds", "Engineered for modern Windows 10/11 environments with optional macOS and Linux cross-compatibility."),
            ("fa fa-sync-alt", "Automated Silent Background Updates", "Seamless auto-update pipelines ensure team workstations always run the latest validated release.")
        ],
        
        "tools": {
            "native": ["C# / .NET 8", "WPF (Windows Presentation Foundation)", ".NET MAUI", "Electron", "Python / PyQt", "C++"],
            "custom": ["SQLite", "LiteDB", "SQL Server", "COM Port / RS-232", "USB HID Drivers", "REST APIs", "WebSockets"]
        },
        
        "portfolio": [
            {
                "title": "Warehouse Dispatch & Barcode Shipping Station",
                "img": "https://images.unsplash.com/photo-1553413077-190dd305871c?auto=format&fit=crop&w=800&q=80",
                "problem": "Web-based shipping portal crashed during holiday peak; thermal label printing took 8 seconds per package.",
                "built": "Native C# .NET desktop station printing ZPL labels directly via USB in under 300ms with offline queueing.",
                "tools": "C# .NET, SQLite, Zebra ZPL, REST API"
            },
            {
                "title": "Clinical Laboratory Diagnostic Equipment Controller",
                "img": "https://images.unsplash.com/photo-1582719478250-c89cae4dc85b?auto=format&fit=crop&w=800&q=80",
                "problem": "Lab technicians had to manually retype spectrometer sensor data into spreadsheets, causing errors.",
                "built": "Python desktop utility interfacing with RS-232 ports to automatically capture, chart, and export diagnostic reads.",
                "tools": "Python, PyQt6, SQLite, RS-232 Serial"
            },
            {
                "title": "Point-of-Sale & Offline Inventory Terminal",
                "img": "https://images.unsplash.com/photo-1556742044-3c52d6e88c62?auto=format&fit=crop&w=800&q=80",
                "problem": "Retail showroom experienced costly sales disruption whenever local fiber internet dropped.",
                "built": "WPF desktop terminal processing sales locally with SQLite, automatically syncing transactions to cloud ERP when online.",
                "tools": "C# WPF, .NET Core, SQLite, Cloud Sync API"
            }
        ],
        
        "faqs": [
            ("Do you develop for both Windows and macOS?", "Yes. We build native Windows applications using C# and .NET for maximum enterprise performance, and cross-platform desktop applications using Electron or .NET MAUI for simultaneous Windows and macOS deployment."),
            ("Can the desktop application run completely offline?", "Yes. We design offline-first architectures using local embedded databases (SQLite). Your staff can continue processing data and transactions, which sync automatically to your cloud database once connection is restored."),
            ("How are software updates and patches rolled out to workstations?", "We integrate auto-updater pipelines that silently check for signed releases, download updates in the background, and apply them on application restart without requiring administrator intervention."),
            ("Can the desktop application interact with specialized physical hardware?", "Yes. We write native drivers for serial COM ports, USB devices, industrial scales, thermal label printers (ZPL/EPL), barcode scanners, and RFID readers."),
            ("Who owns the intellectual property and source code?", "You own 100% of the compiled software and complete source code repository upon completion. There are zero ongoing runtime royalties.")
        ]
    }
]

# ==============================================================================
# 2. DETAIL PAGE HTML TEMPLATE GENERATOR
# ==============================================================================

def render_dev_detail_page(s):
    # 02 Problems HTML with WOW animation
    problems_html = ""
    for i, (title, desc) in enumerate(s["problems"]):
        delay = f"{0.1 * (i+1):.1f}s"
        problems_html += f'''            <div class="problem-card wow fadeInUp" data-wow-delay="{delay}">
               <div class="problem-badge"><i class="fa fa-exclamation-circle"></i> Operational Friction</div>
               <h3 class="problem-title">{title}</h3>
               <p class="problem-desc">{desc}</p>
            </div>\n'''

    # 04 Outcomes HTML
    outcomes_html = ""
    for i, (stat, title, desc) in enumerate(s["outcomes"]):
        delay = f"{0.1 * (i+1):.1f}s"
        outcomes_html += f'''            <div class="outcome-card wow fadeInUp" data-wow-delay="{delay}">
               <div class="outcome-stat">{stat}</div>
               <h4 class="outcome-title">{title}</h4>
               <p class="outcome-desc">{desc}</p>
            </div>\n'''

    # 05 Workflow HTML
    workflow_html = ""
    for i, (step_num, title, desc) in enumerate(s["workflow"]):
        delay = f"{0.08 * (i+1):.2f}s"
        workflow_html += f'''            <div class="workflow-step-card wow fadeInUp" data-wow-delay="{delay}">
               <div class="workflow-step-num">{step_num}</div>
               <h4 class="workflow-step-title">{title}</h4>
               <p class="workflow-step-desc">{desc}</p>
            </div>\n'''

    # 06 Capabilities HTML
    capabilities_html = ""
    for i, (icon, title, desc) in enumerate(s["capabilities"]):
        delay = f"{0.1 * ((i%3)+1):.1f}s"
        capabilities_html += f'''            <div class="feature-light-card wow fadeInUp" data-wow-delay="{delay}">
                <div class="fl-icon"><i class="{icon}"></i></div>
                <h3 class="fl-title">{title}</h3>
                <p class="fl-desc">{desc}</p>
            </div>\n'''

    # 07 Tools HTML (Native vs Custom)
    native_tools_pills = "".join([f'<span class="tool-tag tool-tag-native"><i class="fa fa-check-circle" style="color: #10b981; margin-right: 6px;"></i> {t}</span>' for t in s["tools"]["native"]])
    custom_tools_pills = "".join([f'<span class="tool-tag tool-tag-custom"><i class="fa fa-code-branch" style="color: #FF2E3E; margin-right: 6px;"></i> {t}</span>' for t in s["tools"]["custom"]])

    # 08 Portfolio HTML
    portfolio_html = ""
    for i, p in enumerate(s["portfolio"]):
        delay = f"{0.15 * (i+1):.2f}s"
        portfolio_html += f'''            <div class="portfolio-item-card wow fadeInUp" data-wow-delay="{delay}">
               <div class="portfolio-item-img-wrap">
                  <img src="{p['img']}" alt="{p['title']}" loading="lazy">
               </div>
               <div class="portfolio-item-body">
                  <h3 class="portfolio-item-title">{p['title']}</h3>
                  <div class="portfolio-meta-row">
                     <span class="portfolio-meta-label">Problem:</span>
                     <span class="portfolio-meta-val">{p['problem']}</span>
                  </div>
                  <div class="portfolio-meta-row">
                     <span class="portfolio-meta-label">Built:</span>
                     <span class="portfolio-meta-val">{p['built']}</span>
                  </div>
                  <div class="portfolio-meta-row">
                     <span class="portfolio-meta-label">Platforms:</span>
                     <span class="portfolio-meta-val" style="color: #FF2E3E; font-weight: 600;">{p['tools']}</span>
                  </div>
               </div>
            </div>\n'''

    # 12 FAQs HTML
    faqs_html = ""
    for i, (q, a) in enumerate(s["faqs"]):
        delay = f"{0.05 * (i+1):.2f}s"
        faqs_html += f'''            <div class="fv-faq-item fv-faq-modern-item wow fadeInUp" data-wow-delay="{delay}">
               <div class="fv-faq-header fv-faq-modern-header">
                  <h3>{q}</h3>
                  <i class="fa fa-chevron-down"></i>
               </div>
               <div class="fv-faq-content fv-faq-modern-content">
                  <p>{a}</p>
               </div>
            </div>\n'''

    return f'''<!DOCTYPE html>
<html lang="en">
<head>
   <meta charset="UTF-8">
   <meta name="viewport" content="width=device-width, initial-scale=1.0">
   <meta http-equiv="X-UA-Compatible" content="ie=edge">
   <meta name="description" content="{s['meta_desc']}">
   <link rel="shortcut icon" href="../img/softoweb.png">
   <link rel="preconnect" href="https://fonts.gstatic.com">
   <!-- TECHTOX BRAND GUIDELINES TYPOGRAPHY: SORA ACROSS ALL WEIGHTS (100 to 800) -->
   <link href="https://fonts.googleapis.com/css2?family=Sora:wght@100;200;300;400;500;600;700;800&display=swap" rel="stylesheet">
   <link rel="stylesheet" href="../css/bootstrap.css">
   <link rel="stylesheet" href="../css/animate.css">
   <link rel="stylesheet" href="../css/owl.carousel.min.css">
   <link rel="stylesheet" href="../css/owl.theme.default.min.css">
   <link rel="stylesheet" href="../css/magnific-popup.css">
   <link rel="stylesheet" href="../css/custom.css">
   <link rel="stylesheet" href="../css/index.css">
   <link rel="stylesheet" href="../css/service.css">
   <link rel="stylesheet" href="../css/chatbot.css">
   <title>{s['title']}</title>

<style>
/* -------------------------------------------------------------
   TECHTOX BRAND GUIDELINES TYPOGRAPHY (SORA ONLY, TRACKING -10)
------------------------------------------------------------- */
body, h1, h2, h3, h4, h5, h6, p, span, a, li, button, input, label {{
   font-family: 'Sora', sans-serif !important;
   letter-spacing: -0.015em;
}}

/* Navigation Dropdown */
.nested-services-menu {{
    padding: 10px; 
    border-radius: 8px; 
    box-shadow: 0 10px 25px rgba(0,0,0,0.1); 
    border: 1px solid #e5e7eb; 
    min-width: 280px; 
    background: #ffffff;
    list-style: none;
    margin: 0;
}}
.dropdown-submenu {{
    position: relative;
    padding: 2px 0;
}}
.dropdown-submenu > .dropdown-menu {{
    top: 0;
    left: 100%;
    margin-top: -5px;
    display: none;
    border-radius: 8px;
    box-shadow: 0 10px 25px rgba(0,0,0,0.1);
    border: 1px solid #e5e7eb;
    min-width: 260px;
    background: #ffffff;
    padding: 10px;
}}
.dropdown-submenu:hover > .dropdown-menu {{
    display: block;
}}
.nested-item {{
    padding: 10px 15px !important;
    font-weight: 500 !important;
    font-size: 15px !important;
    color: #374151 !important;
    border-radius: 6px;
    transition: all 0.2s;
    display: flex !important;
    justify-content: space-between !important;
    align-items: center !important;
}}
.nested-item:hover {{
    background-color: #f9fafb !important;
    color: #000000 !important;
}}
.nested-subitem {{
    padding: 8px 15px !important;
    font-weight: 500 !important;
    font-size: 14px !important;
    color: #4b5563 !important;
    border-radius: 6px;
    transition: all 0.2s;
    display: flex !important;
    align-items: center !important;
}}
.nested-subitem:hover {{
    background-color: #f9fafb !important;
    color: #FF2E3E !important;
}}
@media (max-width: 991px) {{
    .dropdown-submenu > .dropdown-menu {{
        display: block;
        position: static;
        box-shadow: none;
        border: none;
        padding-left: 20px;
        margin-top: 5px;
        background: transparent;
    }}
    .nested-item i.fa-angle-right {{ display: none; }}
}}

/* Brand Section Titles & Eyebrows */
.vibe-eyebrow {{
   color: #FF2E3E !important;
   font-family: 'Sora', sans-serif !important;
   font-size: 13px !important;
   font-weight: 700 !important;
   letter-spacing: 2px !important;
   text-transform: uppercase !important;
   margin-bottom: 12px !important;
   display: inline-block;
}}
.vibe-heading {{
   font-family: 'Sora', sans-serif !important;
   font-size: 40px !important;
   font-weight: 700 !important;
   color: #000000 !important;
   letter-spacing: -1.2px !important;
   margin-bottom: 16px !important;
   line-height: 1.15 !important;
}}
.vibe-lead {{
   color: #6b7280 !important;
   font-size: 17px !important;
   font-family: 'Sora', sans-serif !important;
   font-weight: 400 !important;
   margin: 0 !important;
   line-height: 1.65 !important;
   letter-spacing: -0.3px !important;
}}

/* Hero View Demo Button */
.vibe-btn-demo {{
   color: #ffffff !important;
   font-family: 'Sora', sans-serif !important;
   font-size: 14px;
   font-weight: 600;
   padding: 12px 26px;
   border: 1px solid rgba(255, 255, 255, 0.25);
   border-radius: 9999px;
   text-decoration: none !important;
   display: inline-flex;
   align-items: center;
   gap: 10px;
   background: rgba(255, 255, 255, 0.08);
   backdrop-filter: blur(8px);
   transition: all 0.3s cubic-bezier(0.16, 1, 0.3, 1);
   letter-spacing: -0.01em;
   cursor: pointer;
}}
.vibe-btn-demo:hover {{
   background: rgba(255, 46, 62, 0.2);
   border-color: #FF2E3E;
   color: #ffffff !important;
   transform: translateY(-2px);
   box-shadow: 0 10px 25px rgba(255, 46, 62, 0.3);
}}
.vibe-btn-demo .vibe-play-circle {{
   width: 26px;
   height: 26px;
   border-radius: 50%;
   background: #FF2E3E;
   color: #ffffff;
   display: inline-flex;
   align-items: center;
   justify-content: center;
   font-size: 10px;
   padding-left: 2px;
   transition: transform 0.25s ease;
}}
.vibe-btn-demo:hover .vibe-play-circle {{
   transform: scale(1.15);
}}

/* Section 05 Live Demo Video Card */
.video-demo-card {{
   position: relative;
   border-radius: 16px;
   overflow: hidden;
   background: #0b0f17;
   border: 1px solid rgba(255, 255, 255, 0.1);
   box-shadow: 0 20px 40px rgba(0, 0, 0, 0.3);
   margin-bottom: 40px;
}}
.video-demo-inner {{
   position: relative;
   height: 360px;
   width: 100%;
   display: flex;
   align-items: center;
   justify-content: center;
   background-size: cover;
   background-position: center;
}}
.video-play-pulse {{
   width: 80px;
   height: 80px;
   border-radius: 50%;
   background: #FF2E3E;
   display: flex;
   align-items: center;
   justify-content: center;
   box-shadow: 0 0 0 14px rgba(255, 46, 62, 0.25), 0 12px 30px rgba(255, 46, 62, 0.45);
   transition: transform 0.3s cubic-bezier(0.16, 1, 0.3, 1), box-shadow 0.3s ease;
   cursor: pointer;
}}
.video-demo-card:hover .video-play-pulse {{
   transform: scale(1.1);
   box-shadow: 0 0 0 20px rgba(255, 46, 62, 0.35), 0 15px 35px rgba(255, 46, 62, 0.55);
}}
.video-play-trigger {{
   display: flex;
   flex-direction: column;
   align-items: center;
   gap: 18px;
   text-decoration: none !important;
}}

/* Magnific Popup Fade Animation */
.mfp-fade.mfp-bg {{
  opacity: 0;
  transition: all 0.25s ease-out;
}}
.mfp-fade.mfp-bg.mfp-ready {{
  opacity: 0.88;
}}
.mfp-fade.mfp-bg.mfp-removing {{
  opacity: 0;
}}
.mfp-fade.mfp-wrap .mfp-content {{
  opacity: 0;
  transform: scale(0.95);
  transition: all 0.25s ease-out;
}}
.mfp-fade.mfp-wrap.mfp-ready .mfp-content {{
  opacity: 1;
  transform: scale(1);
}}
.mfp-fade.mfp-wrap.mfp-removing .mfp-content {{
  opacity: 0;
  transform: scale(0.95);
}}

/* 02 - Problem Cards */
.problem-grid {{
   display: grid;
   grid-template-columns: 1fr;
   gap: 24px;
}}
@media (min-width: 768px) {{ .problem-grid {{ grid-template-columns: repeat(2, 1fr); }} }}
.problem-card {{
   background: #ffffff;
   border: 1px solid #fee2e2;
   border-radius: 12px;
   padding: 32px;
   box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.03);
   transition: transform 0.25s cubic-bezier(0.16, 1, 0.3, 1), box-shadow 0.25s ease;
}}
.problem-card:hover {{
   transform: translateY(-4px);
   box-shadow: 0 12px 24px -4px rgba(239, 68, 68, 0.12);
}}
.problem-badge {{
   display: inline-flex;
   align-items: center;
   gap: 6px;
   background: #fef2f2;
   color: #ef4444;
   font-family: 'Sora', sans-serif !important;
   font-size: 12px;
   font-weight: 700;
   padding: 4px 10px;
   border-radius: 6px;
   margin-bottom: 16px;
   letter-spacing: 0.5px;
   text-transform: uppercase;
}}
.problem-title {{
   font-family: 'Sora', sans-serif !important;
   font-size: 20px;
   font-weight: 700;
   color: #111827;
   margin-bottom: 10px;
   letter-spacing: -0.5px;
}}
.problem-desc {{
   font-family: 'Sora', sans-serif !important;
   font-size: 15px;
   font-weight: 400;
   color: #6b7280;
   line-height: 1.6;
   margin: 0;
   letter-spacing: -0.2px;
}}

/* 03 - Solution Box */
.solution-box {{
   background: #000000;
   color: #ffffff;
   border-radius: 16px;
   padding: 56px 48px;
   border: 1px solid rgba(255, 255, 255, 0.1);
   position: relative;
   overflow: hidden;
}}
.solution-title {{
   font-family: 'Sora', sans-serif !important;
   font-size: 34px;
   font-weight: 700;
   color: #ffffff;
   letter-spacing: -1px;
   margin-bottom: 16px;
   line-height: 1.2;
}}
.solution-desc {{
   font-family: 'Sora', sans-serif !important;
   font-size: 17px;
   font-weight: 300;
   color: #d1d5db;
   line-height: 1.7;
   max-width: 820px;
   margin: 0;
   letter-spacing: -0.2px;
}}

/* 04 - Outcome Cards */
.outcome-grid {{
   display: grid;
   grid-template-columns: 1fr;
   gap: 24px;
}}
@media (min-width: 768px) {{ .outcome-grid {{ grid-template-columns: repeat(3, 1fr); }} }}
.outcome-card {{
   background: #f9fafb;
   border: 1px solid #e5e7eb;
   border-radius: 12px;
   padding: 36px 28px;
   text-align: center;
   transition: transform 0.25s cubic-bezier(0.16, 1, 0.3, 1), box-shadow 0.25s ease;
}}
.outcome-card:hover {{
   transform: translateY(-4px);
   box-shadow: 0 10px 20px -2px rgba(0, 0, 0, 0.06);
}}
.outcome-stat {{
   font-family: 'Sora', sans-serif !important;
   font-size: 52px;
   font-weight: 800;
   color: #FF2E3E;
   line-height: 1;
   margin-bottom: 10px;
   letter-spacing: -2px;
}}
.outcome-title {{
   font-family: 'Sora', sans-serif !important;
   font-size: 18px;
   font-weight: 700;
   color: #111827;
   margin-bottom: 8px;
   letter-spacing: -0.4px;
}}
.outcome-desc {{
   font-family: 'Sora', sans-serif !important;
   font-size: 14px;
   font-weight: 400;
   color: #6b7280;
   line-height: 1.55;
   margin: 0;
   letter-spacing: -0.2px;
}}

/* 05 - Workflow Horizontal Flow */
.workflow-grid {{
   display: grid;
   grid-template-columns: 1fr;
   gap: 20px;
}}
@media (min-width: 992px) {{ .workflow-grid {{ grid-template-columns: repeat(5, 1fr); }} }}
.workflow-step-card {{
   background: #ffffff;
   border: 1px solid #e5e7eb;
   border-radius: 12px;
   padding: 28px 22px;
   position: relative;
   display: flex;
   flex-direction: column;
   transition: transform 0.25s cubic-bezier(0.16, 1, 0.3, 1), box-shadow 0.25s ease;
}}
.workflow-step-card:hover {{
   transform: translateY(-4px);
   box-shadow: 0 10px 20px -2px rgba(0, 0, 0, 0.06);
}}
.workflow-step-num {{
   font-family: 'Sora', sans-serif !important;
   font-size: 32px;
   font-weight: 800;
   color: #FF2E3E;
   line-height: 1;
   margin-bottom: 14px;
   letter-spacing: -1px;
}}
.workflow-step-title {{
   font-family: 'Sora', sans-serif !important;
   font-size: 16px;
   font-weight: 700;
   color: #111827;
   margin-bottom: 8px;
   letter-spacing: -0.4px;
}}
.workflow-step-desc {{
   font-family: 'Sora', sans-serif !important;
   font-size: 13px;
   font-weight: 400;
   color: #6b7280;
   line-height: 1.5;
   margin: 0;
   letter-spacing: -0.2px;
}}

/* 06 - Capabilities Grid */
.feature-light-grid {{ display: grid; gap: 24px; grid-template-columns: 1fr; }}
@media (min-width: 768px) {{ .feature-light-grid {{ grid-template-columns: repeat(2, 1fr); }} }}
@media (min-width: 1024px) {{ .feature-light-grid {{ grid-template-columns: repeat(3, 1fr); }} }}
.feature-light-card {{ 
   background: #ffffff; 
   padding: 38px 32px; 
   border-radius: 12px; 
   border: 1px solid #e5e7eb; 
   box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.04); 
   transition: box-shadow 0.25s ease, transform 0.25s cubic-bezier(0.16, 1, 0.3, 1); 
}}
.feature-light-card:hover {{ 
   box-shadow: 0 14px 28px -4px rgba(0, 0, 0, 0.09); 
   transform: translateY(-4px); 
}}
.fl-icon {{ font-size: 24px; color: #FF2E3E; margin-bottom: 16px; }}
.fl-title {{ 
   font-family: 'Sora', sans-serif !important; 
   font-size: 19px; 
   font-weight: 700; 
   color: #000000; 
   margin: 0 0 10px 0; 
   letter-spacing: -0.5px; 
}}
.fl-desc {{ 
   font-family: 'Sora', sans-serif !important; 
   color: #6b7280; 
   font-size: 14px; 
   font-weight: 400;
   line-height: 1.6; 
   margin: 0; 
   letter-spacing: -0.2px; 
}}

/* 07 - Tools Pills */
.tool-category-card {{
   background: #ffffff;
   border: 1px solid #e5e7eb;
   border-radius: 12px;
   padding: 34px;
   height: 100%;
}}
.tool-category-title {{
   font-family: 'Sora', sans-serif !important;
   font-size: 19px;
   font-weight: 700;
   color: #111827;
   margin-bottom: 16px;
   letter-spacing: -0.4px;
}}
.tool-pills-wrap {{
   display: flex;
   flex-wrap: wrap;
   gap: 10px;
}}
.tool-tag {{
   display: inline-flex;
   align-items: center;
   padding: 8px 16px;
   border-radius: 9999px;
   font-family: 'Sora', sans-serif !important;
   font-size: 14px;
   font-weight: 600;
   letter-spacing: -0.2px;
   transition: transform 0.2s ease;
}}
.tool-tag:hover {{
   transform: scale(1.03);
}}
.tool-tag-native {{
   background: #ecfdf5;
   border: 1px solid #a7f3d0;
   color: #065f46;
}}
.tool-tag-custom {{
   background: #fef2f2;
   border: 1px solid #fecaca;
   color: #991b1b;
}}

/* 08 - Portfolio Items */
.portfolio-grid {{
   display: grid;
   grid-template-columns: 1fr;
   gap: 32px;
}}
@media (min-width: 992px) {{ .portfolio-grid {{ grid-template-columns: repeat(3, 1fr); }} }}
.portfolio-item-card {{
   background: #ffffff;
   border: 1px solid #e5e7eb;
   border-radius: 12px;
   overflow: hidden;
   display: flex;
   flex-direction: column;
   box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.04);
   transition: transform 0.25s cubic-bezier(0.16, 1, 0.3, 1), box-shadow 0.25s ease;
}}
.portfolio-item-card:hover {{
   transform: translateY(-4px);
   box-shadow: 0 14px 28px -4px rgba(0, 0, 0, 0.09);
}}
.portfolio-item-img-wrap {{
   aspect-ratio: 16/10;
   background: #f3f4f6;
   overflow: hidden;
}}
.portfolio-item-img-wrap img {{
   width: 100%;
   height: 100%;
   object-fit: cover;
   transition: transform 0.4s ease;
}}
.portfolio-item-card:hover .portfolio-item-img-wrap img {{
   transform: scale(1.05);
}}
.portfolio-item-body {{
   padding: 26px;
   display: flex;
   flex-direction: column;
   gap: 12px;
   flex: 1;
}}
.portfolio-item-title {{
   font-family: 'Sora', sans-serif !important;
   font-size: 19px;
   font-weight: 700;
   color: #111827;
   margin: 0;
   letter-spacing: -0.4px;
}}
.portfolio-meta-row {{
   font-family: 'Sora', sans-serif !important;
   font-size: 13px;
   line-height: 1.55;
   color: #4b5563;
   letter-spacing: -0.2px;
}}
.portfolio-meta-label {{
   font-weight: 700;
   color: #111827;
   display: inline-block;
   margin-right: 4px;
}}

/* 09 - Reliability */
.reliability-grid {{
   display: grid;
   grid-template-columns: 1fr;
   gap: 20px;
}}
@media (min-width: 768px) {{ .reliability-grid {{ grid-template-columns: repeat(2, 1fr); }} }}
@media (min-width: 1024px) {{ .reliability-grid {{ grid-template-columns: repeat(3, 1fr); }} }}
.reliability-card {{
   background: #f9fafb;
   border: 1px solid #e5e7eb;
   border-radius: 12px;
   padding: 26px;
   transition: transform 0.25s cubic-bezier(0.16, 1, 0.3, 1);
}}
.reliability-card:hover {{
   transform: translateY(-3px);
}}
.reliability-card h4 {{
   font-family: 'Sora', sans-serif !important;
   font-size: 16px;
   font-weight: 700;
   color: #111827;
   margin-bottom: 8px;
   letter-spacing: -0.3px;
}}
.reliability-card p {{
   font-family: 'Sora', sans-serif !important;
   font-size: 13px;
   font-weight: 400;
   color: #6b7280;
   line-height: 1.55;
   margin: 0;
   letter-spacing: -0.2px;
}}

/* 10 - Implementation Process */
.process-grid {{
   display: grid;
   grid-template-columns: 1fr;
   gap: 16px;
}}
@media (min-width: 768px) {{ .process-grid {{ grid-template-columns: repeat(3, 1fr); }} }}
@media (min-width: 1024px) {{ .process-grid {{ grid-template-columns: repeat(6, 1fr); }} }}
.process-card {{
   background: #ffffff;
   border: 1px solid #e5e7eb;
   border-radius: 10px;
   padding: 22px 16px;
   text-align: center;
   transition: transform 0.25s cubic-bezier(0.16, 1, 0.3, 1);
}}
.process-card:hover {{
   transform: translateY(-3px);
}}
.process-num {{
   font-family: 'Sora', sans-serif !important;
   font-size: 26px;
   font-weight: 800;
   color: #FF2E3E;
   line-height: 1;
   margin-bottom: 8px;
   letter-spacing: -1px;
}}
.process-title {{
   font-family: 'Sora', sans-serif !important;
   font-size: 14px;
   font-weight: 700;
   color: #111827;
   margin-bottom: 6px;
   letter-spacing: -0.3px;
}}
.process-desc {{
   font-family: 'Sora', sans-serif !important;
   font-size: 12px;
   font-weight: 400;
   color: #6b7280;
   line-height: 1.45;
   margin: 0;
   letter-spacing: -0.2px;
}}

/* 11 - Scope Split */
.scope-grid {{
   display: grid;
   grid-template-columns: 1fr;
   gap: 24px;
}}
@media (min-width: 768px) {{ .scope-grid {{ grid-template-columns: repeat(2, 1fr); }} }}
.scope-card {{
   background: #ffffff;
   border: 1px solid #e5e7eb;
   border-radius: 12px;
   padding: 34px;
}}
.scope-card h4 {{
   font-family: 'Sora', sans-serif !important;
   font-size: 19px;
   font-weight: 700;
   color: #111827;
   margin-bottom: 18px;
   letter-spacing: -0.4px;
}}
.scope-list {{
   list-style: none;
   padding: 0;
   margin: 0;
   display: flex;
   flex-direction: column;
   gap: 12px;
}}
.scope-list li {{
   font-family: 'Sora', sans-serif !important;
   font-size: 14px;
   font-weight: 400;
   color: #4b5563;
   display: flex;
   align-items: flex-start;
   gap: 10px;
   letter-spacing: -0.2px;
}}
.scope-list li i {{
   margin-top: 3px;
}}

/* 12 - Website Native FAQ Accordion */
.fv-faq-modern-accordion .fv-faq-modern-item {{
  background: transparent !important;
  border: none !important;
  border-bottom: 1px solid #e5e7eb !important;
  border-radius: 0 !important;
  padding: 24px 0 !important;
  margin-bottom: 0 !important;
  box-shadow: none !important;
  cursor: pointer;
}}
.fv-faq-modern-accordion .fv-faq-modern-item:last-child {{
  border-bottom: none !important;
}}
.fv-faq-modern-header {{
  display: flex !important;
  align-items: center !important;
  justify-content: space-between !important;
  cursor: pointer;
}}
.fv-faq-modern-header h3 {{
  color: #000000 !important;
  font-family: 'Sora', sans-serif !important;
  font-size: 18px !important;
  font-weight: 600 !important;
  margin: 0 !important;
  letter-spacing: -0.3px !important;
  transition: color 0.3s ease !important;
}}
.fv-faq-modern-header .fa {{
  color: #000000 !important;
  font-size: 16px !important;
  transition: transform 0.3s ease, color 0.3s ease !important;
}}
.fv-faq-modern-content {{
  max-height: 0;
  opacity: 0;
  overflow: hidden;
  transition: all 0.4s ease;
  transform: translateY(-8px);
}}
.fv-faq-modern-content p {{
  color: #6b7280 !important;
  font-family: 'Sora', sans-serif !important;
  font-size: 15px !important;
  font-weight: 400 !important;
  line-height: 1.65 !important;
  margin: 0 !important;
  padding-top: 14px !important;
  letter-spacing: -0.2px !important;
}}
.fv-faq-modern-accordion .fv-faq-item.active .fv-faq-header h3 {{
  color: #FF2E3E !important;
}}
.fv-faq-modern-accordion .fv-faq-item.active .fv-faq-header .fa {{
  color: #FF2E3E !important;
  transform: rotate(180deg) !important;
}}
.fv-faq-modern-accordion .fv-faq-item.active .fv-faq-content {{
  max-height: 400px;
  opacity: 1;
  transform: translateY(0);
}}
</style>

<!-- Techtox ENTITY SCHEMA -->
<script type="application/ld+json">
{{
  "@context": "https://schema.org",
  "@type": ["Service", "WebPage"],
  "name": "{s['h1']}",
  "provider": {{
    "@type": "Organization",
    "name": "Techtox",
    "url": "https://techtox.com"
  }},
  "description": "{s['meta_desc']}"
}}
</script>

    <!-- FAVICON -->
    <link rel="icon" type="image/png" href="../img/favicon.png">
    <link rel="shortcut icon" href="../img/favicon.ico">
</head>
<body>

   <!-- NAVIGATION -->
   <nav id="navigration" class="navbar fixed-top p-0">
      <div class="container">
         <a class="logo d-flex align-items-center" href="../index.html" style="text-decoration: none;"><img src="../img/logo.png" alt="Techtox Logo" style="height: 45px; width: auto;"></a>
         <div class="sidenav">
            <div class="header">
               <a class="logo d-lg-none d-flex align-items-center" href="../index.html" style="text-decoration: none;"><img src="../img/logo.png" alt="Techtox Logo" style="height: 45px; width: auto;"></a>
               <a href="#" class="d-lg-none" id="showsidenav"><i class="fa fa-times" style="font-size: 28px; color: #ffffff; cursor: pointer;"></i></a>
            </div>
             <ul class="mb-0 position-relative d-lg-flex align-items-center" id="main-nav-list">
                <li class="nav-item"><a class="nav-link" href="../index.html">Home</a></li>
                <li class="nav-item dropdown active">
                   <a class="nav-link dropdown-toggle" data-toggle="collapse" href="#servicesDropdown" aria-expanded="false" aria-haspopup="true">Services <i class="fa fa-angle-down"></i></a>

<div id="servicesDropdown" class="dropdown-menus collapse" style="padding:0; border:none; box-shadow:none; background:transparent;">
   <ul class="nested-services-menu">
       
       <li class="dropdown-submenu">
           <a class="dropdown-item nested-item" href="#">
               <span><i class="fa fa-code" style="width:20px; color:#FF2E3E; margin-right:8px; display:inline-block; text-align:center;"></i> Development</span>
               <i class="fa fa-angle-right" style="color: #9ca3af;"></i>
           </a>
           <ul class="dropdown-menu">
               <li><a class="dropdown-item nested-subitem" href="../services/web-applications.html"><i class="fal fa-globe" style="width:20px; color:#FF2E3E; margin-right:8px; display:inline-block; text-align:center;"></i> Web Applications</a></li>
               <li><a class="dropdown-item nested-subitem" href="../services/api-software-integration.html"><i class="fal fa-plug" style="width:20px; color:#FF2E3E; margin-right:8px; display:inline-block; text-align:center;"></i> API & Integrations</a></li>
               <li><a class="dropdown-item nested-subitem" href="../services/wordpress-solutions.html"><i class="fab fa-wordpress" style="width:20px; color:#FF2E3E; margin-right:8px; display:inline-block; text-align:center;"></i> WordPress Solutions</a></li>
               <li><a class="dropdown-item nested-subitem" href="../services/shopify-stores.html"><i class="fab fa-shopify" style="width:20px; color:#FF2E3E; margin-right:8px; display:inline-block; text-align:center;"></i> Shopify Stores</a></li>
               <li><a class="dropdown-item nested-subitem" href="../services/desktop-applications.html"><i class="fal fa-desktop" style="width:20px; color:#FF2E3E; margin-right:8px; display:inline-block; text-align:center;"></i> Desktop Apps</a></li>
           </ul>
       </li>

       <li class="dropdown-submenu">
           <a class="dropdown-item nested-item" href="#">
               <span><i class="fal fa-robot" style="width:20px; color:#FF2E3E; margin-right:8px; display:inline-block; text-align:center;"></i> Automation</span>
               <i class="fa fa-angle-right" style="color: #9ca3af;"></i>
           </a>
           <ul class="dropdown-menu">
               <li><a class="dropdown-item nested-subitem" href="../services/lead-crm-automation.html"><i class="fal fa-filter" style="width:20px; color:#FF2E3E; margin-right:8px; display:inline-block; text-align:center;"></i> Lead & CRM Automation</a></li>
               <li><a class="dropdown-item nested-subitem" href="../services/appointment-follow-up-automation.html"><i class="fal fa-calendar-check" style="width:20px; color:#FF2E3E; margin-right:8px; display:inline-block; text-align:center;"></i> Appointment & Follow-up</a></li>
               <li><a class="dropdown-item nested-subitem" href="../services/ai-customer-support.html"><i class="fal fa-headset" style="width:20px; color:#FF2E3E; margin-right:8px; display:inline-block; text-align:center;"></i> AI Customer Support</a></li>
               <li><a class="dropdown-item nested-subitem" href="../services/custom-dashboards.html"><i class="fal fa-chart-pie" style="width:20px; color:#FF2E3E; margin-right:8px; display:inline-block; text-align:center;"></i> Reporting & Dashboards</a></li>
               <li><a class="dropdown-item nested-subitem" href="../services/api-software-integration.html"><i class="fal fa-plug" style="width:20px; color:#FF2E3E; margin-right:8px; display:inline-block; text-align:center;"></i> API & Integrations</a></li>
               <li><a class="dropdown-item nested-subitem" href="../services/ai-voice-workflow-agents.html"><i class="fal fa-robot" style="width:20px; color:#FF2E3E; margin-right:8px; display:inline-block; text-align:center;"></i> Voice & Workflow Agents</a></li>
           </ul>
       </li>
       
       <li class="dropdown-submenu">
           <a class="dropdown-item nested-item" href="#">
               <span><i class="fa fa-paint-brush" style="width:20px; color:#FF2E3E; margin-right:8px; display:inline-block; text-align:center;"></i> Creative</span>
               <i class="fa fa-angle-right" style="color: #9ca3af;"></i>
           </a>
           <ul class="dropdown-menu">
               <li><a class="dropdown-item nested-subitem" href="../services/ui-ux-design.html"><i class="fa fa-mobile-alt" style="width:20px; color:#FF2E3E; margin-right:8px; display:inline-block; text-align:center;"></i> UI/UX Design</a></li>
               <li><a class="dropdown-item nested-subitem" href="../services/graphic-design.html"><i class="fa fa-pen-nib" style="width:20px; color:#FF2E3E; margin-right:8px; display:inline-block; text-align:center;"></i> Graphic Design</a></li>
               <li><a class="dropdown-item nested-subitem" href="../services/video-editing.html"><i class="fa fa-video" style="width:20px; color:#FF2E3E; margin-right:8px; display:inline-block; text-align:center;"></i> Video Editing</a></li>
               <li><a class="dropdown-item nested-subitem" href="../services/social-media-design.html"><i class="fa fa-share-alt" style="width:20px; color:#FF2E3E; margin-right:8px; display:inline-block; text-align:center;"></i> Social Media Design</a></li>
               <li><a class="dropdown-item nested-subitem" href="../services/3d-vfx.html"><i class="fa fa-cube" style="width:20px; color:#FF2E3E; margin-right:8px; display:inline-block; text-align:center;"></i> 3D & VFX</a></li>
           </ul>
       </li>

       <li class="dropdown-submenu">
           <a class="dropdown-item nested-item" href="#">
               <span><i class="fa fa-bullhorn" style="width:20px; color:#FF2E3E; margin-right:8px; display:inline-block; text-align:center;"></i> Marketing</span>
               <i class="fa fa-angle-right" style="color: #9ca3af;"></i>
           </a>
           <ul class="dropdown-menu">
               <li><a class="dropdown-item nested-subitem" href="../services/linkedin-growth.html"><i class="fab fa-linkedin" style="width:20px; color:#FF2E3E; margin-right:8px; display:inline-block; text-align:center;"></i> LinkedIn Growth</a></li>
               <li><a class="dropdown-item nested-subitem" href="../services/digital-marketing.html"><i class="fa fa-ad" style="width:20px; color:#FF2E3E; margin-right:8px; display:inline-block; text-align:center;"></i> Digital Marketing</a></li>
               <li><a class="dropdown-item nested-subitem" href="../services/email-marketing.html"><i class="fa fa-envelope-open-text" style="width:20px; color:#FF2E3E; margin-right:8px; display:inline-block; text-align:center;"></i> Email Marketing</a></li>
               <li><a class="dropdown-item nested-subitem" href="../services/freelancing-platform-management.html"><i class="fa fa-briefcase" style="width:20px; color:#FF2E3E; margin-right:8px; display:inline-block; text-align:center;"></i> Platform Management</a></li>
           </ul>
       </li>

       <li><hr class="dropdown-divider" style="margin: 8px 0; border-top: 1px solid #e5e7eb;"></li>
       <li>
           <a class="dropdown-item nested-item" href="../services.html" style="color: #FF2E3E !important; font-weight: 600 !important; justify-content: flex-start !important;">
               <i class="fa fa-arrow-right" style="width:20px; margin-right:8px;"></i> Explore All Services
           </a>
       </li>
   </ul>
</div>

                </li>
                <li class="nav-item dropdown">
                   <a class="nav-link dropdown-toggle" data-toggle="collapse" href="#industriesDropdown" aria-expanded="false" aria-haspopup="true">Industries <i class="fa fa-angle-down"></i></a>
                   <div id="industriesDropdown" class="dropdown-menus collapse" style="padding: 15px; border-radius: 8px; box-shadow: 0 10px 25px rgba(0,0,0,0.1); border: 1px solid #e5e7eb; min-width: 260px; background: #ffffff;">
                       <a class="dropdown-item" href="../industries/real-estate.html" style="padding: 10px; font-weight: 500; font-size: 15px;"><i class="fa fa-building" style="width:20px; color:#FF2E3E; margin-right:8px; display:inline-block; text-align:center;"></i> Real Estate</a>
                       <a class="dropdown-item" href="../industries/b2b-saas.html" style="padding: 10px; font-weight: 500; font-size: 15px;"><i class="fa fa-cloud" style="width:20px; color:#FF2E3E; margin-right:8px; display:inline-block; text-align:center;"></i> B2B SaaS</a>
                       <a class="dropdown-item" href="../industries/ecommerce.html" style="padding: 10px; font-weight: 500; font-size: 15px;"><i class="fa fa-shopping-cart" style="width:20px; color:#FF2E3E; margin-right:8px; display:inline-block; text-align:center;"></i> E-Commerce</a>
                       <a class="dropdown-item" href="../industries/legal.html" style="padding: 10px; font-weight: 500; font-size: 15px;"><i class="fa fa-balance-scale" style="width:20px; color:#FF2E3E; margin-right:8px; display:inline-block; text-align:center;"></i> Legal Practices</a>
                       <a class="dropdown-item" href="../industries/healthcare.html" style="padding: 10px; font-weight: 500; font-size: 15px;"><i class="fa fa-heartbeat" style="width:20px; color:#FF2E3E; margin-right:8px; display:inline-block; text-align:center;"></i> Healthcare</a>
                       <a class="dropdown-item" href="../industries/financial.html" style="padding: 10px; font-weight: 500; font-size: 15px;"><i class="fa fa-chart-line" style="width:20px; color:#FF2E3E; margin-right:8px; display:inline-block; text-align:center;"></i> Financial Services</a>
                   </div>
                </li>
                <li class="nav-item"><a class="nav-link" href="../about.html">About</a></li>
                <li class="nav-item"><a class="nav-link" href="../faq.html">FAQ</a></li>
                <li class="nav-item"><a class="nav-link" href="../contact.html">Contact</a></li>
             </ul>
         </div>
         <a href="../contact.html" class="fv-nav-circle d-none d-md-flex" aria-label="Let's Connect">
            <i class="fa fa-arrow-right arrow-main"></i>
            <i class="fa fa-arrow-right arrow-hover"></i>
         </a>
         <div id="hamburger" class="d-lg-none"><i class="fa fa-bars" style="font-size: 28px; color: #ffffff; cursor: pointer;"></i></div>
      </div>
   </nav>

   <!-- =============================================================
        01 — HERO SECTION
   ============================================================= -->
   <section class="fv-page-hero" style="background-image: linear-gradient(rgba(17, 24, 39, 0.88), rgba(17, 24, 39, 0.96)), url('{s['hero_img']}'); background-size: cover; background-position: center; border-bottom: 1px solid #000000;">
      <div class="container text-center">
         <span class="fv-eyebrow wow fadeInUp" data-wow-delay="0.1s">{s['eyebrow']}</span>
         <h1 class="wow fadeInUp" data-wow-delay="0.2s">{s['h1']}</h1>
         <p class="fv-lead wow fadeInUp" data-wow-delay="0.3s">{s['hero_desc']}</p>
         <div class="d-flex justify-content-center align-items-center flex-wrap wow fadeInUp" data-wow-delay="0.4s" style="gap: 16px; margin-top: 32px;">
            <a href="../contact.html" class="fv-dual-btn">
               <span class="fv-btn-pill">DISCUSS YOUR WORKFLOW</span>
               <div class="fv-btn-circle">
                  <i class="fa fa-arrow-right arrow-main"></i>
                  <i class="fa fa-arrow-right arrow-hover"></i>
               </div>
            </a>
            <a href="{s['demo_video_url']}" class="popup-youtube vibe-btn-demo" target="_blank" rel="noopener noreferrer">
               <span class="vibe-play-circle"><i class="fa fa-play"></i></span>
               <span>View Demo</span>
            </a>
         </div>
      </div>
   </section>

   <!-- =============================================================
        02 — THE PROBLEM
   ============================================================= -->
   <section class="py-5" style="background-color: #ffffff; padding-top: 80px !important; padding-bottom: 80px !important; border-bottom: 1px solid #f3f4f6;">
      <div class="container">
         <div class="mb-5 d-flex flex-column align-items-start wow fadeInUp" style="gap: 10px;">
            <span class="vibe-eyebrow">THE OPERATIONAL FRICTION</span>
            <h2 class="vibe-heading">What's Slowing Down Your Operations?</h2>
            <p class="vibe-lead">Common bottlenecks businesses face prior to implementing structured workflow automation.</p>
         </div>
         <div class="problem-grid">
{problems_html}         </div>
      </div>
   </section>

   <!-- =============================================================
        03 — THE SOLUTION
   ============================================================= -->
   <section class="py-5" style="background-color: #f9fafb; padding-top: 80px !important; padding-bottom: 80px !important; border-bottom: 1px solid #e5e7eb;">
      <div class="container">
         <div class="solution-box wow fadeInUp" data-wow-delay="0.1s">
            <span style="color: #FF2E3E; font-family: 'Sora', sans-serif !important; font-size: 13px; font-weight: 700; letter-spacing: 2px; text-transform: uppercase; margin-bottom: 12px; display: inline-block;">THE ARCHITECTED SOLUTION</span>
            <h2 class="solution-title">{s['solution']['title']}</h2>
            <p class="solution-desc">{s['solution']['desc']}</p>
         </div>
      </div>
   </section>

   <!-- =============================================================
        04 — OUTCOMES
   ============================================================= -->
   <section class="py-5" style="background-color: #ffffff; padding-top: 80px !important; padding-bottom: 80px !important; border-bottom: 1px solid #f3f4f6;">
      <div class="container">
         <div class="text-center mb-5 pb-2 mx-auto wow fadeInUp" style="max-width: 700px;">
            <span class="vibe-eyebrow">TANGIBLE BUSINESS RESULTS</span>
            <h2 class="vibe-heading">Predictable Operational Outcomes</h2>
            <p class="vibe-lead">Measurable efficiency gains achieved by replacing manual processes with automated pipelines.</p>
         </div>
         <div class="outcome-grid">
{outcomes_html}         </div>
      </div>
   </section>

   <!-- =============================================================
        05 — HOW IT WORKS & DEMO VIDEO
   ============================================================= -->
   <section class="py-5" id="how-it-works" style="background-color: #f9fafb; padding-top: 80px !important; padding-bottom: 80px !important; border-bottom: 1px solid #e5e7eb;">
      <div class="container">
         <div class="mb-5 d-flex flex-column align-items-start wow fadeInUp" style="gap: 10px;">
            <span class="vibe-eyebrow">OPERATIONAL BLUEPRINT</span>
            <h2 class="vibe-heading">How It Works & Live Architecture</h2>
            <p class="vibe-lead">Watch the end-to-end workflow walkthrough or inspect the structured 5-step operational pipeline below.</p>
         </div>

         <!-- Live Demo Video Card -->
         <div class="video-demo-card wow fadeInUp" data-wow-delay="0.15s">
            <div class="video-demo-inner" style="background-image: linear-gradient(rgba(11, 15, 23, 0.72), rgba(11, 15, 23, 0.88)), url('{s['hero_img']}');">
               <a href="{s['demo_video_url']}" class="popup-youtube video-play-trigger" target="_blank" rel="noopener noreferrer">
                  <div class="video-play-pulse">
                     <i class="fa fa-play" style="color: #ffffff; font-size: 26px; margin-left: 4px;"></i>
                  </div>
                  <div class="text-center">
                     <span style="display: block; color: #ffffff; font-family: 'Sora', sans-serif !important; font-size: 20px; font-weight: 700; letter-spacing: -0.4px;">Watch {s['h1']} Live Demo</span>
                     <span style="display: inline-flex; align-items: center; gap: 6px; color: #d1d5db; font-family: 'Sora', sans-serif !important; font-size: 14px; font-weight: 400; margin-top: 6px;">
                        <i class="fa fa-play-circle" style="color: #FF2E3E;"></i> Click to launch live video walkthrough
                     </span>
                  </div>
               </a>
            </div>
         </div>

         <div class="workflow-grid">
{workflow_html}         </div>
      </div>
   </section>

   <!-- =============================================================
        06 — CAPABILITIES INCLUDED
   ============================================================= -->
   <section class="py-5" id="capabilities" style="background-color: #ffffff; padding-top: 80px !important; padding-bottom: 80px !important; border-bottom: 1px solid #f3f4f6;">
      <div class="container">
         <div class="text-center mb-5 pb-2 mx-auto wow fadeInUp" style="max-width: 700px;">
            <span class="vibe-eyebrow">INCLUDED IN SCOPE</span>
            <h2 class="vibe-heading">Engineered Capabilities</h2>
            <p class="vibe-lead">Everything built, tested, and integrated when you deploy {s['h1']}.</p>
         </div>
         <div class="feature-light-grid">
{capabilities_html}         </div>
      </div>
   </section>

   <!-- =============================================================
        07 — TOOLS & INTEGRATIONS
   ============================================================= -->
   <section class="py-5" style="background-color: #f9fafb; padding-top: 80px !important; padding-bottom: 80px !important; border-bottom: 1px solid #e5e7eb;">
      <div class="container">
         <div class="mb-5 d-flex flex-column align-items-start wow fadeInUp" style="gap: 10px;">
            <span class="vibe-eyebrow">TECHNOLOGY STACK</span>
            <h2 class="vibe-heading">Supported Platforms & Integrations</h2>
            <p class="vibe-lead">We integrate directly with your existing software stack using native connectors or custom API endpoints.</p>
         </div>
         
         <div class="row">
            <div class="col-lg-6 mb-4 mb-lg-0 wow fadeInLeft" data-wow-delay="0.1s">
               <div class="tool-category-card">
                  <h4 class="tool-category-title">Popular Native & Supported Platforms</h4>
                  <p style="font-family: 'Sora', sans-serif !important; font-size: 14px; color: #6b7280; line-height: 1.5; margin-bottom: 20px;">
                     Pre-built connectors with full two-way data sync capabilities for market-leading platforms.
                  </p>
                  <div class="tool-pills-wrap">
                     {native_tools_pills}
                  </div>
               </div>
            </div>
            
            <div class="col-lg-6 wow fadeInRight" data-wow-delay="0.1s">
               <div class="tool-category-card">
                  <h4 class="tool-category-title">Custom Middleware & Automation Engines</h4>
                  <p style="font-family: 'Sora', sans-serif !important; font-size: 14px; color: #6b7280; line-height: 1.5; margin-bottom: 20px;">
                     Advanced integration engines, custom webhook pipelines, and resilient middleware tailored to your custom logic.
                  </p>
                  <div class="tool-pills-wrap">
                     {custom_tools_pills}
                  </div>
               </div>
            </div>
         </div>
      </div>
   </section>

   <!-- =============================================================
        08 — OPERATIONAL IMPLEMENTATIONS / PORTFOLIO
   ============================================================= -->
   <section class="py-5" id="portfolio" style="background-color: #ffffff; padding-top: 80px !important; padding-bottom: 80px !important; border-bottom: 1px solid #f3f4f6;">
      <div class="container">
         <div class="mb-5 d-flex flex-column align-items-start wow fadeInUp" style="gap: 10px;">
            <span class="vibe-eyebrow">OPERATIONAL EVIDENCE</span>
            <h2 class="vibe-heading">Recent Deployments & Architectures</h2>
            <p class="vibe-lead">Production-tested workflows engineered to eliminate friction in live client environments.</p>
         </div>
         <div class="portfolio-grid">
{portfolio_html}         </div>
      </div>
   </section>

   <!-- =============================================================
        09 — RELIABILITY & HUMAN OVERSIGHT
   ============================================================= -->
   <section class="py-5" style="background-color: #f9fafb; padding-top: 80px !important; padding-bottom: 80px !important; border-bottom: 1px solid #e5e7eb;">
      <div class="container">
         <div class="mb-5 d-flex flex-column align-items-start wow fadeInUp" style="gap: 10px;">
            <span class="vibe-eyebrow">FAIL-SAFE ARCHITECTURE</span>
            <h2 class="vibe-heading">Reliability, Error Handling & Oversight</h2>
            <p class="vibe-lead">Automations engineered with strict validation, automatic retries, and immediate human escalation.</p>
         </div>
         
         <div class="reliability-grid">
            <div class="reliability-card wow fadeInUp" data-wow-delay="0.05s">
               <h4><i class="fa fa-shield-alt text-danger mr-2"></i> Payload Schema Validation</h4>
               <p>Every incoming webhook is verified against expected data schemas before processing to filter malformed payloads.</p>
            </div>
            <div class="reliability-card wow fadeInUp" data-wow-delay="0.1s">
               <h4><i class="fa fa-redo text-danger mr-2"></i> Exponential Backoff Retries</h4>
               <p>If a destination API is temporarily down, requests automatically queue and retry exponentially without data loss.</p>
            </div>
            <div class="reliability-card wow fadeInUp" data-wow-delay="0.15s">
               <h4><i class="fa fa-file-alt text-danger mr-2"></i> Dead-Letter Audit Logs</h4>
               <p>Comprehensive execution logs record every transaction ID, payload timestamp, and response code for 30 days.</p>
            </div>
            <div class="reliability-card wow fadeInUp" data-wow-delay="0.2s">
               <h4><i class="fa fa-key text-danger mr-2"></i> Encrypted Credentials</h4>
               <p>OAuth 2.0 tokens and API keys are stored in encrypted client environment vaults—never exposed in client code.</p>
            </div>
            <div class="reliability-card wow fadeInUp" data-wow-delay="0.25s">
               <h4><i class="fa fa-bell text-danger mr-2"></i> Slack Anomaly Alerts</h4>
               <p>If an unrecoverable exception occurs, instant alerts notify our engineering channel and your team lead immediately.</p>
            </div>
            <div class="reliability-card wow fadeInUp" data-wow-delay="0.3s">
               <h4><i class="fa fa-user-check text-danger mr-2"></i> Human-in-the-Loop Triggers</h4>
               <p>Edge cases or flagged VIP accounts automatically route to human representatives before automated actions execute.</p>
            </div>
         </div>
      </div>
   </section>

   <!-- =============================================================
        10 — IMPLEMENTATION PROCESS
   ============================================================= -->
   <section class="py-5" style="background-color: #ffffff; padding-top: 80px !important; padding-bottom: 80px !important; border-bottom: 1px solid #f3f4f6;">
      <div class="container">
         <div class="text-center mb-5 pb-2 mx-auto wow fadeInUp" style="max-width: 700px;">
            <span class="vibe-eyebrow">DEPLOYMENT METHODOLOGY</span>
            <h2 class="vibe-heading">Our 6-Stage Delivery Process</h2>
            <p class="vibe-lead">A structured engineering process from initial workflow audit to production deployment.</p>
         </div>
         
         <div class="process-grid">
            <div class="process-card wow fadeInUp" data-wow-delay="0.05s">
               <div class="process-num">01</div>
               <div class="process-title">Discovery</div>
               <div class="process-desc">Audit current workflows, data fields, and bottlenecks.</div>
            </div>
            <div class="process-card wow fadeInUp" data-wow-delay="0.1s">
               <div class="process-num">02</div>
               <div class="process-title">Architecture</div>
               <div class="process-desc">Map logic trees, data schemas, and failovers.</div>
            </div>
            <div class="process-card wow fadeInUp" data-wow-delay="0.15s">
               <div class="process-num">03</div>
               <div class="process-title">Build</div>
               <div class="process-desc">Configure connectors, scripts, and endpoints.</div>
            </div>
            <div class="process-card wow fadeInUp" data-wow-delay="0.2s">
               <div class="process-num">04</div>
               <div class="process-title">QA & Testing</div>
               <div class="process-desc">Simulate edge cases, traffic spikes, and payload errors.</div>
            </div>
            <div class="process-card wow fadeInUp" data-wow-delay="0.25s">
               <div class="process-num">05</div>
               <div class="process-title">Deployment</div>
               <div class="process-desc">Switch endpoints live with active monitoring.</div>
            </div>
            <div class="process-card wow fadeInUp" data-wow-delay="0.3s">
               <div class="process-num">06</div>
               <div class="process-title">Handover</div>
               <div class="process-desc">Documentation handover and team onboarding.</div>
            </div>
         </div>
      </div>
   </section>

   <!-- =============================================================
        11 — SCOPE & REQUIREMENTS
   ============================================================= -->
   <section class="py-5" style="background-color: #f9fafb; padding-top: 80px !important; padding-bottom: 80px !important; border-bottom: 1px solid #e5e7eb;">
      <div class="container">
         <div class="mb-5 d-flex flex-column align-items-start wow fadeInUp" style="gap: 10px;">
            <span class="vibe-eyebrow">CLEAR BOUNDARIES</span>
            <h2 class="vibe-heading">Scope & Requirements</h2>
            <p class="vibe-lead">Transparent expectations regarding deliverables, client inputs, and ownership.</p>
         </div>
         
         <div class="scope-grid">
            <div class="scope-card wow fadeInLeft" data-wow-delay="0.1s">
               <h4><i class="fa fa-check text-danger mr-2"></i> What Is Included</h4>
               <ul class="scope-list">
                  <li><i class="fa fa-check text-success"></i> Full architectural diagram and data schema documentation</li>
                  <li><i class="fa fa-check text-success"></i> Custom webhook endpoints and API integrations</li>
                  <li><i class="fa fa-check text-success"></i> Complete error-handling and dead-letter retry queues</li>
                  <li><i class="fa fa-check text-success"></i> Team chat notifications (Slack or Microsoft Teams)</li>
                  <li><i class="fa fa-check text-success"></i> 14-day post-launch hypercare monitoring and support</li>
               </ul>
            </div>
            
            <div class="scope-card wow fadeInRight" data-wow-delay="0.1s">
               <h4><i class="fa fa-info-circle text-danger mr-2"></i> Client Requirements & Ownership</h4>
               <ul class="scope-list">
                  <li><i class="fa fa-arrow-right text-muted"></i> Client owns all third-party software accounts (Zero lock-in)</li>
                  <li><i class="fa fa-arrow-right text-muted"></i> Admin or developer API access to relevant platforms</li>
                  <li><i class="fa fa-arrow-right text-muted"></i> Provisioning of sample test data and expected field formats</li>
                  <li><i class="fa fa-arrow-right text-muted"></i> Designation of a primary team contact for feedback</li>
                  <li><i class="fa fa-arrow-right text-muted"></i> Complex custom database migrations quoted as separate scope</li>
               </ul>
            </div>
         </div>
      </div>
   </section>

   <!-- =============================================================
        12 — FAQS (EXACT NATIVE ACCORDION WITH ANIMATION)
   ============================================================= -->
   <section class="py-5" style="background-color: #ffffff; padding-top: 80px !important; padding-bottom: 80px !important; border-bottom: 1px solid #f3f4f6;">
      <div class="container" style="max-width: 860px;">
         <div class="text-center mb-5 pb-2 mx-auto wow fadeInUp">
            <span class="vibe-eyebrow">COMMON QUESTIONS</span>
            <h2 class="vibe-heading">Frequently Asked Questions</h2>
            <p class="vibe-lead">Practical answers regarding implementation, maintenance, security, and timelines.</p>
         </div>
         
         <!-- NATIVE ACCORDION CONTAINER -->
         <div class="fv-faq-modern-accordion">
{faqs_html}         </div>
      </div>
   </section>

   <!-- =============================================================
        13 — FINAL CTA (SPLIT)
   ============================================================= -->
   <section class="fv-cta-split py-5" id="contactArea" style="position: relative; overflow: hidden;">
      <img src="../img/cta_bg_2.webp" alt="Abstract Background" loading="lazy" class="wow fadeIn" data-wow-duration="1.5s" style="position: absolute; inset: 0; width: 100%; height: 100%; object-fit: cover; z-index: 0;">
      <div style="position:absolute; inset:0; background: linear-gradient(90deg, rgba(17,24,39,0.95) 0%, rgba(17,24,39,0.7) 100%); z-index:0;"></div>
      
      <div class="container" style="position:relative; z-index:1; padding-top: 100px; padding-bottom: 100px;">
         <div class="row align-items-center">
            
            <div class="col-lg-6 mb-5 mb-lg-0 pr-lg-5 wow fadeInLeft" data-wow-delay="0.1s">
               <h2 class="fw-bold mb-4" style="color: #ffffff; font-family: 'Sora', sans-serif !important; font-size: 56px; line-height: 1.1; letter-spacing: -1.5px;">
                  Ready to eliminate operational friction?
               </h2>
               <p style="color: #d1d5db; font-family: 'Sora', sans-serif !important; font-size: 18px; line-height: 1.6; max-width: 500px; margin-bottom: 40px; letter-spacing: -0.2px;">
                  Tell us where your team is losing hours to repetitive work or disconnected tools. We will design a clean, reliable automation pipeline built around your business.
               </p>
               <a href="../contact.html" class="fv-dual-btn">
                  <span class="fv-btn-pill">REQUEST A WORKFLOW AUDIT</span>
                  <div class="fv-btn-circle">
                     <i class="fa fa-arrow-right arrow-main"></i>
                     <i class="fa fa-arrow-right arrow-hover"></i>
                  </div>
               </a>
            </div>

            <div class="col-lg-5 offset-lg-1 wow fadeInRight" data-wow-delay="0.2s">
               <ul class="cta-check-list list-unstyled m-0">
                  <li class="d-flex align-items-center mb-4 pb-2">
                     <i class="fa fa-check text-white mr-4" style="font-size: 22px;"></i>
                     <span style="color: #ffffff; font-family: 'Sora', sans-serif !important; font-size: 20px; font-weight: 600; letter-spacing: -0.3px;">Clear Operational ROI</span>
                  </li>
                  <li class="d-flex align-items-center mb-4 pb-2">
                     <i class="fa fa-check text-white mr-4" style="font-size: 22px;"></i>
                     <span style="color: #ffffff; font-family: 'Sora', sans-serif !important; font-size: 20px; font-weight: 600; letter-spacing: -0.3px;">Zero Vendor Lock-in (You Own the System)</span>
                  </li>
                  <li class="d-flex align-items-center mb-4 pb-2">
                     <i class="fa fa-check text-white mr-4" style="font-size: 22px;"></i>
                     <span style="color: #ffffff; font-family: 'Sora', sans-serif !important; font-size: 20px; font-weight: 600; letter-spacing: -0.3px;">Robust Error-Handling & Fallbacks</span>
                  </li>
                  <li class="d-flex align-items-center mb-4 pb-2">
                     <i class="fa fa-check text-white mr-4" style="font-size: 22px;"></i>
                     <span style="color: #ffffff; font-family: 'Sora', sans-serif !important; font-size: 20px; font-weight: 600; letter-spacing: -0.3px;">Full Team Onboarding & Documentation</span>
                  </li>
                  <li class="d-flex align-items-center">
                     <i class="fa fa-check text-white mr-4" style="font-size: 22px;"></i>
                     <span style="color: #ffffff; font-family: 'Sora', sans-serif !important; font-size: 20px; font-weight: 600; letter-spacing: -0.3px;">Ongoing Proactive Monitoring</span>
                  </li>
               </ul>
            </div>
            
         </div>
      </div>
   </section>

   <!-- FOOTER -->
   <footer id="footerSection"><div class="container"><div class="row">
      <div class="col-lg-4 mb-5 mb-lg-0">
         <a class="logo d-flex align-items-center" href="../index.html" style="text-decoration: none;"><img src="../img/logo-dark.png" alt="Techtox Logo" style="height:40px; width: auto; margin-right:12px;"></a>
         <p class="about" style="font-family: 'Sora', sans-serif !important;">Design, build, automate and scale with full-service digital solutions designed around your business.</p>
         <div class="social-links">
            <a href="#"><i class="fab fa-instagram"></i></a>
            <a href="#"><i class="fab fa-facebook-f"></i></a>
            <a href="#"><i class="fab fa-twitter"></i></a>
            <a href="#"><i class="fab fa-linkedin-in"></i></a>
         </div>
      </div>
      <div class="col-6 col-lg-2 mb-4 mb-lg-0"><div class="footer-box"><p class="title" style="font-family: 'Sora', sans-serif !important;">Company</p><a href="../about.html">About</a><a href="../faq.html">FAQ</a></div></div>
      <div class="col-6 col-lg-3 mb-4 mb-lg-0"><div class="footer-box"><p class="title" style="font-family: 'Sora', sans-serif !important;">Departments</p><a href="../services.html#development">Development</a><a href="../services.html#automation">Automation</a><a href="../services.html#creative">Creative</a><a href="../services.html#marketing">Marketing</a></div></div>
      <div class="col-lg-3"><div class="footer-box"><p class="title" style="font-family: 'Sora', sans-serif !important;">Resources</p><a href="mailto:contact@techtox.com">Email Us</a><a href="../contact.html">Request a Strategy Call</a><a href="#">Islamabad, Pakistan</a><a href="#">Serving globally</a></div></div>
   </div><div class="row mt-5 pt-4 footer-bottom"><div class="col-md-6"><p>&copy; 2026 Techtox. All rights reserved.</p></div><div class="col-md-6 text-md-right"><a href="../terms.html" class="mr-4">Terms and Conditions</a><a href="../privacy.html">Privacy Policy</a></div></div></div></footer>

   <a href="#" class="scroll-up"><i class="fa fa-chevron-up"></i></a>
   <script src="../js/jquery.min.js"></script>
   <script src="../js/bootstrap.min.js"></script>
   <script src="../js/popper.min.js"></script>
   <script src="../js/font-awesome-pro.js"></script>
   <script src="../js/wow.min.js"></script>
   <script src="../js/mixitup.min.js"></script>
   <script src="../js/jquery.magnific-popup.min.js"></script>
   <script src="../js/jquery.counterup.min.js"></script>
   <script src="../js/jquery.waypoints.min.js"></script>
   <script src="../js/owl.carousel.min.js"></script>
   <script src="../js/custom.js"></script>
   <script src="../js/chatbot.js"></script>
   
   <!-- NATIVE FAQ ACCORDION & DEMO VIDEO LIGHTBOX SCRIPT -->
   <script>
   $(document).ready(function() {{
      // Native FAQ Accordion
      $('.fv-faq-modern-header').on('click', function() {{
         var item = $(this).closest('.fv-faq-modern-item');
         var isActive = item.hasClass('active');
         $('.fv-faq-modern-item').removeClass('active');
         if (!isActive) {{
            item.addClass('active');
         }}
      }});

      // Magnific Popup YouTube Video Lightbox
      if ($.fn.magnificPopup) {{
         $('.popup-youtube').magnificPopup({{
            type: 'iframe',
            mainClass: 'mfp-fade',
            removalDelay: 160,
            preloader: false,
            fixedContentPos: false,
            iframe: {{
               patterns: {{
                  youtube: {{
                     index: 'youtube.com/',
                     id: 'v=',
                     src: 'https://www.youtube.com/embed/%id%?autoplay=1&rel=0'
                  }}
               }}
            }}
         }});
      }}
   }});
   </script>
</body>
</html>'''

# ==============================================================================
# 3. CLEAN DEVELOPMENT GRID FOR services.html
# ==============================================================================

CLEAN_DEV_SECTION_SERVICES_HTML = '''    <div id="development" class="w-full py-5 lg:py-5" style="border-bottom: 1px solid #f3f4f6; padding-top: 80px !important; padding-bottom: 80px !important;">
      <div class="container mx-auto">
        <!-- Dept Header -->
        <div class="mb-5 d-flex flex-column align-items-start wow fadeInUp" style="gap: 12px; margin-bottom: 50px !important;">
            <div style="display: inline-flex; align-items: center; border-radius: 9999px; background-color: #000000; color: #ffffff; padding: 6px 16px; font-size: 13px; font-weight: 600; font-family: 'Sora', sans-serif; letter-spacing: 1px; text-transform: uppercase;">
              Phase 02
            </div>
            <h2 style="font-family: 'Sora', sans-serif; font-size: 48px; font-weight: 500; color: #000000; letter-spacing: -1.5px; margin: 0; line-height: 1.1;">
              Development
            </h2>
            <p style="color: #6b7280; font-size: 18px; font-family: 'Sora', sans-serif; margin: 0; max-width: 650px; line-height: 1.6;">
              We design, build, and deliver digital products that work — from custom web applications to scalable e-commerce, desktop software, and robust system integrations.
            </p>
        </div>
        
        <div class="shadcn-service-grid">

           <!-- Card 1: Custom Web Applications -->
           <a href="services/web-applications.html" class="shadcn-service-card wow fadeInUp" data-wow-delay="0.1s" style="display: flex; flex-direction: column;">
              <img class="shadcn-img-block" src="https://images.unsplash.com/photo-1498050108023-c5249f4df085?auto=format&fit=crop&w=800&q=80" alt="Custom Web Applications" loading="lazy" style="object-fit: cover; width: 100%; display: block;">
              <div class="d-flex flex-column" style="gap: 8px; flex: 1;">
                  <h3 class="shadcn-card-title">Custom Web Applications</h3>
                  <p class="shadcn-card-desc">Bespoke web applications that streamline business operations, organize information, and automate complex workflows.</p>
                  <ul style="list-style: none; padding: 0; margin: 10px 0 4px 0; display: flex; flex-direction: column; gap: 6px;">
                     <li style="font-family: 'Sora', sans-serif; font-size: 13px; color: #4b5563; display: flex; align-items: center; gap: 8px;">
                        <i class="fa fa-check" style="color: #FF2E3E; font-size: 11px;"></i> Business Management Systems & Dashboards
                     </li>
                     <li style="font-family: 'Sora', sans-serif; font-size: 13px; color: #4b5563; display: flex; align-items: center; gap: 8px;">
                        <i class="fa fa-check" style="color: #FF2E3E; font-size: 11px;"></i> Customer & Employee Portals (Role-Based)
                     </li>
                     <li style="font-family: 'Sora', sans-serif; font-size: 13px; color: #4b5563; display: flex; align-items: center; gap: 8px;">
                        <i class="fa fa-check" style="color: #FF2E3E; font-size: 11px;"></i> Database-Backed Architectures (React, Node, .NET)
                     </li>
                  </ul>
                  <div style="margin-top: auto; padding-top: 12px; font-family: 'Sora', sans-serif; font-size: 13px; font-weight: 600; color: #FF2E3E; display: flex; align-items: center; gap: 6px;">
                      Explore Service <i class="fa fa-arrow-right" style="font-size: 11px;"></i>
                  </div>
              </div>
           </a>

           <!-- Card 2: WordPress Solutions -->
           <a href="services/wordpress-solutions.html" class="shadcn-service-card wow fadeInUp" data-wow-delay="0.2s" style="display: flex; flex-direction: column;">
              <img class="shadcn-img-block" src="https://images.unsplash.com/photo-1616469829581-73993eb86b02?auto=format&fit=crop&w=800&q=80" alt="WordPress Solutions" loading="lazy" style="object-fit: cover; width: 100%; display: block;">
              <div class="d-flex flex-column" style="gap: 8px; flex: 1;">
                  <h3 class="shadcn-card-title">WordPress Solutions</h3>
                  <p class="shadcn-card-desc">High-performance corporate websites and custom Gutenberg architectures built for speed, security, and editorial ease.</p>
                  <ul style="list-style: none; padding: 0; margin: 10px 0 4px 0; display: flex; flex-direction: column; gap: 6px;">
                     <li style="font-family: 'Sora', sans-serif; font-size: 13px; color: #4b5563; display: flex; align-items: center; gap: 8px;">
                        <i class="fa fa-check" style="color: #FF2E3E; font-size: 11px;"></i> Custom Theme Development & Block Styling
                     </li>
                     <li style="font-family: 'Sora', sans-serif; font-size: 13px; color: #4b5563; display: flex; align-items: center; gap: 8px;">
                        <i class="fa fa-check" style="color: #FF2E3E; font-size: 11px;"></i> Core Web Vitals & Sub-1.5s Speed Optimization
                     </li>
                     <li style="font-family: 'Sora', sans-serif; font-size: 13px; color: #4b5563; display: flex; align-items: center; gap: 8px;">
                        <i class="fa fa-check" style="color: #FF2E3E; font-size: 11px;"></i> Enterprise Security Hardening & Zero Plugin Bloat
                     </li>
                  </ul>
                  <div style="margin-top: auto; padding-top: 12px; font-family: 'Sora', sans-serif; font-size: 13px; font-weight: 600; color: #FF2E3E; display: flex; align-items: center; gap: 6px;">
                      Explore Service <i class="fa fa-arrow-right" style="font-size: 11px;"></i>
                  </div>
              </div>
           </a>

           <!-- Card 3: Shopify Stores -->
           <a href="services/shopify-stores.html" class="shadcn-service-card wow fadeInUp" data-wow-delay="0.3s" style="display: flex; flex-direction: column;">
              <img class="shadcn-img-block" src="https://images.unsplash.com/photo-1556742049-0cfed4f6a45d?auto=format&fit=crop&w=800&q=80" alt="Shopify Stores" loading="lazy" style="object-fit: cover; width: 100%; display: block;">
              <div class="d-flex flex-column" style="gap: 8px; flex: 1;">
                  <h3 class="shadcn-card-title">Shopify Stores</h3>
                  <p class="shadcn-card-desc">Conversion-driven e-commerce storefronts designed to maximize average order value and provide frictionless buying journeys.</p>
                  <ul style="list-style: none; padding: 0; margin: 10px 0 4px 0; display: flex; flex-direction: column; gap: 6px;">
                     <li style="font-family: 'Sora', sans-serif; font-size: 13px; color: #4b5563; display: flex; align-items: center; gap: 8px;">
                        <i class="fa fa-check" style="color: #FF2E3E; font-size: 11px;"></i> Custom Liquid Themes & Modular Sections
                     </li>
                     <li style="font-family: 'Sora', sans-serif; font-size: 13px; color: #4b5563; display: flex; align-items: center; gap: 8px;">
                        <i class="fa fa-check" style="color: #FF2E3E; font-size: 11px;"></i> Slide-Out Cart, Product Bundles & Subscriptions
                     </li>
                     <li style="font-family: 'Sora', sans-serif; font-size: 13px; color: #4b5563; display: flex; align-items: center; gap: 8px;">
                        <i class="fa fa-check" style="color: #FF2E3E; font-size: 11px;"></i> Payment Gateways, ERP & 3PL Warehouse Sync
                     </li>
                  </ul>
                  <div style="margin-top: auto; padding-top: 12px; font-family: 'Sora', sans-serif; font-size: 13px; font-weight: 600; color: #FF2E3E; display: flex; align-items: center; gap: 6px;">
                      Explore Service <i class="fa fa-arrow-right" style="font-size: 11px;"></i>
                  </div>
              </div>
           </a>

           <!-- Card 4: Desktop Applications -->
           <a href="services/desktop-applications.html" class="shadcn-service-card wow fadeInUp" data-wow-delay="0.4s" style="display: flex; flex-direction: column;">
              <img class="shadcn-img-block" src="https://images.unsplash.com/photo-1517694712202-14dd9538aa97?auto=format&fit=crop&w=800&q=80" alt="Desktop Applications" loading="lazy" style="object-fit: cover; width: 100%; display: block;">
              <div class="d-flex flex-column" style="gap: 8px; flex: 1;">
                  <h3 class="shadcn-card-title">Desktop Applications</h3>
                  <p class="shadcn-card-desc">Purpose-built desktop software for business workflows requiring dedicated local computing, hardware controls, and offline speed.</p>
                  <ul style="list-style: none; padding: 0; margin: 10px 0 4px 0; display: flex; flex-direction: column; gap: 6px;">
                     <li style="font-family: 'Sora', sans-serif; font-size: 13px; color: #4b5563; display: flex; align-items: center; gap: 8px;">
                        <i class="fa fa-check" style="color: #FF2E3E; font-size: 11px;"></i> Internal Business Utilities & Batch Record Processing
                     </li>
                     <li style="font-family: 'Sora', sans-serif; font-size: 13px; color: #4b5563; display: flex; align-items: center; gap: 8px;">
                        <i class="fa fa-check" style="color: #FF2E3E; font-size: 11px;"></i> Direct Hardware Control (Thermal Printers, Scanners)
                     </li>
                     <li style="font-family: 'Sora', sans-serif; font-size: 13px; color: #4b5563; display: flex; align-items: center; gap: 8px;">
                        <i class="fa fa-check" style="color: #FF2E3E; font-size: 11px;"></i> Offline SQLite Databases with Cloud Sync
                     </li>
                  </ul>
                  <div style="margin-top: auto; padding-top: 12px; font-family: 'Sora', sans-serif; font-size: 13px; font-weight: 600; color: #FF2E3E; display: flex; align-items: center; gap: 6px;">
                      Explore Service <i class="fa fa-arrow-right" style="font-size: 11px;"></i>
                  </div>
              </div>
           </a>

           <!-- Card 5: API & System Integration -->
           <a href="services/api-software-integration.html" class="shadcn-service-card wow fadeInUp" data-wow-delay="0.5s" style="display: flex; flex-direction: column;">
              <img class="shadcn-img-block" src="https://images.unsplash.com/photo-1558494949-ef010cbdcc31?auto=format&fit=crop&w=800&q=80" alt="API & System Integration" loading="lazy" style="object-fit: cover; width: 100%; display: block;">
              <div class="d-flex flex-column" style="gap: 8px; flex: 1;">
                  <h3 class="shadcn-card-title">API & System Integration</h3>
                  <p class="shadcn-card-desc">Connect applications, SaaS platforms, and databases so information moves in real-time with zero manual data entry.</p>
                  <ul style="list-style: none; padding: 0; margin: 10px 0 4px 0; display: flex; flex-direction: column; gap: 6px;">
                     <li style="font-family: 'Sora', sans-serif; font-size: 13px; color: #4b5563; display: flex; align-items: center; gap: 8px;">
                        <i class="fa fa-check" style="color: #FF2E3E; font-size: 11px;"></i> Custom REST & GraphQL Endpoints & Documentation
                     </li>
                     <li style="font-family: 'Sora', sans-serif; font-size: 13px; color: #4b5563; display: flex; align-items: center; gap: 8px;">
                        <i class="fa fa-check" style="color: #FF2E3E; font-size: 11px;"></i> Bi-Directional CRM, ERP & SaaS Data Synchronization
                     </li>
                     <li style="font-family: 'Sora', sans-serif; font-size: 13px; color: #4b5563; display: flex; align-items: center; gap: 8px;">
                        <i class="fa fa-check" style="color: #FF2E3E; font-size: 11px;"></i> Failover Queues, Webhook Pipelines & Dead-Letter Logs
                     </li>
                  </ul>
                  <div style="margin-top: auto; padding-top: 12px; font-family: 'Sora', sans-serif; font-size: 13px; font-weight: 600; color: #FF2E3E; display: flex; align-items: center; gap: 6px;">
                      Explore Service <i class="fa fa-arrow-right" style="font-size: 11px;"></i>
                  </div>
              </div>
           </a>

        </div>
      </div>
    </div>'''

def main():
    # 1. Generate the 4 detail pages in services/
    print("Generating development detail pages...")
    for s in DEV_SERVICES_DATA:
        filepath = os.path.join("services", s["filename"])
        html = render_dev_detail_page(s)
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(html)
        print(f"  -> Generated: {filepath}")

    # 2. Update services.html
    print("Updating services.html...")
    with open("services.html", "r", encoding="utf-8") as f:
        services_content = f.read()

    # Replace <div id="development" ... up to <div id="marketing"
    pattern = r'<div id="development" class="dev-department-wrapper".*?(?=\s*<div id="marketing")'
    new_services_content = re.sub(pattern, CLEAN_DEV_SECTION_SERVICES_HTML + "\n\n", services_content, flags=re.DOTALL)

    # Remove the admin video script at the bottom of services.html if present
    script_pattern = r'// 3\. Admin Video Management Drawer Toggle & Persistence.*?\}\);\s*</script>\s*</body>'
    clean_closing = '''   });
   </script>
</body>'''
    new_services_content = re.sub(script_pattern, clean_closing, new_services_content, flags=re.DOTALL)

    with open("services.html", "w", encoding="utf-8") as f:
        f.write(new_services_content)
    print("  -> Updated services.html with clean Phase 02 Development grid and removed video drawer script.")

if __name__ == "__main__":
    main()
