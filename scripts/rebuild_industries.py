# -*- coding: utf-8 -*-
import os
import re

os.makedirs('c:/Users/my/Desktop/chatgpt/industries', exist_ok=True)

with open('c:/Users/my/Desktop/chatgpt/services/web-applications.html', 'r', encoding='utf-8', errors='ignore') as f:
    template = f.read()

# Extract NAV and HEAD
# Find everything before the first <section class="fv-page-hero"
nav_match = re.search(r'(?s)(.*?)(<section class="fv-page-hero")', template)
if nav_match:
    nav = nav_match.group(1)
else:
    print("Nav match failed!")
    exit()

# Extract CTA and Footer
cta_match = re.search(r'(?s)(<section class="fv-cta-split[^>]*>.*)', template)
if cta_match:
    cta_footer = cta_match.group(1)
else:
    print("CTA match failed!")
    exit()

industries = [
    {
        "id": "real-estate",
        "title": "Real Estate & PropTech",
        "hero_desc": "Automated lead routing, MLS integrations, and high-conversion funnels for top-producing brokerages.",
        "bg_img": "https://images.unsplash.com/photo-1560518883-ce09059eeffa?auto=format&fit=crop&w=1920&q=80",
        "features": [
            {"icon": "fa-funnel-dollar", "title": "Lead Routing Automation", "desc": "Instantly route Zillow and organic leads to the right agent via WhatsApp and SMS within seconds."},
            {"icon": "fa-database", "title": "MLS API Integrations", "desc": "Custom IDX/MLS integrations that keep your property listings synced in real-time across all your digital assets."},
            {"icon": "fa-robot", "title": "AI Qualifying Agents", "desc": "Custom trained AI bots that qualify buyers and sellers 24/7, booking highly qualified appointments directly to your calendar."}
        ]
    },
    {
        "id": "b2b-saas",
        "title": "B2B SaaS Companies",
        "hero_desc": "Enterprise API integrations, custom dashboard development, and automated onboarding workflows.",
        "bg_img": "https://images.unsplash.com/photo-1551288049-bebda4e38f71?auto=format&fit=crop&w=1920&q=80",
        "features": [
            {"icon": "fa-plug", "title": "Complex API Integrations", "desc": "We connect your disparate systems. Stripe, HubSpot, Salesforce, and your proprietary database talking to each other flawlessly."},
            {"icon": "fa-chart-network", "title": "Automated Onboarding", "desc": "Reduce churn by automating the entire user onboarding sequence based on in-app behavior and product usage analytics."},
            {"icon": "fa-browser", "title": "Custom Dashboards", "desc": "Internal admin panels and client-facing analytics dashboards built on React and Node.js for sub-second performance."}
        ]
    },
    {
        "id": "ecommerce",
        "title": "High-Volume E-Commerce",
        "hero_desc": "Headless architecture, inventory automation, and retention systems for 7-figure and 8-figure brands.",
        "bg_img": "https://images.unsplash.com/photo-1661956602116-aa6865609028?auto=format&fit=crop&w=1920&q=80",
        "features": [
            {"icon": "fa-shopping-cart", "title": "Headless Shopify", "desc": "Lightning-fast frontend experiences decoupled from Shopify's backend, maximizing conversion rates and SEO scores."},
            {"icon": "fa-boxes", "title": "Inventory Automation", "desc": "Automate PO generation, low-stock alerts, and multi-warehouse syncing without human intervention."},
            {"icon": "fa-envelope-open-dollar", "title": "Retention Workflows", "desc": "Aggressive, data-driven email and SMS automation sequences that recover abandoned carts and drive repeat purchases."}
        ]
    },
    {
        "id": "legal",
        "title": "Law Firms & Attorneys",
        "hero_desc": "Secure client portals, automated intake forms, and case management integrations for modern practices.",
        "bg_img": "https://images.unsplash.com/photo-1589829085413-56de8ae18c73?auto=format&fit=crop&w=1920&q=80",
        "features": [
            {"icon": "fa-file-signature", "title": "Automated Intake", "desc": "Dynamic forms that collect client data, automatically populate legal documents, and create matters in Clio or PracticePanther."},
            {"icon": "fa-lock-alt", "title": "Secure Client Portals", "desc": "Encrypted environments where clients can upload sensitive documents, check case status, and pay invoices autonomously."},
            {"icon": "fa-calendar-check", "title": "Consultation Routing", "desc": "Qualify leads before they eat up billable hours, routing only high-value cases to an attorney's calendar."}
        ]
    },
    {
        "id": "healthcare",
        "title": "Healthcare & Med Spas",
        "hero_desc": "HIPAA-compliant data routing, automated appointment follow-ups, and reputation management.",
        "bg_img": "https://images.unsplash.com/photo-1629909613654-28e377c37b09?auto=format&fit=crop&w=1920&q=80",
        "features": [
            {"icon": "fa-shield-check", "title": "Compliant Automation", "desc": "Secure data pipelines that move patient information between your web forms and EMR/EHR systems without violating HIPAA."},
            {"icon": "fa-calendar-plus", "title": "No-Show Reduction", "desc": "Automated SMS and WhatsApp reminders, pre-appointment instructions, and automated rescheduling flows."},
            {"icon": "fa-star", "title": "Reputation Management", "desc": "Automated post-appointment sequences that capture internal feedback for unhappy patients and push 5-star reviews to Google."}
        ]
    },
    {
        "id": "financial",
        "title": "Financial Services & Wealth Management",
        "hero_desc": "Secure document routing, CRM automation, and client reporting dashboards for high-net-worth advisors.",
        "bg_img": "https://images.unsplash.com/photo-1611974789855-9c2a0a7236a3?auto=format&fit=crop&w=1920&q=80",
        "features": [
            {"icon": "fa-chart-line", "title": "Client Dashboards", "desc": "Custom reporting portals that aggregate portfolio data from multiple APIs into a single, beautiful client experience."},
            {"icon": "fa-users-cog", "title": "CRM Automation", "desc": "Automate annual review scheduling, compliance document signing workflows, and lead nurturing sequences."},
            {"icon": "fa-file-invoice", "title": "Secure Onboarding", "desc": "Frictionless digital onboarding flows that securely capture sensitive financial data and route it directly to your core systems."}
        ]
    }
]

