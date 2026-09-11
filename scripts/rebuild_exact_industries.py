# -*- coding: utf-8 -*-
import os
import re

with open('c:/Users/my/Desktop/chatgpt/services/web-applications.html', 'r', encoding='utf-8', errors='ignore') as f:
    template = f.read()

nav_match = re.search(r'(?s)(.*?)(<section class="fv-page-hero")', template)
nav = nav_match.group(1) if nav_match else ''

cta_match = re.search(r'(?s)(<!-- CLOSING CTA \(SPLIT\) -->.*)', template)
cta_footer = cta_match.group(1) if cta_match else ''

industries = [
    {
        "id": "real-estate",
        "title": "Real Estate & PropTech",
        "hero_desc": "Automated lead routing, MLS integrations, and high-conversion funnels for top-producing brokerages.",
        "bg_img": "https://images.unsplash.com/photo-1560518883-ce09059eeffa?auto=format&fit=crop&w=1920&q=80",
        "problem_title": "Real estate moves fast. Manual data entry doesn't.",
        "problem_desc": "If it takes your agents more than 5 minutes to respond to a Zillow lead, that lead is already talking to your competitor. You are losing millions in GCI because your team is manually copy-pasting data between your CRM, your inbox, and your phone.",
        "pillars": [
            {"title": "Automated Lead Routing", "desc": "Instantly capture leads from Zillow, Realtor.com, and Facebook, and route them to the right agent via SMS in under 2 seconds.", "icon": "fa-funnel-dollar", "img": "https://images.unsplash.com/photo-1560518883-ce09059eeffa?auto=format&fit=crop&w=800&q=80"},
            {"title": "Custom MLS Integrations", "desc": "We build direct API connections to your local MLS so your website and internal databases update properties in real-time.", "icon": "fa-database", "img": "https://images.unsplash.com/photo-1551288049-bebda4e38f71?auto=format&fit=crop&w=800&q=80"},
            {"title": "AI Appointment Setters", "desc": "Custom-trained AI agents that text and qualify buyers 24/7, booking highly qualified tours directly into your agents' Calendly.", "icon": "fa-robot", "img": "https://images.unsplash.com/photo-1460925895917-afdab827c52f?auto=format&fit=crop&w=800&q=80"},
            {"title": "Transaction Automation", "desc": "Automated document generation and compliance routing using Dotloop, DocuSign, and your internal CRM.", "icon": "fa-file-signature", "img": "https://images.unsplash.com/photo-1589829085413-56de8ae18c73?auto=format&fit=crop&w=800&q=80"}
        ],
        "deliverables": [
            {"title": "HubSpot / Follow Up Boss Setup", "desc": "Complete CRM architecture."},
            {"title": "Zillow API Integration", "desc": "Instant lead capture workflows."},
            {"title": "Automated SMS Nurture", "desc": "Long-term drip campaigns."},
            {"title": "AI Buyer Qualification Bot", "desc": "24/7 web chat support."},
            {"title": "Dashboard Analytics", "desc": "Real-time GCI reporting."},
            {"title": "Automated Review Generation", "desc": "Google & Zillow 5-star workflows."}
        ]
    },
    {
        "id": "b2b-saas",
        "title": "B2B SaaS Companies",
        "hero_desc": "Enterprise API integrations, custom dashboard development, and automated onboarding workflows.",
        "bg_img": "https://images.unsplash.com/photo-1551288049-bebda4e38f71?auto=format&fit=crop&w=1920&q=80",
        "problem_title": "Your churn rate is a systems problem.",
        "problem_desc": "When users sign up for your software and get a generic welcome email instead of a personalized, data-driven onboarding sequence, they churn. When your sales team cannot see product usage data inside Salesforce, they lose upsells.",
        "pillars": [
            {"title": "Data Warehouse Syncing", "desc": "We connect your PostgreSQL database directly to HubSpot or Salesforce so sales teams have real-time data.", "icon": "fa-database", "img": "https://images.unsplash.com/photo-1551288049-bebda4e38f71?auto=format&fit=crop&w=800&q=80"},
            {"title": "Automated Onboarding", "desc": "Complex email and in-app messaging sequences triggered by exact user behaviors.", "icon": "fa-chart-network", "img": "https://images.unsplash.com/photo-1460925895917-afdab827c52f?auto=format&fit=crop&w=800&q=80"},
            {"title": "Custom Analytics Dashboards", "desc": "Executive-level dashboards built in React that aggregate Stripe revenue and product usage.", "icon": "fa-browser", "img": "https://images.unsplash.com/photo-1555066931-4365d14bab8c?auto=format&fit=crop&w=800&q=80"},
            {"title": "Churn Prevention AI", "desc": "Predictive models that flag accounts at high risk of churning before they actually cancel.", "icon": "fa-brain", "img": "https://images.unsplash.com/photo-1611974789855-9c2a0a7236a3?auto=format&fit=crop&w=800&q=80"}
        ],
        "deliverables": [
            {"title": "Stripe API Automation", "desc": "Billing & upgrade workflows."},
            {"title": "Salesforce Bi-directional Sync", "desc": "Real-time product usage data."},
            {"title": "Custom React Admin Panels", "desc": "Internal operations control."},
            {"title": "Intercom / Zendesk Chatbots", "desc": "Automated L1 support resolution."},
            {"title": "Automated Drip Campaigns", "desc": "Hyper-segmented onboarding."},
            {"title": "API Endpoint Architecture", "desc": "Secure, scalable backend access."}
        ]
    },
    {
        "id": "ecommerce",
        "title": "High-Volume E-Commerce",
        "hero_desc": "Headless architecture, inventory automation, and retention systems for 7-figure and 8-figure brands.",
        "bg_img": "https://images.unsplash.com/photo-1661956602116-aa6865609028?auto=format&fit=crop&w=1920&q=80",
        "problem_title": "Shopify templates are killing your conversion rate.",
        "problem_desc": "When your store takes 4 seconds to load on mobile, you lose 40% of your traffic instantly. When your abandoned cart emails are generic, you leave millions on the table. Standard out-of-the-box setups cannot scale to 8 figures.",
        "pillars": [
            {"title": "Headless Shopify Builds", "desc": "We decouple your frontend using Next.js or React, delivering sub-second load times.", "icon": "fa-shopping-cart", "img": "https://images.unsplash.com/photo-1661956602116-aa6865609028?auto=format&fit=crop&w=800&q=80"},
            {"title": "Advanced Klaviyo Flows", "desc": "Hyper-segmented email and SMS automation sequences based on purchase history and browsing behavior.", "icon": "fa-envelope-open-dollar", "img": "https://images.unsplash.com/photo-1556742049-0cfed4f6a45d?auto=format&fit=crop&w=800&q=80"},
            {"title": "Inventory Syncing", "desc": "Automated API integrations between Shopify, your 3PL warehouse, and your ERP to prevent overselling.", "icon": "fa-boxes", "img": "https://images.unsplash.com/photo-1586528116311-ad8dd3c8310d?auto=format&fit=crop&w=800&q=80"},
            {"title": "Post-Purchase Automation", "desc": "Automated review requests, upsell offers, and shipping notifications that build loyalty.", "icon": "fa-box-heart", "img": "https://images.unsplash.com/photo-1555066931-4365d14bab8c?auto=format&fit=crop&w=800&q=80"}
        ],
        "deliverables": [
            {"title": "Headless Frontend Development", "desc": "Next.js/React architecture."},
            {"title": "Klaviyo Advanced Segmentation", "desc": "Predictive LTV modeling flows."},
            {"title": "3PL / ERP API Integrations", "desc": "Automated fulfillment routing."},
            {"title": "Subscription Model Engineering", "desc": "ReCharge API custom builds."},
            {"title": "Automated Upsell Funnels", "desc": "Post-purchase 1-click offers."},
            {"title": "Sub-second Lighthouse Scores", "desc": "Maximum SEO & CVR optimization."}
        ]
    },
    {
        "id": "legal",
        "title": "Law Firms & Legal Practices",
        "hero_desc": "Secure client portals, automated intake forms, and case management integrations for modern practices.",
        "bg_img": "https://images.unsplash.com/photo-1589829085413-56de8ae18c73?auto=format&fit=crop&w=1920&q=80",
        "problem_title": "Billable hours are being wasted on administrative chaos.",
        "problem_desc": "Your attorneys are spending hours hunting down client documents, manually entering data into Clio, and chasing signatures. This is non-billable time that destroys your firm's profitability.",
        "pillars": [
            {"title": "Automated Client Intake", "desc": "Secure, dynamic web forms that capture client data and automatically create matters in Clio.", "icon": "fa-file-signature", "img": "https://images.unsplash.com/photo-1589829085413-56de8ae18c73?auto=format&fit=crop&w=800&q=80"},
            {"title": "Secure Document Portals", "desc": "Encrypted environments where clients can securely upload discovery documents and track case progress.", "icon": "fa-lock-alt", "img": "https://images.unsplash.com/photo-1551288049-bebda4e38f71?auto=format&fit=crop&w=800&q=80"},
            {"title": "Consultation Routing", "desc": "Automated qualification bots that screen leads and only book high-value cases onto an attorney's calendar.", "icon": "fa-calendar-check", "img": "https://images.unsplash.com/photo-1460925895917-afdab827c52f?auto=format&fit=crop&w=800&q=80"},
            {"title": "Automated Document Prep", "desc": "Systems that take intake data and automatically populate standard retainers and pleadings via DocuSign APIs.", "icon": "fa-file-invoice", "img": "https://images.unsplash.com/photo-1555066931-4365d14bab8c?auto=format&fit=crop&w=800&q=80"}
        ],
        "deliverables": [
            {"title": "Clio / PracticePanther Integration", "desc": "End-to-end case management sync."},
            {"title": "DocuSign API Automation", "desc": "Zero-touch retainer generation."},
            {"title": "Secure Client Dashboard", "desc": "Encrypted file vault systems."},
            {"title": "Automated Intake Web Forms", "desc": "Conditional logic lead capture."},
            {"title": "Case Status SMS Alerts", "desc": "Proactive client updates."},
            {"title": "HIPAA/Confidentiality Compliance", "desc": "Military-grade data security."}
        ]
    },
    {
        "id": "healthcare",
        "title": "Healthcare Clinics & Med Spas",
        "hero_desc": "HIPAA-compliant data routing, automated appointment follow-ups, and reputation management.",
        "bg_img": "https://images.unsplash.com/photo-1629909613654-28e377c37b09?auto=format&fit=crop&w=1920&q=80",
        "problem_title": "No-shows and manual follow-ups are draining your revenue.",
        "problem_desc": "If your front desk is manually calling patients to confirm appointments or asking them to fill out paper intake forms in the waiting room, you are operating in the past. It ruins the patient experience and increases no-show rates.",
        "pillars": [
            {"title": "HIPAA-Compliant Automation", "desc": "Secure data pipelines that move patient intake forms directly into your EMR/EHR system.", "icon": "fa-shield-check", "img": "https://images.unsplash.com/photo-1629909613654-28e377c37b09?auto=format&fit=crop&w=800&q=80"},
            {"title": "No-Show Reduction Systems", "desc": "Automated SMS and WhatsApp sequences that confirm appointments and handle rescheduling.", "icon": "fa-calendar-plus", "img": "https://images.unsplash.com/photo-1551288049-bebda4e38f71?auto=format&fit=crop&w=800&q=80"},
            {"title": "Reputation Engine", "desc": "Post-appointment automated workflows that intercept negative feedback privately and push 5-star reviews to Google.", "icon": "fa-star", "img": "https://images.unsplash.com/photo-1555066931-4365d14bab8c?auto=format&fit=crop&w=800&q=80"},
            {"title": "Membership Billing", "desc": "Automated recurring billing architectures for Med Spas and concierge clinics using Stripe.", "icon": "fa-credit-card", "img": "https://images.unsplash.com/photo-1460925895917-afdab827c52f?auto=format&fit=crop&w=800&q=80"}
        ],
        "deliverables": [
            {"title": "EMR / EHR API Integration", "desc": "DrChrono / JaneApp syncing."},
            {"title": "HIPAA-Compliant Intake Forms", "desc": "Encrypted digital paperwork."},
            {"title": "Automated Appointment Reminders", "desc": "Multi-channel SMS/Email flows."},
            {"title": "Google Review Automation", "desc": "Sentiment-based routing systems."},
            {"title": "Concierge Membership Portals", "desc": "Self-service subscription management."},
            {"title": "WhatsApp Patient Support Bots", "desc": "Automated FAQ resolution."}
        ]
    },
    {
        "id": "financial",
        "title": "Financial Services & Wealth Management",
        "hero_desc": "Secure document routing, CRM automation, and client reporting dashboards for high-net-worth advisors.",
        "bg_img": "https://images.unsplash.com/photo-1611974789855-9c2a0a7236a3?auto=format&fit=crop&w=1920&q=80",
        "problem_title": "High-net-worth clients expect seamless digital experiences.",
        "problem_desc": "You cannot manage millions in AUM while asking clients to email PDFs or manually scheduling annual reviews. The friction in your onboarding and reporting process makes you look outdated to modern investors.",
        "pillars": [
            {"title": "Client Wealth Dashboards", "desc": "Custom reporting portals that aggregate portfolio data from multiple financial APIs into a single client experience.", "icon": "fa-chart-line", "img": "https://images.unsplash.com/photo-1611974789855-9c2a0a7236a3?auto=format&fit=crop&w=800&q=80"},
            {"title": "Frictionless Onboarding", "desc": "Secure digital workflows that capture sensitive financial data, ID verification, and e-signatures seamlessly.", "icon": "fa-user-check", "img": "https://images.unsplash.com/photo-1551288049-bebda4e38f71?auto=format&fit=crop&w=800&q=80"},
            {"title": "CRM Automation", "desc": "Automated triggers for annual review scheduling, compliance document renewals, and high-touch milestone outreach.", "icon": "fa-users-cog", "img": "https://images.unsplash.com/photo-1460925895917-afdab827c52f?auto=format&fit=crop&w=800&q=80"},
            {"title": "Secure Document Routing", "desc": "Automated pipelines that move tax documents and statements directly to secure storage without using email.", "icon": "fa-file-invoice", "img": "https://images.unsplash.com/photo-1589829085413-56de8ae18c73?auto=format&fit=crop&w=800&q=80"}
        ],
        "deliverables": [
            {"title": "Custom Reporting Portals", "desc": "Multi-API data aggregation."},
            {"title": "Salesforce Financial Services Sync", "desc": "Enterprise CRM deployment."},
            {"title": "Plaid / Finicity Integrations", "desc": "Real-time banking data feeds."},
            {"title": "Automated KYC/AML Workflows", "desc": "Frictionless ID verification."},
            {"title": "Secure File Vault Architecture", "desc": "Encrypted document exchange."},
            {"title": "Automated Review Scheduling", "desc": "Calendly/HubSpot integration."}
        ]
    }
]