for ind in industries:
    middle = f'''
   <!-- HERO SECTION -->
   <section class="fv-page-hero" style="background: linear-gradient(rgba(17,24,39,0.8), rgba(17,24,39,0.9)), url('{ind["bg_img"]}') no-repeat center center/cover; padding: 160px 0 100px 0;">
        <div class="container text-center">
           <span class="fv-eyebrow wow fadeInUp" data-wow-delay="0.1s" style="color:#fb383b; letter-spacing:2px; font-weight: 700;">INDUSTRY SOLUTIONS</span>
           <h1 class="wow fadeInUp" data-wow-delay="0.2s" style="font-family:'Rubik', sans-serif; font-weight:600; font-size: 56px; letter-spacing:-1.5px; color: #ffffff; max-width: 900px; margin: 15px auto;">
              {ind["title"]}
           </h1>
           <p class="fv-lead wow fadeInUp" data-wow-delay="0.3s" style="font-family: 'Rubik', sans-serif; font-size: 20px; color: #d1d5db; max-width: 700px; margin: 20px auto 0;">
              {ind["hero_desc"]}
           </p>
        </div>
   </section>

   <!-- LIGHT GRID FEATURES -->
   <section class="py-5" style="background-color: #f9fafb; padding-top: 100px !important; padding-bottom: 100px !important;">
        <div class="container">
            <div class="text-center mb-5 pb-3">
                <span style="color: #fb383b; font-family: 'Rubik', sans-serif; font-size: 13px; font-weight: 700; letter-spacing: 2px; text-transform: uppercase; margin-bottom: 15px; display: inline-block;">ARCHITECTURE</span>
                <h2 style="font-family:'Rubik', sans-serif; font-size: 42px; font-weight: 500; color: #111827; letter-spacing: -1.5px; margin: 0; line-height: 1.1;">
                    How we scale {ind["title"]}.
                </h2>
            </div>
            
            <div class="row">
                <div class="col-lg-4 mb-4 wow fadeInUp" data-wow-delay="0.1s">
                    <div style="background: #ffffff; padding: 40px; border-radius: 12px; border: 1px solid #e5e7eb; height: 100%; box-shadow: 0 4px 6px -1px rgba(0,0,0,0.05);">
                        <i class="fal {ind["features"][0]["icon"]}" style="font-size: 32px; color: #fb383b; margin-bottom: 24px;"></i>
                        <h3 style="font-family: 'Rubik', sans-serif; font-size: 22px; font-weight: 600; color: #111827; margin-bottom: 12px;">{ind["features"][0]["title"]}</h3>
                        <p style="color: #6b7280; font-size: 16px; line-height: 1.6; margin: 0;">{ind["features"][0]["desc"]}</p>
                    </div>
                </div>
                <div class="col-lg-4 mb-4 wow fadeInUp" data-wow-delay="0.2s">
                    <div style="background: #ffffff; padding: 40px; border-radius: 12px; border: 1px solid #e5e7eb; height: 100%; box-shadow: 0 4px 6px -1px rgba(0,0,0,0.05);">
                        <i class="fal {ind["features"][1]["icon"]}" style="font-size: 32px; color: #fb383b; margin-bottom: 24px;"></i>
                        <h3 style="font-family: 'Rubik', sans-serif; font-size: 22px; font-weight: 600; color: #111827; margin-bottom: 12px;">{ind["features"][1]["title"]}</h3>
                        <p style="color: #6b7280; font-size: 16px; line-height: 1.6; margin: 0;">{ind["features"][1]["desc"]}</p>
                    </div>
                </div>
                <div class="col-lg-4 mb-4 wow fadeInUp" data-wow-delay="0.3s">
                    <div style="background: #ffffff; padding: 40px; border-radius: 12px; border: 1px solid #e5e7eb; height: 100%; box-shadow: 0 4px 6px -1px rgba(0,0,0,0.05);">
                        <i class="fal {ind["features"][2]["icon"]}" style="font-size: 32px; color: #fb383b; margin-bottom: 24px;"></i>
                        <h3 style="font-family: 'Rubik', sans-serif; font-size: 22px; font-weight: 600; color: #111827; margin-bottom: 12px;">{ind["features"][2]["title"]}</h3>
                        <p style="color: #6b7280; font-size: 16px; line-height: 1.6; margin: 0;">{ind["features"][2]["desc"]}</p>
                    </div>
                </div>
            </div>
        </div>
   </section>
'''
    page_html = nav + middle + cta_footer
    page_html = re.sub(r'<title>.*?</title>', f'<title>{ind["title"]} Solutions | Flow Vello</title>', page_html)
    
    with open(f'c:/Users/my/Desktop/chatgpt/industries/{ind["id"]}.html', 'w', encoding='utf-8') as fw:
        fw.write(page_html)

print("Regenerated 6 high-value industry pages successfully.")