for ind in industries:
    middle = f'''
   <!-- HERO SECTION -->
   <section class="fv-page-hero" style="background-image: linear-gradient(rgba(17, 24, 39, 0.85), rgba(17, 24, 39, 0.95)), url('{ind["bg_img"]}'); background-size: cover; background-position: center; border-bottom: 1px solid #1f2937;">
        <div class="container text-center">
           <span class="fv-eyebrow wow fadeInUp" data-wow-delay="0.1s">INDUSTRY SOLUTIONS</span>
           <h1 class="wow fadeInUp" data-wow-delay="0.2s">{ind["title"]}</h1>
           <p class="fv-lead wow fadeInUp" data-wow-delay="0.3s">{ind["hero_desc"]}</p>
        </div>
   </section>

   <!-- PROBLEM SECTION: EXACT COPY OF "ABOUT PAGE" F72 FEATURE GRID -->
   <section class="py-5" style="background-color: #fafafa; padding-top: 100px !important; padding-bottom: 100px !important;">
      <div class="container" style="max-width: 1200px;">
          <div class="d-flex flex-column" style="gap: 60px;">
              <!-- Header Block -->
              <div style="max-width: 800px;" class="wow fadeInUp" data-wow-delay="0.1s">
                  <span style="color: #fb383b; font-family: 'Rubik', sans-serif; font-size: 13px; font-weight: 700; letter-spacing: 2px; text-transform: uppercase; margin-bottom: 15px; display: inline-block;">THE PROBLEM</span>
                  <h2 style="font-family:'Rubik', sans-serif; font-size: 42px; font-weight: 600; color: #111827; letter-spacing: -1.5px; margin-bottom: 16px; line-height: 1.1;">
                      {ind["problem_title"]}
                  </h2>
                  <p style="color: #6b7280; font-size: 18px; font-family:'Rubik', sans-serif; line-height: 1.6; margin-bottom: 30px;">
                      {ind["problem_desc"]}
                  </p>
              </div>
              
              <!-- Grid Block -->
              <style>
                  .f72-grid {{ display: grid; gap: 32px; grid-template-columns: 1fr; }}
                  @media (min-width: 768px) {{ .f72-grid {{ grid-template-columns: repeat(2, 1fr); }} }}
                  .f72-card {{ display: flex; flex-direction: column; overflow: hidden; border-radius: 12px; border: 1px solid #e5e7eb; background: #ffffff; transition: box-shadow 0.2s ease, transform 0.2s ease; }}
                  .f72-card:hover {{ box-shadow: 0 10px 15px -3px rgba(0, 0, 0, 0.1); transform: translateY(-2px); }}
                  .f72-img-container {{ width: 100%; aspect-ratio: 16/9; background: #f8fafc; border-bottom: 1px solid #e5e7eb; overflow: hidden; }}
                  .f72-img-container img {{ width: 100%; height: 100%; object-fit: cover; transition: transform 0.3s ease; }}
                  .f72-card:hover .f72-img-container img {{ transform: scale(1.05); }}
                  .f72-content {{ padding: 32px; display: flex; flex-direction: column; gap: 12px; }}
              </style>
              <div class="f72-grid">
                  <div class="f72-card wow fadeInUp" data-wow-delay="0.2s">
                      <div class="f72-img-container"><img src="{ind["pillars"][0]["img"]}" alt="{ind["pillars"][0]["title"]}" loading="lazy"></div>
                      <div class="f72-content">
                          <h3 style="font-family: 'Rubik', sans-serif; font-size: 22px; font-weight: 600; color: #111827; margin: 0; letter-spacing: -0.5px;">{ind["pillars"][0]["title"]}</h3>
                          <p style="color: #6b7280; font-size: 16px; line-height: 1.6; margin: 0;">{ind["pillars"][0]["desc"]}</p>
                      </div>
                  </div>
                  <div class="f72-card wow fadeInUp" data-wow-delay="0.3s">
                      <div class="f72-img-container"><img src="{ind["pillars"][1]["img"]}" alt="{ind["pillars"][1]["title"]}" loading="lazy"></div>
                      <div class="f72-content">
                          <h3 style="font-family: 'Rubik', sans-serif; font-size: 22px; font-weight: 600; color: #111827; margin: 0; letter-spacing: -0.5px;">{ind["pillars"][1]["title"]}</h3>
                          <p style="color: #6b7280; font-size: 16px; line-height: 1.6; margin: 0;">{ind["pillars"][1]["desc"]}</p>
                      </div>
                  </div>
                  <div class="f72-card wow fadeInUp" data-wow-delay="0.4s">
                      <div class="f72-img-container"><img src="{ind["pillars"][2]["img"]}" alt="{ind["pillars"][2]["title"]}" loading="lazy"></div>
                      <div class="f72-content">
                          <h3 style="font-family: 'Rubik', sans-serif; font-size: 22px; font-weight: 600; color: #111827; margin: 0; letter-spacing: -0.5px;">{ind["pillars"][2]["title"]}</h3>
                          <p style="color: #6b7280; font-size: 16px; line-height: 1.6; margin: 0;">{ind["pillars"][2]["desc"]}</p>
                      </div>
                  </div>
                  <div class="f72-card wow fadeInUp" data-wow-delay="0.5s">
                      <div class="f72-img-container"><img src="{ind["pillars"][3]["img"]}" alt="{ind["pillars"][3]["title"]}" loading="lazy"></div>
                      <div class="f72-content">
                          <h3 style="font-family: 'Rubik', sans-serif; font-size: 22px; font-weight: 600; color: #111827; margin: 0; letter-spacing: -0.5px;">{ind["pillars"][3]["title"]}</h3>
                          <p style="color: #6b7280; font-size: 16px; line-height: 1.6; margin: 0;">{ind["pillars"][3]["desc"]}</p>
                      </div>
                  </div>
              </div>
          </div>
      </div>
   </section>

  <!-- SHADCN LIGHT BENTO GRID (DELIVERABLES) FROM SERVICES PAGE -->
  <section class="py-5" style="background-color: #ffffff; padding-top: 80px !important; padding-bottom: 80px !important;">
      <div class="container" style="max-width: 1100px;">
          <div class="text-center mb-5 pb-2 mx-auto" style="max-width: 700px;">
              <span style="color: #fb383b; font-family: 'Rubik', sans-serif; font-size: 13px; font-weight: 700; letter-spacing: 2px; text-transform: uppercase; margin-bottom: 15px; display: inline-block;">INCLUDED IN SCOPE</span>
              <h2 style="font-family:'Rubik', sans-serif; font-size: 42px; font-weight: 500; color: #111827; letter-spacing: -1px; margin-bottom: 20px; line-height: 1.15;">
                  Technical Deliverables
              </h2>
          </div>
  
          <style>
              .feature-light-grid {{ display: grid; gap: 24px; grid-template-columns: 1fr; }}
              @media (min-width: 768px) {{ .feature-light-grid {{ grid-template-columns: repeat(2, 1fr); }} }}
              @media (min-width: 1024px) {{ .feature-light-grid {{ grid-template-columns: repeat(3, 1fr); }} }}
              .feature-light-card {{ background: #ffffff; padding: 40px; border-radius: 12px; border: 1px solid #e5e7eb; box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.05); transition: box-shadow 0.2s ease, transform 0.2s ease; }}
              .feature-light-card:hover {{ box-shadow: 0 10px 15px -3px rgba(0, 0, 0, 0.1); transform: translateY(-2px); }}
              .fl-icon {{ font-size: 24px; color: #fb383b; margin-bottom: 20px; }}
              .fl-title {{ font-family: 'Rubik', sans-serif; font-size: 18px; font-weight: 600; color: #111827; margin: 0 0 12px 0; letter-spacing: -0.5px; }}
              .fl-desc {{ font-family: 'Rubik', sans-serif; color: #6b7280; font-size: 15px; line-height: 1.6; margin: 0; }}
          </style>
  
          <div class="feature-light-grid">
              <div class="feature-light-card wow fadeInUp" data-wow-delay="0.1s">
                  <div class="fl-icon"><i class="fal fa-layer-group"></i></div>
                  <h3 class="fl-title">{ind["deliverables"][0]["title"]}</h3>
                  <p class="fl-desc">{ind["deliverables"][0]["desc"]}</p>
              </div>
              <div class="feature-light-card wow fadeInUp" data-wow-delay="0.2s">
                  <div class="fl-icon"><i class="fal fa-database"></i></div>
                  <h3 class="fl-title">{ind["deliverables"][1]["title"]}</h3>
                  <p class="fl-desc">{ind["deliverables"][1]["desc"]}</p>
              </div>
              <div class="feature-light-card wow fadeInUp" data-wow-delay="0.3s">
                  <div class="fl-icon"><i class="fal fa-plug"></i></div>
                  <h3 class="fl-title">{ind["deliverables"][2]["title"]}</h3>
                  <p class="fl-desc">{ind["deliverables"][2]["desc"]}</p>
              </div>
              <div class="feature-light-card wow fadeInUp" data-wow-delay="0.4s">
                  <div class="fl-icon"><i class="fal fa-shield-check"></i></div>
                  <h3 class="fl-title">{ind["deliverables"][3]["title"]}</h3>
                  <p class="fl-desc">{ind["deliverables"][3]["desc"]}</p>
              </div>
              <div class="feature-light-card wow fadeInUp" data-wow-delay="0.5s">
                  <div class="fl-icon"><i class="fal fa-rocket"></i></div>
                  <h3 class="fl-title">{ind["deliverables"][4]["title"]}</h3>
                  <p class="fl-desc">{ind["deliverables"][4]["desc"]}</p>
              </div>
              <div class="feature-light-card wow fadeInUp" data-wow-delay="0.6s">
                  <div class="fl-icon"><i class="fal fa-box-open"></i></div>
                  <h3 class="fl-title">{ind["deliverables"][5]["title"]}</h3>
                  <p class="fl-desc">{ind["deliverables"][5]["desc"]}</p>
              </div>
          </div>
      </div>
  </section>
'''
    page_html = nav + middle + cta_footer
    page_html = re.sub(r'<title>.*?</title>', f'<title>{ind["title"]} Solutions | Flow Vello</title>', page_html)
    
    with open(f'c:/Users/my/Desktop/chatgpt/industries/{ind["id"]}.html', 'w', encoding='utf-8') as fw:
        fw.write(page_html)

print("Industries rebuilt using exact About and Services page HTML templates.")
